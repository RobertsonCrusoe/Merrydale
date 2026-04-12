# Merrydale Repository — CLAUDE.md

## What This Is

A personal TTRPG campaign archive spanning **25+ years of gaming history (2000–2026)**. The repository is named "Merrydale" (the archive project name) and covers ~12 campaign worlds, ~2,162 files, ~24MB of content: session notes, lore documents, character records, email correspondence converted to text archives, published HTML reference documents, and supporting scripts.

**Owner:** Stephen Robertson (player in most campaigns, archive maintainer)

---

## Repository Layout

```
Merrydale-repo/
├── CLAUDE.md                   — this file
├── .gitignore                  — excludes images, PDFs, Office binaries, archives
├── docs/                       — published HTML reference documents (parchment-styled)
│   ├── index.html
│   ├── Sunblades.html
│   ├── Holy_Orders_of_Daggerdale.html
│   ├── Wonderbringer_Warsmiths_of_Daggerdale.html
│   ├── Daggerdale_Concordat.html
│   ├── Songs_of_the_Dagger_and_Other_Verses.html
│   ├── Songs_of_the_Thistle.html
│   └── Whitegate_Thunderstorm_Blackmane_Family_Trees.html
├── Handouts/                   — main archive, organized by campaign
│   ├── Daggerdale/             — primary active campaign (~1,354 files)
│   ├── Wastrel/                — Freeport pirate campaign (~322 files)
│   ├── Avilund/                — custom world campaign (~167 files)
│   ├── Uthmere/                — Golarion/PF2E campaign (~136 files)
│   ├── Eastwitch/              — earliest campaign (~68 files)
│   ├── Hobbity Adventure/      — active hobbit campaign (~26 files)
│   ├── Gonzadrel/              — Dolmenwood campaign (~22 files)
│   ├── Fox in the Henhouse/    — Archendale campaign (~12 files)
│   ├── Call of Cthulhu/        — 1920s Toronto, planning phase
│   ├── Thesk/                  — minor
│   ├── Waterdeep Nights/       — minor
│   └── Meta & OOC/             — cross-campaign correspondence (~34 files)
└── extraction/
    ├── merrydale_extractor.py  — Gmail-to-archive pipeline
    └── Archive Search Script.md — research methodology (8-prong search protocol)
```

---

## The Campaigns

### Daggerdale (Primary — Active)
- **Era:** 1480–1483 DR (Forgotten Realms, Daggerdale region)
- **System:** Pathfinder 2nd Edition
- **DM:** Les Blackwell
- **Players:** Stephen Robertson (Lucan Alavandor), Scott McLaren "Scun" (Jeska), Gus Miranda, Todd Burry, Casey Bauman-Wike "Sprout" (Kineticist)
- **Setting:** Thistle Ridge tower ruins → Dagger Falls → regional liberation arc
- **Key factions:** Sun Blades (standing army), White Cloaks (Torm), Lambent Shield (Ilmater), Wonderbringer Warsmiths, Dark Garden (shadow cult antagonists), Redjacks
- **Key NPCs:** Jasper Hawkford, Ser Rowan, Lucan Alavandor, Jeska, Charrah (antagonist)
- **Key documents:** The Chrysalis Chronicles, The Shadow Lifted (Parts 1–4 + Appendix), Chronicle of Ancient Daggerdale, Warburton's Journal, Casebooks of Lucan Alavandor, The Daggerdale Concordat 1482 DR
- **Published docs (docs/):** Sunblades.html, Holy_Orders_of_Daggerdale.html, Wonderbringer_Warsmiths_of_Daggerdale.html, Daggerdale_Concordat.html, both Songs files, Whitegate/Thunderstorm/Blackmane Family Trees

### Hobbity Adventure (Active)
- **System:** Custom Hobbit-variant D&D
- **DM:** Gus Miranda
- **Players:** Todd Burry, others
- **Setting:** Five Shires (Golarion-derived), Orlane investigation, Spottle Parlour
- **Notable:** One session recording at craig.horse link; hobbit ear design debate resolved as "slightly pointed, like a 1/4 elf"

### Wastrel / Freeport (Historical, 2001–2009)
- **System:** D&D 3E
- **DM:** Todd Burry
- **Setting:** Freeport (Green Ronin), piracy, crime syndicates, naval combat
- **Notable:** Cross-campaign cameo — NPC "Bin" appears in both Eastwitch and Freeport narratives

### Avilund (Historical, 2000s–2010s)
- **System:** D&D 3.5E
- **Scope:** Custom continent-scale setting with detailed religion (Saintly Faith / Cult of Saints), restricted magic post-Repurgo, Bloody Revolution 1348
- **Notable:** Gus's "Caledon" politics-heavy sandbox pitch (2011)

### Eastwitch (Historical, 2000–2004)
- **System:** D&D 3.5E
- **DM:** Les Blackwell
- **Notable:** Earliest surviving group correspondence (Nov 2000); "Brotherhood of the Wolf" cinematic inspiration; Les's legendary drunk email

### Call of Cthulhu (Planning, 2025)
- **System:** Call of Cthulhu
- **DM:** Gus Miranda
- **Setting:** 1920s Toronto, Prohibition era; Ambrose Small case; Uncle Harold's involvement

### Gonzadrel / Dolmenwood (Inactive, 2025)
- **DM:** Todd Burry
- **Setting:** Dolmenwood (OSR)

---

## Gaming Group

