---
title: "CSCE 465 Lecture 3a — Secret Key Cryptography (I)"
type: source
tags: [csce465, cryptography, secret-key, des, aes, feistel, block-cipher]
sources: []
course: CSCE 465
updated: 2026-09-22
---

Lecture 3a of [[CSCE 465]] (`raw/CSCE465_03a_SecretKeyCrypto.pdf`, 32 PDF pages laid out two slides per page ≈ 63 logical slides, instructor [[Guofei Gu]]). The first lecture to work through complete algorithms — [[DES]] component by component, [[Triple DES]] with the attack that shaped it, and [[AES]] at the round level — framed by the design theory that all three share. The deck's roadmap: introductory remarks, Feistel cipher, DES, Triple DES, AES.

The "(I)" in the title implies a second secret-key lecture is coming. It arrived as [[CSCE 465 Lecture 3b — Secret Key Cryptography (II): Modes of Operation|Lecture 3b]], which covers modes of operation — **but not** the AES key schedule this deck defers. That question is still open.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–7 | **Introduction** | Definition; four applications; block encryption; key sizes over time; notation; [[Confusion and Diffusion]]; the generic modern block cipher |
| 8–11 | **Feistel cipher** | One round of encryption and decryption; the complete cipher with its final swap; parameters; why f need not be invertible |
| 12–24 | **DES** | Criteria; parameters; top-level view; initial/final permutation; key schedule; the mangler function (E, S-boxes, P); implementation; S-box principles; avalanche; weak and semi-weak keys; key size |
| 25–27 | **Triple DES** | Double DES and its two concerns; meet-in-the-middle; EDE; strength and cost |
| 28–31 | **AES** | Rijndael; parameters; the state; one round; decryption conceptual vs actual; assessment |
| 32 | **Side channels + summary** | Timing and power attacks; four closing claims |

## Pages Derived

| Page | Type | What it holds |
|---|---|---|
| [[Secret Key Cryptography]] | concept | Definition, four applications, notation, key sizes, the three ciphers compared |
| [[Confusion and Diffusion]] | concept | Shannon's principles, S/P alternation, the generic template, avalanche effect with DES data |
| [[Block Ciphers]] | concept | Generic block encryption, block size trade-off, the operation list, S-boxes, HW vs SW |
| [[Feistel Cipher]] | algorithm | The round, decryption by reversal, the final swap, parameters |
| [[DES]] | algorithm | Everything from criteria to weak keys |
| [[Triple DES]] | algorithm | Double DES, meet-in-the-middle, EDE, strength table |
| [[AES]] | algorithm | State, round operations, decryption, assessment, DES comparison |
| [[Side-Channel Attacks]] | concept | Timing, power, why they escape the security models |

## Content Worth Keeping

**Secret key crypto does four things, not one.** Secure channel, secure storage, message integrity via an encrypted MIC, and authentication — with the caveat that symmetric authentication convinces only the other key holder. → [[Secret Key Cryptography]]

**Five key bits per decade.** If computing power grows 40% per year, key length must grow ~5 bits per decade to stand still. → [[Secret Key Cryptography]]

**Confusion by substitution, diffusion by permutation, alternating.** The one-sentence theory of modern symmetric cryptography. → [[Confusion and Diffusion]]

**The Feistel structure makes any function invertible.** `f` is only ever computed forward, in both directions; reversibility comes from XOR. → [[Feistel Cipher]]

**DES's initial permutation does not improve security.** Fully specified, key-independent — kept for hardware convenience and because the standard says so. → [[DES]]

**The S-box is the only nonlinear part of DES.** Everything else is linear and would fall to linear algebra alone. → [[DES]], [[Block Ciphers]]

**Avalanche in numbers.** 1 → 6 → 21 → 35 → 39 bits changed over rounds 0–4; full diffusion by round 3–4, oscillating around 32 thereafter. → [[Confusion and Diffusion]]

**Double DES gives one bit, not 56.** Meet-in-the-middle: 2⁵⁷ work for 112 bits of key material. Key material and key strength are different quantities. → [[Triple DES]]

