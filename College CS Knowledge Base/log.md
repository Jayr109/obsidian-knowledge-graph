# Log

Append-only operation log. Newest entries first.
Parse recent entries: `grep "^## \[" log.md | head -10`

---

## [2026-09-03] ingest | CSCE 465 — HW1 Build and Threat-Model an AI Agent (1 file)

**Source ingested** (copied to `raw/` as `CSCE465_hw1-intro.pdf`): `hw1-intro.pdf` — 16 PDF pages, two-up = **31 logical slides**, dated 9/1/26. No image-only slides.

**This is an assignment brief, not a lecture** — but roughly two thirds of it is real technical content, because the assignment teaches prompt injection before asking the student to demonstrate it. Handled by splitting the two: the concepts went to concept pages, the requirements/rules/grading went to the source page. **The source page carries an explicit note that the KB contains no work product for this assignment** — the report, transcripts, diagram, and analysis are the student's to produce, and the course's AI-use policy makes a largely AI-generated report an integrity issue.

**Pages created (5):**
- Concepts (4): AI Agent Security, Prompt Injection, OpenClaw, CVE-2024-5565
- Sources (1): CSCE 465 HW1 — Build and Threat-Model an AI Agent

**Pages updated (6):** `security-threat-landscape.md` (the AI/agentic entry now has real material behind it), `security-attack-taxonomy.md`, `security-design-principles.md`, `guofei-gu.md`, `csce-465.md`, `overview.md`.

**The idea worth keeping.** Prompt injection is a **provenance** failure, not a parsing failure. Direct and indirect injection differ only in *the channel the instruction rides* — the homework's own Task 3 runs both trials with the same agent, the same tool, and the same sentence, varying only origin (a `role:user` turn the operator typed vs. a block inside a retrieved page). The load-bearing sentence: *untrusted data becomes a possible instruction the moment retrieved bytes are concatenated into the prompt with no trust label.* Everything else follows.

**Why this belongs next to Lecture 2 rather than in a corner.** The deck supplies the sharpest possible illustration of Lecture 2's claim that cryptography is not confidentiality. Indirect injection is **not on-path**, so an encrypted, authenticated pipe delivers the poisoned page intact — arguably more reliably. *"Did this arrive unmodified?"* is an integrity question; *"should the agent act on it?"* is an **authorization** question. Cross-linked into `security-attack-taxonomy.md` rather than left isolated on the new pages.

**The 1975-to-2026 through-line, now recorded in both directions.** The AI agent material is not a separate subject:

| Modern failure | Principle violated |
|---|---|
| OpenClaw runs tool calls with `ask=off` by default | Fail-safe defaults, inverted |
| Per-layer trust checks, no unified policy — cross-layer attacks resist local fixes | Complete mediation, failing at *composition* (exactly the policy-composition hazard Lecture 2 warned about) |
| Durable fix for CVE-2024-5565: emit a constrained spec, do not `exec()` model output | Economy of mechanism + least privilege at the model boundary |

Added as an "Applied: the AI Agent Case" section on `security-design-principles.md`, so the principles page earns its claim to be the course's most durable material.

**Where the new attack class strains the existing taxonomy, noted rather than forced.** Indirect injection is closest to **fabrication** (an action attributed to an operator who never requested it), but the mechanism is neither identity spoofing nor message tampering — the page is delivered honestly over a correctly-functioning channel and is treated as authoritative because nothing records that it should not be. Recorded on `security-attack-taxonomy.md` as a limit of the four-family model, not shoehorned into it.

**Deck inconsistencies recorded rather than corrected:** two sections both labeled "Part 4" (slides 17 and 23, with no Part 5), and a slide titled "The kill chain — 6 stages" that shows three numbered phases. Also, Lecture 1 listed the TA office hour as TBD; this deck fixes it at Thursdays 2–4 PM, and the course page now carries the specific time.

---

### Concurrent-session collision, and what it cost

**Another session ingested CSCE 420 Lectures 2–8 into this same knowledge base while this ingest was in progress.** The KB went from 236 to 302 pages underneath me. Recording this because the near-miss is instructive:

- **Nothing was clobbered.** Every edit in this session re-read the file immediately before writing and applied targeted replacements, so the CSCE 420 additions to `overview.md` and `index.md` survived intact underneath the CSCE 465 additions. Verified explicitly after the fact rather than assumed.
- **One edit silently failed.** The `index.md` page-count line was updated with a plain `replace()` and no assertion, so when the other session changed the count from 236 to 302 my replacement matched nothing and did nothing. It was caught only because the post-ingest file count (307) disagreed with the stated count. **Every string replacement in this KB should assert that it matched — the one that did not is the one that broke.**
- The stale count was the *only* damage, and it was cosmetic.

**A real defect inherited from the concurrent work, fixed here.** The CSCE 420 course page still read *"Lectures beyond the first are not yet ingested"* while 8 lectures sat in `wiki/sources/` — the identical failure mode the 2026-08-27 audit found on CSCE 411, and identically a page asserting its own completeness while being wrong. Rebuilt its Ingested Sources section with all 8 lectures plus the practice sets and notebook, and added a caveat that several CSCE 420 concept pages predate the lecture ingests (reconstructed from practice exams), so the lecture source pages are authoritative where framings differ. Source pages unreachable from their own course page: 7 -> 0.

