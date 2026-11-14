---
title: "CSCE 465 Lecture 3 — Introduction to Cryptography"
type: source
tags: [csce465, cryptography, encryption, cryptanalysis, one-time-pad]
sources: []
course: CSCE 465
updated: 2026-09-13
---

Lecture 3 of [[CSCE 465]] (`raw/CSCE465_03_IntroCrypto.pdf`, 15 PDF pages laid out two slides per page = 29 logical slides, instructor [[Guofei Gu]]). The first lecture of the applied cryptography unit, and the first in the course to teach a **mechanism** rather than a framework. It follows a three-part roadmap: basic concepts and definitions, some early (breakable) cryptosystems, and "key" issues.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–13 | **Basic concepts** | Definitions; encryption/decryption pipeline; cryptanalysis and its three attack models; brute force economics; the weakest link; three security models; secret keys vs. secret algorithms |
| 14–23 | **Early ciphers** | Caesar; mono-alphabetic and frequency analysis; permutation ciphers; the one-time pad and Shannon's theorem |
| 24–28 | **"Key" issues** | Taxonomy by key count and by processing; secret key, public key, and hash algorithms |
| 29 | **Summary** | Four closing claims |

## Content Worth Keeping

**The five definitions** — plaintext, ciphertext, encryption, decryption, key — plus the requirement that encryption be **reversible without loss**. → [[Cryptography]]

**Cryptography is not compression.** Usually n bits in, n bits out. They can be combined, and the lecture asks *what's the right order?* without answering. → [[Cryptography]]

**Attack models are about information, not cleverness.** Ciphertext-only, known-plaintext, chosen-plaintext. Difficulty depends on the sophistication of the cipher *and* the amount of information available to the breaker. → [[Cryptanalysis]]

**Brute force is defeated by arithmetic.** 56-bit in a week for $6.7m; 128-bit in a week needs 5.6 × 10²⁶ processors and no price is quoted. → [[Cryptanalysis]]

**Three security models.** Unconditionally secure (`H(p) = H(p|c)`), provably secure (reduces to a supposedly hard problem), computationally secure. Almost every deployed cipher is only the third. → [[Cipher Security Models]]

**Kerckhoffs's principle, as "secret keys vs. secret algorithms."** Publish the algorithm; put the secrecy in the keys. With the commercial/military split as a genuine exception. → [[Cryptography]]

**Early ciphers and how each fails.** Caesar to brute force; mono-alphabetic to frequency analysis *despite* a 2⁸⁸ key space; permutation ciphers preserve letter frequencies entirely. → [[Classical Ciphers]]

**The one-time pad.** Shannon's two requirements, the XOR construction, and why reuse destroys it. → [[One-Time Pad]]

**The two classification axes.** Number of keys (none / one / two → hash / secret key / public key) and how plaintext is processed (stream / block). → [[Cryptography Taxonomy]]

## The Lecture's Own Summary

Four claims, worth keeping as stated:

1. Cryptography is a fundamental, and the most carefully studied, component of security — **and not usually the weak link**.
2. "Perfectly secure" ciphers **are possible**, but too expensive in practice.
3. Early ciphers aren't nearly strong enough.
4. **Key distribution and management is a challenge for any cipher.**

Claims 1 and 4 are the same point from two directions, and together they are the argument for the rest of the course: the mathematics is the part that already works.

## Open Questions the Lecture Poses and Does Not Answer

Four, all answerable, all recorded with derived answers on the concept pages and marked as derived:

| Question | Where answered |
|---|---|
| Compression + encryption — *what's the right order?* | [[Cryptography]] — compress first; ciphertext has no redundancy left |
| Brute force: *when can you recognize if you have succeeded?* | [[Cryptanalysis]] — the recognition problem; why it makes the OTP unbreakable |
| Mono-alphabetic: *how many bits does the key take?* | [[Classical Ciphers]] — log₂(26!) ≈ 88.4, so 89 bits |
| One-time pad: *why can't the key be reused?* | [[One-Time Pad]] — `c1 XOR c2 = p1 XOR p2`; the key cancels |

These read like exam prompts, in the same pattern as [[CSCE 465 Lecture 2 — Security Overview|Lecture 2's]] three unanswered questions.

## Connection Back to Lecture 2

The lecture reuses **"security by obscurity"** verbatim from Lecture 2 and applies it specifically to ciphers — publishing the algorithm and putting secrecy in the keys is the [[Security Design Principles|open design]] principle instantiated. The [[Cipher Security Models|computational security]] model is the **work factor** principle. And [[Cryptography|"cryptography is rarely the weakest link"]] restates Lecture 2's argument that defense is inherently more expensive than offense — the attacker attacks implementation and key management, not the cipher.

The lecture also delivers on Lecture 2's claim that *cryptography underlies many security mechanisms*: [[Security Services]] listed six services, and [[Cryptography Taxonomy]] now names which primitive family supplies each.

## Extraction Note

Text extracted with PyMuPDF. **One genuine visual gap:** slide 17–18 (PDF page 9) carries four images with only 336 characters of text — the **English single-letter frequency histogram** from a large corpus, and the **output of TJ O'Connor's `letter` counting program** run on the Declaration of Independence. Neither the frequencies nor the program output are in the text layer, so the actual distribution is not in the KB.

Minor: the permutation-cipher worked example on slide 20 has its two-row letter grid partially garbled by the text extraction (plaintext and ciphertext rows interleave). The offset vector `<+1,+3,-2,0,-2>` and the plaintext phrase are reliable; the exact per-position output is not, and is flagged as such on [[Classical Ciphers]].

Everything else extracted cleanly. Diagram-supported slides (the encryption/decryption pipeline, the Caesar alphabet mapping, the secret-key and public-key flows, the hash funnel) all carry their content in text.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Cryptography]]
- [[Cryptanalysis]]
- [[Cipher Security Models]]
- [[Classical Ciphers]]
- [[One-Time Pad]]
- [[Cryptography Taxonomy]]
- [[CSCE 465 Lecture 2 — Security Overview]]
- [[Secret Key Cryptography]]
