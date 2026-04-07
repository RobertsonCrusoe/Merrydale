# Style Guide — Daggerdale Campaign HTML Documents

A living reference for producing accessible, semantically structured HTML documents for the Daggerdale campaign archive. All campaign HTML files should conform to these principles unless a specific document has a justified reason to deviate.

---

## 1. Core Principles

### 1.1 Semantic HTML First

Every element should describe **what the content is**, not how it looks. Styling is the job of CSS; the HTML's job is to convey meaning to browsers, screen readers, search tools, and future maintainers.

**In practice this means:**

- Use `<article>` for self-contained compositions (a treaty, a chronicle entry, a roster document).
- Use `<section>` for each thematic division within an article (e.g. "Preamble," "Provisions for Common Defense," "Religious Pluralism"). Every `<section>` should have a heading.
- Use `<header>` for the document's title block (title, subtitle, byline, date).
- Use `<footer>` for source attributions, editorial notes about provenance, and colophons.
- Use `<aside>` for editorial commentary that is not part of the primary text (e.g. GFD notes, Beliard's annotations).
- Use `<nav>` for a table of contents if the document is long enough to warrant one.
- Use `<blockquote>` for quoted material with a `cite` attribute where the source is known.
- Use `<table>` for genuinely tabular data (census figures, cost breakdowns, rosters). Never use tables for layout.
- Use `<ol>` and `<ul>` for ordered and unordered lists. Use `<dl>` (definition list) for term/definition pairs (e.g. signatory roles, god lists with annotations).
- Use `<figure>` and `<figcaption>` for any illustrative content (maps, diagrams, decorative elements) that benefits from a caption.
- Use `<em>` for stress emphasis and `<strong>` for strong importance. Do not use `<i>` or `<b>` for styling — use CSS classes instead.
- Use `<abbr>` with a `title` attribute for abbreviations and in-world acronyms on first use (e.g. `<abbr title="Daggerdale Concordat">DDC</abbr>`).
- Use `<time>` for dates where possible, even in-world dates, to signal temporal content (e.g. `<time>15 Elesias, 1482 DR</time>`).

**What to avoid:**

- `<div>` and `<span>` as structural containers when a semantic element exists. Use them only for styling hooks that have no semantic equivalent.
- Presentational HTML attributes (`align`, `bgcolor`, `border`, `width` on elements). All presentation goes in CSS.
- Heading levels chosen for size rather than hierarchy. `<h1>` is the document title; `<h2>` is a major section; `<h3>` is a subsection; and so on, strictly nested.

### 1.2 Accessibility (WCAG 2.1 AA Target)

Every document should be usable by someone navigating with a screen reader, keyboard, or high-contrast display.

**Required practices:**

- **Language declaration**: `<html lang="en">` on every document.
- **Document title**: A meaningful `<title>` in `<head>` (not just "Document").
- **Heading hierarchy**: Strictly sequential — never skip from `<h2>` to `<h4>`. Screen reader users navigate by heading level.
- **Colour contrast**: All text/background combinations must meet WCAG AA contrast ratios (4.5:1 for body text, 3:1 for large text). The archive palette has been tested against these thresholds (see §3 below).
- **Link purpose**: Link text must describe the destination — never use "click here" or bare URLs.
- **Table accessibility**: All data tables require `<caption>`, `<thead>`, `<th scope="col">` or `<th scope="row">`, and `<tbody>`. Complex tables should use `id`/`headers` attributes.
- **Image alternatives**: All `<img>` elements require `alt` text. Decorative images use `alt=""` and `role="presentation"`.
- **ARIA landmarks**: Use native HTML5 landmark elements (`<main>`, `<nav>`, `<aside>`, `<header>`, `<footer>`) rather than ARIA roles where possible. Add `aria-label` to distinguish multiple landmarks of the same type (e.g. two `<aside>` blocks).
- **Focus visibility**: Never suppress the browser's default focus indicator. Custom focus styles must be at least as visible as the default.
- **Print styles**: Include an `@media print` block. Ensure page breaks don't orphan headings from their content.

### 1.3 Document Type Conventions

The archive contains several kinds of documents. Each maps to a slightly different HTML structure:

| Document Type | Root Element | Typical Sections | Example |
|---|---|---|---|
| **Legal/Constitutional** | `<article>` | Preamble, Articles/Provisions, Signatories, Schedules | Daggerdale Concordat |
| **Roster/Org Chart** | `<article>` | Era headers, Personnel cards, Summary tables | Sun Blades Org Chart |
| **Chronicle/Narrative** | `<article>` | Chapters, Editorial notes, Appendices | Daggerdale Chronicle |
| **Gazetteer/Reference** | `<article>` | Geographic, Political, Economic, Demographic sections | DDC Gazetteer |

---

## 2. Semantic Patterns for Common Content

### 2.1 Editorial / Narrator Voice (GFD Notes, Beliard's Commentary)

These are not part of the primary source text. Mark them as `<aside>` with a consistent class:

```html
<aside class="narrator" aria-label="Editorial note by GFD">
  <p>This document is quite easy to find, but I include a copy...</p>
  <footer class="narrator-sig">—GFD</footer>
</aside>
```

Screen readers will announce these as complementary content, and users can skip past them to stay in the main text.

**Narrator aside styling:** Narrator asides (`<aside class="narrator">`) are visually distinguished by their background colour, left border, and text colour. They are **not** rendered in italic. The only italic editorial style in the archive is the `.footnote` class used for N.B. editorial notes. Do not add `font-style: italic` to the `.narrator` class.

### 2.2 Legal Articles and Provisions

Use `<section>` with a heading for each article or provision. Nested provisions get nested sections:

```html
<section id="common-defense-sunblades">
  <h2>Provisions for the Common Defense — The Sunblades</h2>
  <p>All settlements, nations and other organizations...</p>

  <section id="chain-of-command">
    <h3>Chain of Command</h3>
    <ol> ... </ol>
  </section>

  <section id="costs-and-contributions">
    <h3>Costs and Contributions</h3>
    <table> ... </table>
  </section>
</section>
```

### 2.3 Signatory Lists

Use a definition list to pair roles with names or categories:

```html
<section id="signatories">
  <h2>Signatories</h2>
  <p>As of <time>15 Elesias, 1482 DR</time>.</p>

  <h3>Voting Signatories</h3>
  <dl class="signatory-list">
    <dt>The Mayor of Dagger Falls</dt>
    <dd><!-- name if known --></dd>
  </dl>
</section>
```

### 2.4 Tabular Data (Costs, Census, Rosters)

Always use proper table markup:

```html
<table>
  <caption>Costs per Soldier, per Year</caption>
  <thead>
    <tr>
      <th scope="col">Item</th>
      <th scope="col">Cost (gp/year)</th>
      <th scope="col">Payable In-Kind</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wages</td>
      <td>95</td>
      <td>No</td>
    </tr>
    <!-- ... -->
  </tbody>
</table>
```

### 2.5 Ordered Hierarchies (Chain of Command, Org Charts)

Use nested ordered lists. For command structures where the nesting conveys reporting lines:

```html
<ol class="chain-of-command">
  <li>Consul of the Governors' Assembly
    <ol>
      <li>General
        <ol>
          <li>Captain of the Castle (4 companies)
            <ol>
              <li>4 Lieutenants</li>
              <li>12 Sergeants (3 per Lieutenant)</li>
            </ol>
          </li>
          <!-- ... -->
        </ol>
      </li>
    </ol>
  </li>
</ol>
```

### 2.6 God Lists (Approbata Deorum / Reprobata Deorum)

These are categorised lists with blanket delegations as bullet points and named deities as a comma-separated inline list. Where individual entries carry special conditions (e.g. a higher amendment threshold), mark them with an asterisk and provide a single footnote below the list.

```html
<section id="approbata-deorum">
  <h3>Approbata Deorum</h3>
  <p>Being the gods that all citizens of the dale are entitled to worship...</p>
  <ul>
    <li>All such elven deities as approved by the Ambassador from Myth Drannor</li>
    <li>All such dwarven deities as approved by the Ambassador from Tethyamar</li>
    <li>The gods of men and their exarchs including: Amaunator*, Chauntea*,
        Torm, Ilmater, Mielikki, and Tempus</li>
  </ul>
  <p class="footnote">* Removable only by unanimous vote of the Voting Signatories.</p>
</section>
```

CSS for the footnote:

```css
.footnote {
  font-size: 0.9em;
  color: var(--text-secondary);
  margin-top: var(--space-xs);
}
```

When a god-list section is followed by further content within the same parent, add `padding-bottom: var(--space-md)` to the section to prevent margin collapse.

#### N.B. Editorial Notes

Substantial editorial footnotes use the `.footnote` class with distinct styling from the short god-list asterisk notes above. These are introduced by a bold, non-italic "N.B." label and rendered in italic at a slightly larger size in the heading colour:

```css
.footnote {
  font-size: 0.95em;
  font-style: italic;
  color: var(--text-heading);    /* #4a1e08 */
}
.footnote .nb-label {
  font-style: normal;
  font-weight: bold;
}
```

In the markdown source, N.B. paragraphs begin with `N.B.` and are converted to `<p class="footnote"><span class="nb-label">N.B.</span> …</p>`. Standalone italic paragraphs (e.g. the Malveau asterisk note) also receive the `.footnote` class.

Note: Where a document uses both god-list footnotes and N.B. editorial notes, the converter's `.footnote` definition (0.95em, `--text-heading`) takes precedence. If both styles coexist in a single document, split into `.footnote` and `.footnote-nb` classes as needed.

#### Smart Quotes

The converter applies a text-node-only pass converting straight quotation marks to Unicode curly quotes. This is a rendering concern, not an editorial one — the markdown source retains straight quotes. The conversion handles double quotes (`"` → `"` / `"`), apostrophes and possessives (`'` → `'`), and opening single quotes (`'` → `'`).

### 2.7 Status Indicators — Deceased Marker (Dagger Symbol)

Personnel rosters use an inline dagger icon to mark deceased individuals. The icon is an SVG embedded as a base64 data URI, sized to match the text line height.

**Accessibility requirements:** Wrap the entire name (icon + text) in a `<span>` with `class="deceased"` and `title="Deceased"`. This ensures the tooltip fires anywhere across the name, not just over the small icon. The `<img>` carries `alt="Deceased: "` for screen readers, so the full announcement reads naturally (e.g. "Deceased: Sir Gethard Soulbright"). Do not use `<abbr>` for this — the name is not an abbreviation.

```html
<td>
  <span class="deceased" title="Deceased">
    <img class="dagger" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCA0OCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjQ4Ij4KICA8cGF0aCBkPSJNMTIgMCBMMTUgMjggTDEyIDMyIEw5IDI4IFoiIGZpbGw9IiM4YjIwMTAiIHN0cm9rZT0iIzZhMTgxMCIgc3Ryb2tlLXdpZHRoPSIwLjUiLz4KICA8cGF0aCBkPSJNMTIgNCBMMTMgMjQgTDEyIDI3IEwxMSAyNCBaIiBmaWxsPSIjYTAzMDIwIiBvcGFjaXR5PSIwLjQiLz4KICA8cmVjdCB4PSI1IiB5PSIzMCIgd2lkdGg9IjE0IiBoZWlnaHQ9IjMiIHJ4PSIxIiBmaWxsPSIjOGI0NTEzIiBzdHJva2U9IiM2YTM0MTAiIHN0cm9rZS13aWR0aD0iMC40Ii8+CiAgPHJlY3QgeD0iMTAiIHk9IjMzIiB3aWR0aD0iNCIgaGVpZ2h0PSIxMCIgcng9IjAuOCIgZmlsbD0iIzVhM2QyMCIgc3Ryb2tlPSIjM2EyYTEwIiBzdHJva2Utd2lkdGg9IjAuNCIvPgogIDxsaW5lIHgxPSIxMCIgeTE9IjM1IiB4Mj0iMTQiIHkyPSIzNSIgc3Ryb2tlPSIjM2EyYTEwIiBzdHJva2Utd2lkdGg9IjAuMyIgb3BhY2l0eT0iMC41Ii8+CiAgPGxpbmUgeDE9IjEwIiB5MT0iMzciIHgyPSIxNCIgeTI9IjM3IiBzdHJva2U9IiMzYTJhMTAiIHN0cm9rZS13aWR0aD0iMC4zIiBvcGFjaXR5PSIwLjUiLz4KICA8bGluZSB4MT0iMTAiIHkxPSIzOSIgeDI9IjE0IiB5Mj0iMzkiIHN0cm9rZT0iIzNhMmExMCIgc3Ryb2tlLXdpZHRoPSIwLjMiIG9wYWNpdHk9IjAuNSIvPgogIDxsaW5lIHgxPSIxMCIgeTE9IjQxIiB4Mj0iMTQiIHkyPSI0MSIgc3Ryb2tlPSIjM2EyYTEwIiBzdHJva2Utd2lkdGg9IjAuMyIgb3BhY2l0eT0iMC41Ii8+CiAgPGVsbGlwc2UgY3g9IjEyIiBjeT0iNDQiIHJ4PSIzIiByeT0iMiIgZmlsbD0iIzhiNDUxMyIgc3Ryb2tlPSIjNmEzNDEwIiBzdHJva2Utd2lkdGg9IjAuNCIvPgo8L3N2Zz4="
         alt="Deceased: " role="img">Sir Gethard Soulbright
  </span>
</td>
```

**CSS for the dagger icon and deceased wrapper:**

```css
img.dagger {
  height: 1.1em;
  width: auto;
  vertical-align: -0.15em;
  margin-right: 2px;
  display: inline;
}

.deceased {
  cursor: help;  /* signals that a tooltip is available */
}
```

**When to use:** Any personnel table or roster where a named individual is known to be dead. The dagger always precedes the name. Do not use the dagger for organisations that have been dissolved, positions that have been vacated, or other non-death statuses — those are handled by the status column (e.g. "Disbanded", "Retired").

**SVG source:** The base64 string encodes a small inline SVG of a stylised dagger in the archive's red-brown palette (`#8b2010` blade, `#8b4513` crossguard, `#5a3d20` grip). If you need to regenerate or modify it, decode the base64 and edit the SVG paths directly.

### 2.8 Standard Bullet Style

All unordered lists use a four-pointed star (✦, Unicode `\2726`) in the accent border colour as the bullet marker. This replaces the browser's default disc. The style was established in the Daggerdale Concordat and applies across all campaign documents.

```css
ul {
  list-style: none;
  padding-left: var(--space-md);
}

ul > li {
  padding: 3px 0;
  padding-left: 20px;
  position: relative;
}

ul > li::before {
  content: "\2726";
  position: absolute;
  left: 0;
  color: var(--accent-border);
  font-size: 0.8em;
}
```

Where a document inherits or nests lists (e.g. TOC sub-lists with their own styling), scope the standard bullet to the appropriate container to avoid conflicts.

### 2.9 Scrollable Wide Tables — Drag-to-Scroll

Tables wider than the viewport require a `.table-scroll` wrapper for horizontal scrolling. In addition to the native scrollbar, add a JavaScript-driven click-and-drag behaviour so users can grab the table area and scroll horizontally without accidentally selecting text.

```html
<div class="table-scroll">
  <table id="personnel-table">...</table>
</div>
```

**CSS:**
```css
.table-scroll {
  overflow-x: auto;
  margin: var(--space-lg) 0;
  cursor: grab;
}

.table-scroll.active {
  cursor: grabbing;
  user-select: none;
}
```

**JavaScript** (place at end of `<body>`):
```js
document.querySelectorAll('.table-scroll').forEach(el => {
  let isDown = false, startX, scrollLeft;
  el.addEventListener('mousedown', e => {
    if (e.target.closest('a, button, input, [data-sort]')) return;
    isDown = true;
    el.classList.add('active');
    startX = e.pageX - el.offsetLeft;
    scrollLeft = el.scrollLeft;
  });
  el.addEventListener('mouseleave', () => { isDown = false; el.classList.remove('active'); });
  el.addEventListener('mouseup', () => { isDown = false; el.classList.remove('active'); });
  el.addEventListener('mousemove', e => {
    if (!isDown) return;
    e.preventDefault();
    el.scrollLeft = scrollLeft - (e.pageX - el.offsetLeft - startX);
  });
});
```

The `[data-sort]` exclusion ensures sortable column headers remain clickable. Add exclusions for any other interactive elements within scrollable tables.

---

## 3. Visual Design System

### 3.1 Typography

| Role | Font | Fallback Stack | Weight |
|---|---|---|---|
| **Display / Headings** | IM Fell English SC | Palatino Linotype, serif | 400 |
| **Body Text** | Crimson Text | Palatino Linotype, Book Antiqua, Palatino, Georgia, serif | 400, 600, 700 |
| **Body Italic** | Crimson Text Italic | — | 400 italic |

Import via Google Fonts:
```
@import url('https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400&family=IM+Fell+English+SC&display=swap');
```

Base font size: `20px` (set on `body` or `html`). This applies to all document types. **Every document must include an explicit `font-size: 20px` declaration on the `body` element.** Omitting it causes the browser to fall back to 16px, which makes relative-sized content elements (cards, narrator blocks, table cells) unreadably small.

Body line-height: `1.55` for legal/constitutional documents (denser than the `1.45` used in roster cards, to evoke legal typesetting). Roster and narrative documents continue to use `1.45`–`1.6`.

### 3.2 Colour Palette

All colours have been tested for WCAG AA compliance against the backgrounds they appear on.

| Token | Hex | Use | Contrast vs #f4ead5 |
|---|---|---|---|
| `--bg-parchment` | `#f4ead5` | Page background | — |
| `--bg-inset` | `#f7f0e0` | Narrator/aside blocks, inset panels | — |
| `--bg-section-header` | `#ede0c8` | Section heading backgrounds (flat fallback) | — |
| `--bg-section-gradient` | `linear-gradient(90deg, #f4ead5, #e8d5b0, #f4ead5)` | `h2` and era-header gradient — fades from page background through a warm band and back out. | — |
| `--bg-subsection-gradient` | `linear-gradient(90deg, #f4ead5, #efe3c8, #f4ead5)` | `h3` subsection gradient — a lighter variant of the section gradient. | — |
| `--font-display` | `'IM Fell English SC', 'Palatino Linotype', serif` | Display font variable — used on headings, `strong`, card subtitles, and captions. | — |
| `--text-body` | `#2c1e0e` | Primary body text | 12.8:1 ✓ |
| `--text-heading` | `#4a1e08` | H1, H2 headings | 9.5:1 ✓ |
| `--text-subheading` | `#6b2a0a` | H3, section titles | 6.7:1 ✓ |
| `--text-secondary` | `#5a3d20` | Bylines, signatures, secondary info | 5.8:1 ✓ |
| `--text-aside` | `#3a2a15` | Narrator/aside text | 10.2:1 ✓ |
| `--accent-border` | `#8b4513` | Left borders on major sections | — |
| `--accent-border-light` | `#c9a96e` | Horizontal rules, subtle borders | — |
| `--accent-link` | `#3a5a7c` | Hyperlinks, cross-references | 5.1:1 ✓ |

### 3.3 Document-Type Visual Modifiers

**Legal/Constitutional documents** (like the Concordat) add:

- A centred title block with small-caps heading and formal subtitle
- Slightly tighter line-height (`1.55`) to evoke legal typesetting
- Indented provisions within sections (left margin on nested `<section>` elements)
- A ruled border above and below the signatory block
- A more restrained use of decorative elements compared to roster documents

**Roster documents** continue to use the existing card-based layout system.

**Era headers (all document types):** The `.era-header` class uses the gradient background (`--bg-section-gradient`) rather than the flat `--bg-section-header`. This creates a subtle vellum-band effect that fades from the page background through a warm centre band and back out. The flat colour remains available as a fallback or for lower-level section headings where the gradient would be too prominent.

### 3.4 Spacing Scale

Use a consistent spacing scale derived from a `16px` base:

| Token | Value | Use |
|---|---|---|
| `--space-xs` | `4px` | Tight gaps (label to value) |
| `--space-sm` | `8px` | Intra-component spacing |
| `--space-md` | `16px` | Standard paragraph/section gaps |
| `--space-lg` | `24px` | Between major sections |
| `--space-xl` | `36px` | Between top-level divisions |

### 3.5 Responsive and Print Behaviour

- Maximum content width: `900px`, centred with auto margins.
- At viewport widths below `600px`, reduce heading sizes by ~20% and body padding to `16px`.
- Print stylesheet: suppress decorative backgrounds, force black-on-white for text, enforce `page-break-after: avoid` on all headings.

---

## 4. File Naming and Metadata

### 4.1 File Names

Pattern: `{Document_Title}.html` — use underscores for spaces, no location suffix.

Examples:
- `Daggerdale_Concordat.html`
- `Sun_Blades_Org_Chart.html`
- `Holy_Orders_of_Daggerdale.html`

### 4.2 Folder Structure — Editorial Pipeline

Campaign HTML documents pass through three stages, each with its own folder:

| Folder | Contents | Purpose |
|---|---|---|
| `Editorial/` | Markdown (`.md`) | Source of truth. All substantive edits happen here. |
| `Drafts/` | HTML (`.html`) | Browser-reviewable HTML generated from Editorial markdown while the document is still being revised. Not synced to the repository or GitHub Pages. |
| `Published/` | HTML (`.html`) | Final HTML, synced to `docs/` in the repository for GitHub Pages serving. |

**Workflow:**

1. Edit the markdown in `Editorial/`.
2. Generate HTML into `Drafts/` for browser review (layout, cards, tables, dagger glyphs, etc.).
3. Iterate — revise the markdown, regenerate into `Drafts/` — until satisfied.
4. When the document is ready, move or regenerate the HTML into `Published/` and sync to `docs/`.

**Rules:**

- Never edit `Published/` or `Drafts/` HTML directly as the primary edit. The markdown in `Editorial/` is always the source of truth. Targeted patches to HTML are acceptable for small fixes (e.g. a typo caught after generation), but any substantive change must originate in the markdown and be regenerated.
- Drafts are working files. They may be incomplete, contain known issues, or reflect a document mid-revision. They are not committed to the repository.
- A document may skip `Drafts/` and go straight to `Published/` if the author is confident in the conversion. The stage exists for review, not as a mandatory gate.

### 4.3 HTML Metadata

Every document should include:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="[One-sentence description of the document]">
<title>[Document Title]</title>
```

---

## 5. Editorial Conventions (Cross-Reference)

The authoritative editorial rules are in **STANDING RULES — Copy Editing**. The following are restated here for convenience, as they affect HTML structure and conversion:

- **Reproduce, don't rewrite**: Player-authored material is preserved exactly. Use `<blockquote>` with attribution, never paraphrase.
- **Flag contradictions, don't paper over them**: When source material conflicts, present both facts with dates. Use a `.contradiction` box (see existing roster files for the pattern).
- **No inline source citations**: A `<footer>` at the document level listing sources is sufficient.
- **The Concordat is the structural anchor**: Military organization documents should cross-reference the Concordat's provisions where relevant.

### 5.1 Punctuation — Dashes

Two dash characters are used. They are not interchangeable.

- **Em-dash (—)**: Used *only* in running prose for parenthetical interruptions, abrupt breaks, or appositive phrases. Always closed (no spaces on either side). Example: "He is notably a follower of Torm rather than Amaunator, despite commanding—and being widely respected within—an overwhelmingly Amaunatori institution."
- **En-dash (–)**: Used for *all other* dash functions: structural separators between a name/label and its description (e.g. `**Captain Lucius** – Captain of the 1st Company`), numerical ranges (e.g. `1479–1483 DR`), compound attributives (e.g. `Dagger Falls–Castle Radiance road`), and any non-prose connective. An en-dash used as a structural separator takes a thin space or regular space on each side for readability; an en-dash used in a range is closed.

In HTML output, use `&mdash;` and `&ndash;` respectively, or the literal Unicode characters (U+2014, U+2013).

### 5.2 Capitalisation — "the Dale"

"The Dale" is capitalised *only* when it refers to Daggerdale as a political entity, analogous to "the Crown" for the monarchy. When used as a common noun for the geographic valley — even when the referent is unambiguously Daggerdale — it remains lowercase.

- **Capitalised (political entity):** "the military establishment of the Dale"; "the Dale's governors"; "the Concordat binds the Dale."
- **Lowercase (geographic/common noun):** "across the dale"; "all men in the dale required to serve"; "the most widely dispersed company in the dale."

The test: if you could substitute "the polity" or "the state" and the sentence still reads correctly, capitalise. If "the valley" or "the region" fits better, leave it lowercase.

### 5.3 Punctuation — American Convention for Commas and Periods

Commas and periods always go inside closing quotation marks, regardless of whether they are part of the quoted material. This is the American typographic convention and applies throughout the archive.

- **Correct:** He called them "the finest soldiers in the Dale," though others disagreed.
- **Incorrect:** He called them "the finest soldiers in the Dale", though others disagreed.

Question marks and exclamation marks follow logic: inside if part of the quote, outside if part of the surrounding sentence.

---

## 6. Heading Navigation Pattern

Every `<h2>`, `<h3>`, and `<h4>` must carry both an `id` attribute (for incoming links) and a child `<a>` element that links upward in the heading hierarchy:

- `<h2>` links to `#toc` (the table of contents).
- `<h3>` links to its parent `<h2>` section's id.
- `<h4>` links to its parent `<h3>` section's id.

```html
<h2 id="companies"><a href="#toc">III. Companies</a></h2>
  <h3 id="1st-company-dalehearth"><a href="#companies">1st Company – "Dalehearth"</a></h3>
    <h4 id="1st-escort-cormanthor"><a href="#1st-company-dalehearth">1st Company, Escort Platoon – Cormanthor (1483)</a></h4>
```

This gives the reader a way to navigate upward by clicking any heading. Every heading that appears in the document must also appear in the `<nav id="toc">` table of contents.

**No heading should be left without an id and an anchor link.** This was the cause of broken navigation in the Sun Blades document where Section I subheadings had plain `<h3>` tags with no ids or links.

---

## 7. Card Layout System (Roster Documents)

Roster documents use a card system to visually group organisational units (companies, command groups, divisions). Cards are `<div>` elements with class-based styling — they have no semantic HTML equivalent, so `<div>` is correct here.

### 7.1 Card Classes

| Class | Border Colour | Background | Use |
|---|---|---|---|
| `.card` | `#8b4513` (saddlebrown) | `#f7f0e0` (inset) | Base card — standalone entries |
| `.card-company` | `#6b7c4a` (olive) | `#f5f4e8` | Company-level cards |
| `.card-command` | `#b8860b` (dark goldenrod) | `#f9f4e2` | Command-level cards |
| `.card-division` | `#4a6a8a` (steel blue) | — | Division-level cards |

### 7.2 Card Internal Structure

```html
<div class="card card-company">
    <h3 id="1st-company-dalehearth"><a href="#companies">1st Company – "Dalehearth"</a></h3>
    <p class="card-subtitle">Garrison of Dagger Falls</p>
    <p class="assignment"><strong>Assignment:</strong> Dagger Falls – Town walls, Tower, gates</p>
    <p class="status"><strong>Strength:</strong> 4 platoons</p>
    <aside class="narrator">
        <p>Primary garrison of the town...</p>
    </aside>
    <p><strong>Captain Lucius</strong>—Captain of the 1st Company...</p>
</div>
```

### 7.3 Card Subtitle (Display Font)

The `.card-subtitle` class renders the company's operational descriptor (e.g. "Garrison of Dagger Falls," "Mountain Operations") in the display font at a subdued size:

```css
.card-subtitle {
    font-family: var(--font-display);
    font-size: 0.95em;
    color: var(--text-secondary);
    margin: var(--space-xs) 0;
}
```

### 7.4 Field Labels — Small Caps

Field labels like "Assignment" and "Strength" use small caps rather than full capitals to reduce visual weight:

```css
.assignment strong,
.status strong {
    font-weight: 600;
    font-family: var(--font-display);
    color: var(--text-subheading);
    font-variant: small-caps;
    text-transform: lowercase;
    letter-spacing: 0.04em;
}
```

The `text-transform: lowercase` feeds lowercase letters to `font-variant: small-caps`, which renders them as small capitals. The HTML source can use any case (the original "ASSIGNMENT:" will be normalised by CSS).

### 7.5 Canonical CSS for Card Element Classes

**This section is normative.** When building or rebuilding any roster document, these CSS definitions must be used exactly. Do not invent custom font sizes, colours, or line-heights for these classes. The values below are drawn from the Sun Blades document (the archive's first and most thoroughly reviewed roster) and constitute the standard.

**Rationale:** The Holy Orders rebuild (2026-04) diverged from the Sun Blades by shrinking `.rank`, `.assignment`, `.detail`, and `.footnote` to 0.85–0.9em with non-standard colours. This created a visible mismatch between documents that should look like they belong to the same archive. The root cause was that the style guide specified class names and structure but not the actual CSS values, so the rebuild agent improvised.

```css
/* Field lines — rank, assignment, status, strength */
.rank {
    margin: var(--space-xs) 0;
    font-weight: normal;
}

.rank strong {
    font-weight: 600;
    font-family: var(--font-display);
    color: var(--text-subheading);
}

.assignment,
.status {
    margin: var(--space-xs) 0;
    font-weight: normal;
}

.assignment strong,
.status strong {
    font-weight: 600;
    font-family: var(--font-display);
    color: var(--text-subheading);
    font-variant: small-caps;
    text-transform: lowercase;
    letter-spacing: 0.04em;
}

/* Card body text — no font-size reduction */
.detail {
    margin: var(--space-sm) 0;
    color: var(--text-body);
    line-height: 1.55;
}

/* Footnotes (N.B. blocks) */
.footnote {
    font-size: 0.95em;
    font-style: italic;
    color: var(--text-heading);
    margin: var(--space-sm) 0;
}

.footnote .nb-label {
    font-weight: 600;
    font-style: normal;
    letter-spacing: 0.04em;
}

/* Narrator / editorial aside (used only where aside styling is appropriate) */
.narrator {
    color: var(--text-aside);
}
```

**Key constraint:** None of `.rank`, `.assignment`, `.status`, or `.detail` set a `font-size`. They inherit the body size (20px at desktop). Only `.footnote` reduces size, and only to `0.95em`. Do not add `font-size` to these classes.

---

## 8. Title Block Pattern

The document title block uses a split structure: the title on its own line with decorative swords, and the subtitle below it centred and balanced.

```html
<header>
    <h1>⚔ The Sun Blades ⚔</h1>
    <p class="document-subtitle">The Strength, Organization &amp; Disposition of Daggerdale's Standing Army</p>
    <p><em>Part I of The Military Establishment of Daggerdale — A report prepared for...</em></p>
</header>
```

### 8.1 Subtitle Styling

```css
.document-subtitle {
    font-family: var(--font-display);
    font-size: 1.3em;
    color: var(--text-subheading);
    margin: 0 0 var(--space-md) 0;
    font-weight: 400;
    letter-spacing: 0.02em;
    text-align: center;
    text-wrap: balance;
}
```

Key points:

- `text-wrap: balance` distributes words across lines to avoid orphans (e.g. a single word on the last line). Degrades gracefully in older browsers.
- `text-align: center` must be set explicitly because the global `p { text-align: justify }` rule wins over the `header { text-align: center }` inheritance (element selectors beat inherited values).
- Bottom margin should equal the gap above the subtitle (from the h1's bottom margin) for visual symmetry.

---

## 9. Table Sizing

### 9.1 Autofitting Columns

Avoid setting large `min-width` values on table columns. These create excessive white space when content is shorter than the minimum. Instead:

- Use `white-space: nowrap` on narrow columns where content should never wrap (numbers, abbreviations, short labels).
- Use `text-align: center` on numeric columns.
- Let the browser's table layout algorithm distribute remaining width to text-heavy columns (Title, Assignment, Notes).
- Reserve `min-width` for the personnel table's Name and Notes columns where a minimum is genuinely needed for readability.

### 9.2 Location Abbreviations in Tables

To save horizontal space in assignment/location columns, use standard abbreviations with a legend footnote:

| Abbreviation | Location |
|---|---|
| CR | Castle Radiance |
| DF | Dagger Falls |
| TR | Thistle Ridge |
| FL | Fort Luminous |
| TV | Tesh Valley |

Farm names drop the word "Farm" (e.g. "Crossed Blades" not "Crossed Blades Farm"). Add a legend footnote below the table: "CR = Castle Radiance; DF = Dagger Falls; TR = Thistle Ridge; FL = Fort Luminous; TV = Tesh Valley."

---

## 10. Era-Note Boxes

The `.era-note` class marks a boxed contextual summary that sets the historical scene for a section. It should contain only the scene-setting summary — not detailed exposition that belongs in body text.

**Correct pattern:**

```html
<div class="era-note">
    <p>In Elesias 1482, the Daggerdale Concordat transferred administrative and financial control of the Sun Blades from the Church of Amaunator to the newly formed Governors' Assembly. What changed was the governance, the funding model, and the imposition of a new divisional superstructure.</p>
</div>

<p>The Concordat expanded the Sun Blades from a force of roughly four hundred to a planned Standard Order of 1,296 soldiers...</p>
```

**Incorrect pattern (merging exposition into the era-note):**

```html
<!-- DON'T do this — the box becomes too long and buries important details -->
<div class="era-note">
    <p>In Elesias 1482, the Daggerdale Concordat transferred... What changed was the governance... The Concordat expanded the Sun Blades from... Costs are shared... The General holds a seat... An attack on one signatory is to be considered an attack on all.</p>
</div>
```

The era-note is a visual signpost, not a container for all contextual content. If it grows beyond 3–4 sentences, split the detailed exposition into body paragraphs below it.

---

## 11. Known Failure Modes

### 11.1 CRITICAL: Curly Quotes in HTML Attributes

**Symptom:** Card divs, navigation links, table classes, or other styled elements silently fail to render. The HTML source looks correct on visual inspection — `class="card card-company"` appears normal — but the browser ignores the class, id, or href.

**Root cause:** A text-processing pass (e.g. em-dash conversion, smart-quote conversion, or punctuation normalisation) converted straight double quotes (`"`, U+0022) inside HTML tags to Unicode right double quotation marks (`"`, U+201D). The browser's HTML5 parser does not recognise curly quotes as attribute delimiters, so `class="card card-company"` is parsed as an unquoted attribute with value `\u201ccard` — the class `card-company` is silently discarded.

**Why it's hard to spot:** Curly quotes and straight quotes are visually near-identical in most code editors and terminal fonts. The HTML source reads correctly to the human eye. The only reliable way to detect the problem is:

1. **html5lib parsing test** (Python):
   ```python
   import html5lib
   doc = html5lib.parse(content, namespaceHTMLElements=False)
   cards = [d for d in doc.iter('div') if 'card-company' in d.get('class', '')]
   print(len(cards))  # Should be 13, not 5
   ```
2. **Hex inspection of attribute quotes:**
   ```python
   for m in re.finditer(r'.{3}card card-company.{3}', content):
       print([(c, hex(ord(c))) for c in m.group()])
       # U+0022 = correct; U+201C/U+201D = broken
   ```

**Fix:** Replace curly quotes with straight quotes *only inside HTML tags*, leaving prose text untouched:

```python
import re
def fix_quotes_in_tags(match):
    tag = match.group()
    return tag.replace('\u201c', '"').replace('\u201d', '"').replace('\u2018', "'").replace('\u2019', "'")

fixed = re.sub(r'<[^>]+>', fix_quotes_in_tags, content)
```

**Prevention:** Any automated text-processing pass (smart quotes, em-dash conversion, punctuation normalisation) must operate only on text nodes, never on HTML tag content. When running such passes on an HTML file, either (a) parse the HTML first and walk text nodes only, or (b) run the pass on the markdown source before HTML generation. **Never run a naive find-and-replace across the raw HTML string.**

### 11.2 Parallel Agents Editing the Same File

**Symptom:** Some edits from one agent appear while others are lost; the file may contain a mixture of changes from two different operations that partially overwrite each other.

**Root cause:** Two agents launched in parallel both read the same file at the same moment, made their respective changes to their own copy, and wrote back. The second write overwrites the first agent's changes.

**Prevention:** Never launch parallel agents that will edit the same file. If two types of changes are needed on the same file (e.g. em-dash fixes and TOC generation), run them sequentially — complete one, verify, then start the next. Parallel agents are safe only when they operate on different files.

### 11.3 Global CSS Inheritance Surprises

**Symptom:** An element inside `<header>` (or another container with `text-align: center`) renders as justified or left-aligned instead of centred.

**Root cause:** A more specific element selector (e.g. `p { text-align: justify }`) overrides the inherited `text-align: center` from the parent. In CSS, a direct element selector always beats inheritance, regardless of where the parent rule is declared.

**Fix:** Add an explicit `text-align` to the specific class that needs it (e.g. `.document-subtitle { text-align: center }`).

**General principle:** When a CSS property set on a parent doesn't seem to reach a child element, check whether any element-level selector on the child is overriding the inherited value.

---

## Revision History

| Date | Change |
|---|---|
| 3 April 2026 | Initial version, drafted alongside the Concordat HTML. |
| 4 April 2026 | Added §5.1 (dash conventions: em-dash for prose, en-dash for structure/ranges) and §5.2 (capitalisation rule for "the Dale" as political entity vs. common noun). |
| 4 April 2026 | Added `--bg-section-gradient` token to §3.2 colour palette; added era-header gradient note to §3.3 document-type visual modifiers. |
| 5 April 2026 | Added base font size (`20px`) to §3.1 typography. Added `--bg-subsection-gradient`, `--font-display` tokens to §3.2. Bold `h1`, display font on `strong`, gradient backgrounds on `h2`/`h3` now standard across all documents. |
| 7 April 2026 | Added §4.2 (folder structure and editorial pipeline: Editorial → Drafts → Published). Renumbered §4.2 HTML Metadata to §4.3. |
| 7 April 2026 | §5 now explicitly defers to STANDING RULES — Copy Editing as the authoritative location for editorial rules. |
| 7 April 2026 | §3.1: Strengthened base font size rule — explicit `font-size: 20px` on `body` is now mandatory, not merely recommended. |
| 7 April 2026 | Added §2.8 (standard bullet style: ✦ diamond in accent-border colour), §2.9 (drag-to-scroll JS for wide tables). Clarified narrator aside styling in §2.1: no italic on `.narrator`. |
| 7 April 2026 | Added §5.3 (American punctuation convention), §6 (heading navigation pattern), §7 (card layout system), §8 (title block pattern), §9 (table sizing and location abbreviations), §10 (era-note boxes), §11 (known failure modes: curly quotes in attributes, parallel agent edits, CSS inheritance surprises). |

| Date | Change |
|---|---|
| 3 April 2026 | Initial version, drafted alongside the Concordat HTML. |
| 4 April 2026 | Added §5.1 (dash conventions: em-dash for prose, en-dash for structure/ranges) and §5.2 (capitalisation rule for "the Dale" as political entity vs. common noun). |
| 4 April 2026 | Added `--bg-section-gradient` token to §3.2 colour palette; added era-header gradient note to §3.3 document-type visual modifiers. |
| 5 April 2026 | Added base font size (`20px`) to §3.1 typography. Added `--bg-subsection-gradient`, `--font-display` tokens to §3.2. Bold `h1`, display font on `strong`, gradient backgrounds on `h2`/`h3` now standard across all documents. |
| 7 April 2026 | Added §4.2 (folder structure and editorial pipeline: Editorial → Drafts → Published). Renumbered §4.2 HTML Metadata to §4.3. |
| 7 April 2026 | §5 now explicitly defers to STANDING RULES — Copy Editing as the authoritative location for editorial rules. |
| 7 April 2026 | §3.1: Strengthened base font size rule — explicit `font-size: 20px` on `body` is now mandatory, not merely recommended. |
| 7 April 2026 | Added §2.8 (standard bullet style: ✦ diamond in accent-border colour), §2.9 (drag-to-scroll JS for wide tables). Clarified narrator aside styling in §2.1: no italic on `.narrator`. |