**Third false-positive class found in the link checker.** It reported 3 broken links — `[[(d0,1)]]`, `[[(d1,3)]]`, `[[1]]` — all of which are **nested-list search-frontier notation inside fenced code blocks** in the new CSCE 420 search pages. The checker did not skip ``` fences. Fixed the checker, not the pages. Running list of things this linter must not "repair": escaped `\|` in table cells, and now anything inside a code fence.

**Eight more instances of the table-pipe bug, inherited and fixed.** The concurrent CSCE 420 ingest introduced 7 unescaped alias pipes inside table cells (`deep-learning.md`, `deep-reinforcement-learning.md`, `neural-networks.md`, `prolog.md`) plus one conditional-probability pipe inside LaTeX (`$p(s_{t+1}|s_t,a_t)$` in `deep-reinforcement-learning.md`). The alias pipes were escaped as `\|`; the LaTeX one was **not** escaped but rewritten as `\mid`, because `\|` inside math renders as a double bar and would have silently corrupted the notation. Escaping is right for markdown, wrong for math — worth remembering as a distinct case.

**A detector I wrote and discarded.** A regex for math pipes inside table rows produced ~70 hits, essentially all false: in a row with several `$...$` spans it matches from one span's closing `$` across the cell delimiter to the next span's opening `$`. The cell-count check is the only reliable table detector; the regex was thrown away rather than kept and worked around.

**Result:** 302 -> 307 pages. Broken wiki-links 0 (excluding code fences). Malformed table rows 0. Orphans 0. Source pages unlinked from their course 7 -> 0. Index count corrected to 307 and accurate in both directions.

---

## [2026-09-01] lint | Confirmation audit — deep check added, 4 defects fixed

Re-ran the standing audit at the user's request (0 issues), then wrote a **second, independent checker** covering 12 problem classes the standing audit does not look at — because re-running the same script mostly confirms the script, not the data.

New checks: empty/stub files, malformed or unclosed frontmatter, encoding damage (U+FFFD), mangled LaTeX escapes, empty See Also sections, unbalanced `[[ ]]`, self-links, dangling `sources:` slugs, references to missing `raw/` files, near-duplicate page bodies (the Exam-3 failure class), and cross-vault links.

**It found 4 real defects, 3 of them mine:**

| File | Defect | Fix |
|---|---|---|
| `sources/csce420-lecture-03-logic.md` | **23 mangled LaTeX escapes** — `\neg`, `\land`, `\dots` etc. | Collapsed to single backslashes |
| `sources/csce420-lecture-02-search-and-game-playing.md` | **5 mangled LaTeX escapes** — `\le`, `\log`, `\sqrt`, `\approx` | Collapsed to single backslashes |
| `sources/csce420-lecture-02-search-and-game-playing.md` | `A\*` — literal backslash plus an emphasis marker | Corrected to `A\*`, an escaped asterisk |
| `concepts/bipartite-matching.md` | Self-link: the page wiki-linked its own title mid-sentence | Plain text |

**Cause of the escape bug, worth recording.** The two affected source pages were authored **directly with the Write tool**, where I typed `\` out of habit from the Python generator scripts — in Python `"\neg"` yields `
eg`, but Write writes literally, so the doubled backslash survived into the file. In MathJax `\` is a line break, so `$f(n) \le f(G_1)$` rendered as a break followed by the letters "le". Pages generated *through* the Python scripts were unaffected. **Rule: when authoring markdown with LaTeX via Write, type single backslashes.**

**A checker bug found too.** The first version of the deep check `break`s out of its token loop after the first match per file, so it reported 1 affected file when there were 2, and 1 escape when there were 28. Corrected to report every hit; a checker that under-reports is worse than none.

**Final state: standing audit 0 issues across all six bases; deep check 0 findings across 463 pages.**

---

## [2026-09-01] ingest | CSCE 420 Lectures 3-8 — logic, planning, probability, ML, deep learning, ethics (467 slides)

Completed the ingest of `lecture_notes_export.zip`. With Lecture 2 done earlier today, **all eight CSCE 420 slide decks are now in the knowledge base.**

**Sources ingested** (all extracted with PyMuPDF, all archived to `raw/` as `CSCE420_slideNN_*.pdf`):

| Deck | Slides | New pages | Reconciled |
|---|---|---|---|
| 3 Logic and Automated Theorem Proving | 145 | 15 | 4 |
| 4 Planning | 27 | 4 | 1 |
| 5 Uncertainty and Probabilistic Reasoning | 67 | 7 | 1 |
| 6 Machine Learning | 124 | 11 | 4 |
| 7 Deep Learning | 84 | 4 | 3 |
| 8 AI Ethics | 20 | 1 | 0 |
| **Total** | **467** | **42 + 6 sources** | **13** |

**Reconciliation, not duplication.** As with Lecture 2, these decks are the instructor's own framing of material this base previously held only as reconstructions from the practice exams. Twenty pages across the two sessions gained a "From the Lecture" section and the new source slug rather than being duplicated: Resolution, Unification, First-Order Logic, Logical Inference, Situation Calculus, Bayesian Networks, Decision Tree Learning, Neural Networks, Self-Organizing Map, Reinforcement Learning, Deep Learning, Deep Q-Network — plus the ten search/game pages from earlier.

**The through-line worth recording.** Each unit is a response to the previous unit's stated failure, and the decks say so explicitly:

- Uninformed search is bounded by *memory*, so iterative deepening trades recomputation for space — and IDA* repeats that trade one level up for A*.
- Propositional logic cannot express general rules (the Socrates challenge on slide 49 of deck 3), so first-order logic adds objects and quantifiers.
- Logic cannot represent *persistence*, so planning needs successor-state axioms — the frame problem.
- Logic cannot represent *doubt*, so probability replaces truth values with degrees of belief.
- Hand-specified models do not scale, so learning fits them from data.
- Hand-designed *features* do not scale, so deep learning learns those too.
- Deck 8 then observes that the last step cost reasoning, causality, and explainability — exactly what deck 3 had.

**Two patterns recur across the whole course**, now linked in both directions:
1. The **predicted-minus-true** gradient shape — the Perceptron rule, Backpropagation's delta, and (in CSCE 421) the softmax cross-entropy gradient.
2. **Buying tractability with expressiveness** — Horn clauses vs. full CNF, heuristic relaxation vs. exact cost, conditional independence vs. the full joint table.

**Individual results captured**: the refutation theorem and its proof; skolemization's constant-vs-function distinction encoding quantifier order; the 1%-base-rate disease calculation; the $n2^k$ vs. $2^n$ compactness result and the fact that bad node ordering destroys it; AlexNet's first-layer kernels resembling mammalian receptive fields; the sigmoid derivative trick $g'=g(1-g)$ letting the forward pass be reused; LSTM's three gates; and the transformer's parallelizability as the reason it displaced RNNs.

**A discrepancy flagged rather than smoothed over**: deck 5's decision-theory example (slides 11-12) lists Action 2's utility as 10000 in the table but computes with 1000. As computed, Action 3 wins; with 10000 it would be Action 2. Noted on the Decision Theory page.

**Extraction gaps**: recorded per-deck on each source page. Deck 6 and deck 7 are the worst affected — deck 7's figures are almost entirely external images (LeCun's tutorial, colah's LSTM diagrams, Jalammar's transformer illustrations), and deck 6's restaurant dataset table extracts as an unstructured value column, though its content is captured in prose. Decks 4 and 8 each end with a **LaTeX "Temporary page!" artifact** carrying no course content.

**Result:** 254 → 302 pages (concepts 103→141, algorithms 49→53, sources 88→94). `index.md`, `wiki/overview.md`, and this log updated. Audit across all six knowledge bases: **0 issues**.

**One error caught during the overview edit:** a `[[Classical Management Perspective]]` link — an MGMT309 page in a *different vault* — was accidentally introduced into the CS overview and removed before it could become a broken link.

---

## [2026-09-01] lint | Full audit of all six knowledge bases

Audited every base in the workspace (CS, GEOL101, MGMT309, STAT212, First Trading, General) for frontmatter validity, broken wiki-links, duplicate titles, index coverage, declared-vs-actual page counts, and dangling `sources:` slugs.

**Result: 0 issues remaining across all six bases.** Four real defects were found and fixed:

| Base | Defect | Fix |
|---|---|---|
| CS | 18 pages from the Lecture 2 ingest were never catalogued in `index.md` | Added under the CSCE 420 concept/algorithm/source sections |
| CS | Declared count stale: 236 vs. 254 actual | Corrected to 254 (103 concepts, 49 algorithms, 1 data structure, 6 courses, 6 people, 88 sources, 1 overview) |
| CS | `raw/CSCE420_slide02_*.pdf` was never archived — the deck was ingested from the scratchpad only | Copied into `raw/` |
| GEOL101 | `wiki/sources/module-6-sedimentary-rocks.md` missing the required `sources:` frontmatter field | Added `sources: []` |
| General | `[[College CS Knowledge Base]]` in `2026-04-09-claude-ai-export.md` links to a different vault and cannot resolve | Changed to plain text "CS KB", matching the same file's own convention on the three adjacent lines |

**Count discrepancy explained, not papered over.** The CS index read 236 while 254 files existed. The gap is not corruption: 18 are the Lecture 2 pages added today, and the earlier baseline of 236 was set correctly by a **CSCE 465 ingest on 2026-08-27** (a separate session — `csce465-lecture-01-course-introduction.md` and related pages). Modification-date histogram confirms three clean cohorts: April (original build), 2026-08-25 (CSCE 420/421), 2026-08-27 (CSCE 465), 2026-09-01 (today).

**Three classes of linter false positive were identified and the checker corrected**, since a checker that cries wolf is worse than none:

1. **Table-escaped pipes.** `[[Maximum Weight Independent Set\|tree DP]]` inside a markdown table cell is correct Obsidian syntax — the backslash stops the cell splitting. The checker was folding the backslash into the target name.
2. **Links inside code fences.** The BFS/DFS/DLS pages show queue evolution as `[[1]]`, `[[(d0,1)]]` — slide notation, inside ``` fences, where Obsidian does not linkify. The checker now strips fenced and inline code before scanning.
3. **Stem references and root-level pages.** `index.md` and `log.md` sit at the base root and are valid link targets; and an index may catalogue a page by filename stem (`[[overview]]`) rather than title (`[[Overview]]`). Both now count as resolved.

Note: the GEOL101 and STAT212 indexes carry no `**Current count:**` line, so count verification is skipped for them. Not an error — a convention difference — but worth adding if those bases are to be checked the same way.

---

## [2026-09-01] ingest | CSCE 420 Lecture 2 — Search and Game Playing (138 slides)

Ingested `raw/CSCE420_slide02_Search_and_Game_Playing.pdf` — deck 2 of 7 recovered from `lecture_notes_export.zip`. Extracted with PyMuPDF; footers and figure digit-runs stripped before reading.

