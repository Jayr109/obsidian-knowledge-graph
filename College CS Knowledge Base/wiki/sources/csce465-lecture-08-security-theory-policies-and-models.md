---
title: "CSCE 465 Lecture 8 — Security Theory: Security Policies and Models"
type: source
tags: [csce465, security-theory, policy, blp, biba, chinese-wall, rbac, undecidability]
sources: []
course: CSCE 465
updated: 2026-10-20
---

Lecture 8 of [[CSCE 465]] (`raw/CSCE465_08_SecurityTheory.pdf`, 24 PDF pages laid out two slides per page = **47 logical slides**, instructor [[Guofei Gu]]). This is the *fundamental security theories* entry in the course outline's OS-and-system-security unit, and it is the most theoretical deck of the semester. Roadmap as given: *fundamental results on safety question; security policy — what they cover; access control model: express security policy — confidentiality policy and BLP model, integrity policy and Biba model, hybrid policy model (Chinese Wall, RBAC)*.

It sits directly on top of [[Access Control Models|Lecture 7]], which gave the mechanisms (ACLs, DAC/MAC, Unix and NTFS permissions). Lecture 8 asks what those mechanisms are *for*, proves that the general question has no answer, and then presents four restricted models that do.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–8 | **The safety question** | The general question; safety vs. security; the safety question stated; the undecidability theorem and its reduction from the halting problem; key points |
| 9–16 | **Security policy** | Policy as a partition of states; formal confidentiality, integrity and availability; the homework-cheating example; mechanisms |
| 17–21 | **Access control and models** | Access control as `P(S,O,R)`; the access control matrix; DAC vs MAC administration; what a security model is; types of security policy |
| 22–30 | **Confidentiality and BLP** | Confidentiality policy and MLS; Bell-LaPadula; the linear-level example; the lattice model and categories; simple security condition; the DocC question; \*-property; Basic Security Theorem |
| 31–36 | **Integrity and Biba** | Integrity policy; integrity vs security labels; the Biba rules and the monk example; an open exercise; low-water mark |
| 37–46 | **Hybrid policies** | Chinese Wall — the conflict-of-interest problem, CDs and COI classes, CW-simple security condition, the Anthony/Susan write leak, CW-\*-property; RBAC — roles vs identity |
| 47 | **Summary** | The four models and their one-line rules |

## Pages Derived

| Page | What it holds |
|---|---|
| [[Safety Problem]] | The general question, safety vs. security, the undecidability theorem and its reduction |
| [[Access Control Matrix]] | `P(S,O,R)`, subjects/objects/rights, the matrix and its two compressions, DAC/MAC administration |
| [[Security Models]] | What a security model is and why one is adopted; policy types; the four-model taxonomy |
| [[Multi-Level Security]] | Linear levels, the lattice model, categories, `(L,C)` labels, dominance |
| [[Bell-LaPadula Model]] | Simple security condition, \*-property, Basic Security Theorem, the DocC worked example |
| [[Biba Integrity Model]] | Integrity vs security labels, no-read-down/no-write-up, the monk example, low-water mark |
| [[Chinese Wall Model]] | COI classes and company datasets, CW-simple, the Anthony/Susan leak, CW-\*-property, sanitization |
| [[Role-Based Access Control]] | Roles vs identity, static permissions with transient membership |

Four existing pages were extended rather than duplicated: [[Security Policy and Mechanism]] (the state-partition definition, the cheating example), [[CIA Triad]] (the formal `X`/`I` definitions), [[Access Control Models]] (AppArmor and the dominance-calculus framing of MAC), and [[Operating System Security]] (a pointer into the theory unit).

## Content Worth Keeping

**The safety problem is undecidable, by reduction from the halting problem.** An arbitrary Turing machine reduces to the safety problem with the TM's final state corresponding to the leaking of a generic right. Cited to Matt Bishop, *Introduction to Computer Security*; the result is Harrison–Ruzzo–Ullman. → [[Safety Problem]]

**Safety is the model; security is the implementation — and the implication is one-way.** A secure system corresponds to a safe model; a safe model does **not** ensure a secure system. → [[Safety Problem]]

**Limiting the scope of systems can make the problem decidable.** This single bullet is the justification for everything after slide 8. → [[Safety Problem]]

**A policy partitions system states into authorized and unauthorized**; a secure system starts authorized and never leaves. Security is a property of every reachable state, not of a snapshot. → [[Security Policy and Mechanism]]

**The policy is a lot of `P(S,O,R)` tuples, whether explicitly represented that way or not.** Unix mode bits, NTFS ACLs and firewall rules are all compressions of one matrix. → [[Access Control Matrix]]

**Bill cheated and Anne did not.** Copying was forbidden, so the system entered an unauthorized state; failing to read-protect a file was not forbidden, so it was not a breach — *if* the policy had required read-protection, it would have been. A clean demonstration that "secure" is meaningless until the policy is written down. → [[Security Policy and Mechanism]]

