---
title: "CSCE 465 Lecture 3b — Secret Key Cryptography (II): Modes of Operation"
type: source
tags: [csce465, cryptography, modes, cbc, ctr, stream-cipher, css]
sources: []
course: CSCE 465
updated: 2026-09-22
---

Lecture 3b of [[CSCE 465]] (`raw/CSCE465_03b_SecretKeyModes.pdf`, 19 PDF pages laid out two slides per page ≈ 37 logical slides, instructor [[Guofei Gu]]). The second half of secret key cryptography: how to use a block cipher on a message longer than one block, how to get integrity that the modes do not provide, and stream ciphers — closing with a full post-mortem of DVD encryption. Roadmap: *modes of operation*, then *more on stream cipher*.

**This resolves the open question from [[CSCE 465 Lecture 3a — Secret Key Cryptography (I)|Lecture 3a]] about what "(II)" would contain — and resolves it differently than predicted.** The 3a source page guessed 3b would cover modes *and* the AES key schedule. It covers modes; the AES key schedule ("Q2: how are round keys generated?") is **still unanswered** and is not in this deck. Both pages have been corrected.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–4 | **Framing** | Why modes exist; the four evaluation criteria |
| 5–10 | **ECB and CBC** | ECB and its reordering attack; CBC; initialization vectors; CBC properties |
| 11–22 | **Keystream modes** | OFB with the pad-reuse warning; CFB including general k-bit CFB; CTR |
| 23–26 | **Integrity** | MAC/MIC; CBC residue; getting confidentiality *and* integrity |
| 27–33 | **Stream ciphers** | PRNG idea; LFSR; properties; the two structural weaknesses |
| 34–37 | **CSS case study** | CSS design; DeCSS; aftermath; fundamental weakness; AACS; summary |

## Pages Derived

| Page | What it holds |
|---|---|
| [[Block Cipher Modes of Operation]] | The four criteria, all five modes, the comparison table |
| [[Initialization Vector]] | What an IV is, why it is public, why it must never repeat |
| [[Message Authentication Code]] | MAC/MIC, CBC residue, confidentiality + integrity together |
| [[Stream Ciphers]] | PRNG construction, LFSR, properties, the two weaknesses |
| [[Content Scrambling System]] | CSS, DeCSS, the three independent failures, AACS |

## Content Worth Keeping

