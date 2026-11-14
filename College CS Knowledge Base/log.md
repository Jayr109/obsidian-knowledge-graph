# Log

Append-only operation log. Newest entries first.
Parse recent entries: `grep "^## \[" log.md | head -10`

## [2026-11-08] ingest | CSCE 421 T11 PCA + Autoencoders (slides + notes) - 5 new pages, 5 updated

Ingested the PCA deck and its companion typed note. **T11 is the first unsupervised topic in CSCE 421** - every deck through T10 is supervised.

**Sources (2):** `CSCE421_T11-PCA-slides.pdf` (32 slides), `CSCE421_T11-PCA-notes.pdf` (8 pages, by Ji with Zhengyang Wang and Ying Wei). Both extract cleanly - no figure reconstruction needed, unlike T04/T08/T09. Slide numbers match PDF pages (no offset).

**Pages created (5):** the two source pages; [[Principal Component Analysis]] (algorithms/); [[Singular Value Decomposition]] and [[Eigendecomposition]] (concepts/).

**Pages updated (5):** [[Autoencoders]] extended with a `# The CSCE 421 Treatment` section and promoted to `course: CSCE 420, CSCE 421`, following the [[Backpropagation]] precedent - this is the sixth dual-course page; [[Unsupervised Learning]] gained an "In CSCE 421" section and the same dual-course promotion; [[CSCE 421]] course page gained a T11 arc row, a **fifth pivot** (labels given up at T11), and the two new sources; `index.md`; `wiki/overview.md`.

**Why three new pages rather than one.** The deck spends slides 2-15 on linear algebra before PCA appears, and the notes mirror that split (SS2 basic concepts, SS3 SVD, SS4 PCA). Eigendecomposition and SVD each carry results used independently of PCA - the best-low-rank-approximation theorem in particular is what makes PCA's reconstruction proof work - so they are their own pages rather than a preamble buried in the PCA page.