**AES is not a Feistel cipher, and pays for it in decryption.** Every operation individually invertible; decryption needs more memory and cycles; hardware only partially reusable. → [[AES]]

**AES-128 is 2⁷² times harder to brute-force than DES**, and runs at 200 MB/s on a PC with no special hardware. → [[AES]]

**The implementation is the target.** Timing and power attacks recover keys from ciphers with no known cryptanalytic weakness. → [[Side-Channel Attacks]]

## The Lecture's Own Summary

1. Secret key crypto is **(a) good quality, (b) faster to compute than public key crypto, and (c) the most widely used crypto.**
2. **DES** is strong enough for non-critical applications, but **Triple DES** is better.
3. **AES** is even better — stronger *and* much faster — with 128-, 192-, and 256-bit versions.
4. Secret key crypto requires **"out-of-band", bilateral key negotiation/agreement.**

Claim 4 is the hand-off to public key cryptography.

## Open Questions the Lecture Poses

This instructor's habit continues — this deck has the most yet. Each is recorded with a derived answer on the relevant page, marked as derived:

| Question | Page |
|---|---|
| Symmetric authentication — *how is that possible?* | [[Secret Key Cryptography]] |
| Block size — *benefits of large k? of short k?* | [[Block Ciphers]] |
| S/P alternation — *do they have to alternate?* | [[Confusion and Diffusion]] |
| Initial permutation does not improve security — *why needed?* | [[DES]] |
| Weak keys `K{K{m}} = m` — *what's bad about that?* | [[DES]] |
| Semi-weak keys `K1{K2{m}} = m` — *what's bad about that?* | [[DES]] |
| DES cracking cost — *ten years ago $250,000; now?* | [[DES]] (left as a pointer; the answer is "much less") |
| Double DES — *is 112 bits of key material 112 bits of strength?* | [[Triple DES]] |
| Triple DES — *why not E-E-E? why not 3 keys? why not the same key 3 times?* | [[Triple DES]] |
| AES — *Q2: how are round keys generated?* | **Still unanswered.** Deferred here, and Lecture 3b turned out to cover modes of operation instead |

## Extraction Note

Text extracted with PyMuPDF. **No image-only slides.** The deck's many diagrams (Feistel rounds, DES top-level view, mangler function, AES state) all carry their content in text.

**Permutation tables are present but scrambled.** The IP, PC-1, PC-2, E, S1, and P tables all extracted as columns of numbers with the row structure lost. First rows were recoverable and are given on [[DES]]; for the complete tables the raw slides or the textbook are authoritative. The S1 table's row 2 is missing entries in the text layer, but the lecture's worked example (`100110 → 1000`) is intact and matches the standard table.

**Borrowed slides.** The two complete-Feistel-cipher diagrams (slides 19–20) carry the watermark *"CSC/ECE 574, Dr. Peng Ning"* — they are reused from Peng Ning's NC State course. Noted for provenance; the content is standard.

## Connection to Earlier Lectures

Lecture 3 said DES, IDEA, AES, and RC4 exist; this lecture builds two of them. [[Classical Ciphers]] showed that substitution alone and transposition alone both leak; [[Confusion and Diffusion]] is the resolution. The [[Cipher Security Models|computational security]] model gets its concrete numbers here — 2⁵⁶ is too few, 2¹¹² is enough for now, 2¹²⁸ is 2⁷² times DES. And [[Side-Channel Attacks]] is the mechanism behind Lecture 3's claim that cryptography is rarely the weakest link.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Secret Key Cryptography]]
- [[Block Ciphers]]
- [[Confusion and Diffusion]]
- [[Feistel Cipher]]
- [[DES]]
- [[Triple DES]]
- [[AES]]
- [[Side-Channel Attacks]]
- [[CSCE 465 Lecture 3 — Introduction to Cryptography]]
- [[Cryptanalysis]]
- [[Cryptography]]
- [[Security Design Principles]]
- [[CSCE 465 Lecture 3b — Secret Key Cryptography (II): Modes of Operation]]
