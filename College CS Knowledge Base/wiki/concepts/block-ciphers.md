---
title: "Block Ciphers"
type: concept
tags: [csce465, security, cryptography, block-cipher, s-box]
sources: [csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation]
course: CSCE 465
updated: 2026-09-22
---

A block cipher converts **one input plaintext block of fixed size k bits to an output ciphertext block, also of k bits**, under control of a key. Long messages are cut into blocks and each block is processed in turn. This is the dominant form of [[Secret Key Cryptography]], and every cipher [[CSCE 465]] studies in depth — [[DES]], [[Triple DES]], [[AES]] — is one.

```
plaintext:   block 0 | block 1 | block 2 | ...
                |         |         |
            [Encryption, key]  (same key, every block)
                |         |         |
ciphertext:  block 0 | block 1 | block 2 | ...
```

## Block Size

The lecture asks: *benefits of large k? of short k?* — and does not answer.

> **Derived, not stated on the slide.**
> - **Large k** resists **codebook attacks**. With small blocks, an attacker who sees enough ciphertext can build a dictionary of `plaintext block → ciphertext block` pairs and read traffic without ever finding the key. 64-bit blocks (DES) start to leak after about 2³² blocks; 128-bit blocks (AES) do not. Large blocks also give [[Confusion and Diffusion|diffusion]] more room to work.
> - **Short k** is cheaper in hardware, wastes less on padding for short messages, and imposes less latency. It also makes the cipher usable in more modes.
>
> The move from 64 to 128 bits between DES and AES is the field deciding the first consideration wins.

**Padding:** since a message is rarely an exact multiple of the block size, the last block must be padded. (Both DES at 64 bits and AES at 128 bits require it.)

## Encrypting More Than One Block

A block cipher defines only what happens to *one* block. How the blocks are chained is a separate decision — the **[[Block Cipher Modes of Operation|mode of operation]]** — and it matters as much as the cipher. The same [[AES]] used in ECB mode and in CTR mode are not equally secure systems: ECB lets an attacker reorder blocks without touching a key, while CTR is parallel, random-access, and leaks nothing about repeated plaintext. Choosing a strong cipher and then wiring it badly is one of the more common real-world failures.

## Building Blocks

The lecture's list of *everything* DES does — which is also, with one addition, everything any block cipher does:

| Operation | Role |
|---|---|
| **Permutation** | Rearrange bits — [[Confusion and Diffusion\|diffusion]] |
| **Swapping halves** | The [[Feistel Cipher]] structure |
| **Substitution (S-box, table lookup)** | Nonlinear mapping — [[Confusion and Diffusion\|confusion]] |
| **Bit discard** | Shrinking (key schedule, S-box output) |
| **Bit replication** | Expanding (so a 32-bit half meets a 48-bit key) |
| **Circular shift** | Key schedule |
| **XOR** | Mixing in key material; self-inverse |

AES adds finite-field multiplication (MixColumns). Nothing on the list is exotic — the security comes from composition, not from any individual operation.

## S-Boxes

The **S-box is the only nonlinear part** of a cipher like DES, which makes it the only part supplying confusion. Everything else — permutation, XOR, shift — is linear, and a cipher made entirely of linear operations can be solved by linear algebra regardless of how many rounds it has.

An S-box is a table: some number of input bits select an output. In DES, **6 bits in, 4 bits out** — for every output there are four inputs that map to it, so the box also *shrinks*.

The lecture's design principles for S-boxes:
- Each **row** of the S-box table should be a **permutation** of the possible output values (every output appears exactly once per row — no output is favored)
- The output of one S-box should **affect other S-boxes in the following round** (so confusion feeds diffusion)

Row and column selection in DES: the outer two bits pick the row, the inner four pick the column. See [[DES]] for the worked example.

## Hardware vs. Software

The lecture's assessment of DES: *hard to implement? HW: No, SW: Yes.* Bit-level permutations are wiring in hardware and expensive shuffling in software. This was a deliberate DES design criterion — and it is exactly what [[AES]] reversed. AES operates on **bytes**, not bits, so it runs at ~16 cycles/byte on a general-purpose CPU with no special hardware.

## Security Boundary

Block ciphers are evaluated against [[Cryptanalysis|brute force]]: the lecture's summary for DES is that **no attacks are significantly better than brute force, for comparable cost**, and for AES that there are **no known successful attacks on the full cipher**. Both are [[Cipher Security Models|computational security]] claims — they say the algorithm is sound; they say nothing about the implementation. [[Side-Channel Attacks]] are what happens when the implementation is the target instead.

## See Also

- [[Secret Key Cryptography]]
- [[Block Cipher Modes of Operation]]
- [[Confusion and Diffusion]]
- [[Feistel Cipher]]
- [[DES]]
- [[Triple DES]]
- [[AES]]
- [[Side-Channel Attacks]]
- [[Cryptography Taxonomy]]
- [[CSCE 465]]
