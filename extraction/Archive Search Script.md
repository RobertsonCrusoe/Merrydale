# Archive Search Script

A systematic method for searching a large handouts archive for material related to a specific topic. The method has two phases: an **8-prong search** that generates candidate file lists, and a **10-step post-search process** that extracts, verifies, and reconciles the findings against the target document.

The search phase is designed to move from narrow/precise searches to broad/contextual ones, progressively widening the net while filtering noise. The post-search phase handles deduplication, gap detection, full-context reading, contradiction flagging, and index reconciliation.

The eight search prongs fall into two tiers:

- **Tier 1 (Prongs 1–4):** High-confidence searches keyed to proper nouns and specific references. A hit in any Tier 1 prong is likely relevant.
- **Tier 2 (Prongs 5–8):** Broad contextual searches that generate more noise. Hits are useful mainly when they overlap with other prongs, or when Tier 1 has been exhausted and you're looking for oblique references.

Run all eight prongs, then follow the ten-step post-search process.

> **A note on diminishing returns.** Tier 2 prongs were tested against three well-documented topics in the Daggerdale archive (the Holy Orders, the Blade of the White Saint, and the Table of the Sun). On topics central to the archive's main narrative, Tier 1 prongs (1–4) captured effectively all the relevant material. Prongs 7 and 8 generated large hit lists (100+ files from Prong 7, 30+ from Prong 8) but after verification, the genuinely new, uncollated material they surfaced was minimal — a single additional file for the Holy Orders (the White Cloaks status document, caught via Prong 7), and a tangential Ardelusk journal reference (caught via Prong 8). Most Prong 7 hits were false positives from pervasive counterpart terms (e.g. "Dark Garden" or "White Cloaks" appearing in hundreds of files), and most Prong 8 hits were files already found under variant names by Tier 1.
>
> **The takeaway:** On well-documented, central topics, Tier 2 mainly serves as a confidence check that Tier 1 was thorough. On obscure or peripheral topics — where the subject rarely appears by name and is more often mentioned in passing within files about something else — Tier 2 prongs are likely to earn their keep more substantially. Budget your time accordingly: run Tier 2 on everything, but invest your reading time in Tier 2 hits proportional to how peripheral the topic is.

---

## Tier 1: High-Confidence Searches

### Prong 1: Direct Name Search

**Purpose:** Find files that explicitly name the subject.

Search for the formal names of the thing you're researching — organisation names, place names, artifact names, document titles. Use exact strings.

**Before searching:** List all known variant spellings and abbreviations. The archive is inconsistent (e.g. "Lastsun" / "Last Sun", "Sunblades" / "Sun Blades", "Bannitt" / "Banitt"). Search for every variant.

**Example (organisation):** "Lambent Shield", "Lambent Rose", "Golden Lion", "Knights of Justice", "Charter Militant"

**Example (artifact):** "Table of the Sun", "Blade of the White Saint"

---

### Prong 2: Named Personnel Search

**Purpose:** Find files about people associated with the subject, even if the subject itself isn't named.

Search for the surnames (or distinctive first names) of every known individual connected to the topic. Include commanders, associates, squires, chaplains, candidates — anyone who appears in the current compiled document or is known from prior research.

**Before searching:** Compile the full personnel list from the existing document. Don't limit yourself to major figures; minor characters sometimes appear in unexpected files with major detail.

**Caution:** Very common names (e.g. "Will", "Dale") will swamp the results. For these, combine with a second term or search only as part of a fuller name string.

**Note on character files:** Some character record files use first names rather than surnames in the filename (e.g. "Knight Commander Kassius.txt" rather than just "Kassius"). If Prong 2 misses a file you'd expect to find, check whether the archive uses a different naming convention for that individual.

**Example (organisation):** Sansum, Grendel, Derfel, Kassius, Pauldron, Soulbright, Lexinauth, Silverlance, Saddlemoor, Overcourt, Eisley, Turan, Quiggan, Durnbold

**Example (artifact):** Banitt, Ardelusk, Lumina, Drake Sterling, Invictus

---

### Prong 3: Location and Infrastructure Search

**Purpose:** Find files that discuss the physical places associated with the subject.

Search for every named location connected to the topic: forts, towers, farms, temples, roads, geographical features. Include alternate names and informal descriptions.

This prong often catches narrative files set at a location that mention the subject in passing — a scene at Fort Last Sun that offhandedly describes a knight's gear, a letter written from Liberty Hill that mentions the cathedral.

**Example (organisation):** "Fort Last Sun", "Fort Sunset", "Fort Sansum", "Shadow Dam", "Fortress Cathedral", "Shepherd's Crook"

