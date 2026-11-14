---
title: "DES"
type: algorithm
tags: [csce465, security, cryptography, block-cipher, des, feistel]
sources: [csce465-lecture-03a-secret-key-cryptography-i]
course: CSCE 465
updated: 2026-09-13
---

DES, the **Data Encryption Standard**, is a [[Feistel Cipher]] proposed by IBM and standardized by NBS in 1976. [[CSCE 465]] walks through it component by component, not because it is still recommended — its 56-bit key is too short — but because it is the clearest worked example of every idea in [[Block Ciphers|block cipher]] design, and because [[Triple DES]] built on it is still deployed.

## Design Criteria

**Official:**
- Provide a high level of security
- **Security must reside in the key, not the algorithm** ([[Cryptography|Kerckhoffs]])
- Not patented
- Must be exportable
- Efficient to implement in **hardware**

**Unofficial** (the lecture's phrasing, with a smiley):
- Must be **slow to execute in software**
- Must be breakable by NSA

The unofficial criteria are a joke that is not entirely a joke. The bit-level permutations that make DES fast in hardware are exactly what make it slow in software, and the 56-bit key size was a reduction from IBM's original proposal.

## Parameters

| | |
|---|---|
| **Block** | 64-bit plaintext in, 64-bit ciphertext out |
| **Rounds** | 16 |
| **Key** | 64 bits nominal — **every 8th bit is a parity bit, so really 56 bits** |
| **Round keys** | 16 sub-keys of 48 bits each |

## Top-Level Structure

```
64-bit input
    |
Initial Permutation (IP)
    |
Round 1   <-- 48-bit K1   \
Round 2   <-- 48-bit K2    |  Feistel rounds
  ...                      |
Round 16  <-- 48-bit K16  /
    |
Swap Halves
    |
Final Permutation (FP = IP^-1)
    |
64-bit output
```

with the 16 round keys produced by a separate **key schedule** from the 56-bit key.

### Initial and Final Permutations

The initial permutation moves input bit 58 to output bit 1, input bit 50 to output bit 2, and so on — the first row of the table is `58 50 42 34 26 18 10 2`. The final permutation is exactly its inverse (output bit 58 ← input bit 1, ...).

Two notes the lecture makes, and the first is a genuine puzzle:

**Note 1:** the initial permutation is **fully specified and independent of the key** — therefore it **does not improve security.** The lecture asks *why needed?*

> **Derived, not stated on the slide.** The standard explanation is hardware convenience for 1970s implementations — loading a 64-bit block byte-by-byte into a shift register naturally produces this bit ordering, so IP is free in that setting. It contributes nothing cryptographically; an attacker simply applies IP⁻¹ first. It is kept because the standard specifies it, not because anyone would design it in today.

**Note 2:** the final permutation *is* needed — to make DES a proper [[Feistel Cipher]] so that **the same hardware serves encryption and decryption.**

## Key Schedule

**Step 1 — First permutation (PC-1):** throw out the 8 parity bits (positions 8, 16, 24, ..., 64), then permute the remaining 56 bits into two 28-bit halves `C_0` and `D_0`. The table is laid out as 8 rows of 7 columns; its first row is `57 49 41 33 25 17 9`.

**Step 2 — Per round, for i = 1..16:**
1. **Circular left shift** each of `C_{i-1}` and `D_{i-1}` independently to produce `C_i`, `D_i`:
   - Rounds **1, 2, 9, 16**: shift by **1** bit
   - All other rounds: shift by **2** bits
2. **Permutation with discard (PC-2):** each 28-bit half becomes 24 bits, giving the 48-bit round key `K_i`. Left half of `K_i` is a permutation of `C_i` (bits 9, 18, 22, 25 left out); right half is a permutation of `D_i` (bits 35, 38, 43, 54 left out).

The total shift over 16 rounds is 28 — exactly one full rotation — so `C_16 = C_0`, which is what lets decryption run the schedule backwards.

## One Round: the Mangler Function f

Each round is a standard [[Feistel Cipher|Feistel round]]: `L_{i+1} = R_i`, `R_{i+1} = L_i XOR f(R_i, K_i)`. The function `f` — the **mangler** — takes a 32-bit half block and a 48-bit round key and returns 32 bits, in three stages:

```
32-bit half block R_i
       |
   Expansion (E)          32 -> 48 bits
       |
      XOR <---- 48-bit K_i
       |
   S-boxes S1..S8         48 -> 32 bits (8 boxes, 6 bits in, 4 bits out each)
       |
   Permutation (P)        32 -> 32 bits
       |
32-bit output
```

### Expansion (E): 32 → 48 bits

The 32 bits are grouped into 8 groups of 4; each group is widened to 6 by **repeating** its neighbors' edge bits. The first row of the table is `32 1 2 3 4 5` — bit 32 and bit 5 are the repeats. Sixteen bits appear twice. The purpose is to make the half block the same width as the round key so they can be XORed, and to make each S-box's input depend on adjacent groups (which feeds [[Confusion and Diffusion|diffusion]]).

### S-Boxes: 48 → 32 bits

Eight boxes `S_1 ... S_8`, each taking 6 bits and producing 4. **6 bits select a 4-bit substitution, so for every output there are four inputs that map to it.**

Addressing: the **outer two bits** (`I1 I6`) select the **row** (0–3); the **inner four bits** (`I2 I3 I4 I5`) select the **column** (0–15). The entry is an integer 0–15, output as 4 bits.

**Worked example from the lecture, on S1:** input `100110`.
- Row = `I1 I6` = `1 0` = **2**
- Column = `I2 I3 I4 I5` = `0011` = **3**
- `S1[2][3]` = **8** → output `1000`

(The S1 table on the slide has row 2 partially garbled in extraction; the entry for column 3 is 8, and the standard table's row 2 is `4 1 14 8 13 6 2 11 15 12 9 7 3 10 5 0`, consistent with the slide's example. For S2..S8 the lecture refers to the textbook.)

**S-box design principles** — the S-box is **the only nonlinear part of DES**, so all of the cipher's [[Confusion and Diffusion|confusion]] lives here:
- Each row should be a permutation of the 16 possible outputs
- Output of one S-box should affect other S-boxes in the following round
- Each row and column of the table contains different numbers

### Permutation (P): 32 → 32 bits

A fixed bit permutation whose first row is `16 7 20 21 29 12 28 17`. Its job is to spread each S-box's 4 output bits across different S-boxes in the next round — the diffusion step that makes the S-box design principle above actually hold.

## The Full Operation List

*That's it.* Everything DES does: permutation, swapping halves, substitution (S-box table lookup), bit discard, bit replication, circular shift, XOR. **Hard to implement? Hardware: no. Software: yes.**

## Analysis

**No attacks on DES so far are significantly better than brute force, for comparable cost.** That is a strong statement about the design — differential and linear cryptanalysis exist but need more chosen/known plaintext than is practical. DES fails on **key size**, not on structure.

### Avalanche

One-bit plaintext difference (`0x0000000000000000` vs `0x8000000000000000`, key `0x016B24621C181C32`) yields ciphertexts differing in **34 of 64 bits**. Full avalanche is reached by round 3–4; the round-by-round table is on [[Confusion and Diffusion]].

### Weak Keys

**Four weak keys** with the property `K{K{m}} = m` — encrypting twice returns the plaintext. These are keys which, after PC-1, are:
- 28 zeros followed by 28 zeros
- 28 zeros followed by 28 ones
- 28 ones followed by 28 zeros
- 28 ones followed by 28 ones

The lecture asks *what's bad about that?*

> **Derived, not stated on the slide.** With `C_0` and `D_0` each all-0 or all-1, circular shifting changes nothing, so **all 16 round keys are identical**. Then the reversed key order used for decryption is the same as the forward order — encryption *is* decryption, and `K{K{m}} = m`. Anyone who can get a message encrypted twice under such a key recovers it, and any construction that relies on encryption and decryption being different (such as [[Triple DES]] EDE) degrades.

**Twelve semi-weak keys** (six pairs) with `K1{K2{m}} = m` — encrypting under one and then the other returns the plaintext. After PC-1 these have each half either constant or alternating `0101...` / `1010...`, so the key schedules of the pair run through the same round keys in opposite orders.

None of this is a practical attack — 16 bad keys out of 2⁵⁶ — but an implementation should reject them.

### Key Size

**56 bits are currently too small to resist brute force with readily-available hardware.** The lecture's dated benchmark: *ten years ago it took $250,000 to build a machine that could crack DES in a few hours. Now?* (The EFF Deep Crack machine, 1998, is the reference point.) Compare the [[Cryptanalysis|brute force table]] from Lecture 3. This is the sole reason [[Triple DES]] and then [[AES]] exist.

## See Also

- [[Feistel Cipher]]
- [[Triple DES]]
- [[AES]]
- [[Block Ciphers]]
- [[Confusion and Diffusion]]
- [[Secret Key Cryptography]]
- [[Cryptanalysis]]
- [[CSCE 465]]
