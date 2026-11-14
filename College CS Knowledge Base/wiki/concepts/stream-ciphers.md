---
title: "Stream Ciphers"
type: concept
tags: [csce465, security, cryptography, stream-cipher, prng, lfsr, rc4]
sources: [csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation]
course: CSCE 465
updated: 2026-09-22
---

A stream cipher encrypts a message **bit by bit rather than in blocks**, by generating a long pseudo-random keystream from a short key and XORing it with the plaintext. [[CSCE 465]] introduces it as a deliberate weakening of the [[One-Time Pad]]: keep the construction, drop the impossible requirement.

## The Idea: Replace "Random" with "Pseudo-Random"

The one-time pad is `Ciphertext(Key, Message) = Message XOR Key`, where **the key must be a truly random bit sequence as long as the message** — which is why it is unusable in practice.

The stream cipher's move:

> Encrypt with a **pseudo-random number generator (PRNG)**. The PRNG takes a **short, truly random secret seed** and expands it into a long "random-looking" sequence.

```
Ciphertext(Key, Msg) = IV, Msg XOR PRNG(IV, Key)
```

The lecture's example: a **128-bit seed expanded into a 10⁶-bit** pseudo-random sequence. The message is processed **bit by bit, not in blocks**, and the [[Initialization Vector|IV]] is sent alongside the ciphertext.

The security requirement, stated on the slide as a caption:

> **No efficient algorithm can tell this sequence from truly random.**

That is the entire definition of a cryptographic PRNG, and everything the cipher offers rests on it. The one-time pad's security was information-theoretic; the stream cipher's is [[Cipher Security Models|computational]] — the pad only *looks* random to an adversary with bounded resources.

## LFSR — Linear Feedback Shift Register

The lecture's concrete (and deliberately weak) generator. A shift register whose new input bit is the XOR of selected existing bits:

```
4-bit LFSR:   b0 -> b1 -> b2 -> b3
               ^                 |
               +------ XOR <-----+     output bit added to the pseudo-random sequence
```

**The key is used as the seed.** With seed `1001`, the generated sequence is `1001101011110001001…` — and it **repeats after 15 bits (2⁴ − 1)**.

That period is the lesson. An *n*-bit LFSR cycles through at most `2ⁿ − 1` states (all-zeros is a fixed point and excluded), so the keystream repeats after that many bits. Repetition is fatal — see the weaknesses below. A bare LFSR is also **linear**, which is exactly what [[Confusion and Diffusion|confusion]] says a cipher must not be: given a stretch of output, the feedback taps and the state solve by linear algebra. LFSRs appear in real designs only in nonlinear combinations.

## Properties

- **Usually very fast** — faster than [[Block Ciphers|block ciphers]]. Used where speed matters: **WiFi, DVD, RFID, VoIP**.
- **Unlike the one-time pad, stream ciphers do not provide perfect secrecy.** They are **only as secure as the underlying PRNG** — but *if used properly, can be as secure as block ciphers*.
- **Most widely used stream cipher: RC4** — SSL/TLS for web security, WEP for wireless.

The lecture also asserts that *a PRNG is, by definition, unpredictable.* Read that as the requirement rather than a guarantee: it is what a generator must achieve to be cryptographic, and the rest of this page is about generators that did not.

## Two Structural Weaknesses

Both follow from XOR's algebra, and both are stated with the algebra on the slide.

### 1. No Integrity

XOR is associative and commutative: `(X XOR Y) XOR Z = (X XOR Z) XOR Y`. Therefore:

```
(M1 XOR PRNG(seed)) XOR M2  =  (M1 XOR M2) XOR PRNG(seed)
```

An attacker who XORs a chosen value into the ciphertext changes the plaintext by **exactly that value**, with no other effect and no signal that anything happened. Knowing nothing about the key, he can flip any bit he can locate. This is the same gap the [[Block Cipher Modes of Operation|keystream modes]] have, and the reason a [[Message Authentication Code|MAC]] is mandatory rather than optional with any XOR-based cipher.

### 2. Keystream Reuse

XOR self-cancels: `X XOR X = 0`. So if the same keystream encrypts two messages:

```
(M1 XOR PRNG(seed)) XOR (M2 XOR PRNG(seed))  =  M1 XOR M2
```

**If the attacker knows M1, he easily recovers M2.** And the lecture adds the part that makes this devastating rather than merely bad:

> Most plaintexts contain **enough redundancy that knowledge of M1 or M2 is not even necessary** to recover both from `M1 XOR M2`.

Two English texts XORed together are separable by statistical methods (crib-dragging) with neither one known in advance. This is the [[One-Time Pad]]'s key-reuse catastrophe inherited exactly — and it is why the [[Initialization Vector|IV must never repeat]] under a given key. WEP's 24-bit IV, which wraps in hours on a busy network, is the canonical production failure.

## See Also

- [[Content Scrambling System]]
- [[One-Time Pad]]
- [[Block Cipher Modes of Operation]]
- [[Initialization Vector]]
- [[Message Authentication Code]]
- [[Cryptography Taxonomy]]
- [[Cipher Security Models]]
- [[CSCE 465]]
