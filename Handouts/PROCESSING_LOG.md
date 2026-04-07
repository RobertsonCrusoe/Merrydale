# Email Archive Processing Log

## 2026-04-06 — Processing Run: Systematic Email Audit and Deep Extraction

### Methodology
Previous email sweeps used keyword-based searches (campaign names, character names, location names). Stephen challenged the completeness of this approach, prompting a systematic audit using **sender-pattern searches** — searching for all email between the gaming group regardless of subject line. This revealed dozens of threads with non-obvious subjects that had been missed.

Three Gmail searches were executed:
1. `from:gus.miranda to:les.blackwell has:attachment after:2024/1/1`
2. `from:gus.miranda (to:les.blackwell OR to:contact@toddburry OR to:robertsoncrusoe) -subject:"hobbity" -subject:"daggerdale" [etc.] after:2024/1/1`
3. `from:les.blackwell (to:gus.miranda OR to:contact@toddburry) -subject:"hobbity" -subject:"daggerdale" [etc.] after:2024/1/1`

### Files Created This Run

#### Daggerdale Campaign
| File | Source Thread | Content | Size |
|------|-------------|---------|------|
| Back in Dagger Falls - Session Notes and DM Corrections - Jun 2025.txt | 19778e286e605f3d | Stephen's session recap (Mirtul 2-4), Gus's DM corrections, Jasper's political rant, Beholder speculation | ~15K |
| Daggerdale - Orb Names Analysis - AI-Generated - Stephen Robertson - Jul 2025.txt | 198145d1bd085d2d | AI analysis of Vortellius/Varros/Verinius orb names | ~5K |
| Wrapping up Charrahs Chambre - Post-Session Roleplay and DM Rulings - May 2025.txt | 196ca0fb7ad82bc6 | Post-session roleplay (Scott's Jeska sequences, dragon discussion, DM rulings) | ~5K |
| Selected Entries from the Journal of Aisling Maeliticus - Discussion Thread - Jun 2025.txt | 1977508eb9a77adb | Player lore analysis of Aisling journal (Palus/Netheril theories) | ~4K |

#### Hobbity Adventure
| File | Source Thread | Content | Size |
|------|-------------|---------|------|
| Hobbity Adventure - Hobbit Replacements - Boffo Death and New Characters - Mar-Apr 2026.txt | 19d180f3b9f67fbb | Boffo's death, replacement character options, class discussion | ~3K |
| Hobbity Adventure - Post-Session Discussion - Toads and XP - Jan-Feb 2026.txt | 19c0ceb02f3fb2e4 | Post-session banter, XP award (310xp), True Detective reference | ~2K |

#### Call of Cthulhu (NEW CAMPAIGN FOLDER)
| File | Source Thread | Content | Size |
|------|-------------|---------|------|
| Call of Cthulhu - Campaign Planning - A Call to Madness - Jul-Aug 2025.txt | 1984a2093640ab65 | Gus's 1920s Toronto setting, character concepts, historical research | ~4K |

#### Gonzadrel
| File | Source Thread | Content | Size |
|------|-------------|---------|------|
| Gonzadrel - Welcome to Dolmenwood - Todd Burry DM - Aug 2025.txt | 198723cb5823488a | Campaign intro, Dolmenwood setting introduction | ~1K |

#### Meta & OOC
| File | Source Thread | Content | Size |
|------|-------------|---------|------|
| Songs of the Dagger and Other Verses - Campaign Songbook - Stephen Robertson - Mar 2026.txt | 19cc125bd495da4b | Compiled campaign songbook from recovered wiki content | ~1K |
| Adventures in Robot D&D - AI DM Experiment - Gus Miranda - Jun 2025.txt | 197574860966109b | Gus's AI DM prompt, discussion of AI as D&D DM | ~2K |

### Content Already Archived (confirmed this run)
The following content from these threads was already present in the archive from prior processing:
- "A Visit to the Historic Wing" — Brother Vessuvian's journal (filed as "8 Mirtul 1483 DR - A Visit to the Historic Wing.txt")
- "Excerpts from The Catacombs of Sembian Expatriats" (filed as existing file)
- "From the Casebooks of Lucan Alavandor: The Slave Orbs" (filed from prior email extraction)
- "Journal of Iolus Warburton" (filed as existing file)
- "Dinner with Alen Reks" (filed as existing file)
- "Getting Caught Up" thread overview (filed as existing file)
- "1 Mirtul 1483 DR - Charrah's Chambre" DM narrative (filed from wiki/forum)
- All "From the Archives" biographies (Garth Shanks, Tomas Quoyle, Mourn Raventree, Arkos Thunderstaff, Rychel Voordan, Luminous Whitegate, Thagdul, The Warders)

## 2026-04-06 — Processing Run 2: Continuation Deep Extraction

### Methodology
Continued from Processing Run 1 after context window filled. Systematically extracted all remaining identified threads. Added sender-pattern searches for Scott McLaren (scunny1973@gmail.com) which revealed several in-universe threads with non-obvious subjects. Also searched Steve Hicks, Casey Bauman-Wike, Alex Francom, and Rob Schmidt.

### Files Created This Run

#### Daggerdale Campaign
| File | Source Thread | Content |
|------|-------------|---------|
| A Speculative History of Thistle Ridge - Lore Analysis - Jun 2025.txt | 1978439473685f75 | Stephen's comprehensive speculative timeline + Scott's "hard facts" from prior campaigns. Major lore analysis: Alavandor/Clarandal families, Palus, Tenebrius Ostia, Lobelia/Loki, Netherese conspiracy |
| Heres Most of It - Chapter 7 Sitrep and Player Theories - Jun 2025.txt | 1976067b455590e2 | Les delivers Chapter 7 compilation (262+ pages), player reactions, Jasper's to-do list, Scott's 10-point lore analysis of campaign mysteries |
| Charrahs Chambre - End of Last Session Narrative - Pre-Session Discussion - May 2025.txt | 196a212ad40fbc3b | Les's vivid Charrah's throne room narrative, Gus's crisis of conscience, "monkey" running joke, invisibility rules analysis and DM rulings |
| Loot from Thistle Ridge Tower Dungeon - Distribution Discussion - Jan 2025.txt | 19481b9904c9ffbd | 25-message loot distribution: Karn's Lair & Ribalest's Tomb items, Potency Rune +2 debate, rune non-transferability ruling |
| Loot - Post-Charrah Battle Distribution - Jun-Jul 2025.txt | 197750ce877c3b5f | Post-Charrah loot: grimoire contents, rune debate, power curve concerns |
| Crafting - House Rules and Alchemical Arrows - Jul 2025.txt | 197cb4c5b9b09b74 | Stephen's Crafting Proposal.docx, Gus's crafting rant, Les's simplified house rules |
| Crafting - Jaspers Formula Extraction Proposal - Gus Miranda - Oct 2024.txt | 1925d4e14966c697 | Single message: Gus's initial Magical Crafting formula extraction proposal |
| Legality Ooopsy - Boxfray Barracks Contract Dispute - Jul 2025.txt | 197db50fc3b6b8fe | Jeska/Boxfray barracks contract breach, Ferguson's right of first refusal |
| Ferguson Contract and Lucans Creative Curses - Jun 2025.txt | 197b726058d682dd | Missing Ferguson contract, comprehensive list of Lucan's in-character oaths |
| Jaspers Shopping and Crafting - Downtime Actions - Jun-Jul 2025.txt | 19776a419d855ba4 | Jasper and Lucan tenday schedules (Greengrass–Mirtul 10), spell learning, crafting, shopping |
| Assorted Thoughts on Spells and Such - Gus Miranda - Jul 2025.txt | 197e1002a57bff63 | Cross-edition Fireball/Magic Missile damage comparison tables, "Wizards have no business casting damage spells" |
| Weekend - Post-Session Shadowfell and Pathbuilder Discussion - Aug 2025.txt | 198c9bc406a35d1b | Post-session: Jeska led party into Shadowfell, Pathbuilder 2E recommendation |
| Random Campaign Artwork - AI Generated Character and Scene Art - May-Dec 2025.txt | 196a1c1af69677f4 | 48-message art thread: ~20+ AI images, "Duality of Jasper Hawkford", monastery designs, Ser Rowan portraits |

#### Hobbity Adventure
| File | Source Thread | Content |
|------|-------------|---------|
| Hobbity Adventure - Old Hobbity Images and Spottle Discussion - Mar-Apr 2026.txt | 19d46f373879da0c | Gus's 9 campaign images, Todd's transcription discussion, Spottle Parlour "only 5% played", Huddle Farm PDF |
| Hobbity Adventure - Wedge Portrait and Hobbit Ears Discussion - Apr 2026.txt | 19d4f24cd76c6630 | Wedge portrait requests, hobbit ear consensus ("slightly pointed, like a 1/4 elf") |

#### Meta & OOC
| File | Source Thread | Content |
|------|-------------|---------|
| Adventures in Robot D&D - AI DM Experiment - Gus Miranda - Jun 2025.txt | 197574860966109b | UPDATED full extraction: Rowan.docx AI DM prompt, LLM comparison, ChatGPT's sonnet, AI setting preferences |
| DnD Realm - Malazan Book of the Fallen Suggestion - Scott McLaren - Aug 2025.txt | 198ba22478d1d6fe | Scott suggests Malazan for new campaign setting, Les: "The AI will have already read those books" |

#### Call of Cthulhu
| File | Source Thread | Content |
|------|-------------|---------|
| Call of Cthulhu - Campaign Planning - A Call to Madness - Jul-Aug 2025.txt | 1984a2093640ab65 | UPDATED full extraction: character concepts, radio/Marconi history, Middenheim taxation anecdote, Ambrose Small, Uncle Harold photos |

### Remaining Group Member Search Results
- **Steve Hicks**: 201+ emails. Campaign threads from 2022: "Remote DnD Redux" (1817d0934392fe22), "Finding a Date for Session 0" (1818b6b43a1e3423), "An introduction..." (1818dc6db7d38cc9), "Dicey Situations Podcast" (17f420fa660d5475). Early campaign formation threads.
- **Casey Bauman-Wike**: 201+ emails, mostly 2003-2004 era. No current campaign threads.
- **Alex Francom**: 3 emails, overlapping with Steve Hicks threads (Session 0 planning).
- **Rob Schmidt**: 0 emails found.

### Threads Remaining for Future Passes
- **"A Trip Through The Shadowfell"** (19caa4ae7bd8375d) — Mainly scheduling for Les's Daggerdale side-quest. Low narrative content.
- **"Finding a Date for Session 0"** (1818b6b43a1e3423) — Jun 2022 scheduling thread.
- **"The Dicey Situations Podcast"** (17f420fa660d5475) — Mar-Apr 2022 podcast/campaign naming.
- **Random Campaign Artwork - NSFW** — Image attachments need manual download (20+ images across 48 messages).
- **"Raidfest in Freeport..."** (f49d0c49e021f52) — Apr 2003 Freeport campaign thread. Not yet fetched.
- **"THE THING THAT WORE A NIGHTMARE PART I"** (f91d1e98683aa31) — Nov 2003 narrative thread. Not yet fetched.
- **"DND"** (edc92107f118044) — May 2002 campaign thread. Not yet fetched.
- **"Roll initiative..."** (11bceb59cb91dc9f) — Aug 2008 Avilund map sharing. Not yet fetched.
- **"D&D and my shittiness..."** (138249170dd64091) — Jun 2012 Steve Hicks thread. Not yet fetched.
- **"Daggerdale Online Forum & Wiki"** (12dccec3f0c71366) — Jan 2011 forum/wiki setup. Not yet fetched.
- **"Freeport" / Todd's Eastwitch share** (1208952481665643) — Apr 2009. Not yet fetched.
- **"withdrawal ... shakes ... fix ... bliss ... repeat"** (11b0be419928722d) — Jul 2008 campaign nostalgia. Not yet fetched.

## 2026-04-06 — Processing Run 3: Historical Archive Deep Extraction

### Methodology
Expanded extraction beyond the current-era campaigns (2024-2026) to the full historical archive. Keyword searches for campaign names (Avilund, Eastwitch, Freeport, Wastrel, Loudwater, Spellgard) revealed threads going back to 2000. Also processed two massive previously-saved threads ("DnD Revisited" at 563K chars, "DnD Handouts and Session 0" at 1.25M chars) via Python extraction from saved JSON files.

### Files Created This Run

#### Meta & OOC
| File | Source Thread | Content |
|------|-------------|---------|
| Death on the Vine - Online Daggerdale Called Off - Aug 2012.txt | 1390df63a12893c7 | Les calls off Online Daggerdale, group discusses alternatives (d20Modern, Pathfinder Waterdeep), Scott's "A distraction from reality. Not a commitment to an alternate one." |
| DnD Revisited - Current Daggerdale Campaign Formation - Jul-Oct 2023.txt | 1895110d65b8d6b9 | ORIGIN THREAD for current campaign. Les pitches base-building campaign, attaches Chapter 7 PDF. System discussion (PF2E wins). Character concepts from all players. Todd joins via Glass Cannon. Casey Wike included. 30 messages. |
| DnD Handouts and Session 0 - Campaign Launch - Nov 2023.txt | 18bcae8800b3699f | 74-message LAUNCH THREAD. Les delivers Thistle Ridge PHB. All characters declared: Casey's Kineticist "Sprout," Scott's Jeska, Todd's Cleric, Gus's historian, Stephen's Lucan concept. ChatGPT lore analysis (Garth Shanks, Thagdul, Jafar/Beljuril). Session 0 booked Dec 1. |
| Remote DnD Redux - Campaign Formation and Hicksys Golarion Campaign - Jun 2022.txt | 1817d0934392fe22 + 1818dc6db7d38cc9 | (Created in Run 2) Steve Hicks's PF2E Golarion campaign, group origin |
| Update on Pathfinder and the Pod - Steve Hicks Steps Away - Jul 2022.txt | 181deb88b6e1971f | Steve steps away from PF2E campaign, Stephen's supportive reply mentioning "Mungo" character concept and yearning for Freeport |

#### Eastwitch
| File | Source Thread | Content |
|------|-------------|---------|
| The Which-es and Whys of Eastwitch - Campaign Discussion - Nov 2000.txt | e3022e0ea25a36e | OLDEST THREAD in archive (Nov 2000). Casey argues for druids in Eastwitch, Todd backs him. Stephen corrects Paladin lore. Steve calls Stephen a "rules Nazi." Les's legendary drunk mail. Resent in 2008 and 2010 for comedic value. |

#### Wastrel/Freeport
| File | Source Thread | Content |
|------|-------------|---------|
| THE DND - Freeport Session Planning - Apr 2001.txt | e5a337e10ee26d1 | Todd DMing Freeport. Les plays Salazar (wizard). Bloody Vengeance, Scarbelly, the Unspeakable one. In-person play, D&D 3E. |

#### Avilund
| File | Source Thread | Content |
|------|-------------|---------|
| Ok Ramblers Lets Get Rambling - Gus Caledon Campaign Pitch - Sep-Oct 2011.txt | 132b12b9c303260a | Gus pitches "Caledon" — politics-heavy sandbox in his own world (elves vs dragons, Free City). Stephen proposes "Absalom Pale." 3.5 vs 4E debate. Monte Cook returns to WotC. Jeremy Pettiman wiki link confirms Avilund wiki URL. |

## 2026-04-06 — Processing Run 4: Completion of Historical Archive Extraction

### Methodology
Final extraction pass completing all threads identified in the "Threads Remaining" list from Processing Run 3. All remaining threads fetched via Gmail MCP and written to archive files.

### Files Created This Run

#### Wastrel/Freeport
| File | Source Thread | Content |
|------|-------------|---------|
| DND - Salazar Wants a Boat - May 2002.txt | edc92107f118044 | Les wants a ship for Salazar, Todd discusses ship rules (variable speeds, smokepowder guns — "the guns in the DMG 'Suck'" — three full rounds to reload), nautical maps. Casey's upcoming campaign mentioned. |
| Freeport - Todd Shares Narrative Documents - Apr 2009.txt | 1208952481665643 | Stephen requests old Freeport files from Todd. Todd sends 5 .doc attachments: Zechary and Smiling Jack, Voyage to the Isle of the Lich, Raidfest in Freeport for PCs, Madness In Freeport Narratives, A Simple Mission. Plus Eastwitch narrative: Bin and His Companions at the Green Grizzly. Todd admits Wastrel was overpowered, Casey bringing Freeport back "ticked me off." |

#### Avilund
| File | Source Thread | Content |
|------|-------------|---------|
| Roll Initiative - Avilund Map Sharing - Aug 2008.txt | 11bceb59cb91dc9f | Stephen delivers digitized Avilund map to Les. URL: robertsoncrusoe.com/avilund/. Les "overfuckingwhelmed." Corrections: Bight of St. Solomine, northern terrain. Publishing ambitions discussed. |
| Withdrawal Shakes Fix Bliss Repeat - Campaign Nostalgia and Barbarossa - Jul 2008.txt | 11b0be419928722d | Stephen's campaign withdrawal, poring over old EOI emails. Proposes "Barbarossa" character for Waldheim/Crusades setting (Azeem from Robin Hood analogy). Contains two quoted Les emails on DM philosophy (2001, 2003). |

#### Meta & OOC
| File | Source Thread | Content |
|------|-------------|---------|
| DnD and My Shittiness - Steve Hicks Returns - Online Daggerdale Revival - Jun 2012.txt | 138249170dd64091 | Steve Hicks apologizes for disappearing (creative burnout after Loudwater). Les shifts leadership to Beliard (Stephen's PC), adds 5th PC tank for Steve. Stephen's Oxford viva voce on Friday — "fighting a level boss." Gus: "petulant douchebaggery of players." Two months before "Death on the Vine." |

### Threads Fully Processed (Remaining List Cleared)
All threads from the "Threads Remaining for Future Passes" list in Processing Run 3 have now been processed:
- ✓ "DND" (edc92107f118044) — May 2002, filed under Wastrel
- ✓ "Roll initiative..." (11bceb59cb91dc9f) — Aug 2008, filed under Avilund
- ✓ "withdrawal...shakes...fix..." (11b0be419928722d) — Jul 2008, filed under Avilund
- ✓ "Freeport" / Todd's narrative share (1208952481665643) — Apr 2009, filed under Wastrel
- ✓ "D&D and my shittiness..." (138249170dd64091) — Jun 2012, filed under Meta & OOC

### Threads Still Remaining
- **"A Trip Through The Shadowfell"** (19caa4ae7bd8375d) — Mainly scheduling for Les's Daggerdale side-quest. Low narrative content.
- **"Finding a Date for Session 0"** (1818b6b43a1e3423) — Jun 2022 scheduling thread.
- **"The Dicey Situations Podcast"** (17f420fa660d5475) — Mar-Apr 2022 podcast/campaign naming.
- **Random Campaign Artwork images** — 20+ images across 48 messages need manual download.
- **Steve Hicks historical threads (2022)** — 201+ emails, mostly "Remote DnD Redux" era campaign formation.

## 2026-04-06 — Processing Run 5: Pure Sender-Cluster Sweep

### Methodology
Previous runs all used keyword-based searches — subject-line terms, campaign names, character names, or sender+keyword combinations. Stephen identified that this approach missed threads with oblique subjects (e.g. "Political bardery" from Les discussing the Beliard online campaign). The fix: **pure sender-cluster searches** querying all mail from each group member with NO keyword requirement.

Updated `merrydale_extractor.py` with 24 new Tier 2 queries (one per email address for all group members). Also added `snah@rogers.com` (Steve Hicks) and `rschmidt@shawcable.com` / `rschmid1@uwinnipeg.ca` (Rob Schmidt) to GROUP_MEMBERS. Added `archendale`, `tomdril`, `hollowbough` to Fox in the Henhouse classification rules.

Six Gmail searches across all group members returned 456 unique threads, 358 not in the 59 already-archived IDs. Snippet keyword-filtering flagged 145 as potentially campaign-relevant. Manual triage of the top 40 threads (those with strongest in-universe signals) yielded 26 archive-worthy threads.

### Files Created This Run

#### Daggerdale Campaign
| File | Source Thread | Content |
|------|-------------|---------|
| From the Archives - Garth Shanks - Character Portrait.txt | 19cc6a4093181bd4 | Character portrait and lore analysis of Garth Shanks from Waterdeep campaign. 5 messages, Mar 2026. |
| From the Archives - Tomas Quoyle - Character Portrait.txt | 19cc6cb605a2cae9 | Comprehensive character portrait of Tomas Quoyle including death scene and thematic analysis. 3 messages, Mar 2026. |
| A Tale of the Darkest Deep - Pellias Vignette - Mar 2025.txt | 195b7035ab8b5f76 | In-universe Pellias character vignette (frustrated in ship hold), session debrief. 5 messages. |
| Jeska's Speech to Dagger Falls - After the Competition - Jul 2024.txt | 190e61f60b12d66f | Jeska's formal address to the community after competition victory; Redjacks decree, Thistle Ridge vision. 1 message. |
| Lucan Alavandor - Investigation Notes - Lobelia Parentage - Jun 2025.txt | 19774f6682919bdd | Gus's theory on Lobelia's parentage and Palus/Loki connections. 1 message. |
| Lucan Alavandor - Case File - Lobelia and Loki Identity - Jun 2025.txt | 197838481d5cfbef | Formal investigation connecting Lobelia Alavandor to Shadovar agent Loki Mouvranesh. Stephen's follow-up deductions. 5 messages. |
| Jeska and Sir Rowan - Rune Gifting Scene - Jan 2025.txt | 1949ed73fd4bd9f0 | In-character scene: Jeska gifts Ser Rowan a rune. Emotional character moment. 3 messages. |
| Jeska and Lucan - The Enchanted Hauberk - Jul 2024.txt | 190e6b9da834ff77 | In-character Jeska/Lucan dialogue about the enchanted hauberk. Trust and stewardship themes. 2 messages. |
| The Next Tenday - Tarsakh 1 to 10 - Character Actions - Jul 2024.txt | 190dc14e2ce251b8 | Character action montage (Jasper's library, Jeska's meditation and training). 4 messages. |
| Thistle Ridge - Chrysalis Negotiations and Swelter Deals - Aug 2024.txt | 19137c0c91df7dcc | In-character negotiations with Swelter, weapon upgrades, anonymous construction company front. 5 messages. |
| Thistle Ridge - Ridge and River Renewal Company - Aug 2024.txt | 1912f6fab346b309 | Jeska's plan for anonymous construction company. Jasper's frustration with admin. 4 messages. |
| Winning the Competition - Castellan Promotion - Jul 2024.txt | 190e54a63efabb06 | Post-competition strategy; Ser Rowan promoted to Castellan of the Embassy. 6 messages. |
| Early Morning of the 30th - Jeska's Defense Rally - Apr 2025.txt | 196091119fcc5bad | Jeska rallies party for defense at the Tower. Strategic briefing. 1 message. |
| Aftermath - Post-Combat Debrief - May 2025.txt | 196c6e126be96065 | Post-combat scene with recovered artifacts discussion. Character voice. 2 messages. |
| Post Assassination Attempt - Netherese Assassins at Temple - Apr 2025.txt | 195ed161dbc4c51e | Assassination attempt aftermath, loot handling, DM narrative. 8 messages. |
| A Surprise Visit by Sanduskin Vale - Apr 2025.txt | 195f75eecbcf925e | Narrative encounter with Sanduskin Vale. 2 messages. |
| Swelter and Lucan - Thistle Ridge Vendor Deals - Oct 2024.txt | 19285a415ca47703 | Vendor agreements for Thistle Ridge settlement. 4 messages. |
| The 25th in Hudson - Thistle Ridge Recon Planning - Apr 2025.txt | 196069db4c800afa | Tactical planning for Thistle Ridge recon/assault. 2 messages. |
| After the Limestone Quarry - Session Debrief - Mar 2025.txt | 195572e5d78e38a3 | Post-session debrief: combat analysis, character reflections, 10-day planning. 7 messages. |
| The Shadow Lifted - Campaign Discussion and Wrap-Up - Jun 2011.txt | 1304bfcd031e46a8 | Campaign wrap-up narrative, DND Camp planning. 13 messages. |
| Daggerdale in the Summer - Character Concepts - Mar-Apr 2012.txt | 13652256d8210935 | Character concepts: Nathan "The Drake" Gale, Beliard, Zancanelli Rudolfo. 10 messages. |
| The Plan - Loudwater Scheming - Feb 2012.txt | 135b11d9e229575a | In-character scheming at Everbright farm, Grey Vale domination. 4 messages. |

#### Hobbity Adventure
| File | Source Thread | Content |
|------|-------------|---------|
| Boffo's Hobbit Thanksgiving - Todd Burry - Nov 2025.txt | 19a51f3f3371047e | Standalone in-universe narrative: Boffo's winter story. 31 messages. |
| A Hobbity Adventure - Recap and Mystery Investigation - Nov-Dec 2025.txt | 19ad3c1b5ad4bf95 | Session recap and mystery investigation analysis. 7 messages. |

#### Fox in the Henhouse
| File | Source Thread | Content |
|------|-------------|---------|
| Archendale Campaign Recruitment - Tomdril Jon Hollowbough - Sep 2000.txt | e1a19d9ec4921fb | Campaign recruitment for Archendale. Character: Tomdril Jon Hollowbough (halfling Rogue/Ranger). 7 messages. |

#### Uthmere
| File | Source Thread | Content |
|------|-------------|---------|
| Campaign Introduction - Golarion Narrative Setup - Jun 2022.txt | 1818dc6db7d38cc9 | Steve Hicks's campaign intro narrative for PF2E Golarion setting. |

### Archive Statistics After Run 5
- Total archived Gmail Thread IDs: 85 (up from 59)
- New threads archived this run: 26
- Campaign folders with new content: Daggerdale (22), Hobbity Adventure (2), Fox in the Henhouse (1), Uthmere (1)

### Threads Still Remaining
- ~105 additional threads flagged as potentially campaign-relevant (from the 145 total) were triaged as scheduling, logistics, or OOC banter with minimal in-universe content
- The 33 campaign-keyword threads from Les identified in the prior session's targeted search still need individual review
- Older Hotmail-era threads (theblackcobb@hotmail.com, 2004-2005) still pending: "message for garth shanks" (84KB), "dnd stuff" with handout, "Secrets" (34KB)
- Random Campaign Artwork images (20+ across 48 messages) need manual download

## 2026-04-06 — Processing Run 6: Les Blackwell Deep Extraction (Gmail + Hotmail)

### Methodology
Targeted search on Les Blackwell's two email addresses: `from:les.blackwell@gmail.com` with campaign keywords, and `from:theblackcobb@hotmail.com` (full sweep). Cross-referenced against 85 known thread IDs. 88 new Gmail threads and 72 new Hotmail threads identified. After dedup against existing archive content (Ambassadorial Conclave, Catacombs of Sembian, Jasper's Report to Khara, Casebooks of Lucan, From Out of the Mists, Chapter 7 content all already present), 13 threads contained genuinely new in-universe or campaign content.

### Files Created This Run

#### Daggerdale Campaign
| File | Source Thread | Content |
|------|-------------|---------|
| Tojo - Scun's Investigator Character Concept - Oct 2003.txt | f82559cfb0b0e19 | Scun's old rogue Investigator (62 yrs old, CSI/Sherlock style, lion figurettes). House rules discussion. 9 messages, Oct 2003. |
| The Unjust Rule of the Assassin-Lord Dynasty of Waterdeep - Handout - Mar 2004.txt | fb58a8ae2fa9e33 | In-universe handout: political manifesto on Waterdeep's Assassin-Lord Dynasty. For Steele, Rychel, Garth. 1 message, Mar 2004. |
| Conclusion - Session Wrap-Up and Vampire Coven Article - Mar 2004.txt | fb772153e48cc3a | Session wrap-up from Black/Scunny/Hicksey/Burry session. Attached "Vampire Coven Uncovered in Little Chessenta" article. 1 message, Mar 2004. |
| Fathers Day Handout - Charrah Aftermath Excerpt - Jun 2025.txt | 197745e4843178a2 | DM handout excerpt from Chapter 7 on Charrah aftermath. 1 message. |
| Catching Up - Character Tenday Actions Summary - Jul 2025.txt | 1980973f5ef7ff2a | DM summary of character tenday actions (Lucan, Jasper, others). Spell learning, crafting, purchasing. 3 messages. |
| Lucan's Notes on Lobelia Alavandor - Investigation Thread - Apr-May 2025.txt | 1967c18681968ec0 | Stephen's in-character investigation notes on Lobelia's heterochromia and hagspawn genealogy. 6 messages. |
| What's Next - Post-Battle Strategic Planning - Apr 2025.txt | 19631047479cc519 | Greengrass siege planning, goblin defense, tower reconnaissance. 11 messages. |
| A Small Daggerdale Vignette - Jasper and Lucan - Mar 2025.txt | 195eb485cc110ce9 | Gus's comedic vignette: Jasper juggling romantic interests, Lucan's reaction. 2 messages. |
| Fourth Level - Party Level-Up and Accomplishments - Apr 2025.txt | 195f23d704895489 | DM's list of 15 accomplishments for level-up. Player celebrations. 7 messages. |

#### Eastwitch
| File | Source Thread | Content |
|------|-------------|---------|
| Eastwitch on Film - Brotherhood of the Wolf Discussion - Nov 2003.txt | f8d551569426675 | Brotherhood of the Wolf as Eastwitch inspiration. Warden class, worldbuilding direction. 3 messages. |

#### Wastrel
| File | Source Thread | Content |
|------|-------------|---------|
| The Great Dale - Battle Upon the Sea of Fallen Stars - Opening Narrative - Feb 2004.txt | fa7e2342a8e1a53 | DM opening narrative for a Wastrel session. Evocative sea-storm prose. 1 message. |

#### Meta & OOC
| File | Source Thread | Content |
|------|-------------|---------|
| Fun With Dice - Gaming Weekend Planning - Feb 2005.txt | 102230051e6504b9 | Weekend gaming options: Waterdeep w/Rychel, Garth, Steele (Return of the Guild Lords, vampiric monks), Wastrel in Great Dale, Kethoth discussion. 10 messages. |
| Clan Grimwood - Nordock Online DND Session - Nov 2003.txt | f8d8e704597f214 | Les and Gus play Nordock online: Eleazer and Rowen Grimwood (brothers, rogue/bear-handler). 5-hour session recap. 6 messages. |

### Archive Statistics After Run 6
- Total archived Gmail Thread IDs: 98 (up from 85)
- New threads archived this run: 13
- Campaign folders with new content: Daggerdale (9), Eastwitch (1), Wastrel (1), Meta & OOC (2)
- Total archive: 1,876+ files across 12 campaign folders

### Threads Still Remaining
- ~92 additional threads from the Run 5 sender-cluster sweep flagged as scheduling/logistics
- Older Hotmail-era threads not yet triaged (Les's personal/social emails, ~60 threads)
- Random Campaign Artwork images (20+ across 48 messages) need manual download
- Google Calendar invites (Daggerdale sessions, DND Camp, Gonzadrel) — scheduling only, no narrative content

## 2026-04-06 — Processing Run 7: Wiki Dump Gap Closure

### Methodology
Cross-referenced the wiki-derived archive at `Merrydale/Handouts/` (2,035 files across 9 campaign folders) against the editorial archive at `Handouts/` (1,876 files across 12 campaign folders). Found that every campaign folder except Daggerdale had been fully copied over. Daggerdale had **275 files** present in the wiki dump but missing from the editorial archive.

### What Was Missing
The 275 files broke down as:
- **87 substantial files (>5KB)** — including The Chrysalis Chronicles (116KB, Todd Burry's campaign document), The Account of Magistrate Invictus, The Chronicle of Ancient Daggerdale, The Liberation of Dagger Falls, Sign of the Red Herring, The Shadow Lifted (Parts 1-4), Warburton's Journal entries (Bloodpine, Dark Garden, Deadnettle Affair), The Fall of Aldebarran, The Troubling Tale of Leirran Grennirath, Songs of the Thistle, Storm from the East, and 70+ more narrative and lore documents
- **50 medium files (1KB-5KB)** — location entries, character histories, strategic notes
- **88 small files (100B-1KB)** — NPC entries, location stubs, short lore references
- **50 stubs (<100 bytes)** — name-only entries for minor NPCs and locations

### Action Taken
Copied all 275 files from `Merrydale/Handouts/Daggerdale/` to `Handouts/Daggerdale/`. Total: 1.9 MB.

### Verification
Post-copy verification confirmed zero remaining gap: every file in the wiki dump now exists in the editorial archive.

### Archive Statistics After Run 7
- Total files in editorial archive: **2,162** (up from 1,887)
- Daggerdale: 1,361 files (up from 1,084)
- All other campaign folders: unchanged (already complete)
- Wiki dump ↔ editorial archive gap: **0 files**
