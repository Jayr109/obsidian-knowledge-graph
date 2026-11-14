---
title: "Triple DES"
type: algorithm
tags: [csce465, security, cryptography, block-cipher, des, meet-in-the-middle]
sources: [csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

Triple DES answers the question [[CSCE 465]] poses after [[DES]]'s key turns out to be too short: *can we apply DES multiple times to increase the strength of encryption?* The answer is yes — but the obvious way (twice) fails, and the way that works (three times, encrypt-decrypt-encrypt) is shaped entirely by that failure. Most of what this page teaches is the **meet-in-the-middle attack**, which is why doubling a cipher does not double its key strength.

## Double DES, and Why Not

Encrypt twice with two different keys:

```
Encryption:  P --E_K1--> X --E_K2--> C
Decryption:  C --D_K2--> X --D_K1--> P

Observation:  X = E_K1{P} = D_K2{C}
```

Total key material is **112 bits**. The lecture asks: *is that the same as key strength of 112 bits?*

**No.** Two concerns:

### Concern 1 — Is DES a Group?

If DES were a **group** under composition, then for every `K1, K2` there would exist a `K3` with `E_K2(E_K1(P)) = E_K3(P)` for all `P`. Double encryption would collapse to single encryption with some other key — strength 56 bits, not 112. **It was not clear at the time whether DES was a group.** (It is not; this was proven later, in 1992.) But at design time, the possibility alone made multiple encryption suspect.

### Concern 2 — Meet-in-the-Middle

A **known-plaintext attack**, better than brute force. The observation `X = E_K1{P} = D_K2{C}` is the entire attack:

> **The attack, as derived from the lecture's observation (the lecture defers detail to the KPS textbook):**
> 1. Given one known pair `(P, C)`.
> 2. **Encrypt forward:** for all 2⁵⁶ values of `K1`, compute `E_K1{P}` and store `(X, K1)` in a table.
> 3. **Decrypt backward:** for all 2⁵⁶ values of `K2`, compute `D_K2{C}` and look it up in the table.
> 4. A match gives a candidate `(K1, K2)`. Check against a second known pair to eliminate false positives.
>
> **Cost:** about 2⁵⁶ + 2⁵⁶ = **2⁵⁷ operations** and 2⁵⁶ storage — not the 2¹¹² that 112 bits of key material suggests. Double DES buys **one bit** of security over single DES, at twice the cost.

Meet-in-the-middle shows up once more in the course: Lecture 4 names it as a reason **not** to build a [[Hash Functions\|hash function]] out of a block cipher, since a message with a chosen hash can be constructed by working from both ends.

The lesson generalizes: **composing a cipher with itself does not compose its key space**, because the attacker can work from both ends and meet in the middle. Key *material* and key *strength* are different quantities.

## Triple DES-EDE

Apply DES **three times**, as encrypt–decrypt–encrypt, with two keys:

```
Encryption:  P --E_K1--> --D_K2--> --E_K1--> C
Decryption:  C --D_K1--> --E_K2--> --D_K1--> P
```

Three design questions the lecture raises:

**Why not E-E-E?** — Again, it wasn't clear if DES was a group. More practically, the middle **D** gives backward compatibility: set `K1 = K2` and EDE collapses to a single DES encryption (`E_K1 D_K1 E_K1 = E_K1`), so a Triple DES implementation can talk to legacy single-DES systems by choosing keys appropriately. EEE with `K1 = K2` would be triple encryption under one key — not compatible with anything.

**Why not 3 different keys?** — Three keys would give 168 bits of key material, but meet-in-the-middle still applies (split after the first or second stage), capping effective strength at about 2¹¹² — the same as two keys. The third key adds cost without proportionate strength.

**Why not the same key 3 times?** — That is single DES, three times as slow.

### Strength

- **Widely used**, with **equivalent strength to a 112-bit key**
- Against meet-in-the-middle: about **2¹¹⁰** (as stated on the slide)

### Cost

**Inefficient and expensive to compute:** one third as fast as DES on the same platform — and **DES is already designed to be slow in software.** This is the entire motivation for [[AES]]: a cipher that is *both* stronger than Triple DES *and* much faster.

## Summary Table

| | Keys | Key material | Effective strength | Speed vs DES |
|---|---|---|---|---|
| DES | 1 | 56 | 56 | 1× |
| Double DES | 2 | 112 | ~57 (meet-in-the-middle) | ½× |
| Triple DES EDE | 2 | 112 | ~112 | ⅓× |
| Triple DES, 3 keys | 3 | 168 | ~112 | ⅓× |

The middle row is the one to remember: it is the concrete case of *more key does not mean more security* that [[Classical Ciphers|mono-alphabetic ciphers]] illustrated abstractly.

## See Also

- [[DES]]
- [[AES]]
- [[Feistel Cipher]]
- [[Block Ciphers]]
- [[Cryptanalysis]]
- [[Hash Functions]]
- [[Secret Key Cryptography]]
- [[CSCE 465]]
