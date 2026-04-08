#!/usr/bin/env python3
"""
Merrydale Campaign Email Extractor
===================================
Searches a Gmail account for RPG campaign correspondence and produces
archive-ready text files for the Merrydale repo.

Setup:
  1. Go to https://console.cloud.google.com/
  2. Create a project (or use an existing one)
  3. Enable the Gmail API
  4. Create OAuth 2.0 credentials (Desktop application)
  5. Download the credentials JSON file
  6. Place it as 'credentials.json' in this script's directory
  7. pip install google-auth-oauthlib google-api-python-client
  8. Run: python3 merrydale_extractor.py

First run will open a browser for Google OAuth consent. After that,
a token.json file is saved for future runs.

Usage:
  python3 merrydale_extractor.py [options]

  --output-dir DIR    Where to write archive files (default: ./extracted)
  --archive-dir DIR   Existing Merrydale Handouts dir for dedup (optional)
  --dry-run           Search and report but don't write files
  --max-results N     Max threads per search query (default: 50)
  --verbose           Print detailed progress
"""

import os
import sys
import re
import json
import argparse
import base64
import email.utils
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Gmail API imports (fail gracefully with install instructions)
# ---------------------------------------------------------------------------
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Required packages not installed. Run:")
    print("  pip install google-auth-oauthlib google-api-python-client")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# RPG group members — email addresses across eras
GROUP_MEMBERS = {
    'Les Blackwell': [
        'les.blackwell@gmail.com',
        'theblackcobb@hotmail.com',
        'beljuril@hotmail.com',  # Note: also used by Casey
    ],
    'Todd Burry': [
        'contact@toddburry.com',
        'todd.burry@gmail.com',
        'toddburry@hotmail.com',
        'myself@toddburry.com',
        'tburry@dymaxium.com',
    ],
    'Stephen Robertson': [
        'robertsoncrusoe@gmail.com',
        'stephen.robertson@utoronto.ca',
        'stephen.robertson@anthro.ox.ac.uk',
        'robertsoncrusoe@hotmail.com',
        'srobertson@dymaxium.com',
    ],
    'Gus Miranda': [
        'gus.miranda@gmail.com',
        'gmiranda@ncf.ca',
        'gusmiranda@gmail.com',
        'gmiranda@canada.com',
    ],
    'Scott McLaren': [
        'scunny1973@gmail.com',
        'SCUNNY1973@aol.com',
        'smclaren@canusacps.shawcor.com',
        'smclaren@husky.on.ca',
    ],
    'Steve Hicks': [
        'snahfu@gmail.com',
        'Steven.Hicks@telus.com',
        'asteroid_pillow@hotmail.com',
        'snah@rogers.com',
    ],
    'Casey Bauman-Wike': [
        'hellocasey@gmail.com',
        'beljuril@hotmail.com',
    ],
    'Alex Francom': [
        'jeffreyafrancom@gmail.com',
    ],
    'Rob Schmidt': [
        'robert.ak.schmidt@gmail.com',
        'rschmidt@shawcable.com',
        'rschmid1@uwinnipeg.ca',
    ],
}

# Build a flat lookup: email_address -> display_name
EMAIL_TO_NAME = {}
for name, addrs in GROUP_MEMBERS.items():
    for addr in addrs:
        EMAIL_TO_NAME[addr.lower()] = name

