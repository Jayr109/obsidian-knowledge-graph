---
title: "CSCE 465 Lecture 4 — Hash Functions"
type: source
tags: [csce465, cryptography, hash, md5, sha-1, hmac, birthday-attack]
sources: []
course: CSCE 465
updated: 2026-10-01
---

Lecture 4 of [[CSCE 465]] (`raw/CSCE465_04_Hash.pdf`, 24 PDF pages laid out two slides per page ≈ 47 logical slides, instructor [[Guofei Gu]]). The third family of the [[Cryptography Taxonomy|crypto taxonomy]] — the one with **no key**. Roadmap: *hash function lengths, hash function applications, MD5 standard, SHA-1 standard, Hashed Message Authentication Code (HMAC)*.

**This closes the numbering gap the KB has been flagging since 2026-09-26.** The decks run 1, 2, 3, 3a, 3b, **4**, 5; Lecture 4 was missing and the overview predicted from the course outline that it would be hashes and message digests. It is. **Applied cryptography in CSCE 465 is now completely ingested.**

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–5 | **Properties and length** | Definition and aliases; four desirable properties; why 128/160 bits; the birthday paradox and its generalization |
| 6–11 | **Applications** | File authentication (Tripwire); user authentication; commitment protocols; message encryption; message authentication; digital signatures; "is encryption a good hash function?" |
| 12 | **The standards** | MD5 broken 2004; SHA weaknesses; SHA-1 broken not cracked; SHA-256/384 |
| 13–17 | **MD5** | Compression function; Merkle–Damgård structure; notation; four passes F/G/H/I; the T table; step logic; insecurity |
| 18–21 | **SHA-1** | Parameters and IV; message schedule; 80 steps; `f(t,B,C,D)`; per-step processing; comparison with MD5; security |
| 22–24 | **HMAC** | Extension attacks; digest-inside-a-digest; HMAC processing; summary |

## Pages Derived

| Page | Type | What it holds |
|---|---|---|
| [[Hash Functions]] | concept | Definition, the four properties, why ≥128 bits, encryption-as-hash, the standards table |
| [[Birthday Attack]] | concept | The paradox, the √n generalization, the 2^(m/2) bound, why it governs strong collision resistance |
| [[Hash Function Applications]] | concept | All six applications with every posed question answered |
| [[MD5]] | algorithm | Compression function, padding and chaining, F/G/H/I, the T table, step logic, the X.509 collisions |
| [[SHA-1]] | algorithm | Parameters, message schedule, 80 steps, round functions, the MD5 comparison |
| [[HMAC]] | algorithm | The extension attack and why Merkle–Damgård enables it; the nested construction |

## Content Worth Keeping

**Weak vs strong collision resistance differ in who picks the messages.** Weak: you are handed `m` and must find a colliding `m'`. Strong: you pick both. Strong is the binding constraint because picking both is what the birthday attack exploits. → [[Hash Functions]]

**A hash's collision resistance is half its output length.** 2^(m/2) work by birthday, so a 128-bit digest gives 64 bits and a 160-bit digest gives 80. That is why digests are longer than cipher keys of comparable strength. → [[Birthday Attack]]

**The two "brute force" figures quoted for MD5 and SHA-1 — 2⁶⁴ and 2⁸⁰ — are birthday bounds**, not exhaustive searches of the digest space. → [[Birthday Attack]], [[SHA-1]]

**Encryption makes a poor hash.** Block size too short (DES = 64 → birthday at 2³²), a message with a target hash is constructible via meet-in-the-middle, and extension attacks apply. → [[Hash Functions]]

**Five of the six applications add a key, a nonce, or both.** A bare hash proves *nothing changed*; a hash plus a key proves *who*; a hash plus a nonce proves *not a recording*. → [[Hash Function Applications]]

**MD5's T table is `⌊2^32·|sin(i)|⌋`** — a nothing-up-my-sleeve construction, verifiable by anyone, so no backdoor can hide in the constants. → [[MD5]]

**The feed-forward addition is what makes the compression function one-way.** `output = input digest + output of last pass`, in both MD5 and SHA-1. Remove it and the passes run backwards. → [[MD5]], [[SHA-1]]

**SHA-1's real difference from MD5 is the message schedule** — 16 words expanded to 80 by XOR-mixing, rather than 16 words reused four times. → [[SHA-1]]

**SHA-1's per-step code is a simultaneous assignment**, not sequential. The deck says so explicitly (*"everything to right of = is input value to this step"*), and read sequentially it is wrong. → [[SHA-1]]

**A Merkle–Damgård digest is a resumable intermediate state**, which is the whole extension attack: given `H(K|M1|pad)` you can compute `H(K|M1|pad|M2|newpad)` without knowing `K`. → [[HMAC]]