**Example (artifact):** "Cathedral of Liberty Hill", "tomb of Ardelusk", "nave", "sarcophagus", "Tower of Liberty Hill"

---

### Prong 4: Historical Event Search

**Purpose:** Find files about battles, treaties, expeditions, trials, and other specific events that involved the subject.

Search for the names of events, battles, legal proceedings, ceremonies, and historical moments connected to the topic. Include dates in DR format where known.

Event searches tend to surface raw narrative files — session write-ups, letters, journal entries — that contain details not present in compiled sources. These are the files most likely to hold uncollated material.

**Example (organisation):** "Anathar's Dell", "Paladin's Grave", "cenotaph", "Daggerdale Expedition", "1372"

**Example (artifact):** "Saint's Battle", "Ritual of Corruption", "Army of the White Saint", "Kythorn 1", "Greengrass"

---

## Tier 2: Broad Contextual Searches

### Prong 5: Contextual System Search

**Purpose:** Find oblique references where the subject isn't named but the system it belongs to is.

Search for the institutional, theological, political, or structural framework the subject sits inside. The question this prong answers is: "What larger system does this subject belong to, and where is that system discussed?"

For a military order, that's its patron deity and church hierarchy. For a merchant house, it's trade guilds and economic systems. For a magical artifact, it's schools of magic, planar connections, or crafting traditions. For a settlement, it's the political entity it belongs to and the treaties that govern it.

**Expect noise.** This prong will hit 50+ files in a large archive. Most will be irrelevant. The value is in the 3–5 files that mention the subject in a context none of the Tier 1 prongs would catch. Filter aggressively: skim the matched lines in context before committing to a full read.

**Example (organisation):** "Torm", "Ilmater", "Tyr", "Amaunator" — the patron deities of the four chartered orders

**Example (artifact):** "White Saint", "pilgrim", "pilgrimage", "relic", "Guardian of the Tomb"

---

### Prong 6: Type and Category Search

**Purpose:** Find files that discuss the subject's *kind of thing* without using its specific name.

Search case-insensitively for the generic terms that describe what the subject is — its role, its category, its function. This catches narrative text where the author uses informal descriptions ("they fought their way up the tower") rather than proper names ("the Table of the Sun").

Cross-reference hits from this prong against Prong 4 (events) to separate relevant files from noise. A file that mentions "battlements" and also mentions "Liberty Hill" is a strong candidate; a file that mentions "battlements" in a Waterdeep context is not.

**Example (organisation):** "paladin", "templar", "holy order", "knight commander", "master knight"

**Example (artifact):** "citadel", "battlements", "tower", "prison", "confinement"

---

### Prong 7: Relationships and Counterparts Search

**Purpose:** Find files organised around *something else* that mention the subject in passing because of a known relationship.

Search for the names of allied organisations, rival factions, partner units, trading partners, or any entity that is known to interact with the subject. The subject often appears in these files as a secondary reference — "the Lambent Shield was already committed to the western front" in a White Cloaks narrative, for instance.

This is where uncollated material *can* hide, because no one thinks to look in the White Cloaks file for Lambent Shield detail, or in a Mule Company narrative for Golden Lion information. However, in a tightly interconnected archive where counterpart terms are pervasive, this prong generates a high volume of false positives. The cross-referencing step (checking counterpart hits for subject-specific terms) is essential but labour-intensive.

**Before searching:** List every organisation, faction, or entity that the compiled document mentions as having interacted with the subject. Search for their names.

**Example (organisation):** "White Cloaks", "Mule Company", "Sun Blades", "Free Defence League", "Redjacks", "Tethyamar League", "Dark Garden", "Netheril"

**Example (artifact):** "Black Hand", "Slave Orbs", "Imperialis Orbis", "Gaebril Tremalkin" — counterpart relics and the enemies they were used against

---

### Prong 8: Narrator and Author Search

**Purpose:** Find files written by narrators who are likely to have discussed the subject, where the material is organised by *who wrote it* rather than *what it's about*.

The archive has identifiable authorial voices. Some narrators are grab-bags who touch everything they encountered during a particular period. If you know which narrators were in a position to observe the subject, searching for their names or their known document titles catches material that the other prongs miss because it's filed under the narrator's name rather than the subject's.

This prong tends to surface the richest qualitative material — character judgements, atmospheric detail, first-person observations, diplomatic analysis — rather than factual data. However, when the subject is well-documented, narrator files tend to overlap heavily with Tier 1 results, since the same events are captured both by subject-name searches and by narrator-name searches.