# Search queries — each targets a different angle on campaign content.
# Gmail search syntax: https://support.google.com/mail/answer/7190
SEARCH_QUERIES = [
    # Direct campaign name searches
    'subject:(DND OR D&D OR "dungeons and dragons")',
    'subject:(Daggerdale OR "Thistle Ridge" OR Chrysalis)',
    'subject:(Eastwitch OR Waldheim OR Avilund)',
    'subject:(Freeport OR Wastrel OR Salazar OR Zechary)',
    'subject:(Hobbity OR hobbit OR halfling)',
    'subject:(Cthulhu OR "call to madness")',
    'subject:(Dolmenwood OR Gonzadrel)',
    'subject:(Pathfinder OR PF2E)',
    'subject:(Loudwater OR Spellgard OR Caledon)',
    'subject:(campaign OR adventure OR session)',
    # Searches involving group members with game keywords
    '{from:les.blackwell@gmail.com from:theblackcobb@hotmail.com} (DND OR D&D OR campaign OR adventure OR character OR session OR Daggerdale OR Eastwitch OR Freeport)',
    '{from:contact@toddburry.com from:todd.burry@gmail.com from:tburry@dymaxium.com} (DND OR D&D OR campaign OR adventure OR character OR session OR Freeport OR Eastwitch)',
    '{from:snahfu@gmail.com from:asteroid_pillow@hotmail.com} (DND OR D&D OR campaign OR Daggerdale OR Loudwater)',
    '{from:gus.miranda@gmail.com from:gmiranda@ncf.ca} (DND OR D&D OR campaign OR adventure OR character OR Hobbity OR Cthulhu)',
    '{from:scunny1973@gmail.com from:SCUNNY1973@aol.com} (DND OR D&D OR campaign OR adventure)',
    # Broader in-universe content searches
    'subject:(handout OR narrative OR "character sheet" OR backstory)',
    'subject:("roll initiative" OR "session 0" OR "level up")',

    # -----------------------------------------------------------------------
    # Tier 2: Pure sender-cluster searches (NO keyword requirement)
    # -----------------------------------------------------------------------
    # These catch campaign threads with oblique subjects (e.g. "Political
    # bardery", inside jokes, character names not in keyword lists). Every
    # mail from/to a group member is pulled; classification + dedup handles
    # the rest. Added 2026-04-06 after discovering coverage gaps.
    #
    # Note: These will return non-campaign mail (personal, work, etc.) that
    # the classifier will route to Meta & OOC or skip. That's by design —
    # better to over-fetch and filter than to miss in-universe content.
    # -----------------------------------------------------------------------

    # Les Blackwell — all addresses
    'from:les.blackwell@gmail.com',
    'from:theblackcobb@hotmail.com',

    # Todd Burry — all addresses
    'from:contact@toddburry.com',
    'from:todd.burry@gmail.com',
    'from:toddburry@hotmail.com',
    'from:myself@toddburry.com',
    'from:tburry@dymaxium.com',

    # Gus Miranda — all addresses
    'from:gus.miranda@gmail.com',
    'from:gmiranda@ncf.ca',
    'from:gusmiranda@gmail.com',
    'from:gmiranda@canada.com',

    # Scott McLaren — all addresses
    'from:scunny1973@gmail.com',
    'from:SCUNNY1973@aol.com',
    'from:smclaren@canusacps.shawcor.com',
    'from:smclaren@husky.on.ca',

    # Steve Hicks — all addresses
    'from:snahfu@gmail.com',
    'from:Steven.Hicks@telus.com',
    'from:asteroid_pillow@hotmail.com',
    'from:snah@rogers.com',

    # Casey Bauman-Wike — all addresses
    'from:hellocasey@gmail.com',
    'from:beljuril@hotmail.com',

    # Alex Francom
    'from:jeffreyafrancom@gmail.com',

    # Rob Schmidt — all addresses
    'from:robert.ak.schmidt@gmail.com',
    'from:rschmidt@shawcable.com',
    'from:rschmid1@uwinnipeg.ca',
]

