---
title: "Cryptanalysis"
type: concept
tags: [csce465, security, cryptography, cryptanalysis, brute-force]
sources: [csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03a-secret-key-cryptography-i]
course: CSCE 465
updated: 2026-09-13
---

Cryptanalysis is *code breaking* — attacking the cipher. [[CSCE 465]] frames its difficulty along two axes, and the second is the one students underrate:

1. The **sophistication of the cipher**
2. The **amount of information available to the code breaker**

That second axis is why attacks are classified by *what the attacker gets to see*, not by how clever they are. A weak cipher may survive a ciphertext-only attack and fall instantly to a chosen-plaintext one.

## The Recognition Problem

**Any cipher can be broken by exhaustive trials**, but rarely practically. The lecture attaches a question to that claim which is easy to skip past:

> *When can you recognize if you have succeeded?*

Brute force is not just "try every key" — it is "try every key **and know when to stop.**" That requires a way to distinguish plaintext from garbage, which means the attack needs either enough ciphertext for statistical structure to appear, or a known property of the message. A short random-looking message encrypted with a short key can be undecidable in principle: several keys may produce plausible outputs, with nothing to choose between them. This is precisely what makes the [[One-Time Pad]] unbreakable rather than merely expensive to break.

## The Three Attack Models

| Model | What the attacker has | Why it matters |
|---|---|---|
| **Ciphertext only** | Only intercepted ciphertext | Weakest position. Exhaustive search until "recognizable plaintext" — needs *enough* ciphertext for recognition to work |
| **Known plaintext** | A `<ciphertext, plaintext>` pair, revealed by a spy or by the passage of time | *Great for monoalphabetic ciphers* — the pair directly exposes part of the substitution table |
| **Chosen plaintext** | The attacker picks text and gets it encrypted | Useful when there is a limited set of possible messages — encrypt them all, compare |

The progression is one of increasing attacker power. Modern ciphers are expected to resist all three (and more), which is why "it survived a ciphertext-only attack" is not a security claim.

Note how the models map onto real access: known-plaintext arises from *disclosure over time* (yesterday's secret is today's public record), and chosen-plaintext arises whenever an attacker can submit input to a system that encrypts it — a far more common position than it sounds.

## Brute Force Economics

The lecture's numbers, which date the deck but make the scaling vivid. Baseline assumption: **1 million to 1 billion encryptions per second** per processor.

| Key size | Time | Processors | Cost |
|---|---|---|---|
| 56-bit | 1 week | 120,000 | $6.7m |
| 56-bit | 1 month | 28,000 | $1.6m |
| 64-bit | 1 week | 3.1 × 10⁷ | $1.7b |
| 128-bit | 1 week | 5.6 × 10²⁶ | — (no cost given) |

The last row has no price because there is no price. Each additional key bit **doubles** the work, so the 72-bit gap from 56 to 128 is a factor of roughly 4.7 × 10²¹. The table's real lesson is that brute force is defeated by arithmetic, not by cleverness — and correspondingly, that a cipher with an adequate key length is never broken by brute force in practice. It is broken somewhere else.

Which is the setup for the lecture's next claim: [[Cryptography|cryptography is rarely the weakest link]]. Implementation flaws and key management are.

## Two Attacks That Are Not Brute Force

Lecture 3a supplies the first concrete attacks better than exhaustive search:

- **Meet-in-the-middle** — a known-plaintext attack on double encryption. Working from both ends at once, it breaks Double [[DES]] in about 2⁵⁷ work instead of the 2¹¹² its key material suggests. The general lesson: composing a cipher with itself does not compose its key space. See [[Triple DES]].
- **[[Side-Channel Attacks]]** — timing and power analysis recover keys from the *implementation*, bypassing the algorithm entirely. They break the assumption every attack model above makes: that the attacker sees only inputs and outputs.

## See Also

- [[Cryptography]]
- [[Classical Ciphers]]
- [[Triple DES]]
- [[Side-Channel Attacks]]
- [[Cipher Security Models]]
- [[One-Time Pad]]
- [[CSCE 465]]