**Four questions, asked of every mode.** Information leakage; ciphertext manipulation (*assuming the plaintext structure is known* — block 1 is employee #1's salary); parallel processing; error propagation. The checklist is worth more than any individual diagram. → [[Block Cipher Modes of Operation]]

**ECB is broken by a picture, not a proof.** The lecture shows a decryption diagram fed `C1 C4 C3 C2` producing `M1 M4 M3 M2`. No key is learned; the blocks are simply permuted, and the plaintext permutes with them. → [[Block Cipher Modes of Operation]]

**ECB's virtues and its flaw are the same property.** Full parallelism and no error propagation come from block independence, which is exactly what lets an attacker reorder blocks. → [[Block Cipher Modes of Operation]]

**An IV is public but must never repeat under one key.** Both halves matter and students reverse them. → [[Initialization Vector]]

**OFB, CFB, and CTR all make a block cipher behave like a stream cipher.** The "No block decryption required!" note appears on both the OFB and CFB decryption slides, and CTR has the same shape: the cipher generates a pad, the pad is XORed with the plaintext, and decryption runs the cipher *forward*. → [[Block Cipher Modes of Operation]]

**CTR allows decryption at any location** — ideal for random access, and the only mode parallel in both directions. → [[Block Cipher Modes of Operation]]

**No mode provides integrity.** Every one answers "can ciphertext be manipulated profitably?" with some form of yes. → [[Message Authentication Code]]

**CBC residue as a MAC.** Send the plaintext plus only the last CBC block; any change to the plaintext changes the residue. → [[Message Authentication Code]]

**Stream cipher = one-time pad with "random" replaced by "pseudo-random."** 128-bit seed to a 10⁶-bit sequence, with the requirement that *no efficient algorithm can tell this sequence from truly random*. → [[Stream Ciphers]]

**The two XOR weaknesses, with their algebra.** No integrity, from associativity/commutativity; catastrophic keystream reuse, from `X XOR X = 0` — and most plaintexts carry enough redundancy that neither message need be known to recover both. → [[Stream Ciphers]]

**CSS failed three independent ways.** A self-encrypted verification entry that hands the attacker an oracle; one compromised player key breaking every disk ever pressed; and a proprietary 40-bit cipher whose structural flaws left ~16 bits of effective key. → [[Content Scrambling System]]

## The Lecture's Own Summary

- **ECB mode is not secure** — **CBC** is the most commonly used mode of operation.
- **Stream cipher is simple, fast** — key size needs to be large enough; other weaknesses apply.

## Open Questions the Lecture Poses

The pattern holds, and this deck is the most `???`-heavy yet — the property slides for four of the five modes leave entries literally marked `???`. All are answered on the derived pages inside blockquotes marked as derived:

| Question | Answered on |
|---|---|
| ECB: all four property questions | [[Block Cipher Modes of Operation]] — answered by the reordering diagram |
| IV: *why is [changing key or IV changing the ciphertext] useful?* | [[Initialization Vector]] |
| CBC: *how many ciphertext blocks does each plaintext block depend on?* | [[Block Cipher Modes of Operation]] — two, on decryption |
| CBC / OFB / CFB / CTR: *can ciphertext be manipulated profitably?* `???` | [[Block Cipher Modes of Operation]] — targeted bit flips; keystream modes are worst |
| OFB / CFB / CTR: *do ciphertext errors propagate?* `???` | [[Block Cipher Modes of Operation]] — one bit, bounded, one bit |
| OFB: *if a bad guy knows the plaintext and ciphertext, can he send arbitrary (valid) messages?* | [[Block Cipher Modes of Operation]] — yes; `pad = M XOR C` |
| CSS: *what happens if even a single player key is compromised?* | [[Content Scrambling System]] — every disk ever pressed |

## Connection to Earlier Material

The deck closes several loops at once. [[One-Time Pad]]'s key-reuse failure reappears three times — in the OFB pad warning, in the [[Initialization Vector|IV]] rule, and as the second [[Stream Ciphers|stream cipher weakness]] — which is the clearest signal in the course that it was not a historical aside. [[Content Scrambling System|CSS]] was named in one line in Lecture 3 as the [[Security Design Principles|open design]] cautionary tale and is now the full story, including [[Security Assurance|security by legislation]] arriving as the fallback after the technical strategy failed. And the [[Block Ciphers|block cipher]] page's claim that the mode matters as much as the cipher is what this entire lecture demonstrates: the same [[AES]] in ECB and in CTR are not equally secure systems.

## Extraction Note

Text extracted with PyMuPDF. **No image-only slides.**

**The mode diagrams extract as loose label clouds.** Every mode is drawn as a figure — boxes, arrows, and `64` bit-width annotations — and the text layer preserves the labels (`E`, `D`, `IV`, `M1..M4`, `C1..C4`, `46 + padding`) without the wiring. The diagrams on the derived pages were **reconstructed from the labels plus the accompanying property text**, not read off the slide. They are standard and match the named modes, but for exact figure layout the raw slides are authoritative. The `46 + padding` annotation on every diagram's fourth block is the lecture's own example of a partial final block.

Two smaller artifacts: the stream cipher slide's **10⁶** renders as `106` in the text layer (a lost superscript — the seed/expansion example is 128 bits to 10⁶ bits), and the LFSR's `2⁴−1` renders as `24-1`. Both corrected on the derived pages.

One slide carries the **"CSC/ECE 574"** watermark, the same NC State course borrowed from in Lecture 3a.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Block Cipher Modes of Operation]]
- [[Initialization Vector]]
- [[Message Authentication Code]]
- [[Stream Ciphers]]
- [[Content Scrambling System]]
- [[CSCE 465 Lecture 3a — Secret Key Cryptography (I)]]
- [[Secret Key Cryptography]]
- [[Cryptography Taxonomy]]