**HMAC's two pad constants (0x36, 0x5c) differ in half their bits on purpose** — they derive two distinct keys from one, the same never-reuse-a-key-for-two-jobs discipline as the P+I construction. → [[HMAC]]

## Worked Math — All Verified

Every quantitative claim was recomputed during ingest and **all are correct**:

| Claim | Check |
|---|---|
| Birthday paradox `k ≈ 23` | P(22) = 0.4757, P(23) = 0.5073 — 23 is the exact threshold ✓ |
| `k = √(2 ln2 · n) = 1.18√n` | √(2 ln 2) = 1.1774 ✓ |
| `1.18·√365 = 22.54` | 22.54 ✓ |
| MD5 `T[i] = floor(2^32 * abs(sin i))` | T[1] = `0xD76AA478`, T[2] = `0xE8C7B756`, T[64] = `0xEB86D391` — match the published MD5 constants ✓ |
| 2^(m/2) bound | m=64 → 2³²; m=128 → 2⁶⁴; m=160 → 2⁸⁰ — consistent with the MD5/SHA-1 figures the deck quotes ✓ |

## Open Questions the Lecture Poses

Twelve, the second-most of any CSCE 465 deck. All answered on the derived pages in blockquotes marked as derived:

| Question | Answered on |
|---|---|
| Why 128 or 160 bits in the output? | [[Hash Functions]] / [[Birthday Attack]] |
| File auth: *why not just store a duplicate copy of F???* | [[Hash Function Applications]] |
| User auth: *why not just send K in plaintext? Or H(K)? What is the purpose of R?* | [[Hash Function Applications]] |
| Commitment: *how to prevent this?* / *can either party cheat now?* | [[Hash Function Applications]] |
| Commitment: *why is sending H(X) better than X?* | [[Hash Function Applications]] |
| Commitment: *why is H(X) good enough to prevent A cheating?* | [[Hash Function Applications]] |
| Commitment: *why need B not send H(Y)?* | [[Hash Function Applications]] |
| Commitment: *what if the set of X is small? what if B can predict X?* | [[Hash Function Applications]] |
| Message encryption via C+H: *as good as encryption?* | [[Hash Function Applications]] |
| Message auth: *why is R needed? why is K needed?* | [[Hash Function Applications]] |

## Connection to the Rest of the Unit

The lecture completes the three-family taxonomy and ties back in three directions:

- **To Lecture 3b.** The [[Message Authentication Code|CBC residue]] MAC and [[HMAC]] are now both in the KB — two MAC constructions on different primitives, neither giving non-repudiation. The C+H message-encryption application is literally the [[Block Cipher Modes of Operation|OFB diagram]] with the cipher swapped for a hash.
- **To Lecture 5.** [[Digital Signatures]] sign `H(m)`, not `m` — and the reason is on this page: [[RSA]] needs `m < n`. MD5's colliding X.509 certificates are a [[Public Key Infrastructure|PKI]] break *at the hash layer*, the same shape as the Comodo failure.
- **To Lecture 3a.** Meet-in-the-middle, which defeated [[Triple DES|Double DES]], reappears as a reason not to build a hash from a block cipher.

## Extraction Note

Text extracted with PyMuPDF. **No image-only slides.**

**Superscripts and math symbols are flattened throughout**, as in every deck in this unit: `2^(m/2)` appears as `2m/2`, `365^k` as `365k`, `2^32` as `232`, and `⌊x⌋` as `ëxû`. The logical operators survive as `Ù Ú Å ~` (AND, OR, XOR, complement) and `|` as concatenation. All formulas on the derived pages were rebuilt with explicit operators and **verified numerically** against the deck's own stated answers.

**The structural diagrams extract as label clouds** — the MD5 high-level view, the per-step logic, the HMAC processing flow, and the OFB-style C+H diagram all lose their boxes and arrows. Diagrams on the derived pages were reconstructed from the labels plus the accompanying prose; the raw deck is authoritative for exact figure layout.

**One ambiguity recorded, not resolved:** the properties slide annotates both collision-resistance entries with a parenthetical **"(free)"** whose meaning is not recoverable from the text layer — possibly a lost symbol or abbreviation. Flagged on [[Hash Functions]] rather than guessed at.

**Borrowed slides again.** Two slides (the MD5 pass overview and the HMAC processing figure) carry the **"CSC/ECE 574, Dr. Peng Ning"** watermark — the third CSCE 465 deck to reuse material from that NC State course, after Lectures 3a and 3b.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Hash Functions]]
- [[Birthday Attack]]
- [[Hash Function Applications]]
- [[MD5]]
- [[SHA-1]]
- [[HMAC]]
- [[CSCE 465 Lecture 3b — Secret Key Cryptography (II): Modes of Operation]]
- [[CSCE 465 Lecture 5 — Public Key Cryptography]]
