---
title: "HMAC"
type: algorithm
tags: [csce465, security, cryptography, hash, hmac, extension-attack, mac]
sources: [csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

HMAC (Hashed Message Authentication Code) is the standard way to build a [[Message Authentication Code|MAC]] out of a [[Hash Functions|hash function]]. [[CSCE 465]] introduces it by first showing what breaks without it: the **extension attack**, which lets an attacker forge a valid digest for a message they have never seen the key for.

The lecture's closing summary states its purpose in one line: **HMAC protects message digests from extension attacks.**

## The Extension Attack

The naive keyed hash — the construction the [[Hash Function Applications|message authentication application]] actually uses — is `H(K | M | padding)`. It looks sound: without `K` you cannot compute it. But:

> Given `M1`, `M2`, and `H(K|M1|padding)`, it is easy to compute
> ```
> H(K | M1 | padding | M2 | newpadding)
> ```
> **Simply use `H(K|M1|padding)` as the IV for computing the hash of `M2|newpadding`** — and this **does not require knowing the value of the secret key K.**

That is the whole attack, and it is a direct consequence of the [[MD5|Merkle–Damgård]] structure both MD5 and [[SHA-1]] use. The chaining variable *is* the complete state carried between blocks: nothing about the earlier message survives except the running digest. So a digest is not an endpoint — **it is a resumable intermediate state**. An attacker who holds one can keep hashing from there.

**Why this is a real forgery.** The attacker produces a valid authenticator for `M1 | padding | M2`, a message the key holder never authorized, having only observed a legitimate `(M1, tag)` pair. They never learn `K` and never need to. Appending to a message is often enough to change its meaning entirely — `"transfer $10 to Bob"` extended with `"...and $10000 to Eve"`.

Note the lecture already flagged extension attacks as a reason [[Hash Functions|encryption makes a poor hash]]. This is where that bullet gets cashed out.

## The Fix

> Many proposed solutions to the extension attack, but **HMAC is the standard.**
>
> **Essence: digest-inside-a-digest, with the secret used at both levels.**
>
> The particular hash function used determines the length of the message digest = length of HMAC output.

Nesting is what defeats the attack. The attacker's extension trick needs the *output* digest to be a usable intermediate state — but in HMAC the value that gets published is the result of a **second, outer** hash whose input the attacker cannot control or extend. The inner digest is never exposed, so there is nothing to resume from.

That the output length equals the underlying hash's digest length is worth noting: HMAC-MD5 gives 128 bits, HMAC-SHA-1 gives 160. HMAC is a *construction*, not an algorithm — it takes a hash as a parameter.

## HMAC Processing

```
Key K ── pad on right with 0's to 512 bits ──┐
                                             │
                            ┌────────────────┴──┐
                            │                   │
                   XOR 0x3636…36        XOR 0x5c5c…5c
                            │                   │
                 concatenate Message M          │
                            │                   │
                 compute message digest         │
                            └─── concatenate ───┤
                                                │
                                      compute message digest
                                                │
                                      HMAC(key, message)
```

In the lecture's terms:

1. Pad `K` on the right with zeros to **512 bits** (one block of the underlying hash)
2. XOR the padded key with **0x36** repeated — the *inner pad*
3. Concatenate the message `M` and **compute the message digest**
4. XOR the padded key with **0x5c** repeated — the *outer pad*
5. Concatenate the inner digest from step 3 and **compute the message digest** again

The result is `HMAC(key, message)`.

**The two pad constants are different on purpose.** 0x36 and 0x5c differ in half their bits, so the inner and outer keys are effectively two *distinct* keys derived from one — which is the same discipline [[Message Authentication Code|the P+I construction]] applies by demanding separate keys for encryption and authentication: never reuse one key for two jobs. Here the derivation is free, done with an XOR.

Padding the key to a full block means the key-mixing costs exactly one extra compression-function call at each level, so HMAC runs at roughly the cost of hashing the message plus two blocks.

## Where It Sits Among the MACs

The KB now has two MAC constructions from the course, built on different primitives:

| Construction | Built from | Source |
|---|---|---|
| **CBC residue** | A [[Block Ciphers\|block cipher]] in [[Block Cipher Modes of Operation\|CBC mode]] — send the plaintext plus the last ciphertext block | Lecture 3b |
| **HMAC** | A hash function, nested, with the key at both levels | Lecture 4 |

Both give [[CIA Triad|data integrity]] and authentication under a shared key, and **neither gives non-repudiation** — a third party cannot tell which key holder produced the tag. For that you need a [[Digital Signatures|digital signature]]. HMAC is the one that dominates in practice, because hashing is much cheaper than block encryption and because the construction has a security proof reducing to properties of the underlying hash.

## See Also

- [[Hash Functions]]
- [[Message Authentication Code]]
- [[MD5]]
- [[SHA-1]]
- [[Hash Function Applications]]
- [[Digital Signatures]]
- [[Block Cipher Modes of Operation]]
- [[CSCE 465]]
