---
title: "SHA-1"
type: algorithm
tags: [csce465, security, cryptography, hash, sha, nist]
sources: [csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

SHA-1 is the Secure Hash Algorithm, producing a **160-bit digest**. Developed by **NIST** and specified in the Secure Hash Standard (1993); SHA-1 is the **revised 1995 version** of the original SHA, which had weaknesses. It is specified as the hash algorithm in the **Digital Signature Standard (DSS)**. [[CSCE 465]] presents it immediately after [[MD5]], and the comparison is the point — SHA-1 is the same construction with more of everything.

Its status per the lecture: **"broken, but not yet cracked."**

## Parameters

| | |
|---|---|
| **Input message** | Must be **< 2⁶⁴ bits** |
| **Block size** | 512 bits, with **the same padding as MD5** |
| **Digest** | **160 bits** — five 32-bit words `A, B, C, D, E` |
| **Steps per block** | **80** (vs 64 for MD5) |
| **Byte order** | Words stored **big-endian** |

**Initialization vector:**

```
A = 0x67452301
B = 0xEFCDAB89
C = 0x98BADCFE
D = 0x10325476
E = 0xC3D2E1F0
```

The first four are MD5's IV words — SHA-1 reuses them and adds a fifth. The `< 2⁶⁴ bits` limit exists because the padding appends the message length in a 64-bit field, the same as MD5.

## Message Schedule (Preprocessing)

Each 512-bit block is sixteen 32-bit words `W0..W15`. These are **expanded into eighty** words:

```
for 16 <= t <= 79:
    W_t = (W_{t-16} XOR W_{t-14} XOR W_{t-8} XOR W_{t-3}) << 1
```

(`<<` is a circular shift, per the [[MD5|shared notation]].)

This is the structural difference from MD5, and it is where SHA-1's extra strength comes from. MD5 feeds each of its 16 message words directly into four steps. SHA-1 instead **derives 64 additional words by XOR-mixing earlier ones**, so a single changed input bit propagates into many schedule words before processing even begins. The one-bit rotation is what the 1995 revision added to the original SHA — without it the expansion has a weakness.

## Block Processing

**80 steps.** Inputs to each step `0 ≤ t ≤ 79`:

- `W_t` — the scheduled message word
- `K_t` — a round constant
- `A, B, C, D, E` — current values

Outputs: new `A, B, C, D, E`. **The output of the last step is added to the input of the first step** to produce the 160-bit digest — the same feed-forward addition that makes [[MD5|MD5's compression function]] non-invertible.

### The Round Function f(t, B, C, D)

Three different functions across four rounds of 20 steps:

| Round | `f(t,B,C,D)` | MD5 equivalent |
|---|---|---|
| 0 ≤ t ≤ 19 | `(B∧C) ∨ (~B∧D)` | `F = (x∧y) ∨ (~x∧z)` |
| 20 ≤ t ≤ 39 | `B ⊕ C ⊕ D` | `H = x ⊕ y ⊕ z` |
| 40 ≤ t ≤ 59 | `(B∧C) ∨ (B∧D) ∨ (C∧D)` | — (majority function; new) |
| 60 ≤ t ≤ 79 | `B ⊕ C ⊕ D` | `H = x ⊕ y ⊕ z` |

**SHA-1 makes no use of MD5's `G` or `I`.** It keeps the multiplexer (`F`) and XOR (`H`), drops the other two, and adds a **majority** function for rounds 40–59. Note that rounds 1 and 3 use the *same* function — SHA-1 has four rounds but only three distinct functions.

### Processing Per Step

*Everything to the right of "=" is the input value to this step* — the assignments happen simultaneously, not sequentially:

```
for t = 0 upto 79:
    A = E + (A << 5) + W_t + K_t + f(t,B,C,D)
    B = A
    C = B << 30
    D = C
    E = D
endfor
```

That simultaneity caveat is load-bearing. Read sequentially the code is wrong — `B = A` would use the just-updated `A`. Read as a parallel assignment, the five words shift down one position while the new `A` absorbs everything: the old `E`, a 5-bit rotation of the old `A`, the message word, the round constant, and the round function of `B, C, D`. The `C = B << 30` is the only rotation applied during the shuffle, and it is what keeps the five words from being a plain rotation of each other.

## Comparison with MD5

| | MD5 | SHA-1 |
|---|---|---|
| Digest | 128 bits | **160 bits** |
| Steps per block | 64 | **80** |
| Distinct round functions | 4 (F, G, H, I) | 3 (F, XOR, majority) |
| Message schedule | 16 words used 4× each | **16 words expanded to 80** |
| Brute-force work | 2⁶⁴ | **2⁸⁰** |
| Speed | — | **about twice as expensive** |

The lecture's verdict: **SHA-1 is a stronger algorithm** — brute force requires on the order of 2⁸⁰ operations versus 2⁶⁴ for MD5 — and **about twice as expensive to compute**. But **both MD5 and SHA-1 are much faster to compute than [[DES]]**, which is why hashing is cheap enough to apply to every message in a protocol.

Those two work figures are the [[Birthday Attack|birthday bounds]] for 128- and 160-bit digests (2^(m/2)), not exhaustive searches of the digest space.

## Security

- **"Broken", but not yet cracked**
- Collisions in **2⁶⁹ hash operations**, much less than the brute-force attack of **2⁸⁰**
- Results **circulated in February 2005**, published at **CRYPTO '05 in August 2005**
- Successors named: **SHA-256, SHA-384, …**

The distinction from [[MD5]] is worth holding precisely. MD5's break is *practical* — real colliding X.509 certificates, eight hours on one desktop. SHA-1's break at the time of this deck was a **demonstration that the work factor is 2⁶⁹ rather than the 2⁸⁰ its length promises** — an 11-bit reduction, enough to call the algorithm broken as a matter of theory while still being far out of reach of a casual attacker. Hence "broken, but not yet cracked." (A practical SHA-1 collision was eventually produced, in 2017's SHAttered — after this deck's framing was written.)

## See Also

- [[Hash Functions]]
- [[MD5]]
- [[HMAC]]
- [[Birthday Attack]]
- [[Digital Signatures]]
- [[DES]]
- [[CSCE 465]]