# Campaign classification rules — maps keywords in subject/body to folders.
# Checked in order; first match wins. More specific rules first.
CAMPAIGN_RULES = [
    # Current campaigns
    (['thistle ridge', 'chrysalis', 'greenwood farm', 'dagger falls',
      'abbot ambershields', 'coventina', 'jasper hawkford', 'lucan alavandor',
      'ser rowan', 'jeska', 'charrah', 'aisling', 'maeliticus',
      'birchgrove', 'vessuvian'], 'Daggerdale'),
    (['hobbity', 'hobbit', 'spottle', 'boffo', 'halfling adventure',
      'wedge', 'huddle farm'], 'Hobbity Adventure'),
    (['cthulhu', 'call to madness', 'lovecraft', 'sanity',
      '1920s', 'toronto 1921'], 'Call of Cthulhu'),
    (['dolmenwood', 'gonzadrel'], 'Gonzadrel'),
    # Historical campaigns
    (['eastwitch', 'waldheim', 'bin fletcher', 'green grizzly',
      'dargar'], 'Eastwitch'),
    (['freeport', 'wastrel', 'salazar', 'zechary', 'zech',
      'smiling jack', 'scarbelly', 'bloody vengeance', 'raidfest',
      'gaffer', 'captain lydon', 'isle of the lich'], 'Wastrel'),
    (['avilund', 'caledon', 'heirgallad', 'barbarossa',
      'online daggerdale', 'daggerdale wiki'], 'Avilund'),
    (['loudwater', 'spellgard'], 'Daggerdale'),  # Loudwater was a Daggerdale-era campaign
    (['waterdeep nights'], 'Waterdeep Nights'),
    (['fox in the henhouse', 'archendale', 'tomdril', 'hollowbough'], 'Fox in the Henhouse'),
    (['thesk'], 'Thesk'),
    (['uthmere'], 'Uthmere'),
    # Catch-all for general D&D group discussion
    (['dnd', 'd&d', 'dungeons', 'pathfinder', 'pf2e', 'campaign',
      'session 0', 'character sheet', 'level up'], 'Meta & OOC'),
]


# ---------------------------------------------------------------------------
# Gmail API helpers
# ---------------------------------------------------------------------------

def get_gmail_service(credentials_file='credentials.json', token_file='token.json'):
    """Authenticate and return a Gmail API service object."""
    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_file):
                print(f"ERROR: {credentials_file} not found.")
                print("Download OAuth credentials from Google Cloud Console.")
                print("See script header for setup instructions.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_file, 'w') as f:
            f.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)


def search_threads(service, query, max_results=50):
    """Search Gmail and return a list of thread IDs matching the query."""
    thread_ids = []
    page_token = None
    while len(thread_ids) < max_results:
        try:
            result = service.users().threads().list(
                userId='me', q=query, pageToken=page_token,
                maxResults=min(100, max_results - len(thread_ids))
            ).execute()
        except HttpError as e:
            print(f"  Search error: {e}")
            break
        threads = result.get('threads', [])
        if not threads:
            break
        thread_ids.extend(t['id'] for t in threads)
        page_token = result.get('nextPageToken')
        if not page_token:
            break
    return thread_ids


def fetch_thread(service, thread_id):
    """Fetch a complete thread with all messages."""
    try:
        thread = service.users().threads().get(
            userId='me', id=thread_id, format='full'
        ).execute()
        return thread
    except HttpError as e:
        print(f"  Error fetching thread {thread_id}: {e}")
        return None


def decode_body(payload):
    """Recursively extract plain text body from a Gmail message payload."""
    if payload.get('mimeType') == 'text/plain' and payload.get('body', {}).get('data'):
        return base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8', errors='replace')
    parts = payload.get('parts', [])
    # Prefer text/plain over text/html
    for part in parts:
        if part.get('mimeType') == 'text/plain' and part.get('body', {}).get('data'):
            return base64.urlsafe_b64decode(part['body']['data']).decode('utf-8', errors='replace')
    # Recurse into multipart
    for part in parts:
        if part.get('mimeType', '').startswith('multipart/'):
            text = decode_body(part)
            if text:
                return text
    # Fall back to html if no plain text
    for part in parts:
        if part.get('mimeType') == 'text/html' and part.get('body', {}).get('data'):
            html = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8', errors='replace')
            # Crude HTML strip
            text = re.sub(r'<br\s*/?\s*>', '\n', html, flags=re.IGNORECASE)
            text = re.sub(r'<[^>]+>', '', text)
            text = re.sub(r'&nbsp;', ' ', text)
            text = re.sub(r'&amp;', '&', text)
            text = re.sub(r'&lt;', '<', text)
            text = re.sub(r'&gt;', '>', text)
            text = re.sub(r'&#39;', "'", text)
            text = re.sub(r'&quot;', '"', text)
            return text
    return ''


