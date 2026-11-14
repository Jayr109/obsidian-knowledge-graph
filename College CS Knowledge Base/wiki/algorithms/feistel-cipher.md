---
title: "Feistel Cipher"
type: algorithm
tags: [csce465, security, cryptography, block-cipher, feistel]
sources: [csce465-lecture-03a-secret-key-cryptography-i]
course: CSCE 465
updated: 2026-09-13
---

The Feistel cipher is not a cipher but a **template** for building a [[Block Ciphers|block cipher]] — and, per [[CSCE 465]], a very influential one. Its major benefit is that **encryption and decryption can be done with the same hardware**: decryption is the same sequence of operations with the round keys in reverse order. [[DES]] and RC5 are Feistel ciphers; [[AES]] deliberately is not.

The construction's real trick, and the reason it is worth understanding on its own: it turns *any* function into an invertible cipher. The round function `f` **never needs to be inverted**, so it can be as ugly and nonlinear as you like.

## One Round of Encryption

The block is split into left and right halves, `L_i` and `R_i`, each `w` bits wide (block size `2w`).

```
         L_i              R_i
          |                |
          |          +-----+-----+
          |          |           |
          |        f(R_i, K_i)   |
          |          |           |
         XOR <-------+           |
          |                      |
        R_{i+1}                L_{i+1}
```

In steps:

1. Break input block `i` into left and right halves `L_i` and `R_i`
2. **Copy `R_i`** to create output half-block `L_{i+1}` — the right half passes through untouched
3. Half block `R_i` and round key `K_i` are "scrambled" by function `f`
4. **XOR** the result with `L_i` to create output half-block `R_{i+1}`

As equations:

```
L_{i+1} = R_i
R_{i+1} = L_i XOR f(R_i, K_i)
```

Only half the block is modified per round. That is why Feistel ciphers need many rounds — DES uses 16 — for every bit to have been through `f` enough times.

## One Round of Decryption

*Just reverse the arrows.* Given `(L_{i+1}, R_{i+1})` and `K_i`:

```
R_i = L_{i+1}                          (it was copied, so copy it back)
L_i = R_{i+1} XOR f(R_i, K_i)          (= R_{i+1} XOR f(L_{i+1}, K_i))
```

The second line works because `R_i` is now known, so `f(R_i, K_i)` can be **recomputed** — not inverted — and XORed off. This is the whole argument:

> **Reversibility of the Feistel cipher derives from the reversibility of XOR.** The function `f` can be anything — hopefully something easy to compute — and **there is no need to invert `f`.**

The round function is only ever evaluated in the forward direction, in both encryption and decryption.

## The Complete Cipher

`n` rounds, with round keys `K_1 ... K_n` derived from the master key:

```
Plaintext (2w bits) = (L_0, R_0)
   Round 1 with K_1
   Round 2 with K_2
   ...
   Round n with K_n
   -> (L_n, R_n)
   FINAL SWAP -> (L_{n+1}, R_{n+1}) = (R_n, L_n)
Ciphertext (2w bits)
```

**Note the final swap.** After the last round the two halves are exchanged one more time — the lecture flags this twice. It is what makes decryption *literally identical* to encryption: feed the ciphertext into the same circuit with keys in the order `K_n, K_{n-1}, ..., K_1`, and the plaintext comes out. Without the final swap, the round structure would be off by one half-block and the same hardware could not be reused.

**Decryption** is therefore: same structure, same `f`, **round keys applied in reverse order.**

## Parameters

A concrete Feistel cipher is specified by five choices:

| Parameter | DES's choice |
|---|---|
| **Block size** | 64 bits (w = 32) |
| **Key size** | 56 bits |
| **Number of rounds** | 16 |
| **Subkey generation algorithm** | Permutation, split, circular shifts, permutation-with-discard |
| **"Scrambling" function `f`** | The mangler: expand, XOR key, S-boxes, permute |

Everything about a Feistel cipher's security lives in `f`, the key schedule, and the round count. The Feistel structure itself contributes reversibility and nothing else — it is a correctness guarantee, not a security one.

## Why It Was Influential

Before Feistel, a designer wanting an invertible cipher had to design invertible components, which constrains how nonlinear they can be. The Feistel structure removes that constraint entirely. It let [[DES]]'s designers use S-boxes that shrink 6 bits to 4 — plainly non-invertible — inside a cipher that decrypts perfectly. [[AES]] chose a different route (every component individually invertible, with inverse tables) and paid for it: AES decryption needs more memory and cycles than encryption and can only partially reuse the hardware.

## See Also

- [[Block Ciphers]]
- [[DES]]
- [[Triple DES]]
- [[AES]]
- [[Confusion and Diffusion]]
- [[Secret Key Cryptography]]
- [[CSCE 465]]