**Significance:** this is the instructor's own treatment of material that previously existed in this knowledge base only as **reconstructions from the midterm practice exam**. The CSCE 420 memory flagged exactly this risk. Ten pages were therefore reconciled rather than left alone.

**Created (18):** Search Problem Formulation, General Search Algorithm, Uninformed Search, Breadth-First Search, Depth-First Search, Uniform-Cost Search, Depth-Limited Search, Iterative Deepening Search, Bidirectional Search, Repeated States, Best-First Search, Greedy Best-First Search, Admissible Heuristics, Beam Search, Hill Climbing, Game Playing, Game AI Milestones, plus the source page.

**Reconciled (10):** A* Search, IDA*, Heuristic Search, Local Search, Simulated Annealing, Constraint Satisfaction Problems, Minimax, Alpha-Beta Pruning, Expectimax, Adversarial Search — each gained a "From the Lecture" section and the new source slug in frontmatter.

**The organizing idea:** every strategy in the deck is the *same* algorithm with a different queuing function, so a dozen algorithms reduce to one decision — where do expanded nodes go in the node list? The deck's through-line is that **space, not time, is the binding constraint**: BFS is complete and optimal but needs O(b^(d+1)) memory, DFS needs only O(bm) but is incomplete, and iterative deepening resolves this for a constant factor of repeated work. The identical argument recurs one level up, with IDA* standing to A* as IDS stands to BFS.

**Results worth keeping:** A* optimality via f(n) <= f(G1) < f(G2), which holds *because* h is admissible; the subexponential condition |h - h*| <= O(log h*) together with the lecture's verdict that most heuristics fail it; heuristic dominance measured at depth 14 (IDS 3,473,941 nodes vs. A*/h1 539 vs. A*/h2 113); IDA*'s O(N^2) worst case when each f-contour admits one new node; alpha-beta's b^(m/2) = (sqrt b)^m, making chess's b=35 behave like 6; and greedy-vs-A* on Romania, 450 vs. 418.

**Terminology the deck insists on:** a *visit* is fetching a node from the node list and goal-testing it — distinct from *expanding*. Time complexity is counted in visits. Depth is 0 at the root.

**Remaining work — 6 of 7 decks not yet ingested:** slide03-logic (145 slides), slide04-planning (27), slide05-prob (67), slide06-ml (124), slide07-dl (84), slide08-ethics (20). Total 467 slides outstanding. All are extracted to the session scratchpad; the PDFs remain in `~/Downloads/lecture_notes_export.zip` and must be copied into `raw/` as each is ingested.

---

## [2026-09-01] ingest | CSCE 465 — Lecture 2 Security Overview (1 file)

**Source ingested** (copied to `raw/` as `CSCE465_02_SecurityOverview.2026.pdf`):
- `02_SecurityOverview.2026.pdf` — 25 PDF pages, two-up = **50 logical slides**

**Extraction note.** PyMuPDF as always here. **No image-only slides in this deck** — all 25 pages carry substantive text and the extraction is essentially complete, in sharp contrast to Lecture 1 where slides 7–18 had no text layer at all. Several slides are diagram-supported (A→B attacker diagrams, two firewall configurations, the CompSec/ComSec Venn, the ten-principle wheel) but the accompanying text carries the content in every case. Only the OC3Mon appliance photo on slide 18 is unrecoverable, and its spec is in the text.

**Pages created (6):**
- Concepts (5): Security Attack Taxonomy, Security Policy and Mechanism, Security Services, Security Assurance, Security Design Principles
- Sources (1): CSCE 465 Lecture 2 — Security Overview

**Pages updated (6):** `computer-security.md`, `cia-triad.md`, `security-threat-landscape.md`, `csce-465.md`, `guofei-gu.md`, `overview.md`.

**Where Lecture 1 and Lecture 2 disagree, and why both are kept.** Lecture 1 defined security as *the prevention of certain intentional actions*. Lecture 2 gives a formal definition: a **state** in which successful yet **undetected** theft, tampering, and disruption is kept **low or tolerable**. Three differences carry weight — it describes a state rather than an action, it concedes the target is "tolerable" rather than zero, and the word *undetected* is what elevates detection to a first-class goal alongside prevention. Both definitions are on `computer-security.md`; neither was overwritten.

**Genuine internal inconsistency in the lecture, recorded rather than normalized.** Slide 4 says security rests on **four** properties (confidentiality, authenticity, integrity, availability). Slide 5 lists **three**, folding authenticity into integrity as origin integrity. Both framings are standard, and the deck actually uses both: the four-way split when classifying attacks (fabrication targets authenticity specifically), the three-way split when listing objectives and services. Flagged on `cia-triad.md` under "Three Components or Four?" with the advice to state which framing you are using. Silently picking one would have hidden a real ambiguity the student will meet on an exam.

**The organizing insight of the deck.** Attacks are classified by *which property they violate*, one family per component:

| Attack | Violates | Nature |
|---|---|---|
| Interception (eavesdropping) | Confidentiality | Passive — hard to detect by construction |
| Tampering | Integrity (data) | Active |
| Fabrication | Authenticity (origin integrity) | Active |
| Interruption | Availability | Active |

MITM is not a fifth family but a *position* that enables all four — which is why authenticating once at connection setup is insufficient. That is complete mediation restated as an attack.

**The single sharpest idea, and the one most likely to be examined.** *Does cryptography guarantee confidentiality?* **No.** Encryption protects payload content and nothing else; who is talking to whom, from where, and how often all survive. This forced an expansion of `cia-triad.md`: confidentiality now carries the lecture's three-way split into **data**, **existence**, and **configuration** confidentiality, of which encryption addresses only the first.

**Two structural asymmetries worth keeping.**
1. **Prevention is more fundamental than detection** — not by preference but by dependency: detection requires an audit trail, and that trail must be protected from alteration by a preventive mechanism. Yet detection is the *only* option in two cases the lecture names: misuse of legitimately authorized privileges (the insider problem — indistinguishable from use at the moment of access), and modification of messages in a network.
2. **Defense is inherently more expensive than offense** — the defender must secure every path, the attacker needs one weakest link. Two of the ten design principles (work factor, compromise recording) exist purely to ration defensive effort against this, and the prevention/detection/recovery split is a response to it. This is the economic fact under the whole field.

**The ten design principles got their own page** and are the most durable material the course will produce — Saltzer & Schroeder, 1975, and unchanged since. Grouped on the page as structure of the mechanism (1–4), distribution of authority (5–7), and concessions to reality (8–10).

**Three open questions the lecture poses and does not answer** are recorded on the source page rather than answered by me, since they read like exam prompts: what a promiscuous `tcpdump` can see on a *switched* network; where else caching undermines complete mediation; and whether the root/administrator concept violates least privilege.

**Cross-course connection strengthened.** The lecture's claim that *most TCP/IP protocols were not built with security in mind* is the general form of what `arp.md` already documented for one protocol — CSCE 313 taught ARP spoofing as a protocol flaw, CSCE 465 names both the property it violates (origin integrity) and the attack family it belongs to (fabrication). [[Virtual Memory]] also reappears here from CSCE 313, now as an instance of least common mechanism.

**Two defects I introduced and fixed in the same pass.** Alias links `\|` inside table cells in `security-policy-and-mechanism.md` and `csce-465.md` split rows into phantom columns — the exact bug the 2026-08-27 audit catalogued. Caught by re-running the table checker before logging. Escaping alias pipes inside table rows should be treated as a standing rule for this KB.

**Result:** 230 -> 236 pages. Broken wiki-links 0. Malformed table rows 0. Orphans 0. Index accurate in both directions; stated count 236 matches actual.

---

## [2026-08-27] lint | Full KB audit — 15 checks, 14 defects repaired

Ran a 15-check structural audit over all 230 pages after the CSCE 465 ingest. Checks: duplicate titles, missing titles, broken wiki-links, orphans, frontmatter completeness, type-vs-directory agreement, `sources:` slug validity, index coverage both directions, index duplicates, stated-vs-actual page count, course-page source coverage, missing See Also, raw/ coverage, and markdown table well-formedness.