def get_header(headers_list, name):
    """Get a header value from a list of Gmail header dicts."""
    for h in headers_list:
        if h['name'].lower() == name.lower():
            return h['value']
    return ''


def get_attachments(payload):
    """Extract attachment filenames and sizes from a message payload."""
    attachments = []
    parts = payload.get('parts', [])
    for part in parts:
        filename = part.get('filename', '')
        if filename:
            size = int(part.get('body', {}).get('size', 0))
            attachments.append({'filename': filename, 'size': size})
        # Recurse
        attachments.extend(get_attachments(part))
    return attachments


# ---------------------------------------------------------------------------
# Text processing
# ---------------------------------------------------------------------------

def strip_quotes(body):
    """
    Remove quoted reply text from an email body.
    Heuristic: stop at the first line that looks like a quote marker.
    """
    lines = body.replace('\r\n', '\n').split('\n')
    original_lines = []
    for line in lines:
        stripped = line.strip()
        # Lines starting with > are quotes
        if stripped.startswith('>'):
            break
        # "On <date> <person> wrote:" pattern
        if re.match(r'^On .+ wrote:\s*$', stripped):
            break
        # Outlook-style separator
        if stripped.startswith('-----Original Message-----'):
            break
        # Gmail-style "From:" block at end
        if re.match(r'^From:\s+.+@', stripped):
            # Check if this is part of a forwarded message block
            break
        original_lines.append(line)
    result = '\n'.join(original_lines).strip()
    return result


def identify_sender(from_header):
    """Parse a From header into (display_name, email_address)."""
    # Parse "Display Name <email@example.com>" format
    match = re.match(r'^(.*?)\s*<(.+?)>\s*$', from_header)
    if match:
        display = match.group(1).strip().strip('"')
        addr = match.group(2).strip().lower()
    else:
        addr = from_header.strip().lower()
        display = ''
    # Look up in our group member database
    known_name = EMAIL_TO_NAME.get(addr, '')
    if known_name:
        return known_name, addr
    elif display:
        return display, addr
    else:
        return addr, addr


def format_date(internal_date_ms):
    """Convert Gmail internalDate (ms since epoch) to readable date."""
    dt = datetime.fromtimestamp(int(internal_date_ms) / 1000, tz=timezone.utc)
    return dt.strftime('%d %b %Y')


def format_date_range(messages):
    """Get the date range string for a thread's messages."""
    dates = [int(m['internalDate']) for m in messages]
    start = datetime.fromtimestamp(min(dates) / 1000, tz=timezone.utc)
    end = datetime.fromtimestamp(max(dates) / 1000, tz=timezone.utc)
    if start.date() == end.date():
        return start.strftime('%d %b %Y')
    elif start.year == end.year and start.month == end.month:
        return f"{start.strftime('%d')}–{end.strftime('%d %b %Y')}"
    elif start.year == end.year:
        return f"{start.strftime('%d %b')} – {end.strftime('%d %b %Y')}"
    else:
        return f"{start.strftime('%d %b %Y')} – {end.strftime('%d %b %Y')}"


def classify_campaign(subject, body_sample):
    """Determine which campaign folder a thread belongs to."""
    text = (subject + ' ' + body_sample).lower()
    for keywords, folder in CAMPAIGN_RULES:
        for kw in keywords:
            if kw.lower() in text:
                return folder
    return 'Meta & OOC'  # Default


