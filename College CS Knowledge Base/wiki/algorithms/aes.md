---
title: "AES"
type: algorithm
tags: [csce465, security, cryptography, block-cipher, aes, rijndael]
sources: [csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation]
course: CSCE 465
updated: 2026-09-22
---

AES, the **Advanced Encryption Standard**, is the **Rijndael** algorithm (pronounced "Rhine-dall"), selected from an **open competition** and standardized as the replacement for [[DES]]. [[CSCE 465]]'s summary is that AES is *even better* than [[Triple DES]] — **stronger and much faster** — and the "much faster" is not incidental: the whole point of the design was to be secure *and* efficient in software, where DES was deliberately slow.

Main selection criteria: **secure, well justified, fast.** The "well justified" is the [[Cryptography|open design]] principle applied to the competition itself — every candidate's rationale was public.

## Parameters

| | |
|---|---|
| **Block size** | **128 bits** (fixed) |
| **Key sizes** | **128, 192, or 256 bits** — variable |
| **Rounds** | 10 (AES-128), 12 (AES-192), 14 (AES-256) |
| **Structure** | Rounds, round keys, alternating permutation and substitution — **but not a [[Feistel Cipher]]** |

The block doubled from DES's 64 bits (see [[Block Ciphers]] for why that matters), and the key is more than double. Padding is necessary for messages not a multiple of 16 bytes.

## Top-Level Structure (AES-128)

```
128-bit input
    |
   XOR <-- 128-bit K0        (pre-whitening)
    |
Round 1   <-- 128-bit K1
Round 2   <-- 128-bit K2
  ...
Round 10  <-- 128-bit K10    (last round omits MixColumns)
    |
128-bit output
```

The lecture poses two questions about this diagram: *Q1: what happens in each round?* and *Q2: how are round keys generated?* It answers Q1 and leaves Q2 (the key expansion) for later.

## The State

Each 16-byte plaintext block is arranged as a **4 × 4 array of bytes**, filled **column by column**:

```
input bytes:  a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15

state:        a0   a4   a8   a12
              a1   a5   a9   a13
              a2   a6   a10  a14
              a3   a7   a11  a15
```

Every round operation is defined on this grid — on its bytes, its rows, or its columns. Working on **bytes** rather than bits is the structural reason AES is fast in software.

## One Round of AES-128

Three transformations, then the round key:

**1. SubBytes** — apply the **S-box function to each byte** of the state: 16 independent substitutions. This is the nonlinear step, supplying [[Confusion and Diffusion|confusion]]. Unlike DES's eight different 6→4 S-boxes, AES has one 8→8 S-box, algebraically defined (inversion in GF(2⁸) followed by an affine map).

**2. ShiftRows** — rotate each row of the state left:
- Row 0: **unchanged**
- Row 1: left by **1** column
- Row 2: left by **2** columns
- Row 3: left by **3** columns

```
before:   X Y Z M          after:   X Y Z M      (row 0)
          X Y Z M                   Y Z M X      (row 1, shifted 1)
          X Y Z M                   Z M X Y      (row 2, shifted 2)
          X Y Z M                   M X Y Z      (row 3, shifted 3)
```

This moves bytes between columns, so that the next step mixes bytes that started in different columns.

**3. MixColumns** — apply the **MixColumn function to each column** of the state: each column of 4 bytes is multiplied by a fixed 4×4 matrix over GF(2⁸), so every output byte in a column depends on all four input bytes. **The last round omits this step.** ShiftRows and MixColumns together are the [[Confusion and Diffusion|diffusion]] — after two rounds every state byte depends on every input byte.

**4. AddRoundKey** — XOR the 128-bit round key into the state (shown as the ⊕ in the top-level diagram).

## Decryption

**Conceptual:** run the cipher in reverse, replacing each operation with its inverse. Every AES operation is individually invertible:
- XOR is its own inverse
- The inverse of the S-box is just the **inverse table**
- The inverse of a rotation in one direction is rotation in the other
- The inverse of MixColumn is just the **inverse table** (matrix)

**Actual:** run the cipher in the *forward* direction, except use the inverse operations, apply round keys in **reverse order**, and apply InvMixColumn to round keys K1..K9 (an algebraic trick that lets the inverse round keep the same operation order as the forward round).

**The cost of not being Feistel:** decryption takes **more memory and cycles** than encryption, and can only **partially reuse** encryption hardware. A [[Feistel Cipher]] gets free decryption by construction; AES paid for its speed and clean design by giving that up. Whether it matters depends on the deployment — many uses (e.g. counter mode) never decrypt at all.

## Assessment

- **Speed:** about **16 clock cycles per byte** on modern 32-bit CPUs — **200 MByte/s on a PC with no special hardware.** Compare DES, designed to be slow in software, and Triple DES at one third of that.
- **Security:** **no known successful attacks on full AES.** The best attacks work on **7–9 rounds** out of 10–14. Read alongside the [[Confusion and Diffusion|avalanche data]]: full diffusion arrives by round 3–4, so the remaining rounds are margin, and attacks that reach 9 of 10 rounds are still one round short.
- **Clean design.**
- **Brute force:** AES-128 takes **4 × 10²¹ (= 2⁷²) times more effort** than DES — 2¹²⁸ / 2⁵⁶.

## AES Is Only as Good as Its Mode

AES encrypts one 128-bit block. Everything about how a real message is protected — whether repeated plaintext leaks, whether an attacker can reorder or flip bits, whether decryption parallelizes — is decided by the [[Block Cipher Modes of Operation|mode of operation]] wrapped around it, not by AES. AES in ECB mode is insecure despite AES being sound. When [[Content Scrambling System|AACS]] replaced the broken CSS for HD DVD and Blu-ray, the specification named was *128-bit AES (CBC)* — cipher and mode together, because neither alone is a design.

## What AES Kept and What It Changed

| | DES | AES |
|---|---|---|
| Rounds with round keys | Yes | Yes |
| Alternating substitution / permutation | Yes | Yes |
| Structure | [[Feistel Cipher]] — half the block per round | Substitution-permutation network — whole block per round |
| Unit of operation | Bits | Bytes |
| Decryption | Free (same hardware, keys reversed) | Separate inverse operations |
| Fast in | Hardware | Software *and* hardware |
| Design process | Closed (IBM + NSA) | Open competition |

The two ciphers agree on the theory — [[Confusion and Diffusion]] via alternating S and P, keyed per round — and disagree on almost every engineering decision. That is a useful pair to hold in mind: the principles are fixed, the implementations are choices.

## See Also

- [[DES]]
- [[Triple DES]]
- [[Feistel Cipher]]
- [[Block Ciphers]]
- [[Confusion and Diffusion]]
- [[Block Cipher Modes of Operation]]
- [[Content Scrambling System]]
- [[Side-Channel Attacks]]
- [[Secret Key Cryptography]]
- [[CSCE 465]]