**The notes carry material the slides do not**, unlike the T05 note which merely restated its deck. Three additions, all recorded: the **uncentered-reconstruction derivation** (why `GG^T X` is not the truncated SVD of `X`, and why the leftover mean term should not count as error - this is the proof behind slide 24's bare "center the data" advice); the **"will gradient descent give the same result as PCA?"** answer (yes on reconstruction error, not necessarily on `W`, because PCA solutions differ by an orthogonal matrix); and the wider autoencoder family (word2vec, VAE, GAN).

**Two exercises in the notes, neither with a solution.** SS6.1 asks for the SVD of a symmetric matrix whose eigenvalues include **-2** - the point being that singular values must be non-negative and sorted, so the answer is `sigma = (3, 2, 1)` with a sign absorbed into a singular vector and a reordering. SS6.2 asks for a complete proof of the Ky Fan theorem, which the deck states and uses without proving. Flagged on the notes source page as likely homework.

**Three open questions the deck poses without answering** (slide 13) are recorded on [[Singular Value Decomposition]] with worked answers: when SVD and eigendecomposition coincide (symmetric **and** positive semi-definite), why `Lambda` may be negative while `Sigma` may not (SVD has two independent bases, so a sign can be pushed into a singular vector), and why that does not cost generality.

**Audit.** The 5 new and 5 updated pages pass a scoped check with 0 issues. One self-inflicted defect caught before linting: an aliased wiki-link inside a markdown table row on [[Eigendecomposition]] - the same unescaped-pipe class of bug found in the T09/T10 ingest - removed by dropping the alias.

## [2026-11-04] ingest | CSCE 465 Lectures 10 (Network Basics) + 11 (Malware) — 14 new pages, 9 updated

Three files handed over, **one a duplicate**: `CSCE465GDB-1 (1).pdf` hashed identical to `raw/CSCE465_GDB_Basics.pdf` (`b2f926f5…`), ingested 2026-10-25. That is the **third `(1)`-suffixed re-download in three ingests** — after the 3b deck and the Lecture 8 deck. Hash-first is now unambiguously the highest-value step in the pipeline.

The other two open the **network security** unit, the last large gap in the course outline.

**Sources (2):** `CSCE465_10_NetworkBasics.pdf` (13 PDF pages, two-up, 26 slides — the shortest 465 deck) and `CSCE465_11_Malware.pdf` (29 pages, two-up, **57 slides — the largest deck of the semester**).

**Pages created (14):** from L10 — [[Internet Protocol]], [[TCP]], [[ICMP]], [[HTTP]], [[SMTP]]; from L11 — [[Malware]], [[Computer Viruses]], [[Worms]], [[Notable Worms]], [[Search Worms]], [[Botnets]], [[Stuxnet]]; plus both source pages.

**Pages updated (9):** [[Computer Networking]], [[Data Link Layer]], [[ARP]], [[Security Threat Landscape]], [[Buffer Overflow]], [[Buffer Overflow Defenses]], [[Public Key Infrastructure]], [[Password Authentication]], and [[Guofei Gu]] (which gained a BotHunter section and the L11 slug, since real content transferred).

### Five slides deliberately produced no pages

Lecture 10 is background, and a third of it is **already in the KB from [[CSCE 313]]**: OSI/TCP-IP layering and the client-server model on [[Computer Networking]], Ethernet frames and encapsulation on [[Data Link Layer]], and [[ARP]] in full, spoofing section included. **No page was created for any of them.** The three CSCE 313 pages got cross-links into the new protocol pages instead, and the new pages carry only what 313 does not — the datagram service, the TCP header and handshake, ICMP types, and the two application protocols. Third time this split has been applied (Lectures 7, 9, now 10) and the first time it removed most of a deck.

The flip side: `internet-protocol.md` and `computer-networking.md` both discuss IP, so that pair was the duplication risk. They divide as **protocol vs addresses** — datagram semantics, protocol numbers and routing tables here; dotted-decimal, byte order and `inet_pton` there.

### What the two decks are actually for

Lecture 10 has **almost no security content**, and that is the point — it is the protocol background the rest of the unit attacks. It paid off within one deck: Slammer is a single UDP datagram to port 1434, Nimda bulk-mails itself over [[SMTP]], Welchia uses [[ICMP]] to find live hosts, Santy injects over [[HTTP]].

The two derived insights worth keeping are both about **absent authentication**. [[Internet Protocol]]: routers forward on the destination field and nothing checks the source, which is why spoofing is free. [[SMTP]]: `HELO` and `MAIL FROM:` are strings the client types, and the server's *"Sender ok"* means **well-formed, not genuine** — so the deck's innocuous "send an email with telnet" exercise is a demonstration of email spoofing, and the clearest [[CIA Triad|origin integrity]] failure since the hash unit.

### A prediction closed, nine weeks later

[[Security Threat Landscape|Lecture 2's threat survey]] (ingested 2026-09-01) recorded that *"malware analysis is one of the course's network security topics"* and that botnets *"got their own slide, which matches [[Guofei Gu]]'s BotHunter work."* **Lecture 11 delivered both** — and closes on BotHunter by name, with Gu as first author. Same pattern as the Lecture 4 hash gap: recording a gap **with a testable hypothesis** keeps paying.

### Fact agreement checked against Lecture 9, not assumed

Lecture 9 motivated buffer overflow with a worm list; Lecture 11 details the same worms. Three figures overlap and all **agree**: Morris at "6,000 machines" (L9) vs "6–10% of all Internet hosts" (L11) — consistent at roughly 60,000 hosts in 1988; Slammer at **75,000** SQL servers in both; and the worm list itself, where L11 details a subset of L9's. Recorded as a table on the L11 source page.

### A page split along a real seam

[[Notable Worms]] came out at **1,977 words**, the largest page in the KB and well past the ~700-word guidance in `CLAUDE.md`. Rather than leave it (as previous audits did for RSA and Block Cipher Modes), the **search worms** section was split to [[Search Worms]] — a genuinely distinct propagation model with its own defence story, where the countermeasure is a *search engine* refusing to answer. Notable Worms is now 1,619 words and remains a chronology, which reads better whole.

### Extraction

Both decks extracted cleanly as text; **no font mangling this time** (unlike Lectures 8 and 9). Byte counts on L10 were cross-checked between two slides and agree: encapsulation gives 22/20/20/4/64–1500, and the Ethernet slide independently gives preamble 8 + dest 6 + src 6 + type 2 = 22.

**The real gap is Lecture 11's measurement plots**, which are caption-only: the Code Red host-infection-rate curve, the Paxson Code Red I/II plot, the two Slammer world maps from Moore et al., the Blaster plot and the Google/MyDoom query graph. **Their captions state the findings**, which are recorded — but the curves and geographic distributions are not in the KB. Noted on the source page and in the overview.

**Deck erratum:** L10's TCP data-transfer diagram reads **"Send AXK 1"** for *ACK 1*. Also both handshake diagrams label their columns *"Host"* and *"Client"* rather than client and server; the derived page uses **initiator / responder**, which is a presentation change and is flagged as such.

### Also fixed in passing

The overview's CSCE 465 lede still read *"Software security, network security and web security remain outstanding"* — stale since Lecture 9 landed on 2026-10-25 and the sentence was not updated then. Corrected, and the outstanding list is now accurate: **vulnerability analysis, firewalls, intrusion detection, web security**.

### Gaps after these decks

- **Network security is open but incomplete** — vulnerability analysis, firewalls, intrusion detection and web security all outstanding. Intrusion detection is the natural successor given BotHunter, and it is one of the four homework units.
- **No Lecture 6, and 6a still implies a 6b.** Unchanged since Lecture 7.
- **Homework position unchanged** — still only HW1, still only its briefing deck. Now five ingests old.

**Result:** all six bases pass, first run, no defect introduced. CS **462 pages** (448 + 14; one page had been added by a concurrent session since the last count), GEOL 75, STAT 47, MGMT 25, Trading 9, General 5. Count recomputed from disk.

---

## [2026-11-04] lint | Post-ingest audit, all six bases

`tools/kb_lint.py` passes on all six bases, and `deepcheck.py` was recreated because the old copy was gone from the scratchpad. It found two items across 609 pages. One was a real defect, a self-link on [[Password Authentication]], now plain text. The other is a false positive: `MAX[8, MIN[3,7]]` on [[CSCE 420 Homework 2 Solutions — Fall 2026]] is tree notation, not a broken link, so it was left as is and will keep appearing in that check.

---

## [2026-11-04] ingest | CSCE 420 export re-pull #3 — HW4, fixed HW3 notebook, and corrections to earlier pages

Fourth delivery of `course_files_export`. Hash-diffed all 64 content files against `raw/`: 61 byte-identical, 3 new. Checked coverage directly as well: 38 of 38 transcripts match a lecture page by date, and the decks, practice exams, HW1 to HW3, SOM notebook, recordings and demo all have pages.

**New:** `CSCE420_HW4_Fall2026.pdf`, `CSCE420_HW4_Fall2026_ml.ipynb`, `CSCE420_HW3_Fall2026_resolution-fixed.ipynb`. One new page, [[CSCE 420 Homework 4 — Probability, Learning, Deep Learning]], marked `exam: final`, asks only, read from rendered pages so the figures and CPTs are captured. It records errors in the sheet, the main one being P9's worked example (−0.1 × 2.6 printed as −2.6; it is −0.26). The fixed notebook differs from the original by four lines of raw-string changes and no logic.

**Not ingested, on purpose:** 94 Canvas template PNGs, and `course_images/` (a photo of the instructor at his desk, its duplicate, and a Module 12 banner). None has course content.

**Corrections to my 10-20 and 09-30 work, found while re-reading:**
- **HW2 key page was incomplete.** I had read the docx through a 7,000-character cut-off: P12.3 was partly inferred and P12.4 was missing. I had also never opened its two figures, so the per-node α/β values, which HW2 P2(b) grades, were absent. All added. An independent α-β run reproduces root 4 and the same five cuts.
- **HW1 key page:** P10 was written without reading page 7. Node lists added; the earlier text was not wrong, only thin.
- **HW3 page stated something false:** "only one of the three is derivable" for the Unicorn theorem. A truth-table check shows H and G are entailed and M is not. Claim removed.
- **HW2 key P4 note was wrong:** it named one row as the one that matters. Two rows have P ∨ Q false. Fixed.
- **raw/ immutability breach:** on 09-30 I overwrote `CSCE420_HW2_Fall2026.pdf` with the corrected sheet, which the schema forbids. The original is restored from the first export as `CSCE420_HW2_Fall2026_original-4-cuts.pdf`. The corrected sheet stays at the original name because pages cite it there.

Also: added the family tree to the HW3 page (it had been described but not recorded), flagged the sheet's `\\==` against Prolog's `\==`, and updated the stale "Fall has only HW1 and HW2" notes on the 03-18 and 04-08 pages.

**Index** recounted from files. Linter run after writing.

---

## [2026-10-25] query | Begin guided CSCE 465 HW3 setup

Reviewed the HW1 briefing, [[Stack Smashing]], and [[GDB]] for the user's request to work through HW3 slowly by task. Prior-session retrieval verified the HW1 Ubuntu VirtualBox/OpenClaw setup and `~/csce465-agentsec/hw1`; no HW2 session was verified. Retrieved HW3 setup and Task 1 details through available file context after direct PDF reading failed. First user checkpoint: list the existing course project directory inside the VM before making changes. No VM experiments have been run.

---

## [2026-10-25] ingest | CSCE 465 Lecture 9 (Buffer Overflow) + gdb recitation — 11 new pages, 5 updated

Three files were handed over. **One was a duplicate:** `08_SecurityTheory-2 (1).pdf` hashed identical to `raw/CSCE465_08_SecurityTheory.pdf` (`30746bc0…`), already ingested on 2026-10-20 — skipped before any work was done. This is the second time the `(1)` suffix has signalled a re-download of an existing deck; md5-first continues to pay for itself.

The other two opened the **software security** unit, flagged as outstanding after Lectures 7 and 8.

**Sources (2):** `CSCE465_09_BufferOverflow.pdf` (24 PDF pages, two-up, ~47 logical slides) and `CSCE465_GDB_Basics.pdf` (11 pages, **one-up** — the first CSCE 465 deck that is not two-up, and TA-delivered rather than [[Guofei Gu]]'s).

**Pages created (11):** [[Buffer Overflow]], [[Stack Smashing]], [[Shellcode]], [[Heap and Pointer Overflows]], [[Format String Vulnerabilities]], [[Unsafe C Functions]], [[Buffer Overflow Defenses]], [[Stack Canaries]], [[GDB]], plus both source pages.

**Pages updated (5):** [[Processes]] and [[Virtual Memory]] each gained a **Security View** section, [[Process Attributes]], [[Operating System Security]] and [[Security Design Principles]] gained cross-links.

### A page deliberately not created

The deck spends two slides on process memory regions — text, data, heap, stack. [[Processes]] and [[Virtual Memory]] **already carry that layout**, from CSCE 313, under identical headings. Creating a `process-memory-layout` page would have made it the third copy. Instead both CSCE 313 pages gained a *Security View* section explaining what the layout means for an attacker, and the 465 pages link across. Same discipline as the Lecture 7 ingest, applied before writing rather than caught in audit.

### The one slide that needed rendering to recover at all

Slide 40, *"Bugs to Detect in Source Code Analysis"*, extracted as a **substitution cipher** — `! "#$%&'"$(%)*+',-.-/0%` — because the list is set in a font with a scrambled encoding. The mapping is not a simple shift (`c`→`/`, `d`→`5`, `e`→`-`, `r`→`#` is not monotonic), so it was **not reconstructed by hand**. Rendered at 2.4x and read: all **20 defect classes** recovered verbatim onto [[Unsafe C Functions]]. Four of the twenty are overflows; the rest are the lifetime and resource bugs that become exploit primitives later.

The gdb deck's text layer is likewise thin — **3,870 characters across 11 pages**, because slides 6–10 are terminal screenshots. All five rendered and read; both worked sessions (the recursive `backtrace`/`info frame` dump, and the `b main`/`s`-into-`strlen` session) are on [[GDB]]. Nothing in either deck is unrecoverable.

### The cross-link worth having

`info frame` prints `saved rip` and the address it lives at. That is **the exact word [[Stack Smashing|stack smashing]] overwrites**, and `rbp` sits 8 bytes below it, exactly as the frame diagram predicts. The recitation presents this as debugging output; read against Lecture 9 it is a map of the attack surface. Recorded on [[GDB]], along with the lab caveat that **gdb disables ASLR by default**, so an exploit developed under the debugger often fails outside it.

### A defect I introduced, caught, and reverted

Check 14 failed on one row of [[Buffer Overflow]]: `[[Stack Smashing|stack smashing]]` inside a table cell with an **unescaped pipe** — the recurring defect, made again despite being documented.

The fix was worse than the bug. The repair script's regex, `\[\[([^\]\|]*?)\|([^\]]*?)\]\]`, treated an **already-correct** `[[A\|B]]` as unescaped, because its character class matched the backslash and then the pipe. Run wiki-wide it rewrote `\|` to `\\|` in **85 places across 25 files**, most of them pages this ingest never touched — `hmac.md`, `Karp-Reductions.md`, `prolog.md`, `CSCE-411.md`, `overview.md`. It surfaced only because the console crashed on a UnicodeEncodeError while *printing* the summary, after every file had already been written.

Reverted with a targeted script and verified two ways: **zero** `\\|` sequences remain anywhere in the wiki, and every collateral file is now **byte-identical to HEAD** (`git diff --quiet` on each). The one genuine fix survives.

**Two rules out of this.** First, a repair that edits files it was not asked to look at should be **scoped to the pages of the current ingest**, not run wiki-wide — the blast radius was 25 files for a one-line defect. Second, **print the plan before writing anything**: had the script listed its proposed edits and exited, the double-escaping would have been obvious in the first row of output instead of after 85 writes. The UnicodeEncodeError that masked the summary is itself a reason not to rely on post-hoc console output as the safety net.

### Gaps after this deck

- **Software security is open but probably not complete** — this deck is memory corruption only. Integer overflows, race conditions and general input validation would normally also fall under the outline's software-security entry.
- **Network and web security remain entirely outstanding**, along with malware, vulnerability analysis, firewalls and intrusion detection.
- **No Lecture 6, and 6a still implies a 6b.** Unchanged.
- **Homework position unchanged:** still only HW1, still only its briefing deck.

**Result:** all six bases pass — CS **447 pages**, GEOL 75, STAT 47, MGMT 25, Trading 9, General 5. Count recomputed from disk (436 + 11 = 447), not incremented.

---

## [2026-10-25] query | Audit HW3 code and provide LaTeX source

Read the project memory index and the CSCE 421 and homework-writing memory files. Audited both variants inside the submitted ZIP: data loading, both preprocessing modes, unchanged starter sections and comments, and all 20 logged epochs. Independently evaluated the saved model weights using the archived implementations; test accuracies reproduced 64.94% and 61.24%. The written answers agree with [[CSCE 421 T09 - Convolutional Neural Networks]], [[Convolution]], [[Batch Normalization]], [[Dropout]], and [[CNN Architectures]]. Found a copy-and-paste indentation issue caused by wrapping the PDF's run command; corrected it in the requested LaTeX source. Used the stored preference for a plain article template and basic tables. Checked the source and command syntax without compiling or generating a PDF, as requested. The code ZIP required no changes.

---

## [2026-10-25] query | Check CSCE 421 HW3 against the knowledge base

Reviewed the completed HW3 report against [[Convolution]], [[Batch Normalization]], [[Dropout]], [[CNN Architectures]], and [[CSCE 421 T09 - Convolutional Neural Networks]]. Checked the original T09 slides for convolution dimensions and parameter counts (38-41), batch normalization (64-70), dropout (74-76), LeNet (91), and the stride-2 projection shortcut (107). The written answers and implemented architecture agree with these materials; no homework corrections were needed. Training and test results remain the measurements from the completed experiments. User requested that the knowledge base be used when answering.

---

## [2026-10-20] lint | Fourth audit - one real duplication found, and a false-positive check narrowed

Audit of the Lecture 8 ingest. The linter was clean on the first run, so this audit tested the three things it structurally cannot see: **duplication**, **inverted facts**, and **provenance**.

### The one real defect: duplicated DAC/MAC prose

An 8-gram shingle comparison of the eight new pages against the four Lecture 7 pages they sit on returned **17 shared 8-grams**, all between `access-control-matrix.md` and `access-control-models.md` — the AppArmor example, the process-labeling example, and the "dominance calculus" sentence, written into both pages in the same session.

This is exactly the defect the Lecture 7 ingest went out of its way to avoid against CSCE 313, and it recurred **within CSCE 465** because two pages from adjacent lectures both legitimately discuss DAC and MAC. **Fixed by deciding ownership rather than trimming words:** [[Access Control Models]] keeps the full DAC/MAC treatment including the Lecture 8 examples, and [[Access Control Matrix]] now states only what the distinction does to *the matrix itself* — stored and editable under DAC, computed from labels under MAC, which is what makes the [[Safety Problem|safety question]] answerable over a derived matrix and not over a stored one. Re-tested: **0 shared 8-grams.**

The lesson is narrower than "check for duplication." Two pages written in the same session from the same deck are the high-risk pair, not two pages from different courses — those get attention precisely because the overlap is obvious.

### Fact agreement: the rule directions

BLP and Biba are mirror images, so an inverted rule is the single most damaging error this deck could produce and the least visible. Every page stating a direction was checked, plus a pattern test for any sentence naming BLP alongside a Biba direction (or the reverse) outside an explicit "dual" context. **No inversions.** All four rules are stated identically on [[Bell-LaPadula Model]], [[Biba Integrity Model]], [[Security Models]] and the source page.

### The worked example, recomputed independently

The "can DocC leak to Bob?" answer on [[Bell-LaPadula Model]] is derived, not given by the deck, so it was recomputed from the slide-28 labels by a separate script implementing dominance from scratch. The read matrix matches the page cell for cell, and the conclusion holds: Alice and Charlie can read DocC, Bob can read only DocA, and the \*-property blocks both of them from writing to DocA — **no legitimate flow**. The page's caveat that a covert channel is outside the model's scope stands.

### A check that was too broad, narrowed rather than kept

The symbol-hygiene check flagged `¹` as a mangled glyph in **11 pre-existing pages** — all false positives. In those pages it is a legitimate superscript: `IP⁻¹`, `10²¹`, `e⁻¹ mod φ(n)`, `2¹¹²`. Only `Î`, `Í`, `È` and `o¢` are reliable indicators of the symbol-font mangling this deck produces, and the only page containing them is the Lecture 8 **source page**, which documents them deliberately. Same principle as the two checks deleted in audit 3: a check whose output is mostly false positives measures nothing.

### Provenance: 23 blockquotes, all correctly labelled

Nine of the 23 blockquote leads in the new pages carry a *derived* marker; the other 14 are **lecture quotations**, which correctly have none. Each was read individually — "Theorem.", "Simple Security Condition:", "Important point: integrity labels are different from security labels" and the rest are the instructor's words. This confirms audit 3's conclusion that the check cannot be automated: the distinction is between a quote and an inference, and both are well-formed markdown.

### Also verified

- **`sources:` hygiene held.** 13 pages cite the Lecture 8 slug (all received content); 5 link to the new pages **without** citing it ([[Operating System Security]], [[Halting Problem]], [[Decidability and Undecidability]], [[Security Design Principles]], and the source page itself). This is the defect made on five consecutive 465 ingests and **not made on the last two**.
- **No unescaped alias pipes** in any table row across the eight new pages.
- **Page sizes:** 494-866 words. Three sit above the ~700-word guidance in `CLAUDE.md` ([[Bell-LaPadula Model]] 866, [[Chinese Wall Model]] 842, [[Biba Integrity Model]] 807) and were left whole — each is one model with one set of rules, and splitting a model's two rules onto separate pages would cost more than the length does.
- **Index count recomputed from disk, not incremented.** It had claimed 436 while its own breakdown summed to 415 and the real figure was 427.

**Result:** all six bases pass. CS 436 pages, GEOL 75, STAT 47, MGMT 25, Trading 9, General 5.

---

## [2026-10-20] ingest | CSCE 465 Lecture 8 — Security Theory: Policies and Models — 9 new pages, 7 updated

The security-theory deck, and the most abstract lecture of the course: it proves the general security question unanswerable, then presents the four classical models that work around that. Source `08_SecurityTheory-2.pdf` hash-checked against the nine 465 decks already in `raw/` (no match), copied in as `CSCE465_08_SecurityTheory.pdf`, extracted with PyMuPDF — **24 PDF pages, two-up, 47 logical slides**.

**Pages created (9):** [[Safety Problem]], [[Access Control Matrix]], [[Security Models]], [[Multi-Level Security]], [[Bell-LaPadula Model]], [[Biba Integrity Model]], [[Chinese Wall Model]], [[Role-Based Access Control]], and the source page [[CSCE 465 Lecture 8 — Security Theory: Security Policies and Models]].

**Pages updated (7):** [[Security Policy and Mechanism]] (state-partition definition, the Anne/Bill cheating example), [[CIA Triad]] (the formal `X`/`I` definitions and the QoS split of availability), [[Access Control Models]] (AppArmor, process labeling, the dominance-calculus framing of MAC), [[Operating System Security]], [[Halting Problem]], [[Decidability and Undecidability]], [[Security Design Principles]].

### The cross-course link this opens

Lecture 8's central theorem is **undecidability of safety, proved by reduction from the halting problem** — the exact technique from [[CSCE 411]]'s undecidability unit, applied to a protection system. CSCE 465 and CSCE 411 had never touched before. Back-links were added in both directions, and deliberately **without** adding the Lecture 8 slug to the two CSCE 411 pages' `sources:` — a See Also link is not a content transfer, which is the defect that has recurred across five 465 ingests.

### Figures: checked rather than assumed

Four pages were rendered at 2.2x and read, because the deck's two most important examples are diagrams:

- **Slide 28** — the BLP lattice with six labelled nodes, allow-arrows, and a red X on Bob's blocked read of DocC. Fully recovered; the "can DocC leak to Bob?" answer on [[Bell-LaPadula Model]] is worked from it (**no** — Charlie and Alice can each read DocC but the \*-property blocks both from writing down to DocA, the only object Bob can read).
- **Slide 35** — the same cast re-posed under Biba, captioned `?????`. This is an **unanswered in-class exercise** and is recorded as open rather than answered.
- Slides 24 and 26 recovered (the four-level hierarchy, the lattice examples). The remaining images are decorative photographs.

### Symbol mangling, caught and mapped

The PDF encodes set-theory glyphs in a symbol font, so extraction produced `Î` for an element-of, `Í` for subset, `È` for union, `®` for an arrow, `¹` for not-equal and `o¢` for *o-prime*. Every occurrence was mapped back by hand against the rendered pages. A page that silently kept `Í` would have stated the dominance rule wrongly, which is the one thing this deck cannot afford.

### Deck errata recorded, not propagated

The summary slide spells Biba as **"Bida"**, and slide 26 writes **CRYTPO** for CRYPTO in Alice's label (spelled correctly on slide 28). Both noted on the source page; neither copied into the derived pages.

### An index count that was wrong before this ingest

`index.md` claimed **436 pages** while its own breakdown summed to **415**, and the true figure on disk was **427**. Rather than incrementing the stated number, the count was **recomputed from disk** by reading every page's `type:` field. It now reads 436 (196 concepts, 64 algorithms, 1 data structure, 6 courses, 6 people, 162 sources, 1 overview), which sums correctly and matches `find wiki -name '*.md'`. The stale figure came from the concurrent CSCE 421 ingest logged earlier today.

### Also fixed in passing

The CSCE 465 course page carried **two consecutive paragraphs** both announcing that applied cryptography was complete, left over from successive ingests. Collapsed into one. [[Operating System Security]]'s overview lede was likewise stale — it still said "seven sources ... OS, network, and web security remain outstanding" while Lectures 6a and 7 were already in. Rewritten.

### Gaps after this deck

Unchanged from Lecture 7: **there is no Lecture 6**, and **6a implies a 6b** (likely *authentication and security handshake pitfalls*). The OS/system-security unit is now two decks deep with **software security** still outstanding, as are network and web security. Separately, and newly recorded in the overview: **only HW1 is in the KB, and only as its briefing deck** — the assignment handout itself and HW2-HW4 have never been seen, which matters because the instructor has told students to study the slides *and the homeworks*.

**Result:** all 21 failing checks pass on the first run, across all six bases (CS 436 pages, GEOL 75, STAT 47, MGMT 25, Trading 9, General 5). The audit that followed did find one real defect the linter cannot see — see the audit entry above.

---

## [2026-10-20] ingest | CSCE 421 T08-T10 + HW1/HW2 solution keys - 12 new pages, 8 updated

Ingested the three remaining topic decks and both released homework answer keys, closing the CSCE 421 arc from linear models to transformers. Sources copied to `raw/` with the `CSCE421_` prefix and extracted with PyMuPDF (UTF-8 stdout wrapper required, as always for these decks).

**Sources (5):** `CSCE421_T08-conv.pdf` (13 slides), `CSCE421_T09-CNN.pdf` (**127 slides**, the largest deck in the course), `CSCE421_T10-Attn-Transformer-LLM.pdf` (41), `CSCE421_HW1_Solution.pdf` (4 pages), `CSCE421_HW2_Solution.pdf` (3 pages).

**Pages created (12):** five source pages; concepts [[Convolution]], [[Batch Normalization]], [[Activation Functions]], [[Dropout]], [[Transfer Learning]], [[CNN Architectures]], [[Attention Mechanism]].

**Pages updated (8):** [[Convolutional Neural Networks]], [[Transformers]] and [[Large Language Models]] each extended with a `# The CSCE 421 Treatment` section and promoted to `course: CSCE 420, CSCE 421`, following the [[Backpropagation]] precedent - the existing CSCE 420 survey content was preserved above, not replaced; [[Regularization]] gained a "Beyond Weight Penalties" section tying dropout, batch norm and augmentation into the T04 penalty framing; [[CSCE 421]] course page gained a T08-T10 arc table, a fourth pivot (fixed weights given up at T10), and an **Exams** section; `index.md`; `wiki/overview.md`; this log.

**Homework keys recorded with solutions.** These are instructor-released answer keys, not live assignments, so the standing handwritten-homework rule (which governs *the user's own* submissions) does not apply the way it did for the CSCE 420 HW1 page. Coding answers in the keys are themselves "write your own code" and are summarized rather than reproduced.

**HW2 Q2 verified numerically.** Recomputing the LFD 7.8 backprop example in full floating-point precision gives `delta(3) = -3.6062`, `delta(2) = -1.3503`, `delta(1) = [-0.8571, 1.7012]` against the key's `-3.6`, `-1.368`, `[-0.876, 1.734]`. **The method and every structural step are correct**; the key rounds intermediates to two decimals and propagates them (its `delta(2)` uses `1 - 0.90^2 = 0.19` where exact is `0.1873`). Q3's parameter count of 661 confirmed exactly: `(21x10) + 4x(11x10) + (11x1)`.

**Exam scope captured.** T09 slides **46, 47 and 48 are marked "Optional for CSCE 421"** and contain nothing else - recorded on the source page, the course page and in memory. Separately, Ji said on 2026-10-07 that **batch normalization is a final-exam question and not on the midterm**; T09 pages 62-72 turn out to be where that material lives, so the topic flagged three weeks ago now has a home.

**Extraction notes.** T08 is almost pure figures - kernels survive as loose digit grids and were reassembled into 3x3 form; images do not survive. T09 is CS231n, so the batch-norm equations, dropout figures and all photographs are images; equations on the source page are marked `[figure]` where reconstructed from the cited papers, with verbatim text in quotes. T10 extracts cleanly and needed no reconstruction. Two typos noted in the HW2 key: the third weight matrix is printed `W(1)` where it must be `W(3)`, and "Forward propagation fives" for "gives".

**Textbook change recorded.** T01-T07 follow *Learning From Data*; **T10 is based on Chapter 12 of Bishop & Bishop's *Deep Learning: Foundations and Concepts***. T08 and T09 are adapted from other courses (J. Xiao; Stanford CS231n). Noted on the course page since it affects which book to consult.

**Cross-course duplication avoided.** T09 and T10 overlap CSCE 420's CNN, Transformers and LLM pages. Those keep their survey treatment and gained a derivation section below it rather than a parallel CSCE 421 page, per the standing rule that the two courses approach this material from opposite directions.

## [2026-10-20] ingest | CSCE 420 export re-pull #2 — HW3 + released HW1/HW2 answer keys

Third delivery of `course_files_export`. Hash-diffed all 62 content files against `raw/`: **58 byte-identical, 4 new**. Decks, practice exams, transcripts, videos, SOM notebook and the corrected HW2 sheet all unchanged.

**New files, all archived:** `CSCE420_HW3_Fall2026.pdf`, `CSCE420_HW3_Fall2026_resolution.ipynb`, `CSCE420_HW1_Fall2026_solutions.pdf`, `CSCE420_HW2_Fall2026_solutions.docx`.

**Three pages written.**

- **[[CSCE 420 Homework 3 — FOL, Resolution Prover, Prolog]]** — live assignment, so asks and conventions only, no solutions. Marked **`exam: final`**, not midterm: the midterm stops at unification (Deck 3 slide 99) and every part of HW3 sits past that line, matching Spring 2026 where HW3 was walked through after that semester's midterm. Records the Snoopy/Garfield FOL proof with its fixed predicate set and the two translation patterns the sheet supplies; the two-pointer / level-saturation prover with set-of-support, including the duplicate-clause check that prevents an infinite loop and the Unicorn-theorem test over all three candidate conclusions; and the Prolog royal-family KB with its four domain rules, twelve relation rules and nine queries.
- **[[CSCE 420 Homework 1 Solutions — Fall 2026]]** and **[[CSCE 420 Homework 2 Solutions — Fall 2026]]** — the instructor's **released answer keys**, following the existing *Exam N Solutions* convention for CSCE 411. Both flagged as the instructor's own work rather than derived, because the practice-exam pages in this base carry KB-derived answers and the distinction matters when the two disagree.

**Why ingesting keys is consistent with the standing homework rule.** That rule governs work *I* produce for the student to submit; it does not bar archiving an instructor-released key after the due date, which is study material of the same kind as the CSCE 411 exam-solution pages. The HW1 and HW2 assignment pages lost their "this is a live assignment / no solutions" blockquote accordingly and now link their keys. HW3 keeps it.

**The HW2 key settles the cut-count correction**: it enumerates **five** cuts with the triggering α/β at each, confirming the corrected sheet over the original "4 places". It also supplies the variation for Problem 3 — replacing MIN[3,6,4] with MIN[5,6,4] drops the count to 4, because the node must then see all three children before its value reaches 4, leaving nothing to prune.

Notable content captured for study: HW1's greedy-93-vs-A\*-44 contrast on the same graph (greedy commits to B on h = 10 and never reconsiders; A\* keeps `AD_43` alive and finds `AEG_30` beating `ABG_53` for the same node by a cheaper path), the full h vs h\* admissibility table, and the IDS repeat-count arithmetic 1 + 3 + 7 + 6 = 17. HW2's key shows the composition step propagating `w/A` back through to give `y/g(A)` — the exact trap the sheet warns about — and the not-unifiable case bottoming out at D₃ = {A, B}.

**Audit.** The five CSCE 420 pages touched here pass a scoped check with **0 issues** (frontmatter incl. `exam:`, See Also, wiki-links, index and course-page presence, table shape, escapes, and all 10 `raw/` references resolving). The full-base linter reports 8 failures, **none of them from this work** — they belong to a CSCE 421 / CSCE 465 ingest that is **running concurrently in another session** (`access-control-matrix.md` was written one minute before the audit). Those pages are mid-flight and were deliberately left alone; the stale `**Current count:**` line is theirs to finish. Flagged to the user rather than fixed, to avoid racing a live writer.

## [2026-10-08] lint | Third audit — content checks folded into the linter; two checks tried and deleted

The 20-check suite passed on all six bases on the first run, so this audit did three things instead: made the content checks **permanent**, tested the specific risk the previous ingest created, and deleted two checks that measure nothing.

### The content checks are now in the repo

Audit 2 (2026-09-26) wrote checks 21–28 as a throwaway script in the session scratchpad — which was then wiped, exactly as had already happened to the linter itself three times. Those checks were therefore unavailable this session and would have had to be rewritten from memory again.

`tools/kb_lint.py` now carries them. **Checks 1–20 and 24 fail the run; 21, 22 and 26 print `info` only.**

| # | Check | Status |
|---|---|---|
| 21 | Stale-claim wording ("not yet ingested", "coming soon") | **info** — all three current hits are accurate headings naming a real gap |
| 22 | Concept/algorithm pages over 1200 words | **info** — 9 pages; the length judgment was settled in audits 1 and 2 |
| 24 | **Course-specific frontmatter invariants** | **failing check** — declared in an `INVARIANTS` table; CSCE 420 requires `exam:` on every source page |
| 26 | raw/ files with no plausible source page | **info** — 3 hits, all tokenization artifacts verified in audit 2 |

Check 24 is the valuable addition. The CSCE 420 exam-scope requirement is a *standing user requirement*, not a schema rule, and audit 2 found 11 source pages violating it. It is now enforced automatically and declared in one table, so other course-specific invariants can be added the same way.

### Two checks tried and deleted rather than kept

This is the fourth audit in a row where newly-invented checks produced mostly false positives. Two were bad enough to delete outright, with a note in the linter header telling a future run not to re-add them:

**"Page older than a source it cites" — 85 hits, 85 false positives.** The idea was that a page dated before a source it cites may predate the content. Verified against the clearest case: the `DES` page is dated 09-13 and cites the Lecture 3a source page dated 09-22 — but 3a's date moved only because it **gained four back-links** in later sessions, not because its content changed. Source pages get edited for cross-linking long after their content was transferred, so the comparison measures edit recency, not staleness. Deleted.

**"One-way See Also links" — 408 of them across 412 pages.** That is the normal hub→leaf shape of a wiki, not drift. A number nobody can act on is not information. Deleted.

The surviving pattern is worth stating plainly: a check earns a place in the suite only if its output is **both small and actionable**. Three of the four new checks this round are `info` precisely because they fail that test but are still worth eyeballing.

### The real question this audit set out to answer

The previous ingest put CSCE 465 OS-security pages next to CSCE 313 systems pages covering the same mechanisms, and claimed to have avoided duplication. **Tested rather than assumed**, with an 8-gram shingle comparison across all four new 465 pages against all seven 313 pages:

**One shared 8-gram, nine words long** — *"a privilege escalation path if it has a bug"*, appearing in both `unix-file-permissions.md` and the "Security View" section I added to `process-attributes.md` in the same session. That is a deliberate cross-reference echo, not duplicated content. The separation held.

**No contradictions either.** A fact-agreement sweep over all 63 CSCE 465 pages checked 20 facts that appear on multiple pages — DES's 56-bit key (10 pages), SHA-1's 160-bit digest and 2⁶⁹/2⁸⁰ figures (5 and 4 pages), the 2⁵⁷ meet-in-the-middle cost, AES's 2⁷² factor, the password study's 10¹⁸ and 86%, the cold-boot −50 °C and 0.2% figures, Halderman 2008. **Every repeated fact is stated identically everywhere it appears.** Nine lectures deep, the unit is internally consistent.

### One real defect found and fixed

**An unmarked synthesis blockquote.** `access-control-models.md` presented the *"Linux pays at check time, Windows pays at set time"* analysis in a blockquote with no provenance marker, where every other derivation in the CSCE 465 pages carries one ("Derived", "Worked through", "Why the odd case is odd"). The lecture gives the comparison **table**; it does not draw that conclusion — so the blockquote read as if it might be the instructor's. Marked as derived.

That convention exists for a specific reason, established back in the CSCE 420 practice-exam ingest: the KB must never let my inference be mistaken for the instructor's. Auditing it is worth doing because a missing label is invisible to every structural check — it is well-formed markdown making an unsupported attribution.

Spot-checked the other eight pages from that ingest: `password-authentication.md` (the per-attack salt analysis), `operating-system-security.md` (the TCB reasoning), `ntfs-permissions.md` (move-vs-copy), and the rest all carry markers. An earlier, cruder version of this check flagged 53 "unlabelled" blockquotes — nearly all of which are **lecture quotations**, which correctly have no derived label. The check cannot be automated reliably for that reason and stayed manual.

### Also verified

- **The two numbering gaps are recorded in all four places** they should be: the course page, the overview's gaps section, the Lecture 6a source page, and the CSCE 465 project memory. Each states both that there is no Lecture 6 and that "6a" implies a 6b, with the course-outline hypothesis attached.
- **The CSCE 411 and 313 "not yet ingested" lists are accurate** — re-verified against the source pages actually present (411: missing 1, 3, 12, 13, 14, 17, 21, 30; present 2, 4–11, 15, 16, 18–20, 22–29, 31).

### A bug I introduced in the linter and caught

Adding check 26 broke **GEOL 101**, which has no `raw/` directory: my earlier rewrite of check 19 left `raws` unassigned on that branch, so 26 raised `NameError`. It surfaced as a bare exit-1 with all checks printing `ok` — which is the worst failure shape, because the output looks clean. Fixed by initializing `raws = None` before the branch, with a comment saying check 26 reads it.

**Result:** all six bases pass. CS 412 pages, GEOL 75, STAT 47, MGMT 25, Trading 9, General 5. Linter at 21 failing checks plus 3 info lines, in the repo.

---

## [2026-10-08] ingest | CSCE 465 — Lecture 6a User Authentication + Lecture 7 OS Security (2 files)

Two decks, both opening **new units beyond cryptography**. Hash-checked first: neither is a duplicate.

**Sources ingested:**
- `06a_AuthenticationUser.2026.pdf` → `raw/CSCE465_06a_AuthenticationUser.pdf` — 23 PDF pages, two-up ≈ **46 slides**
- `07_OS-Security-1.pdf` → `raw/CSCE465_07_OS_Security.pdf` — 21 PDF pages, two-up ≈ **42 slides**

**Pages created (11):**
- Lecture 6a — concepts: User Authentication, Password Authentication, Biometrics, Authentication Tokens; algorithm: S/Key Protocol; plus source
- Lecture 7 — concepts: Operating System Security, Access Control Models, Unix File Permissions, NTFS Permissions; plus source

**Pages updated (13):** `security-services.md` (twice — authentication *and* access control now have implementations), `hash-functions.md`, `hash-function-applications.md`, `public-key-cryptography.md`, `diffie-hellman-key-exchange.md`, `classical-ciphers.md`, `security-design-principles.md`, `side-channel-attacks.md`, `guofei-gu.md`, `csce-465.md`, plus `overview.md` and `index.md` — **and three CSCE 313 pages**: `operating-systems.md`, `file-systems.md`, `process-attributes.md`.

**The CSCE 313 overlap was the main design decision.** Lecture 7 covers OS concepts, boot, and filesystems — all of which CSCE 313 already has from the systems side. The derived pages deliberately **do not restate the mechanics**; they cover the security surface and link across, and the three CSCE 313 pages got a short "The Security View" section pointing the other way. The alternative — duplicating inodes, hard links, and UID/EUID into CSCE 465 pages — would have created exactly the parallel-page problem the CSCE 420 ingest had to avoid in September.

### Lecture 6a — what is worth keeping

**Identification is a search; authentication is a comparison.** Identification checks against *all* known entities and must be unique; authentication checks against *one previously identified* entity and need not be. The 1-to-N versus 1-to-1 difference is why a biometric adequate to *authenticate* can be useless to *identify* — a false-positive rate that is fine once becomes a certainty across a million comparisons.

**Salt only defeats one of the three dictionary attacks**, and the lecture leaves the answers as diagrams. Derived per attack: online guessing is **unaffected** (the system applies the salt itself); the per-file offline attack costs **the same against one chosen target**; **precomputation is what salt destroys**, because a table built for one function would need to be 2ⁿ times larger. The lecture's own phrasing is honest — *"a bit more difficult."* Worth holding against the common belief that salt makes passwords strong.

**Passwords are exact; biometrics are statistical.** That single difference is the root of every biometric weakness — it is why biometric matching has error *rates* at all, and it propagates into the accuracy, cost, and multifactor problems. Biometrics are also **not revocable**, which a password is.

**The multifactor formulas are a caution, not a recommendation.** With `TP = TP1·TP2` and `FP = 1-(1-FP1)(1-FP2)`, worked through at TP=0.95/FP=0.01 each: TP falls to 0.9025 **and** FP rises to 0.0199 — *both* rates get worse. Combining helps only if combined the other way around (AND on the false positives), and either way one rate improves while the other degrades. Recorded with the arithmetic because the slide states the formulas without drawing the conclusion.

**S/Key walks the hash chain forwards to build and backwards to spend**, and it **does not authenticate the server**. The relay attack is [[Diffie-Hellman Key Exchange|DH man-in-the-middle]] exactly: the fake server gets Alice to compute the one value it cannot. Both protocols are one-way, and both fail the same way — cross-linked in both directions.

**Passive tokens can be cloned by reading them; active ones cannot.** The processor is the whole security difference, and it explains why the cheap tokens on the lecture's own example list (magnetic strips, USB sticks) are the weak ones.

### Lecture 7 — what is worth keeping

**The boot chain is the attack surface.** Every OS protection mechanism is code that runs *once the OS is running*, so anything earlier in the chain sits outside all of it. BIOS passwords, trusted boot, and the TCB each defend one link — and the TCB must be *small* for the economy-of-mechanism reason: it is the part nothing else can check.

**The cold boot attack is the sharpest item in either deck.** Cooling DRAM to −50 °C leaves **< 0.2% decay after one minute**, long enough to reboot into a minimal loader and read the key out of RAM. Demonstrated against **dm-crypt, LoopAES, BitLocker, FileVault, and TrueCrypt** (Halderman et al., USENIX Security 2008): five full-disk encryption systems, **no cipher broken**. Filed as a physical [[Side-Channel Attacks|side channel]] — the abstract model says memory clears at power-off and the device disagrees for a few seconds.

**Linux pays at check time; Windows pays at set time.** Linux walks every path component and requires execute on each, so the effective permission is a property of the *route* — which is why *different paths to the same file are not equivalent* even though the file's ACL is identical. Windows materializes inheritance at assignment, so a check reads one ACL and stops, at the cost of tracking which ACEs were inherited. Neither is more secure; they fail differently (a permissive directory on the path vs a stale inherited ACE).

**Directory permission bits mean different things**, and the consequence students miss: **write on a directory lets you delete a file you cannot write**, because deletion is a directory operation. That is precisely what the sticky bit repairs, and why `/tmp` is `1777`.

**The file-sharing challenge fails twice for the same reason.** Random hard links fail because a hard link can be copied; random symlinks fail because a symlink tells you where it points. Both attempts use *obscurity of the name* as access control, which is the [[Security Design Principles|open design]] failure — and the real lesson is that the user/group/other model is too coarse, which is the argument for POSIX ACLs.

**"Deny always wins" is wrong on NTFS.** The rules are ordered: accumulate all applicable permissions, **explicit beats inherited**, then **deny beats allow**. So an explicit Allow defeats an inherited Deny. And **move within a volume keeps the source's permissions** (a move is a rename, so the ACL never moves) — meaning a file dragged into a protected folder on the same volume sits there unprotected.

### Cross-unit synthesis recorded

Both units *reuse* the crypto unit rather than leaving it, and the overview now says so: password storage and S/Key are [[Hash Functions|one-wayness]] in use; crypto-based authentication is the challenge-response pattern already seen twice; the eToken holds an X.509 private key and is therefore a [[Public Key Infrastructure|PKI]] endpoint. [[Security Design Principles]] gains four concrete instances from Lecture 7 (fail-safe defaults as the closed policy, least privilege suspended by setuid and restored by `sudo`, economy of mechanism as why a TCB is small, compromise recording as event logging with Lecture 2's audit-trail caveat).

And the course's central claim now has an instance in **every** unit: the cold boot attack reads keys out of RAM with no cipher broken, and the attacks that beat strong passwords — keylogging, fake login prompts, phishing — are not cryptographic at all.

### Two new numbering gaps, recorded with a hypothesis

Decks now run 1, 2, 3, 3a, 3b, 4, 5, **6a**, 7. **There is no Lecture 6**, and the **6a** label implies a **6b**. Per the course outline the authentication unit also covers *"authentication and security handshake pitfalls"*, which is the likely content of 6b. Recorded the same way the Lecture 4 gap was — with the hypothesis attached, since that approach proved itself when Lecture 4 arrived and matched the prediction exactly.

### Extraction

PyMuPDF both. Superscripts flattened as usual and corrected on the derived pages. **Three genuine visual gaps:**
- Lecture 6a slide 39, *"The Scorecard From One Study"* — biometric technology comparison, image-only. **Ratings not recoverable.**
- Lecture 7 slide 37, *"Basic NTFS Permissions"* — **28 images, 272 characters.** The per-permission detail is **not recoverable**.
- Lecture 7's measured/trusted-boot figure carries only the TCB definition in text; the stages and measurement flow are not recoverable, so that section's mechanics were derived and marked as such.

Lecture 6a's dictionary-attack and salt slides are diagram-driven — the attack mechanics survive in the bullets, but the per-attack salt answers are conveyed *by the diagrams alone* and were derived. Lecture 7's internal slide numbering jumps **40 → 42**; whether a slide was removed is not determinable.

### Defect I keep making

Two spurious-looking citations (`diffie-hellman-key-exchange.md` and `classical-ciphers.md` ← L6a) were flagged by check 17. On examination **both were genuine** this time — Classical Ciphers quotes L6a's 10¹⁸ and 86% figures, and the DH note is about L6a's S/Key relay attack — so the fix was back-links on the source page rather than removing slugs. That is the **fifth** consecutive CSCE 465 ingest where check 17 fired on my work; the difference is that this time the citations were right and the *source page* was incomplete. Worth distinguishing the two failure modes rather than assuming the slug is always the error.

Also: I wrote a prose anchor using escaped `\|` inside a wiki-link alias. **Escaping is correct in table cells and wrong in prose** — the assertion caught it, but it is the same confusion from the other direction.

**Result:** 401 → 412 pages. All 20 checks pass.

---

## [2026-10-07] query | CSCE 421 interactive study from the beginning

User wants to learn the ingested slides at their full depth through interaction and explicitly says they know nothing and want to start from the top. Begin with T01 slides 3–7: explicit arithmetic rules versus recognizing a tree, labeled examples, adjustable parameters, and predictions on new inputs. A small interactive multiplier exercise was prepared in the chat; its numeric examples are invented teaching examples, not slide data. No understanding or mastery has yet been assessed.

**Tutoring approach:** one small explanation, a worked example, a learner attempt, targeted feedback, then independent explanation and later retrieval. Introduce mathematical prerequisites when needed. Preserve the course progression and full derivations: T01 linear models and normal equations; T02 likelihood, logistic loss, gradient descent and SGD; T03 softmax invariance, binary equivalence and Jacobian/CE derivation; T04 generalization, regularization and validation; T05 six losses and convexity; T06 forward/backpropagation with dimensions and bias handling; T07 numerical computational graphs. Research consulted: Karpicke & Blunt (2011), Atkinson/Renkl/Merrill (2003), Cepeda et al. (2008), Rohrer et al. (2020). Applying those findings to CSCE 421 is instructional synthesis, not a tested course-specific intervention.

**Original PDFs are available in raw/** and were checked alongside [[CSCE 421]] and its nine source pages. Important details to preserve beyond the wiki summaries:
- T01 slide 7 visually distinguishes labeled training data from test inputs. Opening slides 3–7 were inspected visually.
- T02 pages 4–6 cover image pixels as vectors, translation and invariant representations; page 14 illustrates log/exp, and page 22 convexity via chords.
- T03 has 21 PDF pages but 20 slide numbers; physical pages 3–4 are a reveal build of printed slide 3. Later PDF pages run one ahead of footers. Companion notes page 5 contains the full softmax and cross-entropy derivatives.
- T04 slide 9 uses **ln lambda**, so 0 means lambda = 1, not no regularization. The displayed norm penalty includes the bias coefficient.
- T05 square loss increases again beyond margin 1. Strict convexity in scalar margin does not by itself establish strict convexity in weights. The zero-margin zero-one-loss convention is inconsistent between the displayed formula and prose; specify the convention if testing that boundary.
- T06 image-only slides 21–23 contain the full sensitivity recurrence, squared-error factor 2, removal of bias coordinates in hidden sensitivities, and averaged outer-product gradients. The Boolean examples on slide 5 require ±1 inputs.
- T07 page 9 additionally works through f = 2[xy + max(z,w)] at x=3, y=-4, z=2, w=-1: output −20 and gradients (−8,6,2,0). Include this after the (x+y)z example.

Source PDFs were not modified. Course coverage and the user's performance should remain separate: preparing or displaying an exercise does not establish learning.

---

## [2026-10-01] ingest | CSCE 465 — Lecture 4 Hash Functions (1 file) — the Lecture 4 gap is closed

**Source ingested** (copied to `raw/` as `CSCE465_04_Hash.pdf`): `04_Hash-1.pdf` — 24 PDF pages, two-up ≈ **47 logical slides**. Hash-checked first: not a duplicate of anything in `raw/`.

**This closes the numbering gap the KB has carried since 2026-09-26.** The decks ran 1, 2, 3, 3a, 3b, **5**; the overview predicted from the course outline that the missing Lecture 4 would be hashes and message digests. It is, exactly. **Applied cryptography in CSCE 465 is now completely ingested** — secret key, hashes, public key — and no numbering gaps remain. The prediction is worth noting as a case where recording a gap *with a hypothesis* paid off: the hypothesis was testable and turned out right.

**Pages created (7):**
- Concepts (3): Hash Functions, Birthday Attack, Hash Function Applications
- Algorithms (3): MD5, SHA-1, HMAC
- Sources (1): CSCE 465 Lecture 4 — Hash Functions

**Pages updated (8):** `cryptography-taxonomy.md`, `message-authentication-code.md`, `digital-signatures.md`, `public-key-infrastructure.md`, `triple-des.md`, `guofei-gu.md`, `csce-465.md`, plus `overview.md` and `index.md`.

**All of the deck's math verified and correct.** The birthday paradox threshold (P(22) = 0.4757, P(23) = 0.5073 — 23 is exact), the generalization constant (√(2 ln 2) = 1.1774, and 1.18·√365 = 22.54), and the MD5 T-table formula: `T[1] = 0xD76AA478`, `T[2] = 0xE8C7B756`, `T[64] = 0xEB86D391`, which **match the published MD5 constants**, so `⌊2³²·|sin i|⌋` on the slide is the real thing rather than an approximation. The 2^(m/2) bound also reconciles the deck's own figures: 2⁶⁴ for MD5 and 2⁸⁰ for SHA-1 are *birthday bounds* for 128- and 160-bit digests, not exhaustive searches.

**The distinction worth carrying out of this lecture.** Weak and strong collision resistance differ in **who picks the messages** — weak hands you an `m` and asks for a colliding `m'`; strong lets the attacker pick both. Strong is the binding constraint because picking both is precisely what the [[Birthday Attack]] exploits, and it follows that **a hash's collision resistance is half its output length while its preimage resistance is the full length**. That asymmetry is the whole answer to the lecture's opening question of why digests are 128 or 160 bits when cipher keys of comparable strength are shorter.

**The applications section is better than it looks.** Only file authentication uses a bare hash. Five of six add a secret key, a nonce, or both, and the pattern generalizes cleanly: a hash alone proves *nothing changed*; a hash plus a key proves *who*; a hash plus a nonce proves *not a recording*. The commitment protocol is the nicest case — one-wayness makes it *hiding* and collision resistance makes it *binding*, which are exactly the two properties any commitment scheme needs, and the lecture's two failure cases (small X, predictable X) are both about entropy in X rather than about the hash.

**The extension attack deserved its own treatment.** A Merkle–Damgård digest *is* a resumable intermediate state: nothing about the message survives between blocks except the running digest, so holding `H(K|M1|pad)` lets you compute `H(K|M1|pad|M2|newpad)` **without knowing K**. That makes the naive `H(M|K|R)` construction from this deck's own message-authentication application forgeable, which is why [[HMAC]] exists. Noted that HMAC's two pad constants (0x36, 0x5c) differ in half their bits on purpose — they derive two distinct keys from one, the same never-reuse-a-key discipline as the P+I construction from Lecture 3b.

**Three cross-unit connections now recorded in both directions:**

| Connection | Where |
|---|---|
| A hash collision **is** a signature forgery, since signatures cover `H(m)` not `m` — MD5's colliding X.509 certificates broke PKI at the hash layer with the CA behaving perfectly | [[Digital Signatures]], [[Public Key Infrastructure]] |
| Two MAC constructions on different primitives — CBC residue (block cipher) and HMAC (hash) — neither giving non-repudiation | [[Message Authentication Code]] |
| **Meet-in-the-middle appears a third time**, now as a reason not to build a hash from a block cipher | [[Triple DES]] |

The MD5/PKI link is the sharper one: it is the same *shape* as the Comodo breach from Lecture 5 — a valid signature over a statement nobody intended — reached through a broken hash instead of a broken process.

**Twelve unanswered questions**, second-most of any deck in this course, all answered as derived. The "why not just store a duplicate copy of F" one is the most instructive: the real answer is not space but that *the thing you must protect is smaller*, and small secrets are cheap to make tamper-proof.

**Extraction.** PyMuPDF, no image-only slides. Superscripts flattened throughout as in every deck of this unit (`2^(m/2)` → `2m/2`, `2^32` → `232`, `⌊x⌋` → `ëxû`); logical operators survived as `Ù Ú Å ~`. All formulas rebuilt with explicit operators and verified numerically against the deck's own answers. Structural diagrams (MD5 high-level view, per-step logic, HMAC flow, the C+H/OFB figure) extract as label clouds and were reconstructed from labels plus prose. **One ambiguity recorded rather than resolved:** the properties slide annotates both collision-resistance entries with a parenthetical **"(free)"** whose meaning did not survive extraction. Third deck in a row with **"CSC/ECE 574, Dr. Peng Ning"** watermarked slides.

**Two defects I introduced and caught before finishing.** Absolute-value bars in a table cell (`|sin i|`) split the row — fixed by writing `abs(sin i)`, which is pipe-free *and* closer to the slide's own `abs(sin(i))`. And a **spurious source citation**: I added the L4 slug to `cryptography.md`'s `sources:` without adding any L4 content. That is the **third time** I have made that exact mistake on a CSCE 465 ingest (Lectures 3, 3a, 5 before it). Check 17 caught it each time; the rule is that `sources:` means *content came from here*, and adding a cross-link is not adding content.

**Result:** 391 → 401 pages (7 from this ingest, 3 from concurrent work in another session). All 20 checks pass.

---

## [2026-09-30] ingest | CSCE 420 course export re-pull — HW2 correction + 3 missed lecture pages

The user supplied `course_files_export (2).zip` saying "a couple things were updated." Hash-diffed all 58 content files against `raw/`: **56 byte-identical**, 2 changed. The eight slide decks, both practice exams, HW1, the SOM notebook, all 38 transcripts, and all three videos are unchanged — no re-ingest needed. Canvas template assets and `course_images/` skipped as before.

**1. HW2 was revised.** Two substantive changes, only one of which the Canvas announcement flagged:
- Problem 2's hint went from **4 places that need to be cut** to **5** — the change the announcement circled in red. The HW2 page already carried this from the 09-17 announcement, but the **archived PDF was still the pre-correction version**; replaced, and the annotated screenshot archived as `raw/CSCE420_HW2_Fall2026_correction.png`.
- Problem 2 gained a note the announcement did **not** mention: *"When there is a cut, the final αβ values may or may not be updated. Either way does not affect the final outcome."* Added to the page — it changes how part (b) is graded.
- Problem 8 now carries the show-every-step-and-name-the-law requirement explicitly (it previously appeared only in the propositional section). Noted on the page.
- The rest of the diff is cosmetic: duplicate LaTeX section numbers (`1.1`, `2.1`, `3.1` repeated) fixed to `1.2`, `2.2`, `2.3`, `3.2`, and a page-break shift.

**2. A gap in my own earlier ingest, found while diffing.** The transcript folder holds **38** files but only **35** lecture pages existed — the first three Spring 2026 lectures (**01-12, 01-14, 01-16**) were archived on 09-17 but never written up. The 09-17 work started at 01-21 and the count was never checked against the folder. Neither the structural audit nor the linter catches this: both verify that every *page* is well-formed and indexed, not that every *archived source* produced a page. Written now, all deck slide01 (plus the slide02 peek on 01-16), all `exam: midterm`:
- **01-12** — syllabus and grading (25/30/4×10/5, no curving, 1 pt/hour late, one handwritten sheet), the textbook-cover walkthrough, R&N's four definitions of intelligence with his pet-rock and Terence-Tao-vs-Wolfram-Alpha objections, strong vs. weak AI, the flight analogy, and philosophy/mathematics/psychology.
- **01-14** — linguistics, cognitive science, neuroscience (his own Golgi-stained mouse atlas, Hubel & Wiesel, fMRI, his personal TMS session), then the full AI history, and the Breakout DQN demo. **Carries the exam-scope quote**: the discipline material is *"just for fun — except for core concepts like strong AI, weak AI,"* and slide01 contributes *"typically just one question."*
- **01-16** — generative-AI preview, milestone timeline, the philosopherai GPT-3 sessions, the three-era table, the train/taxi/John resolution preview, the CNN scaling story (AlexNet → VGG → Inception), task escalation to VQA, limitations (adversarial stop signs, husky-in-the-snow spurious features), the future, HW1, and the slide02 peek.

Back-linked from the 01-21 page, which previously had no predecessor. **Index** 391 → 394. Audits re-run clean.

## [2026-09-27] query | CSCE 465 HW2 lecture access verification

- Request: Use the knowledge base and confirm access to lectures described as "a 2 3a 3b and 5" for help with the supplied HW2-2.pdf. The first identifier is ambiguous; clarification was requested, and Lecture 1 was also checked.
- Verified that the source notes and original PDFs for CSCE 465 lectures 1, 2, 3, 3a, 3b, and 5 are present and readable. All six PDFs parsed successfully; their page counts are 20, 25, 15, 32, 19, and 30 respectively.
- Read the supplied seven-page Homework 2, "Protect Agent Messages with Classic Cryptography," at `C:/Users/jayra/OneDrive/Documents/CSCE 465 Computer and Network Security/HW2/HW2-2.pdf`; visually checked its task descriptions and rubric. Lecture 3a supplies symmetric-cipher background, 3b covers CTR/modes/IVs/MACs, and 5 covers RSA/signatures/Diffie-Hellman. Lectures 1 and 2 supply security foundations.
- This was an access and reference check; no homework implementation or submission was requested or performed.

## [2026-09-26] lint | Second full audit — all six bases now pass; 8 checks added to the linter

The CS base passed all 20 automated checks on the first run, so this audit's value was in **what the linter does not cover**. A second-pass script (checks 21–28) looked for stale claims, overlapping pages, course-specific invariants, tag hygiene, page-size drift, and raw-file coverage. Findings, fixes, and — as importantly — the findings that turned out to be my own checks misfiring.

### Real defects found and fixed (CS base)

**1. The overview understated CSCE 465 by two sources.** It read *"Five sources are ingested … and two cryptography lectures"* when seven are ingested and four are cryptography lectures (3, 3a, 3b, 5). I wrote that sentence during the 3b ingest and updated it for 3b but not for 5. Corrected. Note the *gaps* section of the same page was accurate — the lede and the gaps drifted apart, which is the same split that produced the stale CSCE 420 gaps block caught in the 09-13 audit.

**2. The CSCE 411 gap list omitted Lecture 1.** It listed lectures 3, 12, 13, 14, 17, 21, 30 as not ingested; Lecture 1 is not in the KB either. Verified against the actual lecture-NN source pages present (2, 4–11, 15, 16, 18–20, 22–29, 31) and corrected. The CSCE 313 list ("3, 4, 13, 17, and others") is accurate as written.

**3. Eleven CSCE 420 source pages were missing `exam:` frontmatter** — and this is the one finding that would actually have hurt. Exam-scope separation is a standing user requirement (*"I don't want to ask about the midterm and have you pull from the final review"*). The 35 Spring session pages all carry `exam:`, but the **eight slide decks plus both practice exams plus the SOM notebook did not** — and the decks are the pages most likely to be cited when answering a concept question. Scope was not guessed: it is stated on the course page's own table, so the values follow directly.

| Page | `exam:` |
|---|---|
| Deck 1 Introduction | `midterm` (one question) |
| Deck 2 Search and Game Playing | `midterm` |
| Deck 3 Logic | `midterm / final` — midterm through unification (slide 99), rest is final |
| Decks 4–7 Planning, Probabilistic, ML, Deep Learning | `final` |
| Deck 8 AI Ethics | `excluded` |
| SOM Notebook | `excluded` |
| Midterm Practice / Final Practice | `midterm` / `final` |

Deck 3, Deck 8, the SOM notebook and Deck 1 also got a short **Exam scope** blockquote in the body explaining the value, since those four are the non-obvious ones.

**4. `Machine Learning` and `Machine Learning Paradigms` linked in one direction only.** Checked for genuine overlap and there is none — ML is Deck 6's framing (generalization, the data deluge), Paradigms is the supervised/unsupervised/RL split and is dual-course with CSCE 421. Distinct pages; added the missing back-link rather than merging.

### Real defects found and fixed (other five bases)

The other bases had never been audited beyond a broken-link sweep.

**STAT 212 — two broken table rows, and they were the important rows.** `sign-test.md` and `signed-rank-test.md` each had absolute-value bars inside a table cell (`|Y-n/2|`, `|Z|`), splitting the row. In both cases the broken row was the **two-sided alternative** — the row a student is most likely to need. Escaping as `\|` would render as a double bar and corrupt the notation, so the fix was `\lvert … \rvert`, the same reasoning that produced `\mid` for the conditional-probability pipe in the CS base on 09-13.

**STAT 212 — course page was not a hub.** Seven note-set source pages were unreachable from the course page, and six of their slugs were missing from its frontmatter. Added an Ingested Sources section and repaired the frontmatter.

**GEOL 101 — three missing back-links** (Hot Spots and Mantle Plumes ← Module 5; Sedimentary Rocks ← Module 1; Volcanoes ← Module 2), **two lab pages unreachable** from the course page, a **missing See Also** on its overview, and **two lab slugs** missing from course frontmatter. All fixed.

**Trading and General — the Overview page was an orphan** in both: nothing linked to it and neither index listed it. One index line each.

### Findings deliberately not acted on

- **87 pages whose tags omit a course slug.** Checked the conventions: CSCE 420's memory states pages are tagged `csce420`, and **0 CSCE 420 pages violate that**. The 87 are CSCE 411/313/finance pages where no such convention was ever stated, so my check had invented a rule. Not a defect; no churn.
- **103 pages over the ~700-word guideline** (up from 45 at the last audit, tracking the KB's growth from 323 to 391 pages). The overview is 4,875 words and exempt by nature. Six stubs under 120 words are all legitimately short (three person pages, two practice pages, one notes page). Unchanged from the 09-13 judgment: splitting single coherent references would fragment lookups.
- **13 of 45 CSCE 465 pages carry a marked "derived" blockquote.** That is the right proportion — not every page has an unanswered question to answer.

### Checks that were wrong, and what that cost

Five of the eight new checks produced mostly or entirely false positives, and the linter itself crashed on one base. Recording this because the pattern is now consistent enough to be a rule:

| Check | Why it misfired |
|---|---|
| 22 near-duplicate titles | 328 "hits", nearly all sequentially-numbered pages (Homework 2 vs Homework 3). Re-run restricted to concepts/algorithms gave 23, of which 22 were genuinely distinct (Best-First vs Breadth-First Search). **One** real finding. |
| 24 course tags | Invented a convention that only CSCE 420 actually has |
| 25 exam: frontmatter | Counted all 147 CSCE 420 pages; the requirement is only on *lecture* pages. Real count was 11, not 104 |
| 28 raw coverage | Grepped for bare filenames; most source pages don't cite their raw path. Re-run by token overlap gave 3, all tokenization artifacts (`Lecture25` vs `lecture-25`, `Perpituity` vs `perpetuity`). **Zero** real findings |
| 11, 12, 19 (in `kb_lint.py`) | Assumed every base has a page-count line, a `courses/` directory, and a `raw/` directory. GEOL 101 has none of the first and third; Trading and General have no `courses/`. Check 19 **crashed** rather than failing cleanly |

**The lesson, repeated from the last two audits: eyeball a new check's first output before believing it.** Every one of these was caught because the count was implausible, not because the check reported cleanly.

### Linter hardened

`tools/kb_lint.py` now:
- **skips** checks 11, 12 and 19 on bases that lack a count line, a `courses/` directory, or a `raw/` directory, printing `skip` rather than `FAIL` or crashing
- treats root-level `index.md` / `log.md` / `CLAUDE.md` as valid `[[wiki-link]]` targets, which removes the `[[index]]` false positive in Trading and General
- documents all seven false-positive classes in its header comment

**Result: all six knowledge bases pass all 20 checks.** CS 391 pages, GEOL 75, STAT 47, MGMT 25, Trading 9, General 5.

---

## [2026-09-26] ingest | CSCE 465 — Lecture 5 Public Key Cryptography (1 file; 1 duplicate skipped)

**Sources offered:** `05_PublicKeyCrypto-1.pdf` and `03b_SecretKeyMode_s-1 (1).pdf`.

**The 3b file was not re-ingested** — it is byte-identical to `raw/CSCE465_03b_SecretKeyModes.pdf` (MD5 `3feb8f59eae4ca90cbfa0513aefc9061` on both), a duplicate download of the deck ingested on 2026-09-22. Checked by hash before reading anything; worth doing routinely now that downloads accumulate `(1)` suffixes.

**Ingested** (copied to `raw/` as `CSCE465_05_PublicKeyCrypto.pdf`): 30 PDF pages, two-up ≈ **59 logical slides**.

**Pages created (6):**
- Concepts (3): Public Key Cryptography, Digital Signatures, Public Key Infrastructure
- Algorithms (2): RSA, Diffie-Hellman Key Exchange
- Sources (1): CSCE 465 Lecture 5 — Public Key Cryptography

**Pages updated (8):** `cryptography-taxonomy.md`, `secret-key-cryptography.md`, `security-services.md`, `side-channel-attacks.md`, `message-authentication-code.md`, `cipher-security-models.md`, `guofei-gu.md`, `csce-465.md`, plus `overview.md` and `index.md`.

**Every numeric example in the deck was recomputed and all of them are correct.** RSA (`p=23, q=11`: `d=79`, encrypt→37, decrypt→80, sign→224, verify→80), the RSA key negotiation (Bob's `589 = 19·31`, `23·47 ≡ 1 mod 540`, all four exchange values), Diffie-Hellman (`p=353, g=3` → `T_A=40`, `T_B=248`, `K=160` both ways), and DH encryption (`<401,5,51>`, `S_B=58`, `S_A=17` → 173, 360, 360, and `T_B` really is `5^58 mod 401`). Recorded as verified on the source page, so the student can trust the worked examples when revising.

**One internal mismatch found by doing that checking.** The DH example's `p = 353` satisfies the deck's own later rule `g^((p-1)/2) ≡ -1 mod p` (`3^176 mod 353 = 352`) but **violates** the companion rule that `(p-1)/2` be prime — `176 = 2⁴ × 11`. Not an error so much as a toy example chosen for slide-sized arithmetic, but recorded on [[Diffie-Hellman Key Exchange]] so it does not read as one. The "obscure mathematical reasons" the lecture waves at are safe primes and small-subgroup attacks; that is noted too.

**A derived claim got confirmed by the instructor.** The KB has asserted since the Lecture 3a ingest that symmetric authentication convinces only the other key holder and therefore cannot deliver non-repudiation — derived, marked as derived, on [[Secret Key Cryptography]] and [[Security Services]]. Lecture 5 states it outright: *non-repudiation is only achievable with public key cryptography.* The derivation stands, and the pages now say the lecture confirms it rather than that the KB inferred it.

**The organizing idea, and the one students reverse.** Signing and encrypting use **opposite** keys — sign with your own private key, encrypt with the recipient's public key — and in RSA they are the *same exponentiation*, so nothing in the arithmetic distinguishes them. [[Digital Signatures]] leads with that table for exactly that reason.

**Eleven unanswered questions**, the most in any CSCE 465 deck so far, all answered as derived. The two most worth having: the `(why?)` on RSA's correctness proof is Euler's theorem applied to `ed = 1 + kφ(n)`, and the two `?` marks on timing-attack countermeasures are that a fixed delay makes every operation pay worst-case latency while a random delay only adds noise that averaging defeats — which is why blinding, the one that removes the *correlation*, is also the only one with a real cost figure attached (<10%).

**A second real-world post-mortem, and a better one.** [[Content Scrambling System|CSS]] failed with weak cryptography *and* bad key management. **Comodo failed with intact cryptography** — the HSMs held, the root keys never leaked, and nine fraudulent certificates for Google, Yahoo, Skype, Live and Mozilla were issued anyway. The two now bracket "cryptography is rarely the weakest link" from both ends, and the overview says so.

**Numbering gap recorded.** The decks run 1, 2, 3, 3a, 3b, **5**. There is no Lecture 4 in the KB, and per the course outline the gap is *hashes and message digests* — which is exactly the one applied-cryptography topic still missing. Flagged on the course page, the source page, and in the overview's gaps, phrased as "unknown whether it exists or the numbering skips" rather than assumed.

---

### Lint debt from the previous session, cleared

The 2026-09-22 session ended mid-triage with four failing checks. All are now resolved:

- **4 malformed table rows** — unescaped alias pipes inside table cells. Two mine (`secret-key-cryptography.md`), two inherited from the CSCE 420 HW2 page. Same class as every ingest since 2026-08-27; escaped.
- **2 spurious source citations removed** — `security-services.md` ← Lecture 3b and `autoencoders.md` ← CSCE 420 Lecture 6. In both cases a See Also link had been added without any content from that source. Confirmed by grepping the source page for the topic: zero hits for "autoencoder" in the Lecture 6 page. `sources:` means *content came from here*; a cross-link is not content. (This is the second time I have made this mistake on a CSCE 465 ingest, and check 17 now catches it automatically.)
- **2 genuine back-links added** — `Cryptography Taxonomy` ← Lecture 3b and `Large Language Models` ← CSCE 420 Lecture 7, both verified as real content citations before linking.
- **CSCE 420 course-page drift** — one missing frontmatter slug, and **36 session-recording source pages not reachable from the course page.** That last one had been deferred once already as "inherited and large." Fixed properly: a `## Session Recordings` section grouped by month, 35 Spring 2026 sessions plus the Fall 2026 notebook walkthrough, generated from the source titles rather than typed.

**The linter now lives in the repo.** The audit scripts had been in the session scratchpad, which was cleared between sessions — so the tooling the 2026-09-13 audit built had to be rewritten from scratch this session. It is now `tools/kb_lint.py` alongside `tools/transcribe.py`, runs as `python tools/kb_lint.py "College CS Knowledge Base"`, exits non-zero on any failure, and carries a header comment listing the four false-positive classes that have bitten previous audits (escaped pipes in tables, `\|` inside math, `[[...]]` inside code fences, H1-then-prose ledes) so they are not "fixed" by a future run.

**Result:** 385 → 391 pages. All 20 checks pass.

---

## [2026-09-22] ingest | CSCE 421 T04-T07 — overfitting, loss functions, MLP, backpropagation

Ingested five decks that close the gap between T03 (softmax) and the current lecture position. Sources copied to `raw/` with the `CSCE421_` prefix and extracted with PyMuPDF.

**Sources (5):** `CSCE421_T04-overfitting.pdf` (14 slides), `CSCE421_T05-loss-slides.pdf` (12), `CSCE421_T05-loss-notes.pdf` (4 pages), `CSCE421_T06-MLP-slides.pdf` (24), `CSCE421_T07-MLP-BP-exp.pdf` (9).

**Pages created (11):** source pages for all five decks; concepts [[Overfitting]], [[Regularization]], [[Model Selection]], [[Loss Functions]], [[Convexity]]; algorithm [[Multilayer Perceptron]].

**Pages updated (4):** [[Backpropagation]] extended with the CSCE 421 derivation (sensitivity `delta^(l)`, the outer-product gradient, and the T07 computational-graph worked example) and promoted to `course: CSCE 420, CSCE 421` following the [[Machine Learning Paradigms]] precedent — the existing CSCE 420 survey content was preserved above it, not replaced; [[CSCE 421]] course page rewritten with a T04-T07 arc table and the three pivots (closed form lost, fit-vs-select, convexity lost); `index.md`; `wiki/overview.md`.

**Extraction notes.** T04 is image-heavy — the polynomial fits, RMS curves, coefficient tables, and cross-validation diagrams carry no text layer, so the numeric figures are not reproduced and the PDF remains the reference. T06's text layer drops overline and accent characters: raw `f = h1h2 + h1h2` is XOR, `f = h1(h2 bar) + (h1 bar)h2`, and slide 11's `tan(x)` is `tanh(x)`, confirmed by slide 15's explicit "Using theta = tanh". T07 is an animation — slides 3-8 are one figure revealed progressively, with gradient values drawn as images; the worked example was reconstructed numerically (f(x,y,z)=(x+y)z at x=-2, y=5, z=-4 gives df/dx = df/dy = -4, df/dz = 3).

**Duplication avoided.** T06 overlaps CSCE 420's [[Perceptron]], [[Linear Separability]], and [[Neural Networks]] pages, which stay on the 420 side and are cross-linked rather than restated, per the standing rule that the two courses approach this material from opposite directions.

**Discrepancy noted.** The T05 note writes the linear score as `s_i = w^T x_i + b` with `x_i in R^d` and a separate bias; the T05 slides fold the bias in via the augmented vector, `x_i in R^(d+1)`. Same model, two conventions — recorded on both source pages.

## [2026-09-19] query | CSCE 420 HW1 Questions 1-5

- Request: Use the knowledge base to answer the homework in reviewable parts; the user limited this part to Questions 1-5 and asked to stop afterward.
- Sources: User-supplied Fall 2026 HW1 PDF and DFS notebook; [[CSCE 420 Homework 1 — Search]], [[Depth-First Search]], [[Breadth-First Search]], [[Depth-Limited Search]], [[Iterative Deepening Search]], and [[CSCE 420 Spring 2026 — 01-21 Uninformed Search]].
- Output: LaTeX source and PDF under `output/pdf/hw1_questions_1-5.*` at the repository root. Traces checked independently and with an executable simulation, using goal checks on removal and root depth 0. No later questions completed.

## [2026-09-18] ingest | CSCE 420 Fall 2026 — 09-18 minmax.ipynb walkthrough (video) + HW2 correction

- Source: `raw/CSCE420_HW1_Minimax_Explanation/CSCE420_HW1_Minimax_Explanation.mp4` (3:44 screen recording from class; filename says HW1 but content is the HW2 minimax starter) — transcribed with tools/transcribe.py (faster-whisper large-v3); scene detection found no cuts, frames pulled every 15 s and cropped
- Pages created (1): `wiki/sources/csce420-fall2026-0918-minmax-notebook-walkthrough.md`
- Pages updated (3): HW2 source page (cut hint corrected 4 -> 5 per Canvas announcement of Sep 17; walkthrough linked), `wiki/algorithms/minimax.md` (course-implementation section), index.md
- Notes: first real run of the video pipeline. Notebook in the video matches `raw/CSCE420_HW2_Fall2026_minmax.ipynb` exactly.

## [2026-09-18] update | CSCE 420 HW1 — Canvas "Homework #1 Explanation" page

- Source: Canvas page screenshots supplied in chat (not archived in raw/)
- Pages updated (1): `wiki/sources/csce420-homework-1-search.md` — new subsection on the Explanation page: nested-list tree semantics, DFS demo trace, `MAT` row=from/col=to convention, and the fixed recipe for Problems 9–10 (swap in `Node.expand`, state goal check, sort node list by h or cost+h)
- Notes: No solutions recorded; live assignment.

---

## [2026-09-17] ingest | CSCE 420 course-files export — 153 files, 3 semesters, 46 pages

Ingested `course_files_export.zip` (153 files) into the CSCE 420 section. The user's stated priority was **exam-scope separation** — a midterm question must never pull from final material — so scope was established first, from the recordings themselves, before any lecture page was written.

**Provenance sorted into three semesters.** Fall 2026 (the user's section): HW1 + HW2 PDFs and notebooks. Spring 2026: 38 Zoom transcripts (`.vtt`), no video. Fall 2025: one midterm-review class recording with captions, one whiteboard video (no captions — transcribed with faster-whisper large-v3), one silent matplotlib demo. Files that were duplicates, Canvas boilerplate, or images already embedded in the slide decks were not ingested. Raw archive: 4 HW files, 3 videos, 1 caption track, and the 38 transcripts under `raw/CSCE420_Spring2026_lecture_transcripts/`.

**Exam scope, as stated by the instructor on the recordings** (02-27, 03-04, 04-13, 04-15, 04-22): midterm = Deck 1 (one question) + Deck 2 + Deck 3 through unification (slide 99); final = post-midterm only, not cumulative, with Self-Organizing Maps and AI Ethics excluded and one FOL theorem-proving question guaranteed. Rules for both: two pages front/back, one paper cheat sheet both sides, most problems ≥ 2 sub-questions. Written into [[CSCE 420 Midterm Review]] (Canvas objectives list transcribed frame-by-frame from the Fall 2025 recording) and [[CSCE 420 Final Review]], and into an exam-scope table on the course page.

**Pages written (46):** 2 review pages; 2 homework pages (asks and conventions only, per the handwritten-homework rule — no solutions); 35 Spring 2026 lecture pages `csce420-sp26-MMDD-*`, each with `exam:` frontmatter (`midterm` ×11, `final` ×18, `excluded` ×2, `midterm / final` ×4 for pages straddling the boundary, each with a body note saying where the line falls); 3 Fall 2025 video pages; 2 new concept pages ([[Autoencoders]], [[Large Language Models]]) created because five lecture pages needed a target that did not exist. Lecture pages record what the instructor *said* — worked numbers, student Q&A, corrections he made live, scheduling facts — not the slides, which the Deck pages already cover; each names the slide range it covers.

**Discrepancies noted, not resolved:** Spring 2026 HW2 said 5 alpha-beta cuts, Fall 2026 HW2 says 4 (the Fall 2026 PDF governs for the user). Spring HW3/HW4 are described from walkthroughs as previews; the Fall 2026 versions have not been released. 03-27 was never recorded; 04-01 is the pre-recorded lecture filed as 03-31; 04-28 (research talk) is absent from the export.

**Forward-link drift caught and fixed (6):** pages were written in date order with forward links to not-yet-written titles; six of those titles changed when the later page was actually written (03-20, 03-25, 02-11, 04-08, 04-13, and *Final Practice* → *Final Exam Practice*). A title-resolution sweep over all new pages now runs before the audit.

**Index:** count 323 → 367 (the 09-13 count predates the CSCE 465 pages another session added; recounted from files). New section *Sources — CSCE 420 Spring 2026 Lecture Recordings* with the exam scope in every hook. Course page: frontmatter sources extended by 42 slugs, exam-scope table, export section.

## [2026-09-13] lint | Post-ingest audit — 17 structural + 10 content checks, 36 defects repaired

Run after the CSCE 465 Lecture 3 / 3a ingests, on the user's request. The 17-check structural suite (`lint_full.py`) was clean on the first pass; this audit added a **content layer** that reads provenance and staleness rather than just link syntax. Findings and fixes:

**Stale claim in the overview (1, fixed).** The CSCE 420 *gaps* block still read *"Only Lecture 1 has been ingested; the lectures covering search, logic, probability, and learning are not yet in the KB"* — twelve days after all eight lectures were ingested. The 2026-09-01 session updated the CSCE 420 *section* of the overview but not its gaps. Same failure mode as the CSCE 411 and CSCE 420 course pages caught in earlier audits: a page asserting incompleteness that is no longer true. Rewritten to the current state, including the per-deck extraction gaps the L3–8 ingest recorded, and the MDP/HMM coverage question updated from "unknown" to "mentioned only in passing, no page."

**Frontmatter provenance drift (3 files, fixed).** The overview's `sources:` list had not been updated since 2026-08-25 and was missing 12 slugs; it now lists all 97. The CSCE 420 course page's frontmatter listed 4 sources while its body (rebuilt 09-03) listed 12 — the 8 lecture slugs and the SOM notebook were added. The finance course page was missing both M13 slugs. A new content check (I) compares each course page's frontmatter against the source pages tagged with that course, so this cannot drift silently again.

**Source pages not linking pages that cite them (25, fixed).** CLAUDE.md: *source pages should link to every algorithm/concept they cover.* A new bidirectional check (B) found 25 concept/algorithm pages citing a source in `sources:` whose source page never linked back. Two kinds:
- **4 spurious citations removed** — all mine, from the L3/L3a ingests, where I had added a source slug to a page's frontmatter after adding only a See Also link, not content (`cia-triad.md` and `computer-security.md` ← L3; `security-services.md` and `cryptography-taxonomy.md` ← L3a). `sources:` means *content came from here*, and a cross-link is not content.
- **21 back-links added** to source pages' See Also sections where the citation was genuine. Two were striking: the *Lecture 18 — Recursive Backtracking* source page had never linked `[[Backtracking]]`, and *Lecture 27 — NP Verifiers* never linked `[[Vertex Cover]]` despite Vertex Cover citing it. The rest: Minimax and Local Search ← midterm practice; First-Order Logic and RL ← final practice; NN and RL ← 420 L1; CAPM and WACC ← M12/M13; Linear Models ← T02; Sigmoid ← T03 notes; Operating Systems ← 313 L2; and 7 from my own L3/L3a/HW1 source pages.

**Checks that ran clean:** `updated:` dates all valid and none in the future; every page has a lede (an earlier version of this check flagged 52 pages that open with an H1 — a false positive, fixed in the checker); every `raw/` path cited in the wiki exists (an earlier regex stopped at the space in `" (1).pdf"` suffixes and flagged 12 false positives); every concept/algorithm/source page carries `course:`; numeric facts repeated across the CSCE 465 pages (2⁵⁷ meet-in-the-middle, 2⁷² AES/DES, 26! ≈ 2⁸⁸, the 1975/1976 public-key date) agree at every occurrence.

**Findings deliberately not acted on:**

1. **45 pages exceed the ~700-word guideline.** The overview (4,113) is the synthesis page and exempt by nature; 20 are source pages for large decks or exams, where length tracks the source. Six concept/algorithm pages exceed 1,000 words: DES (1,388), Neural Networks (1,374), Security Design Principles (1,286), NP Completeness (1,182), Resolution (1,150), First-Order Logic (1,071). Each is a single coherent reference — ten principles, one algorithm walked end to end — and splitting would fragment lookups without improving them. Left intact; flagged for the user. If any is to be split, DES is the candidate (key schedule and mangler function could each stand alone).

2. **67 pages are linked from a source page but do not list it in `sources:`.** Checked and rejected as a defect class: `sources:` records *where a page's content came from*, and a homework solution linking `[[Dynamic Programming]]` does not make it a source of the DP page. The reverse direction (B, above) is the one the schema actually mandates. Spot-checked the plausible-looking cases (Deep Learning ← L7, Neural Networks ← L7, RNN ← L7): Deep Learning already lists L7; the others list L6, which is where the material was introduced. Not touched.

3. **One `\|` inside display math** (`self-organizing-map.md`) is a norm, `\|u-v\|`, and correct. The 09-03 log warned about escaping pipes inside math; this is the case where the backslash-pipe *is* the math.

**Other bases.** Broken-link sweep of the five other knowledge bases: GEOL 101 (75 pages), STAT 212 (47), MGMT 309 (25), Trading (9), General (5) — all zero. The two `[[index]]` hits in Trading and General resolve to their root `index.md`; the scanner only indexed `wiki/` titles.

**Checker corrections this run (3):** path-separator mismatch between `glob` and dict keys crashed check I on Windows (fixed with `normpath`); the lede check treated a leading H1 as "no lede"; the raw-path regex broke on filenames containing spaces. All three were caught because they produced implausible counts, which is the argument for eyeballing any check's first output before trusting it.

**Result:** 323 pages, unchanged. Structural suite clean (17/17). Content suite: 36 repairs, 3 findings flagged, 0 open defects. The audit scripts (`lint_full.py`, `audit_content.py`) live in the session scratchpad; they should be moved into the KB (e.g. a `tools/` directory) if audits are to be repeatable across sessions.

---

## [2026-09-13] ingest | CSCE 465 — Lecture 3a Secret Key Cryptography (I) (1 file)

**Source ingested** (copied to `raw/` as `CSCE465_03a_SecretKeyCrypto.pdf`): `03a_SecretKeyCrypto_s-1.pdf` — 32 PDF pages, two-up ≈ **63 logical slides**. The densest CSCE 465 deck so far, and the first to work through complete algorithms.

**Pages created (9):**
- Concepts (4): Secret Key Cryptography, Confusion and Diffusion, Block Ciphers, Side-Channel Attacks
- Algorithms (4): Feistel Cipher, DES, Triple DES, AES — **the first CSCE 465 algorithm pages**; a new "Algorithms — CSCE 465 (Security)" section was added to `index.md`
- Sources (1): CSCE 465 Lecture 3a — Secret Key Cryptography (I)

**Pages updated (9):** `cryptography-taxonomy.md` (its secret-key section now points at the standalone page), `classical-ciphers.md` (the confusion/diffusion forward pointer became a link), `cryptanalysis.md` (meet-in-the-middle and side channels as the first non-brute-force attacks), `cipher-security-models.md` (DES and AES as concrete computational-security cases), `cryptography.md`, `security-design-principles.md` (least common mechanism → side channels), `security-services.md`, `guofei-gu.md`, `csce-465.md`, plus `overview.md` and `index.md`.

**Nine pages for one lecture, and why that is not over-splitting.** The deck contains three complete algorithms and the design theory they share. Filing DES, Triple DES, and AES as one page would have produced a 3,000-word page that violates the 700-word guideline three times over; filing them as algorithm pages under a shared [[Block Ciphers]] / [[Confusion and Diffusion]] concept layer is what the schema's "algorithm pages link to their parent concept" rule is for. A new lint check (#17) now verifies that rule KB-wide; all 57 algorithm pages pass.

**The idea the whole deck turns on.** The [[Feistel Cipher]] makes *any* function invertible: `L_{i+1} = R_i`, `R_{i+1} = L_i XOR f(R_i, K_i)`, and decryption recomputes `f` forward and XORs it off. The round function is never inverted, in either direction. That is what let DES use S-boxes that shrink 6 bits to 4 — plainly non-invertible — inside a cipher that decrypts perfectly. AES chose the other route (every component individually invertible) and the lecture is explicit about the price: decryption costs more and only partially reuses the hardware.

**Three earlier claims got their concrete instances, and the overview now says so:**

| Earlier claim | Lecture 3a instance |
|---|---|
| *Cryptography is rarely the weakest link* (L3) | [[Side-Channel Attacks]] — timing and power recover keys from implementations of algorithms with no known weakness |
| *A large key space is necessary but not sufficient* (L3, mono-alphabetic) | Double DES: 112 bits of key material, ~57 bits of strength, via meet-in-the-middle |
| *Computational security erodes* (L3) | DES is architecturally sound — no attack significantly better than brute force — and obsolete anyway, purely because 2⁵⁶ stopped being enough |

**Meet-in-the-middle deserved the space it got.** The lecture defers detail to the KPS textbook, giving only the observation `X = E_K1{P} = D_K2{C}`. The attack was written out on [[Triple DES]] from that observation (encrypt forward under all K1, decrypt backward under all K2, match in the middle: 2⁵⁷ work, not 2¹¹²) and marked as derived. It is the single most reusable idea in the deck — *composing a cipher with itself does not compose its key space* — and it explains every design choice in Triple DES: why not double, why EDE not EEE, why two keys not three.

**Ten unanswered questions this time.** The instructor's pattern is now unmistakable (L2: 3, L3: 4, L3a: 10). All answered on the relevant page inside a blockquote marked as derived, except two: the DES cracking-cost "now?" (left as a pointer — the answer is "much less") and AES's "Q2: how are round keys generated?", which the deck genuinely defers and which is presumably the subject of a Lecture 3b along with modes of operation. Both flagged in the overview's gaps section.

**The avalanche data was worth tabulating.** DES round-by-round bit differences for a one-bit plaintext change: 1, 6, 21, 35, 39, 34, 32, 31, 29, 42, 44, 32, 30, 30, 26, 29, 34. Full diffusion arrives by round 3–4 and the count then oscillates around 32 of 64 — exactly the probability-0.5 target the lecture states. The remaining twelve rounds are security margin, which is the frame in which AES's "best attacks reach 7–9 of 10–14 rounds" reads as reassuring rather than alarming. Cross-linked from [[AES]] to [[Confusion and Diffusion]] for that reason.

**Extraction.** PyMuPDF, no image-only slides. **The DES permutation tables (IP, PC-1, PC-2, E, S1, P) all extracted with their row structure scrambled** — columns of numbers, rows lost. First rows were recoverable and are on [[DES]]; the complete tables are in the raw slides or textbook, and the page says so rather than reconstructing them from memory. The S1 worked example (`100110 → 1000`) survived intact and was verified against the standard table (row 2, column 3 = 8). Two slides carry a *"CSC/ECE 574, Dr. Peng Ning"* watermark — borrowed from NC State; noted for provenance.

**Lint.** Full suite plus the new algorithm-parent check. Two malformed table rows — unescaped alias pipes in `block-ciphers.md`, the same class as every ingest since 2026-08-27. Escaped, re-verified. The linter is now saved as a reusable script (`lint_full.py` in the session scratchpad) rather than re-typed each time. Zero broken links, zero orphans, index accurate in both directions.

**Result:** 314 -> 323 pages.

---

## [2026-09-10] ingest | CSCE 465 — Lecture 3 Introduction to Cryptography (1 file)

**Source ingested** (copied to `raw/` as `CSCE465_03_IntroCrypto.pdf`): `03_IntroCrypto-1.pdf` — 15 PDF pages, two-up = **29 logical slides**.

**Pages created (7):**
- Concepts (6): Cryptography, Cryptanalysis, Cipher Security Models, Classical Ciphers, One-Time Pad, Cryptography Taxonomy
- Sources (1): CSCE 465 Lecture 3 — Introduction to Cryptography

**Pages updated (6):** `security-services.md`, `security-design-principles.md`, `computer-security.md`, `cia-triad.md`, `guofei-gu.md`, `csce-465.md`, plus `overview.md` and `index.md`.

**This is the first lecture in the course to teach a mechanism rather than a framework**, and the ingest is organized around that. Six concept pages rather than one, because the lecture covers six genuinely separable things and the later crypto lectures will each attach to one of them.

**The lesson the deck is actually built around.** Mono-alphabetic ciphers have a key space of 26! ≈ 2⁸⁸ — *larger than DES* — and are broken instantly by frequency analysis. **A large key space is necessary but not sufficient.** Everything else in the early-ciphers section is a variation: Caesar leaks because the key space is tiny, mono-alphabetic leaks because the letter distribution survives encryption unchanged, permutation ciphers leak because they preserve letter frequencies *completely*. Each cipher leaks structure; the [[One-Time Pad]] is the one that leaks none, and Shannon's theorem prices that at a key as long as the message, used once.

**Four unanswered questions, answered and marked as derived.** The lecture poses these and moves on. Each is recorded on the relevant concept page inside a blockquote saying the answer was derived during ingest rather than given on the slide — the same convention the CSCE 420 practice-exam ingest established:

| Question | Answer recorded |
|---|---|
| Compression + encryption — what order? | Compress first; ciphertext is random and has no redundancy left. (Noted the CRIME/BREACH length-leak caveat as outside this lecture.) |
| Brute force — when do you know you succeeded? | The recognition problem; it is exactly what makes the OTP unbreakable rather than merely expensive |
| Mono-alphabetic — how many key bits? | log₂(26!) ≈ 88.4, so 89 bits, matching the slide's own 2⁸⁸ |
| OTP — why can't the key be reused? | c1 XOR c2 = p1 XOR p2 — the key cancels, leaving two plaintexts XORed together |

**The cryptography lecture is the design principles instantiated, and that is now cross-linked in both directions.** "Secret keys vs. secret algorithms" is [[Security Design Principles|open design]] under its cryptographic name (Kerckhoffs); [[Cipher Security Models|computational security]] is the work factor principle; and *cryptography is rarely the weakest link* restates Lecture 2's claim that defense is inherently more expensive than offense — the attacker goes after implementation and key management instead. Added the Kerckhoffs naming and the military exception to `security-design-principles.md` rather than leaving the connection implicit.

Also closed a loop opened in Lecture 2: [[Security Services]] listed six services and said cryptography underlies many mechanisms; [[Cryptography Taxonomy]] now names which primitive family delivers which service, including why one-key constructions structurally cannot provide non-repudiation.

**One factual divergence recorded rather than corrected.** The deck dates public key cryptography to **1975**; the commonly cited landmark is Diffie & Hellman's *New Directions in Cryptography* (1976), with Merkle's related work 1974–75. Both dates are on [[Cryptography Taxonomy]] with the discrepancy named, following the same handling as Lecture 2's three-vs-four-properties inconsistency.

**Extraction.** PyMuPDF. **One genuine visual gap:** slides 17–18 (PDF page 9) carry four images and 336 characters — the English single-letter frequency histogram and the output of TJ O'Connor's `letter` program on the Declaration of Independence. Neither is in the text layer, so the actual distribution is not in the KB. Minor: the permutation-cipher grid on slide 20 interleaves its plaintext and ciphertext rows during extraction; the offset vector and the plaintext phrase are reliable, the exact per-position output is not, and `classical-ciphers.md` says so.

**Lint.** Full 16-check suite run before logging. All clean except one malformed table row — an unescaped alias pipe I introduced in the course page's outline table, the same class caught in the last two ingests. Escaped and re-verified. Zero broken links (code fences excluded), zero orphans, zero frontmatter gaps, index accurate in both directions.

**Result:** 307 -> 314 pages.

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