**Dominance needs both conditions.** `(L,C)` dominates `(L′,C′)` iff `L′ ≤ L` **and** `C′ ⊆ C`, which makes the order **partial** — and that partiality is how "need to know" is encoded. → [[Multi-Level Security]]

**BLP: no read up, no write down.** Both rules are needed because the model governs information *flow*, not just access; write-up is permitted because it leaks nothing, at the price of letting a low subject corrupt a high file. → [[Bell-LaPadula Model]]

**The Basic Security Theorem.** Secure initial state + every transition satisfies both rules ⇒ every state is secure. The induction the model exists to make possible. → [[Bell-LaPadula Model]]

**Biba: no read down, no write up — and integrity labels are not security labels.** Security labels limit flow; integrity labels inhibit modification. Higher level = more confidence the program runs correctly and the data is reliable. → [[Biba Integrity Model]]

**Low-water mark replaces refusal with demotion.** A subject starts at the highest integrity and ends up at the integrity of the lowest object it read — taint tracking inside the access control model. → [[Biba Integrity Model]]

**Chinese Wall is the only model here with state.** Whether *s* may read *o* depends on `PR(s)`, the set of objects *s* has already read, so permissions shrink irreversibly as work proceeds. → [[Chinese Wall Model]]

**Two legal reads plus a shared object make an illegal flow.** Anthony and Susan each satisfy CW-simple, yet a write by Anthony to the shared gas-company dataset leaks Bank 1 to Susan — which is why CW-\*-property is so severe that sanitization becomes load-bearing. → [[Chinese Wall Model]]

**RBAC: permissions are static, user-role membership is transient.** Allison leaves, Betty is hired, the bookkeeper role is unchanged. The win is administrative, not expressive. → [[Role-Based Access Control]]

## Connection to the Rest of the KB

- **This is where the course's theory half meets [[CSCE 411]].** The undecidability proof is a reduction from the [[Halting Problem|halting problem]] — the same technique as the [[Decidability and Undecidability|undecidability unit]] in the algorithms course, applied to a protection system. The two courses had not touched before.
- **[[Access Control Models|Lecture 7]] supplied the mechanisms; this supplies the policies.** DAC and MAC appear in both decks; Lecture 8 adds the examples (process labeling, AppArmor) and names the **dominance calculus** that Lecture 7 only gestured at.
- **[[Security Policy and Mechanism|Lecture 2]]'s policy/mechanism/assurance split is now formal.** "Policy says what is allowed" becomes "policy partitions states"; "assurance" becomes the gap between a safe model and a secure system.
- **The [[CIA Triad]] gets formal definitions** in terms of an entity set `X` and information `I`, which sharpen the informal Lecture 1 and 2 treatments without contradicting them.
- **[[Security Design Principles|Least privilege]] gets a fourth instance** in RBAC, after setuid, `sudo` and fail-safe defaults.

## Extraction Note

Text extracted with PyMuPDF; the deck is prose-and-bullets and extracted essentially intact, including all four models' formal rules and the Chinese Wall set-theoretic conditions.

**Symbol mangling in the text layer** — the PDF encodes set-theory glyphs in a symbol font, so extraction produced `Î` for ∈, `Í` for ⊆, `È` for ∪, `®` for →, `¹` for ≠ and `o¢` for *o′*. Every occurrence was mapped back by hand against the rendered pages; the derived pages use the correct symbols.

**Figures checked against rendered pages at 2.2×:**
- **Slide 28** (the DocC question) is a lattice diagram whose node labels are an image. Rendered and read: six labelled nodes plus allow-arrows and one red X marking Bob's blocked read of DocC. Fully recovered, and the worked answer on [[Bell-LaPadula Model]] is derived from it.
- **Slide 24** (BLP) carries the four-level Top Secret / Secret / Confidential / Unclassified figure — recovered.
- **Slide 35** is an **unanswered in-class exercise**: the slide-28 cast under Biba, captioned `?????`. Recorded as open on [[Biba Integrity Model]]; no answer is invented.
- Slides 26, 34, 36 and 46 carry decorative photographs (a lattice fence, a monk, a tide line) with no information content.

**Deck errata, both minor:** the summary slide spells Biba as *"Bida"*, and slide 26 writes *CRYTPO* for CRYPTO in Alice's label (correct on slide 28). Neither affects content.

## Open Gaps

The numbering gaps recorded after Lecture 7 are unchanged: **there is no Lecture 6**, and the **6a** label still implies a **6b** — per the course outline, likely *authentication and security handshake pitfalls*. Lecture 8 follows 7 cleanly, so the OS-and-system-security unit is now two decks deep with *software security* still outstanding.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Safety Problem]]
- [[Access Control Matrix]]
- [[Security Models]]
- [[Multi-Level Security]]
- [[Bell-LaPadula Model]]
- [[Biba Integrity Model]]
- [[Chinese Wall Model]]
- [[Role-Based Access Control]]
- [[Security Policy and Mechanism]]
- [[CIA Triad]]
- [[Access Control Models]]
- [[Halting Problem]]
- [[CSCE 465 Lecture 7 — Operating System Security]]