| Person | Role | Primary Character(s) |
|---|---|---|
| Les Blackwell | DM (Daggerdale, Eastwitch, others) | — |
| Stephen Robertson | Player, archive maintainer | Lucan Alavandor (Daggerdale) |
| Scott McLaren (Scun) | Player | Jeska (Daggerdale) |
| Gus Miranda | Player, DM (Hobbity, CoC) | Various |
| Todd Burry | Player, DM (Wastrel, Gonzadrel) | Various |
| Casey Bauman-Wike (Sprout) | Player | Kineticist (Daggerdale) |
| Steve Hicks | Historical DM/player | — |
| Alex Francom | Historical | — |
| Rob Schmidt | Historical | — |

---

## Conventions

### In-Universe Date Format
`DD Monthname YYYY DR` — e.g., "12 Mirtul 1481 DR"

### Faction Name Capitalization
Always capitalized as proper nouns: Sun Blades, White Cloaks, Lambent Shield, Dark Garden, Redjacks, Wonderbringer Warsmiths, Tethyamar League, Free Defence League, Mule Company

### File Types in This Archive
- `.txt` — email threads extracted from Gmail, session notes, lore documents
- `.html` — published reference documents (in `docs/`)
- `.py` — extraction scripts (in `extraction/`)
- `.md` — documentation (this file, Archive Search Script.md)
- Images, PDFs, Office docs are gitignored (too large / binary)

### Narrative Attribution
In-universe documents (Sunblades, Holy Orders, Wonderbringer Warsmiths) are attributed to **Beliard Emmarask** as the fictional author/chronicler.

---

## Published HTML Documents (`docs/`)

These are polished, parchment-styled HTML reference pages. Design uses:
- Fonts: Crimson Text, IM Fell English SC (Google Fonts)
- Color palette: `--bg-parchment: #f4ead5`, `--text-heading: #4a1e08`, `--accent-border: #8b4513`
- Max content width: 900px

| File | Contents |
|---|---|
| `index.html` | Navigation hub linking all docs |
| `Sunblades.html` | Sun Blades military roster, company structure, command hierarchy (Part I — Beliard Emmarask) |
| `Holy_Orders_of_Daggerdale.html` | Lambent Shield (Ilmater), White Cloaks (Torm), and sister orders (Part II) |
| `Wonderbringer_Warsmiths_of_Daggerdale.html` | Engineering corps, artificer guilds, Gondsmen (Part III) |
| `Daggerdale_Concordat.html` | Constitutional/legal framework established 1482 DR |
| `Songs_of_the_Dagger_and_Other_Verses.html` | In-universe campaign songbook |
| `Songs_of_the_Thistle.html` | Companion songbook |
| `Whitegate_Thunderstorm_Blackmane_Family_Trees.html` | Noble house genealogies (Whitegate, Thunderstorm, Blackmane families) |

---

## Email Extraction Infrastructure

`extraction/merrydale_extractor.py` is a Python 3 Gmail pipeline that:
- Searches Gmail using 30+ queries targeting campaign names, locations, character names, and raw sender-cluster sweeps
- Extracts threads to `.txt` files with metadata headers (thread ID, date range, authors, campaign classification)
- Auto-classifies by campaign using keyword mapping
- Deduplicates via extracted thread ID tracking

`extraction/Archive Search Script.md` documents an **8-prong search methodology** for comprehensive archive research:
- Tier 1 (high-confidence): direct names, personnel, locations, events
- Tier 2 (contextual): system searches, type/category, relationship, narrator searches
- Includes a 10-step post-search verification workflow, deduplication/weighting, and body-to-index reconciliation

Tracked email addresses cover 8 group members across 24+ addresses (multiple accounts per person, Hotmail-era through Gmail).

---

## Common Tasks in This Repo

- **Writing / editing lore documents** — add NPCs, locations, factions, session recaps to the `Handouts/` archive
- **Updating published HTML docs** — editing `docs/*.html` to reflect new campaign developments; maintain parchment aesthetic
- **Researching archive content** — cross-referencing NPCs, timelines, events across thousands of files; the Archive Search Script methodology is the reference protocol
- **Email extraction runs** — running or updating `merrydale_extractor.py` to pull new campaign correspondence from Gmail
- **Family trees / genealogy** — the Whitegate, Thunderstorm, Blackmane families have documented lineages; precision matters (legitimacy, bloodlines, dates)
- **Creating new published docs** — follow existing HTML/CSS conventions in `docs/`

---

## Key Lore Reference Points

- **Daggerdale Concordat (1482 DR)** — the constitutional framework that ended the main campaign arc
- **The Chrysalis Chronicles** — 116KB comprehensive Daggerdale campaign document
- **The Shadow Lifted (Parts 1–4 + Appendix)** — campaign wrap-up narrative
- **Casebooks of Lucan Alavandor** — Stephen's character's investigation files
- **Chronicle of Ancient Daggerdale** — deep historical backstory
- **Warburton's Journal** — military intelligence from campaign events
- **Stories from the Archives** — character biographies (Garth Shanks, Tomas Quoyle, Mourn Raventree, etc.)
- **Avilund Synopsis** — 500+ line foundational document for the Avilund setting

---

## Notes on Scope

- The wiki prefix "Merrydale" is the archive project name; the campaign setting is **Daggerdale**
- The archive originally derived from a 2011–2012 Daggerdale Online Wiki, now grown to 2,162 files
- Some files are OCR'd handwritten notes from early-era campaign notebooks
- Multiple tellings of key events exist (player post-session reports vs. DM recaps) — treat as complementary perspectives
- AI-generated character/scene portraits referenced throughout but not stored in git (binary gitignore)
- "Castle Daggerdale" and "Castle Radiance" are distinct locations — don't conflate them
