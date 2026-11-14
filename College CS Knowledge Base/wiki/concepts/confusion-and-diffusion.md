---
title: "Confusion and Diffusion"
type: concept
tags: [csce465, security, cryptography, shannon, cipher-design, avalanche]
sources: [csce465-lecture-03a-secret-key-cryptography-i]
course: CSCE 465
updated: 2026-09-13
---

Shannon's two principles for cipher design, and the reason every modern [[Block Ciphers|block cipher]] looks the way it does. [[CSCE 465]] presents them as the answer to a question [[Classical Ciphers]] raised: substitution alone leaks (frequency analysis), transposition alone leaks (letter identities survive) — so what does *not* leak?

## The Two Principles

**Confusion** — make the relationship between the `<plaintext, key>` input and the `<ciphertext>` output **as complex (non-linear) as possible.** An attacker who knows the ciphertext should not be able to write down simple equations relating it to the key.

**Diffusion** — **spread the influence of each input bit across many output bits.** A change to one plaintext bit should not stay localized; it should propagate until it has touched a large fraction of the output.

## How They Are Achieved

| Principle | Mainly accomplished by |
|---|---|
| **Confusion** | **Substitutions** (S-boxes — nonlinear table lookups) |
| **Diffusion** | **Permutations** (P-boxes — bit rearrangement) |

The idea is to use **multiple, alternating** permutations and substitutions:

```
S -> P -> S -> P -> S -> ...
P -> S -> P -> S -> P -> ...
```

The lecture asks: *do they have to alternate?* — e.g. `S -> S -> S -> P -> P -> P -> S -> S -> ...`?

> **Derived, not stated on the slide.** Adjacent operations of the same kind collapse. Two permutations in a row compose into a single permutation; two substitutions in a row compose into a single (different) substitution. `S -> S -> S` is just one S-box with a different table, and `P -> P -> P` is one permutation. So a run of same-type operations costs three rounds' worth of work and buys one round's worth of mixing. Alternation is what makes each round add something the previous round did not.

Example ciphers built this way: [[DES]], [[AES]].

## The Basic Form of a Modern Block Cipher

```
plaintext -> S -> P -> S -> P -> S -> ... -> ciphertext
              ^         ^         ^
              key material feeds each stage
```

More precisely, the lecture's generic template:

```
Plaintext block
      |
 Preprocessing
      |
 Rounds of Encryption  i = 1, 2, ..., n     <-- Sub-Key #i from Sub-Key Generation
      |
 Postprocessing
      |
Ciphertext block
```

A **key schedule** derives one **sub-key** (round key) per round from the master key. Each round mixes its sub-key with the state and applies substitution and permutation. Preprocessing and postprocessing are typically fixed permutations. [[Feistel Cipher|Feistel ciphers]] and [[AES]] are two different ways of filling in this template.

## Avalanche Effect

The measurable consequence of good diffusion.

**Roughly:** a small change in either the plaintext or the key should produce a **big change** in the ciphertext.

**Better (the precise version):** any output bit should be inverted with **probability 0.5** if any input bit is changed. Half the output bits flipping is the target, not "many" — if *all* bits flipped, that would itself be a pattern.

For the round function `f` of a cipher this means:
- It must be difficult to un-scramble
- It should achieve the avalanche effect
- Output bits should be **uncorrelated**

### DES Avalanche Example

Two plaintexts differing in **one bit** — `0x0000000000000000` and `0x8000000000000000` — encrypted under the same key `0x016B24621C181C32`, produce ciphertexts differing in **34 bits out of 64**. Similar results when the *keys* differ by one bit.

The lecture's round-by-round experiment, tracking how many bits differ after each round:

| Round | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| **Bits changed** | 1 | 6 | 21 | 35 | 39 | 34 | 32 | 31 | 29 |

| Round | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|
| **Bits changed** | 42 | 44 | 32 | 30 | 30 | 26 | 29 | 34 |

Read it as diffusion happening in real time. One bit becomes 6, then 21, then 35 — full avalanche is reached by **round 3 or 4**, after which the count oscillates around 32 (half of 64), which is exactly the probability-0.5 target. The remaining twelve rounds are not for diffusion; they are the security margin against attacks that can peel off a few rounds. That is why [[AES]]'s "best attacks work on 7–9 rounds out of 10–14" is a reassuring statement rather than an alarming one.

## Why This Matters

Confusion and diffusion are what [[Classical Ciphers]] lacked. A mono-alphabetic cipher has confusion of a sort (an arbitrary table) but zero diffusion — each output letter depends on exactly one input letter, so statistics pass straight through. A permutation cipher has diffusion of a sort but zero confusion — the mapping is linear and the letter identities survive. Alternating the two, many times, keyed differently each round, is the entire design of modern symmetric cryptography.

## See Also

- [[Block Ciphers]]
- [[Feistel Cipher]]
- [[DES]]
- [[AES]]
- [[Classical Ciphers]]
- [[Secret Key Cryptography]]
- [[CSCE 465]]
