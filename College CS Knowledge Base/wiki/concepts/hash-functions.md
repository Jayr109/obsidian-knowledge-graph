---
title: "Hash Functions"
type: concept
tags: [csce465, security, cryptography, hash, collision-resistance, one-way]
sources: [csce465-lecture-04-hash-functions, csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

A hash function maps a message of **arbitrary length** to a **fixed-length short** output. [[CSCE 465]] gives it the third family of the [[Cryptography Taxonomy|crypto taxonomy]] — the one with **no key** — and devotes a full lecture to it. Also known as a **message digest**, **one-way transformation**, **one-way function**, or just a **hash**.

```
message of arbitrary length --[Hash]--> fixed-length short message
```

- The length of `H(m)` is **much shorter** than the length of `m`
- Usually a fixed length: **128 or 160 bits**

Having no key is what gives hashing its role: it answers *"has this changed?"* and never *"what does this say?"* It supplies [[CIA Triad|integrity]], not confidentiality — and as the [[Hash Function Applications|applications]] show, adding a secret key to the input turns it into an authentication primitive as well.

## Four Desirable Properties

| Property | Statement |
|---|---|
| **Performance** | Easy to compute `H(m)` |
| **One-way** | Given `H(m)` but not `m`, it is computationally infeasible to find `m` |
| **Weak collision resistance** | Given `H(m)`, it is computationally infeasible to find `m'` such that `H(m') = H(m)` |
| **Strong collision resistance** | It is computationally infeasible to find **any** `m1, m2` such that `H(m1) = H(m2)` |

The weak/strong distinction is the one to get right, and the difference is **who chooses the messages**:

- **Weak** (also called *second preimage resistance*) — the attacker is handed a specific `m` and must find a *different* message with the same digest. Hard.
- **Strong** (*collision resistance*) — the attacker may pick **both** messages freely, and only needs them to collide with each other. Much easier, because the freedom to choose both is exactly what the [[Birthday Attack]] exploits.

Strong collision resistance is therefore the binding constraint. Any hash that resists it resists the weak form too; the converse does not hold. This is why MD5 is considered broken on the strength of *chosen-pair* collisions even though nobody can invert it.

> **Noted during ingest:** the slide annotates both collision properties with a parenthetical "(free)" whose meaning is not clear from the text layer — possibly a lost symbol or an abbreviation. Recorded rather than guessed at; the property statements themselves are unambiguous.

## Why 128 or 160 Bits?

The lecture poses this directly, and answers it by bounding the output from both sides:

- **Too long** → unnecessary overhead
- **Too short** → the **[[Birthday Attack|birthday paradox]]** applies, and **strong collision resistance is lost**

The conclusion the lecture reaches: **choose m ≥ 128 bits.** Because a birthday attack finds a collision in about `2^(m/2)` work, a 128-bit digest gives only 64 bits of collision resistance, and a 160-bit digest gives 80. **The effective security of a hash against collisions is half its output length** — which is why hash digests are conspicuously longer than cipher keys of comparable strength.

## Is Encryption a Good Hash Function?

A natural thought, since [[Block Cipher Modes of Operation|CBC chaining]] already compresses a long message into one final block. The lecture builds exactly that — chain a [[Block Ciphers|block cipher]] over the message with a constant in place of the key — and then lists why it fails:

- **The encryption block size may be too short** (DES is 64 bits) → vulnerable to a [[Birthday Attack|birthday attack]] at only 2³² work
- **A message with a particular hash can be constructed fairly easily** → **[[Triple DES|meet-in-the-middle]]** attack, the same working-from-both-ends technique that defeated Double DES
- **Extension attacks** → see [[HMAC]]

So a dedicated hash function is not just a convenience. The [[Message Authentication Code|CBC residue]] construction from Lecture 3b is usable as a MAC precisely because it carries a secret key; as a *keyless* hash the same structure is too weak.

## The Standards

| Function | Digest | Status per the lecture |
|---|---|---|
| **[[MD5]]** | 128 bits | **Broken** — collisions published August 2004; too weak for serious applications. (MD2 and MD4 had earlier weaknesses.) |
| SHA | 160 bits | Weaknesses were found |
| **[[SHA-1]]** | 160 bits | **"Broken, but not yet cracked"** — collisions in 2⁶⁹ operations vs 2⁸⁰ brute force; circulated February 2005, published at CRYPTO '05 |
| SHA-256, SHA-384, … | 256/384 bits | Named as the successors; not developed in this lecture |

Note what "broken" means in each row: MD5 has *practical* collisions found in hours, while SHA-1's break was a demonstration that the work factor is 2⁶⁹ rather than the 2⁸⁰ its length promises — damaging but not yet cheap. The lecture's phrase *"broken, but not yet cracked"* captures that distinction precisely.

## The Lecture's Summary

- Hashing is **fast to compute**
- It has **many applications**, some making use of a secret key
- Hash images must be **at least 128 bits** long — but longer is better
- Hash function details are **tedious**
- **[[HMAC]] protects message digests from extension attacks**

## Two More Uses of One-Wayness

Lecture 6a leans on the one-way property twice more. **[[Password Authentication|Password storage]]** stores `F(password)` rather than the password, so compromising the file does not reveal the secrets — and it means the system cannot tell you your password, only check it. **[[S/Key Protocol|S/Key]]** iterates the hash into a chain that can be walked forwards to build and only verified backwards, which is what turns one remembered secret into a list of one-time passwords.

## See Also

- [[Birthday Attack]]
- [[Hash Function Applications]]
- [[MD5]]
- [[SHA-1]]
- [[HMAC]]
- [[Message Authentication Code]]
- [[Password Authentication]]
- [[S/Key Protocol]]
- [[Cryptography Taxonomy]]
- [[CIA Triad]]
- [[CSCE 465]]