**Before searching:** Identify which narrators were present at or near the subject's events, or had reason to write about it. Check for journal entries, letters, reports, and chronicle sections attributed to them.

**Known narrators in the Daggerdale archive:**

| Narrator | Known works / identifiers | Likely coverage |
|---|---|---|
| Grafton FitzDecker (GFD) | Daggerdale Chronicle, "GFD Notes" | Comprehensive; covers everything he witnessed or researched |
| Beliard Emmarask | Journal entries ("000004", "Emmarask's Journal"), embassy reports | Diplomatic and military observations, Castle Radiance period |
| Iolus Warburton | "Warburton's Journal", "Warburton's Report" | White Cloaks operations, character assessments |
| Kesh Oakdale | "Liberty Hill Retaken", "The Shadow Lifted" series | Liberty Hill, post-battle reconstruction, Concordat period |
| Brother Vessuvian | Letters, "8 Mirtul 1483" visit, correspondence | Yellow Abbey, Historic Wing, Cathedral observations |
| Phineas Hoetmer | Referenced in others' accounts; some direct writings | Occult matters, relic analysis, intelligence work |
| Lucan Alavandor | "Casebook of Lucan Alavandor", letters | Investigation, Slave Orbs, Thistle Ridge |
| Jasper Hawkford | Letters to Khara Sulwood, reflections | Thistle Ridge campaign, field observations |
| Ser Reginald Boxfray | "Memoire" entries | Social and military observations |
| Phoebe Birchgrove | Expeditionary records | Thistle Ridge field reports |

**Example search:** To find material about the Table of the Sun, search for "Kesh Oakdale" (who wrote the Liberty Hill reconstruction account) and "Vessuvian" (who visited the Historic Wing where the Slave Orbs were kept).

---

## Post-Search Process

### 1. Deduplicate and weight

Merge all eight file lists. Weight the results:

- **3+ prongs (any tier):** Almost certainly relevant. Read first.
- **2 prongs, at least one Tier 1:** Likely relevant. Read second.
- **2 prongs, both Tier 2:** Worth skimming the matched lines. Read if the context looks promising.
- **1 prong, Tier 1:** Probably relevant but narrow. Read after the multi-prong hits.
- **1 prong, Tier 2 only:** Triage. Skim the matched line in context; skip if the mention is incidental.

### 2. Screen results for unknown entities

Before reading any files, scan the merged results list — filenames, matched lines, and surrounding context — for personal names, place names, or entity names that do not appear in the compiled document or in the personnel/search-term lists used for the eight prongs.

Any unknown name appearing in a search result is a candidate gap — especially if it appears in a filename (e.g. a character file named after a family member not in the compiled pedigree). For each unknown name found:

- Flag it as a potential omission from the compiled document.
- Add it to the Prong 2 personnel list and run a supplementary name search before proceeding to the reading pass.
- Prioritise reading the file that surfaced the unknown name.

This step exists because the personnel list for Prong 2 is bootstrapped from whatever sources were compiled first. If those sources are incomplete, the search terms will be incomplete — but the search *results* may still contain the missing entities, surfaced by broader searches (Prong 1 surname matches, Prong 4 event matches, etc.). Screening the results closes the feedback loop: the search tells you what you didn't know to look for.

> **Origin of this step.** During compilation of the Whitegate–Thunderstorm–Blackmane family trees, the Prong 1 surname search for "Whitegate" returned a file called `Lumen Whitegate.txt` — a character file for a family member not present in the DDC 1480-12 pedigree used as the base source. The file sat in the results list unnoticed because there was no instruction to screen results for unknown names before beginning the reading pass. This step would have caught it at the earliest possible point.

### 3. Cross-reference against cited sources

Check the compiled document's footer, source list, or known source inventory. Separate files into "already cited" and "potentially uncited." Read the uncited files first — that's where new material is most likely to live.

Already-cited files are still worth skimming if they hit on multiple prongs, since a source can be cited without being fully exhausted.

### 4. Read for delta, not for content

When reading a file, you're not looking for everything it says about the topic. You're looking for details that are *not already in the compiled document*. Before beginning the read pass, extract a checklist of known facts from the compiled document and check new findings against it.

**Compare parallel sources entry by entry.** When the same structured data — a pedigree, a roster, a muster roll, a treaty text, an inventory — appears in more than one file, do not read each file independently against the compiled document. Instead, diff the sources against *each other*, entry by entry. A pedigree in File A that lists one child where the pedigree in File B lists three is a critical delta that independent reading can miss, especially if the compiled document was built from File A and the reader unconsciously treats File A as authoritative.

