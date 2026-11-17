---
title: "CSCE 465 Lecture 14 — Intrusion Detection System"
type: source
tags: [csce465, intrusion-detection, ids, network-security, base-rate, anomaly-detection, evasion]
sources: []
course: CSCE 465
updated: 2026-11-16
---

Lecture 14 of [[CSCE 465]] (`raw/CSCE465_14_IDS.pdf`, 12 PDF pages laid out two slides per page = **23 logical slides**, instructor [[Guofei Gu]]). The **shortest** 465 lecture deck so far — three slides shorter than [[CSCE 465 Lecture 10 — Network Basics|Lecture 10]] — and nearly every slide is a figure. It is the *detect* layer after [[CSCE 465 Lecture 13 — Firewall|Lecture 13]]'s *prevent* layer, and the closest lecture in the course to the instructor's own field.

The deck has no roadmap slide. Its order is: definitions and motivation, the anatomy of an IDS, the two detection approaches, how to measure one, then the two deployments (host and network), and finally how a network IDS is defeated.

## Structure

The slides carry no printed numbers, so they are numbered here by position (PDF page *p* holds slides 2*p*−1 and 2*p*; the last page holds one).

| Slides | Section | Content |
|---|---|---|
| 3–6 | **What and why** | Definitions of intrusion and intrusion detection; prevent / detect / react-survive; the two assumptions; components from the algorithmic and architectural views; the pipeline figure |
| 7–10 | **Approaches** | The design space (misuse vs anomaly, network vs host, hand-coded vs learned); misuse detection; anomaly detection; monitoring networks and hosts |
| 11–13 | **Measuring an IDS** | The confusion matrix and the five rates; the Bayesian detection rate and the base-rate fallacy; an example ROC curve |
| 14–16 | **Host-based** | What a HIDS watches; Forrest's *sense of self*; the sliding window over system calls |
| 17–20 | **Network-based** | What a NIDS does; its layered architecture; firewall versus network IDS; the eight requirements |
| 21–23 | **Eluding a network IDS** | The reassembly problem; the insertion attack; the evasion attack |

## Pages Derived

| Page | What it holds |
|---|---|
| [[Intrusion Detection Systems]] | Definitions, the layered-defence picture, the two assumptions and how each fails, components, the three-axis design space |
| [[Misuse and Anomaly Detection]] | The two analysis approaches, their stated weaknesses, and the same split in the antivirus and worm material |
| [[IDS Performance Metrics]] | The confusion matrix, the five rates, the ROC curve with IDS1 and IDS2 |
| [[Base-Rate Fallacy]] | The Bayesian detection rate, the worked example verified, a sensitivity table, the two implications |
| [[Host-Based Intrusion Detection]] | OS auditing, BSM and `strace`, and Forrest's short sequences of system calls |
| [[Network Intrusion Detection]] | Sensors, the layered architecture, firewall vs IDS, the requirements list |
| [[Insertion and Evasion Attacks]] | Why the IDS and the end system can disagree, both attacks, and why normalization is the only fix |

[[Security Design Principles]] took content from this deck as well, for fail-safe defaults (fail-close against fail-open) and compromise recording.

## Content Worth Keeping

**Intrusion detection is identifying *and responding*.** An intrusion is a set of actions aimed to compromise integrity, confidentiality or availability. → [[Intrusion Detection Systems]]

**Prevent, detect, react/survive: layered mechanisms.** Each wall in the figure has holes, which is why there is a next wall. → [[Intrusion Detection Systems]]

**Two assumptions carry the whole field**: system activities are observable, and normal and intrusive activities have distinct evidence. Every weakness in the deck is one of them failing. → [[Intrusion Detection Systems]]

**Misuse detection can't detect new attacks; anomaly detection has a relatively high false positive rate** — *anomalies can just be new normal activities*. → [[Misuse and Anomaly Detection]]

**`if (src_ip == dst_ip) then "land attack"`** is the lecture's whole example of a signature. → [[Misuse and Anomaly Detection]]

**Four rates describe the detector; the fifth describes the alarm.** `P(A|I)` and `P(A|¬I)` condition on reality; the Bayesian detection rate `P(I|A)` conditions on the alarm. → [[IDS Performance Metrics]]