**Clean on first pass:** duplicate titles (0), missing titles (0), frontmatter completeness (0), type-vs-directory (0), `sources:` frontmatter pointing at nonexistent slugs (0), pages missing from `index.md` (0), index entries with no page (0), duplicate index entries (0), stated page count (230, matches actual), missing See Also (0).

**Defects found and repaired (14):**

| # | Defect | Files | Fix |
|---|---|---|---|
| 5 | **Slug-style wiki-links that resolve to nothing** — `[[hw3-solutions\|HW 3]]`-style links used the filename instead of the page title, so they were dead in Obsidian | `practice-proofs.md` (3), `exam-2-sample-solutions.md` (2) | Rewrote to real titles, keeping the display aliases |
| 1 | **`[[overview]]` vs title "Overview"** — case-only mismatch; Obsidian resolves it but the schema requires exact title match | `index.md` | Corrected to `[[Overview]]` |
| 5 | **Unescaped `\|` inside table cells** — literal `\|E\|`, `\|c\|`, `\|x\|` in math text split the row into phantom columns, breaking table rendering | `final-exam-sp26.md` (2 rows), `lecture-26-np.md` (1 row), `CSCE-411.md` (rows I introduced this session) | Escaped as `\|` |
| 1 | **CSCE 411 course page badly stale** | `CSCE-411.md` | See below |
| 2 | **Course pages were not hubs for their own sources** | `csce-420.md`, `csce-421.md`, `csce-465.md`, `finance-valuation.md` | Added `## Ingested Sources` sections |

**The CSCE 411 page was the real problem.** Its heading read "Topics Covered (from ingested lectures)" and listed only lectures 20–31 — but 23 lectures are ingested, so the page silently omitted 13 of them (2, 4–11, 15, 16, 18, 19) plus all 20 exam, homework, practice, and course-notes pages. Frontmatter `sources:` carried the same 10-entry list and `updated:` had been frozen at 2026-04-27 through months of ingests. A page that asserts its own completeness and is wrong is worse than one that says nothing, so this counted as a correctness defect rather than a gap. Rebuilt: full 23-lecture table with concept cross-links, an "Other Ingested Sources" section, all 46 slugs in frontmatter, and the not-yet-ingested lectures (3, 12, 13, 14, 17, 21, 30) named explicitly.

**Orphan result, and why the first number was misleading.** The raw orphan count was 34 pages with no inbound link from any *wiki* page. All 34 were sources reachable from `index.md`, so none were true orphans — but the underlying asymmetry was real: `csce-313.md` listed all 15 of its lectures while every other course page listed none, leaving 70 of 86 source pages unreachable from their own course. Adding source lists to the remaining five course pages closed it. Every source page now has a course-page inbound link, and orphans are 0 by both measures.

**Linter false positives worth recording (same class as the 2026-08-25 sweep).** The table checker initially reported 13 malformed rows; 5 were in `Karp-Reductions.md`, whose header contains a correctly-escaped `[[Turing Reductions\|Turing Reduction]]`. The checker stripped `\|` when counting row cells but not header cells, so it flagged a well-formed table. Fixed the checker, not the page. **`\|` inside a table cell is correct and must not be "repaired" — this is the second time an audit has nearly damaged it.**

**Known gap, not fixable here.** The 15 CSCE 313 source pages have **no archived source in `raw/`** — that material was ingested from text that was never dropped into the KB. Their claims cannot be re-verified against an original. Every other course's sources are archived (71 raw files, all accounted for). Dropping the CSCE 313 slide decks into `raw/` would close it.

**Result:** 230 pages, unchanged. Broken wiki-links 5 -> 0. Malformed table rows 8 -> 0. Orphans 0. Index accurate in both directions.

---

## [2026-08-27] ingest | CSCE 465 Computer & Network Security — Lecture 1 Course Introduction (1 file)

New course added to this knowledge base: **CSCE 465/765 (Computer & Network Security)**, instructor [[Guofei Gu]], director of TAMU's SUCCESS Lab. Filed inside the existing College CS Knowledge Base — same call as CSCE 420 and CSCE 421, and uncontroversial here since this is a CS course.

**Source ingested** (copied to `raw/` as `CSCE465_01_courseIntro.2026.pdf`):
- `01_courseIntro.2026.pdf` — 20 PDF pages laid out **two slides per page** = 39 logical slides

**Extraction note.** PyMuPDF again (poppler unavailable, so page-ranged reads via the harness reader fail). The 39-vs-20 discrepancy is the two-up slide layout, not animation builds. **Slides 7–18 (PDF pages 4–9) have no text layer at all** — 2–5 images per page and under 15 characters of text. These are the news-headline / incident-screenshot slides motivating the course, plus a botnet architecture diagram on slide 15. The specific incidents cited in lecture are unrecoverable from this PDF; flagged on the source page, on `security-threat-landscape.md`, and in the overview's gaps section.

**Pages created (6):**
- Course: CSCE 465 · Person: Guofei Gu
- Concepts (3): Computer Security, CIA Triad, Security Threat Landscape
- Sources (1): CSCE 465 Lecture 1 — Course Introduction

**Pages updated (4):**
- `overview.md` — "five courses" -> "six"; new CSCE 465 section; new gaps subsection.
- `csce-313.md` — added CSCE 465 to See Also as the downstream course that names it a prerequisite.
- `arp.md` — linked ARP spoofing to [[CIA Triad]]: CSCE 313 taught it as a protocol flaw, CSCE 465 names the property it violates (origin integrity).
- `computer-networking.md` — added CSCE 465 as the course that builds network security on this substrate.

**Ingest judgment worth recording.** Roughly two thirds of this deck is administration — grading, project ideas, textbook list. That material went to the **course page**, not to concept pages, and the ~12 slides of real content produced exactly three concepts. Resisting the urge to manufacture a page per bullet is the right call for an intro lecture; the security mechanisms have not been taught yet, and inventing pages for them now would put non-instructor framing in the KB before the instructor's own arrives. This is the same failure the CSCE 420 ingest had to flag when concept pages were reconstructed from practice exams.

**The content that matters.** Security is defined as *the prevention of certain types of intentional actions*. Everything else in the lecture decomposes from the word "intentional":

| Layer | Content |
|---|---|
| Vocabulary | threat (potential action) -> attack (carried out) -> attacker (who) -> asset (target) |
| Goals | prevention, detection, recovery, survivability |
| Components | confidentiality, integrity, availability |

Two distinctions are the ones likely to be tested and are easy to collapse:
1. **Integrity splits in two** — *data* integrity (content unaltered) and *origin* integrity (came from who it claims), and origin integrity **is** authentication. The two are independent; a message can have either without the other.
2. **Only prevention assumes defense works.** Detection, recovery, and survivability all assume it failed, in increasing order of pessimism — survivability demands correct function *during* successful compromise. This is the structural reason intrusion detection is a full unit and a full homework rather than a footnote.

**Course structure worth flagging for planning.** Grading is 50% assignments / 20% Exam 1 / 25% Final / 5% participation, with four lab-heavy homeworks all built on the **OpenClaw AI agent system**. The mini-research project (required for 765, optional for 465) **replaces one homework and the entire final exam** — a 25% component — and the deadline to opt in is about one month out. That is the single most consequential decision in the syllabus and it arrives early.

**Cross-course connection.** CSCE 465 lists [[CSCE 313]] as a prerequisite and genuinely consumes it: `computer-networking.md`, `data-link-layer.md`, and `arp.md` are the substrate for the network security unit, and the process/VM/file-descriptor pages underlie OS security. In the other direction the course closes on AI agent security, which meets [[CSCE 420]] and [[CSCE 421]] from an angle neither covers — those courses ask whether a model is accurate, this one asks whether it is attackable.

**Result:** 224 -> 230 pages. Broken wiki-links: 0. Duplicate titles: 0.

---

## [2026-08-25] ingest | CSCE 421 Machine Learning — T01 Linear Regression, T02 Logistic Regression, T03 Softmax + notes (4 files)

New course added to this knowledge base: **CSCE 421 (Machine Learning)**, instructor [[Shuiwang Ji]], based on *Learning From Data*. Filed inside the existing College CS Knowledge Base rather than a separate base — same decision as CSCE 420.

