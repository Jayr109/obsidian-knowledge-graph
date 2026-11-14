---
title: "Birthday Attack"
type: concept
tags: [csce465, security, cryptography, hash, birthday-paradox, collisions]
sources: [csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

The birthday attack is the reason [[Hash Functions|hash digests]] are 128 bits or longer rather than 64. It is a counting argument, not a cryptanalytic one: **finding *some* collision in a hash function is far cheaper than finding a collision with a *specific* message**, and the gap is a square root. [[CSCE 465]] develops it from the classic birthday puzzle.

## The Paradox

> What is the smallest group size `k` such that the probability that at least two people share a birthday exceeds 0.5? (365 days, all birthdays equally likely.)

Let `Q(365,k)` be the probability that `k` people have `k` *different* birthdays, and `P(365,k)` the probability that at least two collide:

```
Q(365,k) = 365! / ((365-k)! · 365^k)

P(365,k) = 1 - Q(365,k)  >=  0.5
```

**k is about 23.**

> **Verified during ingest:** P(22) = 0.4757, P(23) = 0.5073. Twenty-three is the exact threshold.

It feels wrong because intuition answers a different question. The chance that someone shares *your* birthday in a group of 23 really is small (~6%). The question asked is whether *any pair* collides — and there are C(23,2) = 253 pairs, not 22. **Pairs grow quadratically in the group size**, which is the whole engine of the attack.

## The Generalization

Given a random integer uniform on `1..n` and `k` draws, the smallest `k` giving at least one duplicate with probability > 0.5 is:

```
k = sqrt(2 ln2 · n) = 1.18 · sqrt(n)  ~  sqrt(n)
```

> **Verified:** √(2 ln 2) = 1.1774, and 1.18·√365 = 22.54 — matching both the constant and the worked example on the slide.

The shape is what matters: **`k` grows as the square root of the space**, not linearly. Doubling the space buys only a 1.41× increase in the work needed to collide inside it.

## The Implication for Hash Functions

For a hash function `H` with output length `m` bits, the output space is `n = 2^m`, so:

> Hashing about **2^(m/2)** random inputs produces two messages with the same hash image, with probability at least 0.5.

That is the **birthday attack**. It requires no weakness in the hash at all — only the ability to compute it and store results.

| Digest length `m` | Work for a 50% collision |
|---|---|
| 64 bits | 2³² |
| **128 bits** | **2⁶⁴** |
| **160 bits** | **2⁸⁰** |

**Conclusion from the lecture: choose m ≥ 128.**

The two numbers in that table are exactly the figures the lecture quotes elsewhere as the brute-force cost of [[MD5]] (2⁶⁴) and [[SHA-1]] (2⁸⁰) — so when the deck says SHA-1 is stronger because brute force needs 2⁸⁰ rather than 2⁶⁴, it is quoting the birthday bound, not an exhaustive search of the digest space.

## Why This Governs Collision Resistance Specifically

The attack needs the freedom to choose **both** messages, so it bears on [[Hash Functions|strong collision resistance]] and not on the weak form:

- **Strong collision resistance** — attacker picks both `m1` and `m2`. Birthday attack applies. Effective security: `m/2` bits.
- **Weak collision resistance** — `m` is fixed by someone else, so the attacker is searching for a preimage of one specific digest and the birthday shortcut is unavailable. Effective security: `m` bits.

**So a hash function's collision resistance is half its output length while its preimage resistance is the full length.** That asymmetry is why digests are sized generously compared with cipher keys: a 128-bit key gives 128 bits of security, but a 128-bit digest gives only 64 against collisions.

## Where It Shows Up in the Course

- It is why a [[Hash Functions|block cipher used as a hash]] fails — DES's 64-bit block collides at 2³², which is trivially reachable.
- It is the baseline that makes [[MD5]]'s and [[SHA-1]]'s real breaks notable: MD5 collisions were found by **differential analysis in 8 hours on a 1.6 GHz machine**, *much faster than the birthday attack*, and SHA-1's 2⁶⁹ is well below its 2⁸⁰ birthday bound. The attack is the bar a hash must clear, and both failed to clear it.

## See Also

- [[Hash Functions]]
- [[MD5]]
- [[SHA-1]]
- [[Cryptanalysis]]
- [[Cipher Security Models]]
- [[CSCE 465]]