**With perfect detection and a false alarm rate of 10⁻⁵, one alarm in three is still false**, because the base rate is 2×10⁻⁵. → [[Base-Rate Fallacy]]

**Two implications: reduce the false alarm rate, and deploy where the base rate is high enough.** → [[Base-Rate Fallacy]]

**The ideal IDS is the top-left corner of the ROC plot** — 100% detection, 0% false alarm — and the two example curves cross, so neither wins everywhere. → [[IDS Performance Metrics]]

**A program's normal behaviour can be captured as short sequences of system calls.** Slide a window of length *k* over the trace; if the fraction of matching windows exceeds ε the run is normal. → [[Host-Based Intrusion Detection]]

**A network IDS may be easily defeated by encryption.** → [[Network Intrusion Detection]]

**Firewall: active filtering, fail-close. Network IDS: passive monitoring, fail-open.** → [[Network Intrusion Detection]]

**A network IDS must be resilient to attacks upon the IDS itself.** It is the only requirement with an exclamation mark. → [[Network Intrusion Detection]]

**What the IDS sees may not be what the end system gets.** Insertion: the IDS accepts a packet the host does not (`ATXTACK`). Evasion: the host accepts a packet the IDS does not (`ATTCK`). → [[Insertion and Evasion Attacks]]

## Connection to the Rest of the KB

- **The KB's first CSCE 420 / CSCE 465 link.** The Bayesian detection rate is [[Bayes Rule]] with the labels changed: intrusion for disease, alarm for positive test. CSCE 420's worked example — a 99% accurate test for a 1-in-10,000 disease, giving just under 1% — is the same calculation as this deck's 66%, and the two are set side by side on [[Base-Rate Fallacy]]. The CSCE 420 page gained a back-link only.
- **And one more to [[CSCE 313]].** Forrest's detector reads the system-call trace, and [[System Calls]] is the page that explains why that trace is a complete record of what a process does to the world. `strace` appears on two slides.
- **It answers the foundations lectures three times.** [[Security Policy and Mechanism]] said detection is sometimes the only option and that it depends on a protected audit trail; [[Security Design Principles]] made compromise recording a principle; [[Computer Security]] called intrusion detection *a full unit of the course rather than a fallback*. This is that unit.
- **Misuse versus anomaly was already in the KB under other names** — the signature and behaviour generations of antivirus on [[Computer Viruses]], Nimda outrunning its signature on [[Notable Worms]], Google's anomaly detection on [[Search Worms]].
- **[[Botnets|BotHunter]]'s full title is *IDS-Driven Dialog Correlation*.** Lecture 11 ended on the instructor's paper; this lecture is the background it assumes, and the base-rate slide is the problem dialog correlation addresses.
- **Lecture 12 and this lecture use the same fact about TCP/IP stacks.** [[OS Fingerprinting]]: *each OS implements their TCP stack differently.* Here: *ambiguities in protocols and operating systems.* Reconnaissance in one, evasion in the other.
- **Lecture 13's proxies are this lecture's normalizers.** A [[Proxy Firewalls|circuit-level gateway]] *protects against the fragmentation problem* by rebuilding the connection, which is what "normalize the packets" asks for.
- **[[Biometrics]] did the same error-rate arithmetic** for multifactor authentication: true positives, false positives, and a trade-off between them.
- **[[Stack Smashing]] and [[Shellcode]] explain why system-call sequences work as evidence**: injected code makes calls in an order the program never does.

## Deck Arithmetic, Checked

| Claim on the slide | Check | Result |
|---|---|---|
| Perfect detection, false alarm rate 10⁻⁵, base rate 2×10⁻⁵ gives a Bayesian detection rate of 66% | 2×10⁻⁵ / (2×10⁻⁵ + (1−2×10⁻⁵)×10⁻⁵) = 0.6667 | **Correct** (66.7%, shown rounded down) |
| Sliding window over an 8-call trace, four windows listed then "…" | 8 calls give 5 windows of length 4; the four listed are the first four in order | **Consistent**; *k* = 4 is implied, not stated |