**Sources ingested** (copied to `raw/` as `CSCE421_*.pdf`):
- `T01-LR.pdf` — 20 slides, Introduction and Linear Regression
- `T02-LogR2.pdf` — 30 slides, Logistic Regression for Binary Classification
- `T03-SoftmaxR.pdf` — 20 slides, From Binary to Multi-Class
- `T03-SoftmaxR-notes.pdf` — 6-page typed notes with the full derivations (Ji, compiled by Yaochen Xie)

**Extraction note:** the harness PDF reader could not do page-ranged reads (poppler/`pdftoppm` unavailable), so text was extracted with PyMuPDF instead. All pages carried extractable text; no image-only slides. Several T02 slides on image representations, transformations, and invariant representations are visual-only in substance — flagged as such on the source page.

**Pages created (16):**
- Course: CSCE 421 · Person: Shuiwang Ji
- Concepts (6): Linear Models, In-Sample and Out-of-Sample Error, Sigmoid Function, Softmax Function, Cross-Entropy Loss, Maximum Likelihood Estimation
- Algorithms (4): Linear Regression, Logistic Regression, Softmax Regression, Gradient Descent
- Sources (4): one per file

**Pages updated (4):**
- `machine-learning-paradigms.md` — added CSCE 421's framing, which splits supervised into classification vs regression and names that split as the organizing principle of the T01–T03 arc. Now dual-course (`course: CSCE 420, CSCE 421`).
- `neural-networks.md` — added the single-neuron view: logistic regression *is* one neuron; softmax regression widens it to K outputs.
- `deep-learning.md` — added the bridge from T03's closing slide: keep the softmax head and cross-entropy, swap hand-designed x for a CNN/Transformer. The dividing line is "how to learn X automatically?"
- `overview.md` — "four courses" -> "five"; new CSCE 421 section covering the arc.

**The synthesis worth recording.** The three decks are one continuous argument, not three topics. Every model is a linear model on the signal s = wTx; they differ only in what is applied to s and what error is minimized:

| Model | Applied to s | Target | Error | Optimizer |
|---|---|---|---|---|
| Linear Regression | nothing | y in R | Squared error | Closed form (pseudoinverse) |
| Logistic Regression | sigmoid | y in [0,1] | Cross-entropy | Gradient descent / SGD |
| Softmax Regression | softmax | K-class distribution | Cross-entropy | Gradient descent |

Three results tie it together, and each is on its own page:
1. **Cross-entropy is derived, not chosen** — maximizing likelihood reduces to minimizing it (Maximum Likelihood Estimation). The lecture presents the formula as "complicated and ugly" first, then earns it.
2. **Binary LR is the K=2 case of multi-class LR** — proved twice in T03, via softmax shift-invariance and via loss equivalence.
3. **The gradient is always "predicted minus true"** — dL/da_k = p_k - y_k for softmax cross-entropy, matching X^T(y_hat - y) in linear regression. This is why one optimizer serves all three, and it is the single most reusable fact in the ingest.

**Cross-course connection:** CSCE 420 already had Neural Networks and Deep Learning pages; CSCE 421 reaches the same objects from the opposite direction (bottom-up derivation vs top-down survey). Linked in both directions rather than duplicated.

**Result:** 208 -> 224 pages. Broken wiki-links: 0. Duplicate titles: 0.

---

## [2026-08-25] lint | Broken wiki-link sweep — 17 links repaired

First KB-wide link audit (previous checks covered only newly-ingested pages). Found **17** genuinely broken `[[...]]` links across 6 distinct targets, all pre-existing in CSCE 411/313/finance material.

**Checker correction:** an initial run reported 21. Four were false positives — `[[Maximum Weight Independent Set\|tree DP]]`-style links inside markdown table cells, where the backslash correctly escapes the pipe so the cell doesn't split. The linter was folding the backslash into the target name. Those 4 links (in `Vertex-Cover.md` ×2, `dynamic-programming.md`, `final-exam-sp26.md`) are valid and were left alone. Linter also now ignores `#heading` anchors.

**Repairs:**

| Target | Refs | Fix |
|---|---|---|
| `[[Disjoint Sets]]` | 5 | Page existed but was titled "Disjoint Sets (Union-Find)". **Retitled to "Disjoint Sets"** — satisfies the schema rule that page names match `title` exactly, and matches the filename `disjoint-sets.md`. H1 and body keep the "(Union-Find)" descriptor. |
| `[[Halting Problem]]` | 6 | **Created** `wiki/concepts/halting-problem.md` |
| `[[Turing Machines]]` | 1 | **Created** `wiki/concepts/turing-machines.md` |
| `[[Loop Invariants]]` | 1 | **Created** `wiki/concepts/loop-invariants.md` |
| `[[CAPM]]` | 1 | **Created** `wiki/concepts/capm.md` |
| `[[Sandeep Kumar]]` | 2 | **Created** `wiki/people/sandeep-kumar.md` |
| `[[Greedy Max-Cut]]` | 1 | Self-link sitting directly beneath its own `### Greedy Max-Cut` heading in `Approximation-Algorithms.md`; no such page exists. **Unlinked** to plain bold text. |

**De-duplication (important):** the new pages were written from content that already lived in the KB, so the donor sections were trimmed to summaries plus pointers rather than left duplicated — the same failure mode as the Exam 3 duplicate fixed earlier today.
- `decidability.md`: full "Turing Machines" section and the "The Halting Problem" section (incl. the complete diagonalization proof) → short summaries + `[[Turing Machines]]` / `[[Halting Problem]]` links. Page remains the survey/entry point.
- `wacc.md`: "Computing the Cost of Equity (CAPM)" detail (r_f maturity matching, β sourcing, Damodaran ERP) → 3-line summary + `[[CAPM]]` link. The formula stays inline since WACC needs it.

**Back-links added** per schema: `wacc.md` See Also → `[[CAPM]]`; `csce-313.md` instructor row → `[[Sandeep Kumar]]`, `[[Houngninou]]`; `overview.md` → `[[Sandeep Kumar]]` (2 spots).

**Result:** 203 → 208 pages (concepts 79 → 83, people 3 → 4). Broken wiki-links KB-wide: 17 → 0. Duplicate titles: 0.

---

## [2026-08-25] lint | Dedupe — Exam 3 Solutions (Spring 2026)

- Resolves the open item raised in the CSCE 420 ingest entry below: two source pages carried the identical title "Exam 3 Solutions — Spring 2026", making `[[Exam 3 Solutions — Spring 2026]]` ambiguous.
- Cause: the same source (`raw/CSCE411_Sp26_Exam_3_Solutions.pdf` — only one such PDF exists) was written up twice during the 2026-05-03 ingest, 24 minutes apart, under two filenames.
- Resolution: **merged into `wiki/sources/exam-3-solutions-sp26.md`; deleted `wiki/sources/exam-3-solutions-spring-2026.md`.**
- Filename kept because it matches its ingest-batch siblings (`homework-6-solutions-sp26.md`, `homework-7-solutions-sp26.md`, `final-exam-sp26.md`) and because two pages already cite the slug `exam-3-solutions-sp26` in their frontmatter (`interval-covering.md`, `max-weight-matching-trees.md`) — so no source-slug rewrites were needed.
- Content merged rather than one version discarded. Retained from the deleted page: the matrix-form dualization rule (max cᵀx s.t. Ax ≤ b → min bᵀy s.t. Aᵀy ≥ c), the note that interior-point methods *are* polynomial (Q1h), the "Answer: MWM(r)" line and the vertices-vs-edges comparison to MWIS (Q4), and `[[Graph DP]]` in See Also. Retained from the kept page: the T/F rationale column and the Homework 6 Q1(a) cross-reference.
- Lede corrected: previously claimed coverage "from Dynamic Programming through Approximation Algorithms", but no exam question involves approximation algorithms. Now reads "Dynamic Programming, Greedy Algorithms, and Linear Programming", matching the four questions.
- Tags merged; `updated` bumped to 2026-08-25.
- Page count: 204 → 203 (sources 82 → 81). Index header updated.
- Link check: all 6 inbound `[[Exam 3 Solutions — Spring 2026]]` links resolve to the surviving page; 0 broken links KB-wide; 0 duplicate titles remain.