def make_safe_filename(s, max_len=80):
    """Convert a string to a safe filename."""
    # Remove/replace problematic characters
    s = re.sub(r'[<>:"/\\|?*]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) > max_len:
        s = s[:max_len].rsplit(' ', 1)[0]
    return s


# ---------------------------------------------------------------------------
# Archive file generation
# ---------------------------------------------------------------------------

def process_thread(thread_data):
    """
    Process a fetched Gmail thread into an archive-ready dict.
    Returns a dict with: thread_id, subject, date_range, authors,
    campaign, messages (list of processed messages), attachments,
    archive_text.
    """
    messages = thread_data.get('messages', [])
    if not messages:
        return None

    # Sort messages chronologically
    messages.sort(key=lambda m: int(m['internalDate']))

    thread_id = thread_data['id']
    first_msg = messages[0]
    headers = first_msg.get('payload', {}).get('headers', [])
    subject = get_header(headers, 'Subject') or '(no subject)'
    date_range = format_date_range(messages)

    # Collect authors and process messages
    authors = set()
    processed_msgs = []
    all_attachments = []
    body_sample = ''

    for i, msg in enumerate(messages):
        msg_headers = msg.get('payload', {}).get('headers', [])
        from_header = get_header(msg_headers, 'From')
        sender_name, sender_addr = identify_sender(from_header)
        authors.add(sender_name)
        date_str = format_date(msg['internalDate'])

        # Decode body
        raw_body = decode_body(msg.get('payload', {}))
        original = strip_quotes(raw_body)

        # Collect body sample for campaign classification
        if i == 0:
            body_sample = raw_body[:2000]

        # Collect attachments
        msg_attachments = get_attachments(msg.get('payload', {}))
        all_attachments.extend(msg_attachments)

        # Skip effectively empty messages (quote-only replies)
        if len(original.strip()) < 15:
            continue

        processed_msgs.append({
            'part_num': len(processed_msgs) + 1,
            'sender_name': sender_name,
            'sender_addr': sender_addr,
            'date': date_str,
            'message_id': msg['id'],
            'body': original,
            'attachments': msg_attachments,
        })

    if not processed_msgs:
        return None

    # Classify campaign
    campaign = classify_campaign(subject, body_sample)

    # Build authors string
    authors_str = ', '.join(sorted(authors))

    # Generate archive text
    lines = []
    lines.append('=' * 79)
    lines.append('SOURCE INFORMATION')
    lines.append('=' * 79)
    lines.append(f'Thread Subject: "{subject}"')
    lines.append(f'Gmail Thread ID: {thread_id}')
    lines.append(f'Date Range: {date_range}')
    lines.append(f'Authors: {authors_str}')
    lines.append(f'Campaign: {campaign}')
    lines.append(f'Content Type: Email correspondence')
    lines.append(f'Extracted: {datetime.now().strftime("%Y-%m-%d")} by Merrydale Extractor')
    if all_attachments:
        att_names = ', '.join(a['filename'] for a in all_attachments)
        lines.append(f'Attachments: {att_names}')
    lines.append('=' * 79)
    lines.append('')

    for pm in processed_msgs:
        title = f"PART {pm['part_num']}: {pm['sender_name'].upper()} ({pm['date']})"
        lines.append(title)
        lines.append('-' * len(title))
        lines.append(f"Source: Message {pm['message_id']}")
        lines.append(f"From: {pm['sender_addr']}")
        lines.append('')
        lines.append(pm['body'])
        if pm['attachments']:
            lines.append('')
            lines.append('ATTACHMENTS:')
            for att in pm['attachments']:
                size_kb = att['size'] / 1024
                lines.append(f"  - {att['filename']} (~{size_kb:.0f}K)")
        lines.append('')
        lines.append('')

    archive_text = '\n'.join(lines)

    return {
        'thread_id': thread_id,
        'subject': subject,
        'date_range': date_range,
        'authors': authors_str,
        'campaign': campaign,
        'message_count': len(messages),
        'extracted_count': len(processed_msgs),
        'attachments': all_attachments,
        'archive_text': archive_text,
    }


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def load_existing_thread_ids(archive_dir):
    """Scan existing archive .txt files for Gmail Thread IDs already processed."""
    existing = set()
    if not archive_dir or not os.path.isdir(archive_dir):
        return existing
    for root, dirs, files in os.walk(archive_dir):
        for fname in files:
            if not fname.endswith('.txt'):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    # Only read first 20 lines for the header
                    for _ in range(20):
                        line = f.readline()
                        if not line:
                            break
                        m = re.match(r'Gmail Thread ID:\s*(\S+)', line)
                        if m:
                            existing.add(m.group(1))
                            break
            except Exception:
                pass
    return existing


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Extract RPG campaign emails from Gmail into archive files.'
    )
    parser.add_argument('--output-dir', default='./extracted',
                        help='Directory for output files (default: ./extracted)')
    parser.add_argument('--archive-dir', default=None,
                        help='Existing Merrydale Handouts dir for dedup')
    parser.add_argument('--dry-run', action='store_true',
                        help='Search and report, but do not write files')
    parser.add_argument('--max-results', type=int, default=50,
                        help='Max threads per search query (default: 50)')
    parser.add_argument('--verbose', action='store_true',
                        help='Print detailed progress')
    parser.add_argument('--credentials', default='credentials.json',
                        help='Path to Google OAuth credentials file')
    parser.add_argument('--token', default='token.json',
                        help='Path to cached OAuth token file')
    args = parser.parse_args()

    # Auth
    print("Authenticating with Gmail...")
    service = get_gmail_service(args.credentials, args.token)
    profile = service.users().getProfile(userId='me').execute()
    print(f"Authenticated as: {profile['emailAddress']}")
    print()

    # Load existing thread IDs for dedup
    existing_ids = load_existing_thread_ids(args.archive_dir)
    if existing_ids:
        print(f"Found {len(existing_ids)} already-archived thread IDs for dedup.")
    print()

    # Search phase
    print("Searching for campaign threads...")
    all_thread_ids = set()
    for i, query in enumerate(SEARCH_QUERIES):
        if args.verbose:
            print(f"  Query {i+1}/{len(SEARCH_QUERIES)}: {query[:70]}...")
        ids = search_threads(service, query, args.max_results)
        new_ids = set(ids) - all_thread_ids
        all_thread_ids.update(ids)
        if args.verbose and new_ids:
            print(f"    → {len(ids)} results, {len(new_ids)} new")

    # Remove already-archived threads
    novel_ids = all_thread_ids - existing_ids
    print(f"\nFound {len(all_thread_ids)} total threads, "
          f"{len(all_thread_ids - novel_ids)} already archived, "
          f"{len(novel_ids)} new to process.")

    if not novel_ids:
        print("Nothing new to extract. Done.")
        return

    if args.dry_run:
        print("\n[DRY RUN] Would fetch and process these threads:")
        # Fetch just the metadata for a summary
        for tid in sorted(novel_ids):
            try:
                thread = service.users().threads().get(
                    userId='me', id=tid, format='metadata',
                    metadataHeaders=['Subject', 'From', 'Date']
                ).execute()
                msgs = thread.get('messages', [])
                if msgs:
                    hdrs = msgs[0].get('payload', {}).get('headers', [])
                    subj = get_header(hdrs, 'Subject') or '(no subject)'
                    print(f"  [{tid}] {subj} ({len(msgs)} messages)")
            except Exception as e:
                print(f"  [{tid}] (error: {e})")
        return

    # Fetch and process phase
    print(f"\nFetching and processing {len(novel_ids)} threads...")
    os.makedirs(args.output_dir, exist_ok=True)

    results = []
    errors = []
    skipped = []
    attachments_log = []

    for i, tid in enumerate(sorted(novel_ids)):
        if args.verbose:
            print(f"  Fetching thread {i+1}/{len(novel_ids)}: {tid}")

        thread_data = fetch_thread(service, tid)
        if not thread_data:
            errors.append(tid)
            continue

        result = process_thread(thread_data)
        if not result:
            skipped.append(tid)
            if args.verbose:
                print(f"    → Skipped (no extractable content)")
            continue

        # Determine output path
        campaign_dir = os.path.join(args.output_dir, result['campaign'])
        os.makedirs(campaign_dir, exist_ok=True)

        # Generate filename
        clean_subj = make_safe_filename(result['subject'])
        # Add date range for uniqueness
        date_part = result['date_range'].split(' – ')[0].split(' ')
        if len(date_part) >= 2:
            date_suffix = f" - {date_part[-1]} {date_part[-2] if len(date_part) > 2 else ''}"
        else:
            date_suffix = ''
        filename = f"{clean_subj}{date_suffix.strip()}.txt"
        filepath = os.path.join(campaign_dir, filename)

        # Handle filename collisions
        counter = 1
        while os.path.exists(filepath):
            filepath = os.path.join(campaign_dir, f"{clean_subj}{date_suffix.strip()} ({counter}).txt")
            counter += 1

        # Write the archive file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result['archive_text'])

        results.append({
            'thread_id': tid,
            'subject': result['subject'],
            'campaign': result['campaign'],
            'messages': result['message_count'],
            'extracted': result['extracted_count'],
            'filepath': filepath,
        })

        # Log attachments
        if result['attachments']:
            for att in result['attachments']:
                attachments_log.append({
                    'thread_id': tid,
                    'subject': result['subject'],
                    'filename': att['filename'],
                    'size': att['size'],
                })

        if args.verbose:
            print(f"    → {result['campaign']}/{filename} "
                  f"({result['extracted_count']}/{result['message_count']} messages)")

    # Write summary report
    report_path = os.path.join(args.output_dir, 'EXTRACTION_REPORT.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"Merrydale Campaign Email Extraction Report\n")
        f.write(f"==========================================\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Account: {profile['emailAddress']}\n")
        f.write(f"Threads searched: {len(all_thread_ids)}\n")
        f.write(f"Already archived: {len(all_thread_ids - novel_ids)}\n")
        f.write(f"New threads processed: {len(novel_ids)}\n")
        f.write(f"Files written: {len(results)}\n")
        f.write(f"Errors: {len(errors)}\n")
        f.write(f"Skipped (empty): {len(skipped)}\n\n")

        f.write("FILES CREATED\n")
        f.write("-" * 60 + "\n")
        by_campaign = {}
        for r in results:
            by_campaign.setdefault(r['campaign'], []).append(r)
        for campaign in sorted(by_campaign):
            f.write(f"\n{campaign}:\n")
            for r in by_campaign[campaign]:
                f.write(f"  [{r['thread_id']}] {r['subject']} "
                        f"({r['extracted']}/{r['messages']} msgs)\n")

        if attachments_log:
            f.write(f"\n\nATTACHMENTS NEEDING MANUAL DOWNLOAD\n")
            f.write("-" * 60 + "\n")
            for att in attachments_log:
                f.write(f"  Thread [{att['thread_id']}] {att['subject']}\n")
                f.write(f"    → {att['filename']} ({att['size'] / 1024:.0f}K)\n")

        if errors:
            f.write(f"\n\nERRORS\n")
            f.write("-" * 60 + "\n")
            for tid in errors:
                f.write(f"  {tid}\n")

    # Print summary
    print(f"\n{'=' * 60}")
    print(f"EXTRACTION COMPLETE")
    print(f"{'=' * 60}")
    print(f"Files written:     {len(results)}")
    print(f"Errors:            {len(errors)}")
    print(f"Skipped (empty):   {len(skipped)}")
    print(f"Attachments found: {len(attachments_log)}")
    print(f"\nOutput directory:  {args.output_dir}")
    print(f"Full report:       {report_path}")
    print()

    # Print campaign breakdown
    by_campaign = {}
    for r in results:
        by_campaign.setdefault(r['campaign'], []).append(r)
    for campaign in sorted(by_campaign):
        print(f"  {campaign}: {len(by_campaign[campaign])} files")

    if attachments_log:
        print(f"\n{len(attachments_log)} attachments need manual download.")
        print(f"See {report_path} for details.")


if __name__ == '__main__':
    main()
