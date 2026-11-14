---
title: "MD5"
type: algorithm
tags: [csce465, security, cryptography, hash, md5, merkle-damgard]
sources: [csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

MD5 (Message Digest version 5) produces a **128-bit digest** from a message of arbitrary length. [[CSCE 465]] walks through it as the worked example of how a [[Hash Functions|hash function]] is actually built — and then shows that it is **broken**: collisions were published in August 2004 and it is *too weak to be used for serious applications*. Its predecessors MD2 and MD4 had their own weaknesses.

It is still worth the detail, because the structure MD5 introduced is the structure [[SHA-1]] uses too.

## The Compression Function

The whole design reduces to one fixed-size function applied repeatedly:

```
128-bit input digest (four 32-bit words)   ┐
                                          ├─[ MD5 ]─> 128-bit output digest
512-bit message block (sixteen 32-bit words) ┘
```

That is called a **compression function**: it takes 640 bits in and gives 128 out. Everything else is bookkeeping to feed it.

## High-Level Structure

```
Message | 100…0 | message length (K mod 2^64)
         padding: 1 to 512 bits
         |
split into 512-bit blocks Y0, Y1, ..., YL-1
         |
IV ──[MD5]── CV1 ──[MD5]── CV2 ── … ──[MD5]──> 128-bit digest
      Y0           Y1                   YL-1
   stage 1      stage 2              stage L
```

The message is padded with a 1 followed by zeros, then the original length modulo 2⁶⁴ is appended; padding is **1 to 512 bits** (never zero — there is always at least one bit of padding). Blocks are then chained: each stage's output digest becomes the next stage's input digest, starting from a fixed **IV**.

This chaining construction is **Merkle–Damgård**, and the fact that the running digest *is* the entire state carried between blocks is exactly what makes [[HMAC|extension attacks]] possible. Nothing else about the message survives from one block to the next, so an attacker holding `H(message)` holds a valid intermediate state.

## Notation

| Symbol | Meaning |
|---|---|
| `~x` | bit-wise complement of x |
| `x∧y`, `x∨y`, `x⊕y` | bit-wise AND, OR, XOR |
| `x<<y` | left **circular** shift of x by y bits |
| `x+y` | arithmetic sum, discarding carry-out from the msb |
| `⌊x⌋` | largest integer ≤ x |

Note `<<` here is a *rotation*, not a logical shift, and `+` is addition mod 2³². Both matter: rotation and modular addition are the only nonlinear-over-GF(2) operations in the design, and they are what stop the whole function from being solvable as a linear system.

## Processing a Block

Each message block `Yi` holds 16 32-bit words `m0 … m15`. A block is processed in **4 consecutive passes**, each modifying the MD5 buffer (the digest) `d0, d1, d2, d3`. The passes are called **F, G, H, I**.

```
Input digest CVi (128 bits)
   |
   ├─ 1st pass: F, T[1..16],  Yi ──┐ +
   ├─ 2nd pass: G, T[17..32], Yi ──┤ +
   ├─ 3rd pass: H, T[33..48], Yi ──┤ +
   └─ 4th pass: I, T[49..64], Yi ──┘ +
   |
Output digest CVi+1 = input digest + output of 4th pass
```

Each pass uses one quarter of a **64-element table of constants** `T[1…64]`:

```
T[i] = ⌊ 2^32 · |sin(i)| ⌋ ,  represented in 32 bits
```

> **Verified during ingest:** T[1] = 3614090360 = `0xD76AA478`, T[2] = `0xE8C7B756`, T[64] = `0xEB86D391` — these match the published MD5 constants exactly, so the formula on the slide is the real one. Using `sin` is a "nothing-up-my-sleeve" choice: the constants are arbitrary-looking but verifiable by anyone, so nobody can claim a backdoor was hidden in them. The same reasoning as [[Cryptography|Kerckhoffs's principle]] applied to magic numbers.

**The final addition matters.** `output = input digest + output of 4th pass` — feeding the input forward and adding it is what makes the compression function non-invertible. Without it you could run the passes backwards.

## The Four Pass Functions

```
F(x,y,z) = (x∧y) ∨ (~x∧z)
G(x,y,z) = (x∧z) ∨ (y∧~z)
H(x,y,z) = x ⊕ y ⊕ z
I(x,y,z) = y ⊕ (x∨~z)
```

**Every pass has 16 processing steps** (4 passes × 16 = 64 steps per block), each involving one of these functions and a circular shift.

Note `F` is a bitwise *multiplexer* — it selects `y` where `x` is 1 and `z` where `x` is 0. `H` is pure XOR and therefore linear; the design relies on the other three for nonlinearity, which is the same division of labour as [[Confusion and Diffusion|S-boxes versus permutations]] in a block cipher.

## Logic of Each Step

```
      d0        d1        d2        d3
       |         |         |         |
       |      g(d1,d2,d3) <─── g: F, G, H, or I
       +<──────────┘
       +<─── m_k        (one message word)
       +<─── T[i]       (one table constant)
      <<s               (circular shift)
       +<─── d1
       |
      new d1 ; the other words rotate position
```

Each step mixes in **one message word and one table constant**, rotates, and adds. Over 64 steps every message word is used four times — once per pass — in a different order each time, which is how a one-bit change in the message reaches all 128 output bits.

## (In)security

MD5 is thoroughly broken, and the lecture is specific about how:

- **A few recently discovered methods find collisions in a few hours**
- A few collisions were published in **2004**; many collisions can be found for **1024-bit messages**; more discoveries followed
- In **2005, two X.509 certificates with different public keys and the same MD5 hash were constructed**
- The method is based on **differential analysis**
- **8 hours on a 1.6 GHz computer**
- **Much faster than a [[Birthday Attack|birthday attack]]**

Two things to take from that list. First, the attack beats the birthday bound — MD5's 128-bit digest should have cost 2⁶⁴ to collide, and differential analysis got it to hours on one desktop, so this is a genuine structural break, not just a short digest. Second, the **colliding X.509 certificates** are why this mattered in practice: two certificates with the *same signature* but *different public keys* means a signature on the benign one is equally valid on the malicious one. That is [[Public Key Infrastructure|PKI]] broken at the hash layer, and it is the same shape as the [[Public Key Infrastructure|Comodo]] failure — a correct signature over a statement nobody intended.

## See Also

- [[Hash Functions]]
- [[SHA-1]]
- [[HMAC]]
- [[Birthday Attack]]
- [[Hash Function Applications]]
- [[Public Key Infrastructure]]
- [[Confusion and Diffusion]]
- [[CSCE 465]]