---

## [2026-08-25] ingest | CSCE 420 Artificial Intelligence — Lecture 1, two practice exams, SOM notebook (4 files)

- Sources:
  - `raw/CSCE420_slide01_Introduction.pdf` (60 pages / 42 logical slides; Introduction, Related Disciplines, History, Summary)
  - `raw/CSCE420_midterm-practice.pdf` (2 pages; 10 problems × 10 pts)
  - `raw/CSCE420_final-practice.pdf` (2 pages; 10 problems, 100 pts)
  - `raw/CSCE420_som.ipynb` (7 cells; NumPy Self-Organizing Map, author Yoonsuck Choe, 1/7/2022)
- Text extraction: `pdftotext -layout` for bulk text; page rendering (PyMuPDF → Read) for the image-only Summary slides 33–42 and for all exam figures, since math symbols (∀ ∃ ¬ ∨ ∧ Δ, A*/IDA*) and every diagram were dropped by text extraction.
- **New course added to this KB.** CSCE 420 joins CSCE 411, CSCE 313, and Corporate Finance. Filed here rather than in a separate base since this KB already spans multiple CS courses.
- Pages created (38 new, 204 total):
  - Courses (1): CSCE 420
  - People (1): Yoonsuck Choe
  - Sources (4): CSCE 420 Lecture 1 — Introduction to AI; CSCE 420 Midterm Practice; CSCE 420 Final Exam Practice; SOM Notebook — Self-Organizing Maps (2D Grid)
  - Concepts (22): Artificial Intelligence, Strong AI and Weak AI, Turing Test, Chinese Room, Philosophy of Mind, Foundations of AI, History of AI, Symbolic AI, Neurosymbolic AI, Heuristic Search, Local Search, Constraint Satisfaction Problems, Adversarial Search, First-Order Logic, Logical Inference, Situation Calculus, Bayesian Networks, Decision Tree Learning, Machine Learning Paradigms, Neural Networks, Deep Learning, Reinforcement Learning
  - Algorithms (10): A* Search, IDA*, Simulated Annealing, Minimax, Alpha-Beta Pruning, Expectimax, Resolution, Unification, Self-Organizing Map, Deep Q-Network
- Pages updated (2): `wiki/overview.md` (four-course lede, full CSCE 420 synthesis section, CSCE 420 gaps), `index.md` (count 165→204, three new sections plus course and person entries)
- Link lint: 0 broken wiki-links across all 38 new pages.
- **Both practice exams ship without answer keys.** All worked solutions were derived during ingest and are marked on each page with a blockquote noting they are not official.
- Key entities covered:
  - **Lecture 1**: R&N's four definitions (thinking/acting × humanly/rationally) and the agent-based definition; strong vs. weak AI with the other-minds problem; six foundational disciplines; six-era history from McCulloch-Pitts (1943) to ChatGPT (2022); AI@50 age benchmark; three fuels of the DL revolution (algorithms, big data, GPUs); four DL limitations with illustrations (panda→gibbon, altered stop signs, fire-rescue common sense, husky-vs-snow spurious feature)
  - **Midterm P2**: A* keeps explored set + entire frontier (the area under the f-contour); IDA* keeps only the DFS-CONTOUR call stack (path A→C) — memory scales with area vs. depth
  - **Midterm P3**: P = e^(−ΔE/T) ⟹ lower ΔE and higher T both raise acceptance
  - **Midterm P4**: LCV gives v4 = Red; v1 and v4 are *not* adjacent (the "read the variable number carefully" trap); Blue would exhaust v3's last value
  - **Midterm P6**: **Cut #1 only** — Cut #2 sits at a MAX node whose inherited β is still +∞, so no finite α can trigger it. The "finite vs. infinite bound" test is the whole method.
  - **Midterm P9**: Set 1 not unifiable (repeated variable x forces f, clashing with g); Set 2 MGU = {x/f(A), y/A, z/f(A)} ⟹ P(f(A), A, g(f(A)))
  - **Midterm P10**: premise (2) S ∨ ¬((R∨W)→P) splits into TWO clauses (S∨R∨W) and (S∨¬P) — the exam's explicit "no ∧ in a clause" trap; False in 6 steps
  - **Final P1**: skolemize ∃z to constant C; negated conclusion ∃w¬R(w) becomes universal R(w); False in 4 steps with {x/C},{y/C},{w/C}
  - **Final P2**: Poss on the *left* ⟹ effect axiom; Poss on the *right* ⟹ possibility axiom (no partial credit on this problem)
  - **Final P5**: Gain(E,Attr1) = 2/3, Gain(E,Attr2) = **0** (both branches stay 50/50) ⟹ test Attr 1 first
  - **Final P6**: **No** — proved by odd-cycle argument. The three x-points (1,0), (1,2), (3,2) have o-points exactly at their pairwise midpoints ((1,1), (2,2), (2,1)), so no two may share a half-plane; two hidden units give only two groups.
  - **Final P10**: DQN outputs one Q-value per action (expected cumulative discounted reward), not the action itself; agent takes argmax
- **Open item (pre-existing, not from this ingest):** two source files share the title "Exam 3 Solutions — Spring 2026" (`wiki/sources/exam-3-solutions-sp26.md` and `wiki/sources/exam-3-solutions-spring-2026.md`), so `[[Exam 3 Solutions — Spring 2026]]` is ambiguous. Worth a dedupe pass.
- Student note: none recorded — no graded work or difficulty signal accompanied these files.

---

## [2026-05-06] ingest | Final Exam Solutions — Spring 2026 (PDF)

- Source: `411_Sp26_Final_Exam_Solutions.pdf` (8 pages; 6 problems)
- Text extraction: PDF visual rendering (Read tool)
- Pages created (2 new, 165 total):
  - Sources (1): Final Exam Solutions — Spring 2026
  - Algorithms (1): Longest Valley Subsequence
- Pages updated (5): Binary Search (rotated array variant + FindMax pseudocode), Dynamic Programming (LVS added to algorithm list), Maximum Flow (Fruit Salad reduction to applications), NP Completeness (Half-Cycle added to NP-complete table), index.md (count 163→165, new entries)
- Student note: DP problems were the most challenging topic this exam.
- Key entities covered:
  - **T/F clarifications**: Σdeg = 2|E| not |E| (Handshake Lemma); Bellman-Ford relaxes each edge n−1 times not once; feasible LP can be unbounded; FPTAS with ε=1 gives 2-approx; GreedyMaxCut cut ≥ |E|/2 so cut=100 ⟹ ≤200 edges; NP-complete ⊆ EXP; O(n²) constant check requires n₀≥9 not n₀=3
  - **Q2 Undecidability**: HALTS ≤_T ACCEPTS-ODD-LENGTH; M' runs M(x) then checks parity; standard use-M-as-filter Turing reduction
  - **Q3 Array Rotation**: binary search for index of maximum; answer = n − imax; O(log n); sidenote: also solvable via LDS+LIS DP
  - **Q4 Longest Valley Subsequence**: 2D DP LVS(i,j) = longest valley starting at A[i] ending at A[j]; recurrence peels second and second-to-last elements simultaneously; O(n³) time O(n²) space; fill order: decreasing i and j
  - **Q5 Fruit Salad**: max flow reduction; source→fruit (inventory cap)→customer (per-fruit cap)→sink (demand cap); feasible iff max flow = ΣC[i]
  - **Q6 Half-Cycle NP-completeness**: NP membership via ordered-vertex-list verifier; NP-hardness via HAM-CYCLE ≤_p HALF-CYCLE by adding n isolated vertices to double graph size

---

## [2026-05-03] ingest | HW6, HW7, Exam 3 Solutions (3 PDFs)

- Sources:
  - `raw/CSCE_411_HW6_Solutions.pdf` (10 pages; 6 problems)
  - `raw/CSCE_411_HW7_Solutions.pdf` (5 pages; 4 problems)
  - `raw/CSCE411_Sp26_Exam_3_Solutions.pdf` (6 pages; 4 questions)