## Extraction Note

Text extracted with PyMuPDF. Bullets are clean, and the slides are figure-heavy: 5,547 characters across 23 slides, about 240 per slide. **Every content page was rendered and read**, and the figures below were recovered that way.

| Slide | Figure | Recovered? |
|---|---|---|
| 4 | Three walls: prevent, detect, react/survive | **Yes** — structure and caption |
| 6 | IDS component pipeline | **Yes** — every box, arrow label and both annotations |
| 8 | Misuse detection: patterns, pattern matching, activities | **Yes** |
| 9 | Anomaly detection bar chart | **Partly** — the legend, two of the four axis labels (*CPU*, *Process Size*) and approximate bar heights. Two measures are unlabelled on the slide itself |
| 11 | Confusion matrix | **Yes** |
| 12 | The Bayesian detection rate formula | **Yes** — it extracts as one symbol per line and was read from the render |
| 13 | ROC curve for IDS1 and IDS2 | **Partly** — the shapes and the crossing are recorded; the plot has **no axis ticks**, so the numbers on [[IDS Performance Metrics]] are estimates and are marked as such |
| 16 | Sliding-window flowchart | **Yes** |
| 18 | Layered NIDS architecture | **Yes** |
| 19 | Firewall in line, IDS beside the path | **Yes** |
| 22–23 | Insertion and evasion letter boxes | **Yes** — all three streams on each slide |

The mathematical glyphs came through: `¬` is intact, and exponents extract flattened (`10-5` for 10⁻⁵, `2×10-5`), confirmed against the render. The threshold `ε` on slide 16 extracts as the letter `e`.

**Provenance.** The PDF was created on **2024-11-13**, so this deck is reused from an earlier offering, like Lecture 13 and unlike Lecture 12.

## Attributions Not on the Slides

Three pieces of this deck have well-known origins that the slides do not cite. They are recorded on the derived pages as attributions made during ingest:

- The base-rate example — Axelsson, *The Base-Rate Fallacy and Its Implications for the Difficulty of Intrusion Detection* (1999).
- The layered NIDS architecture and the requirements list — the design of **Bro**. The deck does name Bro, on slide 7, as a signature-based system.
- Insertion and evasion — Ptacek and Newsham, *Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection* (1998).

Slides 15–16 do credit their source: *Prof. Forrest at University of New Mexico* and *Forrest et al. UNM*.

## Questions the Deck Leaves Open

- **Slide 17 ends on "Other problems …"** and slides 21–23 supply one of them. Whether more were given in lecture is not recoverable from the slides.
- **The ROC slide draws two systems and does not say which is better.** A derived reading is on [[IDS Performance Metrics]].
- **The land attack is used as an example and never defined.** A one-line definition is on [[Misuse and Anomaly Detection]], marked derived.
- **Slide 7 offers "learning based on audit data" as a way to build an IDS** and the deck does not return to it, beyond Forrest's learned profile.

## Open Gaps

- **Web security is the one topic left in the network security row of the course outline**, and the hypothesis for Lecture 15.
- **The AI agent unit has still arrived only through HW1.** The outline's last row, *AI agent and security*, has no lecture deck in the KB.
- **No Lecture 6, and 6a still implies a 6b.** Unchanged since Lecture 7.
- **Homework position unchanged** — only HW1, and only its briefing deck. The fourth assignment is *network security and intrusion detection*; Lectures 12, 13 and 14 are its lecture material and the assignment itself has not been seen.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Intrusion Detection Systems]]
- [[Misuse and Anomaly Detection]]
- [[IDS Performance Metrics]]
- [[Base-Rate Fallacy]]
- [[Host-Based Intrusion Detection]]
- [[Network Intrusion Detection]]
- [[Insertion and Evasion Attacks]]
- [[Security Design Principles]]
- [[Bayes Rule]]
- [[System Calls]]
- [[Botnets]]
- [[CSCE 465 Lecture 13 — Firewall]]
- [[CSCE 465 Lecture 12 — Vulnerability Analysis]]
- [[CSCE 465 Lecture 11 — Malware]]
