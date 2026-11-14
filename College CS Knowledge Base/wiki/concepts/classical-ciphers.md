---
title: "Classical Ciphers"
type: concept
tags: [csce465, security, cryptography, caesar-cipher, substitution, transposition]
sources: [csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

The early, breakable ciphers [[CSCE 465]] uses to build intuition. All of them fail, and *how* each one fails is the point — the lecture's summary verdict is that **early ciphers aren't nearly strong enough**. They divide into two families by the operation they perform:

- **Substitution** — replace each symbol with another symbol (Caesar, mono-alphabetic)
- **Permutation / transposition** — keep the symbols, rearrange their positions

## Caesar Cipher

Replace each letter with the one *n* letters later in the alphabet. With n = 3:

```
plaintext  alphabet:  A B C D E F G H I J K ...
ciphertext alphabet:  D E F G H I J K L M N ...

CAT  ->  FDW
```

**Trivial to break** — the lecture says so on the slide. The key is a single number in 0–25, so there are only 25 useful keys. Brute force is 25 trials by hand, and the [[Cryptanalysis|recognition problem]] is easy because English is easy to recognize.

## Mono-Alphabetic Ciphers

The generalization: an **arbitrary but fixed** mapping of one letter to another — any permutation of the alphabet, not just a rotation.

```
26! ≈ 4.0 × 10²⁶ ≈ 2⁸⁸ possible keys
```

The lecture poses a question: *the key must specify which permutation; how many bits does that take?*

> **Answer (derivable, not given on the slide):** log₂(26!) ≈ **88.4 bits**, so 89 bits — matching the slide's own 2⁸⁸ estimate. That is a larger key space than DES's 56 bits, and by the [[Cryptanalysis|brute force table]] it is well out of reach of exhaustive search.

**And it is still broken instantly.** This is the most valuable lesson in the lecture: **a large key space is necessary but not sufficient.** The same lesson returns for [[Password Authentication|passwords]], where 10¹⁸ possibilities coexist with a study finding 86% easily guessed — there the exploitable structure is human rather than mathematical. An 88-bit key buys nothing if the cipher preserves structure the attacker can exploit.

### Frequency Analysis

Mono-alphabetic ciphers are broken by **statistical analysis of letter, word, and phrase frequencies** of the language. Because the mapping is fixed, every occurrence of `E` becomes the same ciphertext letter — so the *distribution* of letters survives encryption unchanged. The attacker matches the ciphertext's frequency profile against English's (E, T, A, O, I, N... most common) and reads off the key.

This is a pure [[Cryptanalysis|ciphertext-only attack]], needing no key guesses at all. And it explains why known-plaintext is described as *"great for monoalphabetic ciphers"* — a single known pair hands over that many entries of the substitution table directly.

> **Visual gap:** the lecture's frequency histogram (single-letter frequencies from a large English corpus) and the output of TJ O'Connor's `letter` counting program run on the Declaration of Independence are **images with no text layer**. The specific frequencies are not recoverable from the PDF.

## Permutation Ciphers

Rather than substituting symbols, **permute (rearrange, transpose) the letters** of the message. The permutation can be fixed, or can change over the length of the message.

The lecture's worked example permutes each successive block of 5 letters by the position offsets `<+1, +3, -2, 0, -2>`:

```
plaintext:   W H Y C A | N T I F L | Y ...
ciphertext:  Y W W O H | C H N A Y | F T Y L I
```

*(The extracted block layout is partially garbled in the PDF text; the offset vector and the plaintext "WHY CAN'T I FLY" are the reliable parts.)*

**What this changes:** a permutation cipher leaves single-letter frequencies **completely untouched** — the ciphertext contains exactly the same letters as the plaintext. So frequency analysis on single letters tells the attacker nothing about the key, though it does immediately reveal that a *transposition* rather than a substitution was used, since the distribution matches plain English too well.

The complementary weakness: transposition destroys digram and trigram structure but preserves letter identity, while substitution destroys letter identity but preserves structure. Neither alone is enough, which is why real block ciphers do **both**, repeatedly — Shannon's [[Confusion and Diffusion]]. Lecture 3a draws the connection explicitly: confusion by substitution, diffusion by permutation, alternating, is the design of [[DES]] and [[AES]].

## Why These Fail — Summary

| Cipher | Key space | Broken by |
|---|---|---|
| **Caesar** | 25 | Trivial brute force |
| **Mono-alphabetic** | 26! ≈ 2⁸⁸ | Frequency analysis — key space is irrelevant |
| **Permutation** | Depends on block size | Preserved letter frequencies reveal the method; anagramming recovers the rest |

The through-line: every one of these leaks **structure**. The [[One-Time Pad]] is the cipher that leaks none, and the next section of the lecture explains what that costs.

## See Also

- [[Cryptanalysis]]
- [[Confusion and Diffusion]]
- [[One-Time Pad]]
- [[Cryptography]]
- [[Cipher Security Models]]
- [[CSCE 465]]