- Text extraction: PDF visual rendering (Read tool)
- Pages created (10 new, 163 total):
  - Sources (3): Exam 3 Solutions — Spring 2026, Homework 6 Solutions — Spring 2026, Homework 7 Solutions — Spring 2026
  - Algorithms (4): Interval Covering, Max-Weight Matching in Trees, Increment and Triple, Blue-Green Trees
  - Concepts (3): Balanced Brackets, König's Theorem, LP Relaxation
- Pages updated (6): Linear Programming (dual construction procedure + worked example + integrality notes + T/F clarifications), Interval Scheduling (alternative greedy strategies table), Greedy Algorithms (backward reasoning section + new algorithm links), Bipartite Matching (LP formulation + König's theorem section), NP and Complexity Classes (Co-NP examples + Primes ∈ Co-NP + L₁−L₂ and L* closure proofs), index.md (count 153→163, new entries)
- Key entities covered:
  - **Exam 3 T/F**: MWIS NP-hard on general graphs; change-making greedy fails for arbitrary denominations; "starts last" greedy works for interval scheduling; "shortest duration" fails; LP cost formula is frequency-weighted; simplex has no poly-time guarantee; not every optimal LP solution is a vertex; dual of feasible LP may be infeasible
  - **LP Duality construction**: one dual variable per primal constraint; dual objective = primal RHS; dual constraint per primal variable; worked example from Exam 3 Q2
  - **Interval Covering**: minimum integer points stabbing all intervals; sort by finish, add finish point when uncovered; O(n log n); distinct from Interval Scheduling; pairwise-disjoint lower bound argument
  - **Max-Weight Matching in Trees**: tree DP; 2-case recurrence (skip edge vs. include edge {u,v}); grandchildren become free subproblems; O(n) via postorder
  - **5 greedy scheduling variants** (HW6 Q1): starts-last ✓ (exchange), ends-last ✗, discard-longest ✗, discard-most-conflicts ✗, discard-containing-then-ends-last ✓ (two-case induction)
  - **Balanced Brackets**: parentheses detection/LBS via greedy counter O(n); braces detection via stack O(n); longest balanced brace subsequence via DP O(n³) with diagonal memoization
  - **Delivering Pizzas**: O(n²) interval DP from central pizza shop; P(i,j) = min reviews ending at A′[j]; fill by increasing |j−i|
  - **Increment and Triple**: greedy backward; if y%3=0 last step was triple; O(log³ y)
  - **Blue-Green Trees**: 3-state DP (BG(v,0/1/2)); state 2 handles "green with forced-blue children"; O(n^{1+log₂3}) due to O(n)-digit multiplications via Karatsuba
  - **Bipartite matching LP + relaxation**: IP → LP relaxation → flow equivalence → Edmonds-Karp gives integral solution; dual = min vertex cover LP; König's theorem via strong LP duality
  - **LP Relaxation concept**: totally unimodular constraint matrices guarantee integral LP optima; TU examples include bipartite incidence matrices
  - **Primes ∈ Co-NP**: factorization certificate; verifier checks k₁·k₂=n and k₁,k₂≠1; poly-time without AKS
  - **NP closure**: L₁−L₂ ∈ NP (compose verifiers with paired certificate); L* ∈ NP (decomposition certificate with per-piece sub-certificates)

---

## [2026-04-27] ingest | Lectures 28, 29, 31 + NP-Hardness practice & scribbles (3 PPTX + 2 PDF)

- Sources:
  - `raw/Lecture28_NP-Completeness.pptx` (21 slides)
  - `raw/Lecture29_NP-Hardness_Proofs.pptx` (31 slides)
  - `raw/Lecture31_Approximation_Algorithms.pptx` (26 slides)
  - `raw/CSCE_411_NP_Hardness_Practice.pdf` (1 page; 5 problems, no solutions provided)
  - `raw/NP_Hardness_Scribbles.pdf` (1 page; embedded as Form XObject — handwritten worked example, rendered to `raw/assets/NP_Hardness_Scribbles.png` via pypdfium2 for visual reading)
- Text extraction: python-pptx (slides), pypdf + pdfium rendering (PDFs)
- Extraction notes: Many lecture slides visual-only — circuit diagrams, gadget constructions (3-SAT→3-COL color gadgets), VC bad-greedy graphs (Ryan O'Donnell construction), approximation-ratio proofs. Slide titles + prose extracted; gadget structures sketched in source pages from prose alone. Scribbles transcribed directly from rendered image.
- Pages created (8 new, 153 total — previous "182" count in index was inflated; recounted from filesystem):
  - Sources (5): Lecture 28 — NP-Completeness, Lecture 29 — NP-Hardness Proofs, Lecture 31 — Approximation Algorithms, NP-Hardness Scribbles, Practice — NP-Hardness
  - Concepts (3): Karp Reductions, Approximation Algorithms, Vertex Cover
- Pages updated (4): NP Completeness (Karp reductions section, reduction chain table, NP-hard ≠ NP-complete with HALTS, Karp reduction tips, full source list, expanded NP-complete table to include kCol, IS, Ham-Cycle, Partition), CSCE 411 (added L28/29/31 rows, final exam logistics May 5), overview (added NP-completeness/approximation lecture rows, new algorithm section, updated gaps), index.md (count corrected to 153 from filesystem; new entries in Concepts, Sources — CSCE 411 Lectures, Sources — Practice Sets; new Sources — Worked Examples section)
- Key entities covered: Karp reductions vs Turing reductions; NP-hard but not NP-complete (HALTS, Theorem 5); Cook-Levin theorem; reduction chain CIRCUIT-SAT → SAT → 3-SAT → 3-COL; failure of naive CIRCUIT-SAT→SAT (exponential blowup) and fix (auxiliary variable per gate); 3-COL gadgets (palette triangle, variable gadget, clause gadget); Karp reduction tips (direction, problem choice by structure, solution-to-solution mapping, gadgets); approximation ratio definition, PTAS, FPTAS; optimization vs decision; how to deal with NP-hardness (3 axes: time/inputs/optimality); VertexCoverApprox 2-approximation via maximal matching; greedy max-degree VC has no constant ratio; greedy Max-Cut 1/2-approximation; Vertex Cover poly on trees (DP) and bipartite (LP/König); 5 practice reductions (kCol via parameter hard-coding, kCycle via Ham-Cycle, Partition via Subset-Sum padding, HalfClique via Clique padding, NAE-4SAT via 3-SAT polarity anchor); worked example 3-COL ≤_p kCol; final exam logistics (May 5)

---

## [2026-04-22] ingest | CSCE 313 Lecture 22 — Network Security: The Data Link Layer (PDF)

- Source: `CSCE313_22.pdf` (18 slides)
- Text extraction: pypdf (installed this session)
- Instructor: Houngninou (new — distinct from Sandeep Kumar who taught L1–L18)
- Extraction notes: Pages 4, 5, 8–12, 16, 18 were visual-only (layer diagrams, Ethernet frame format, packet-switching sequence, ARP broadcast diagram). Flagged in source page.
- Pages created (4 new, 182 total):
  - Sources (1): CSCE 313 Lecture 22 — Network Security: The Data Link Layer
  - Concepts (2): Data Link Layer, ARP (includes ARP spoofing)
  - People (1): Houngninou
- Pages updated (3): Computer Networking (added Data Link Layer pointer), CSCE 313 (L22 row, Houngninou, networking concept links), index.md
- Key entities covered: OSI model (7 layers), data link layer role, Ethernet frame format (visual-only), MAC addresses (48-bit, OUI, spoofable), switch (MAC table, unicast forwarding), packet switching, ARP (broadcast/cache, arp -a), ARP spoofing (gratuitous ARP, unauthenticated, MITM)

---

## [2026-04-21] ingest | M13 — Integrating Concepts, Parts 1 & 2 (2 docx files)

- Sources:
  - `raw/M13 - Integrating Concepts, Part 1 - Transcript.docx`
  - `raw/M13 - Integrating Concepts, Part 2 - Transcript.docx`
- Text extraction: docx skill (unpack.py → XML parse)
- Pages created (3 new, 178 total):
  - Sources (2): M13: Integrating Concepts, Part 1; M13: Integrating Concepts, Part 2
  - Concepts (1): WACC
- Pages updated (2): Free Cash Flow (added m13-p1 source), Net Present Value (added m13-p2 source)
- Key entities covered: sunk cost, incremental cost classification, DDB depreciation schedule, asset disposal with capital gain, inflation-adjusted FCF, NWC treatment, WACC formula, CAPM, beta sourcing (Barron's), Damodaran forward-looking ERP, interpolated risk-free rate, end-to-end NPV calculation (Amcor case)

---

## [2026-04-21] ingest | Lectures 26 & 27 — NP and NP Verifiers (2 PPTX files)

- Sources:
  - `raw/Lecture26_NP.pptx` (25 slides)
  - `raw/Lecture27_NP_Verifiers.pptx` (26 slides)
- Text extraction: markitdown (python-pptx)
- Extraction notes: Many slides were visual-only (formal language/TM definitions, complexity class diagrams, verifier constructions, Venn diagram). Text extraction captured titles, definitions, and example content; visual proofs flagged in source pages.
- Pages created (4 new, 175 total):
  - Sources (2): Lecture 26 — NP, Lecture 27 — NP Verifiers
  - Concepts (2): NP and Complexity Classes, NP Completeness
- Pages updated (2): CSCE 411 (added L26/L27 rows, Exam 3 note), index.md
- Key entities covered: P, NP, Co-NP, EXP, verifier/certificate framework, Cook-Levin theorem, Circuit-SAT, SAT, 3-COL, Vertex Cover, TSP, Clique, complexity hierarchy

---

## [2026-04-10] ingest | Corporate Finance and Valuation Modules 3–12 (14 docx files)

- Sources (14 .docx lecture transcripts):
  - `M3_ Annuity transcript.docx`
  - `M3_ Perpituity.docx`
  - `M3_ Mafia Loan.docx`
  - `M3_ Payday Loan transcript.docx`
  - `M4_ Fischer 1.docx`
  - `M4_ Fischer 2.docx`
  - `M6_ PE Ratios.docx`
  - `M7 - Calculating Volatility - Transcript.docx`
  - `M7_ Diversification- Transcript.docx`
  - `M8 - Twitter 1 - Transcript.docx`
  - `M8 - Twitter 2 - Transcript.docx`
  - `M10 - NPV Rule Is Superior - Transcript.docx`
  - `M11_ Importance of Accounting transcript.docx`
  - `M12_ What Is Free Cash Flow.docx`
- Raw files copied to: `raw/`
- Pages created: 43 new, 171 total
- Course: Corporate Finance and Valuation (1 course page created)
- Concepts created (11): Time Value of Money, Perpetuity, Annuity, Effective Annual Rate, Fischer Equation, PE Ratio, Volatility, Diversification, Efficient Market Hypothesis, Net Present Value, Free Cash Flow
- Sources created (14): one per transcript, slugs m03-annuity through m12-free-cash-flow
- overview.md updated: added Finance section with module arc and concept links
- index.md updated: new course entry, new Concepts — Corporate Finance section, new Sources — Corporate Finance section; count 128 → 171

---

## [2026-04-10] ingest | CSCE 313 Lectures 1–18 (14 PDFs)

- Source file: `csce313_extracted.txt` (text extracted from 14 PDFs, delimited by `====START_NN====` / `====END_NN====` markers)
- Lectures ingested (by marker): 01, 02, 05, 06, 07, 08, 09, 10, 11, 12, 14, 15, 16, 18
- Page counts: L1 (36), L2 (28), L5 (45), L6 (24), L7 (22), L8 (28), L9 (35), L10 (23), L11 (39), L12 (35), L14 (31), L15 (31), L16 (21), L18 (51)
- Instructor: Sandeep Kumar | Textbooks: OSSTEP, APUE | Platform: Linux/GCP
- Text extraction notes: Many slides are diagram-only (memory layouts, CPU diagrams, state machines, three-table kernel diagrams). Flagged in source pages. x86-64 register table (L1 p26) garbled during extraction.
- Pages created (55 new, 128 total):
  - Sources (14): one per lecture
  - Concepts (18): Operating Systems, Processes, Virtual Memory, System Calls, Interrupts and Exceptions, Inter-Process Communication, Pipes and FIFO, Process API, Process Attributes, UNIX File I/O, File Descriptors, File Systems, Threads, Thread Synchronization, Mutexes and Locks, Condition Variables, Semaphores, Computer Networking
  - Courses (1): CSCE 313
  - overview.md updated: added CSCE 313 section
  - index.md updated: new Concepts (CSCE 313), new Sources (CSCE 313), new Course entry

---

## [2026-04-09] ingest | Lectures 2–19 + 18 PDFs — CSCE 411 (bulk ingest)

- Sources — Lectures (13 PPTX files):
  - Lecture2 (15 slides), Lecture4 (19), Lecture5 (10), Lecture6 (21), Lecture7 (19), Lecture8 (28), Lecture9 (36), Lecture10 (49), Lecture11 (38), Lecture15 (29), Lecture16 (27), Lecture18 (22), Lecture19 (14)
- Sources — PDFs (18 files, 1 duplicate noted):
  - Notes: Section 1, Section 2, Chapter 3 (duplicate)
  - Exams: Exam 1, Exam 2, Exam 2 Sample
  - Homework: HW2, HW3, HW4, HW5
  - Practice: Asymptotic, D&C/Graphs, DP+Greedy, DP, Proofs, SP+MSTs, Undecidability
- Text extraction: python-pptx (slides), pdfminer (PDFs)
- Pages created (56 new, 73 total):
  - Sources (30): 13 lecture + 17 PDF source pages
  - Concepts (11): Proofs & Induction, Decidability, Asymptotic Analysis, Master Theorem, D&C, Graph Theory, BFS/DFS, Backtracking, SSSP, MST, Max Flow, Bipartite Matching, Stable Matching
  - Algorithms (16): Turing Reductions, Binary Search, Karatsuba, Topological Sort, SCCs, Dijkstra's, Bellman-Ford, Prim-Jarník, Kruskal's, Ford-Fulkerson, Edmonds-Karp, Gale-Shapley (+ previously: LIS, Subset Sum, Floyd-Warshall, MWIS, Interval Scheduling, Huffman, Simplex)
  - Data Structures (1): Disjoint Sets
- Notes: Slide content heavily visual for mathematical content (equations, diagrams). Key algorithms with visual-only recurrences flagged in wiki pages.

---

## [2026-04-09] ingest | Lectures 20, 22, 23, 24, 25 — CSCE 411

- Sources:
  - `raw/Lecture20_Dynamic_Programming_2.pptx` (15 slides)
  - `raw/Lecture22_Graph_DP.pptx` (15 slides)
  - `raw/Lecture23_Greedy_Algorithms.pptx` (45 slides)
  - `raw/Lecture24_Linear_Programming.pptx` (12 slides)
  - `raw/Lecture25_LP_Pt2.pptx` (21 slides)
- Text extraction method: python-pptx
- Pages created (17 total):
  - Sources (5): Lecture 20, 22, 23, 24, 25
  - Courses (1): CSCE 411
  - People (1): Calvin Beideman
  - Concepts (4): Dynamic Programming, Graph DP, Greedy Algorithms, Linear Programming
  - Algorithms (7): LIS, Subset Sum, Floyd-Warshall, MWIS, Interval Scheduling, Huffman Coding, Simplex
  - Overview (1): overview.md
- Notes: Many slides were visual-only (diagrams, equations on whiteboard-style slides). Text extraction captured titles, definitions, and textual content but not mathematical notation from images. Flagged in relevant wiki pages with "visual slide" notes.

---

## [2026-04-09] setup | Vault initialized

- Schema created: CLAUDE.md
- Files created: index.md, log.md, wiki/overview.md
- Directories: raw/, raw/assets/, wiki/concepts/, wiki/algorithms/, wiki/data-structures/, wiki/courses/, wiki/people/, wiki/sources/
- Notes: Vault created as sibling to First Trading Knowledge Base. PPTX files moved from wrong vault.