The risk is highest when one source is formally presented (a standalone pedigree document, an official roster) and the other is embedded in a larger work (a chapter of a chronicle, a narrative aside). The formal source *looks* more authoritative, but it may be an abridgement, an earlier draft, or a summary that omits detail the embedded version preserves. Treat neither as complete until you have compared them.

### 5. Flag contradictions

If a source says something that conflicts with the compiled document, note it with both the conflicting fact and its date/source. The editorial principle is: present both facts with dates, don't paper over the discrepancy.

### 6. Note provenance

For any new detail, record which file it came from. This matters for the source footer and for later verification.

### 7. Reverse-verify enumerated claims

For documents that enumerate members of a group — pedigrees, rosters, inventories, chapter rolls — perform a targeted audit of the compiled document's own completeness claims after the reading pass is done.

For each entry in the compiled document that implies a count (a parent with listed children, an order with listed knights, a farm with listed tenants), search the archive for narrative references that confirm or contradict the count. Look for plural relational terms ("siblings," "children," "companions") and for specific names adjacent to the entity in question. If a narrative source refers to "Lumina's siblings" and the compiled pedigree lists Lumina as an only child, that is a gap.

This step is a safety net. If the results-screening (step 2) and the parallel-source comparison (step 4) both work correctly, this step should find nothing new. Its value is as a final check on documents where completeness is the primary purpose — where a missing entry is not merely an omission but a substantive error in the document's claims.

### 8. Thematic read of high-weight files

After deduplication and weighting (step 1), take the top 10–15 files by prong-hit count and read them in full — not just the matched passages.

Keyword searches find files; they do not find everything *in* those files. A file that hits on six prongs almost certainly contains relevant material that falls between the keyword cracks: a logistical detail adjacent to a named location, an equipment description embedded in a garrison report, a passing remark about a supply chain or a training practice. These details are invisible to the search because no reasonable set of search terms would have anticipated them, but they become visible immediately upon full-context reading.

The cost of this step scales with the prong-hit threshold: reading 15 files in full is a meaningful time investment. But these are files the search has already identified as highly likely to be relevant — the investment is in extracting their full yield rather than just the passages that happened to contain a search term. If time is limited, prioritise files that are (a) uncited in the compiled document and (b) hit on multiple Tier 1 prongs.

> **Origin of this step.** During the second archive search on the Sun Blades, the Dagger Falls Gazetteer hit on multiple prongs via "Sun Blade" and "Dagger Falls." Reading only the matched passages would have surfaced the Sun Blades unit-structure summary. Reading the file in full also surfaced a description of the Tower garrison ("mostly eagle-eyed young women with short bows"), an equipment description contradicting the primary source ("chain shirts" vs. "chain mail"), and a logistics detail (Olifsen's Smithy mass-producing weapons for the army) — none of which contained any of the search terms.

### 9. Body-to-index reconciliation

After findings have been incorporated into the target document, extract all named entities from the document body and compare against any summary index the document maintains — a personnel table, a location register, a source list, a timeline, or any other structured inventory that claims to enumerate the document's contents.

Any entity present in the body text but absent from the index is a potential omission introduced during the incorporation process. This is a distinct failure mode from search omissions: the information was found, was written into the document's narrative sections, but was not carried forward into the summary tables.

The method is mechanical: extract bolded names (or whatever convention the document uses for entity markup), deduplicate, and diff against the index. Flag any discrepancies for review.

This step is document-format-agnostic. It applies whether the index is a personnel table in a military dossier, a dramatis personae in a narrative, a bibliography in a research document, or a feature list in a technical specification. The principle is the same: any document that maintains both a narrative body and a summary index can develop silent inconsistencies between them, and the inconsistencies compound with each editing pass.

> **Origin of this step.** During the Sun Blades incorporation passes, two named personnel (Sephany and Zelia Oakbough) were described in the body text of the dossier but missing from the personnel summary table. Both had been written into their respective company sections across earlier editing passes but were never carried forward into the table. The omissions were caught by manual inspection during a verification step, but only by accident — the reviewer happened to notice the names while checking something else. A systematic reconciliation would have caught them at the point of incorporation rather than relying on incidental discovery.

### 10. Account for unsearchable formats

Grep only works on text files. The archive may contain PDFs, spreadsheets (.xls, .xlsx), and image files (.jpg, .png) that cannot be searched by text pattern. Note these as a gap. If the subject is likely to appear in non-text formats (e.g. a map, a character sheet, a spreadsheet roster), those files need to be checked manually or with format-specific tools.
