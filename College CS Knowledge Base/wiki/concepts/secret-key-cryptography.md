---
title: "Secret Key Cryptography"
type: concept
tags: [csce465, security, cryptography, symmetric, secret-key]
sources: [csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation, csce465-lecture-05-public-key-cryptography]
course: CSCE 465
updated: 2026-09-26
---

Secret key cryptography uses **the same key for both encryption and decryption**, shared by the two parties who wish to communicate securely. Also called **symmetric key** or **shared key** cryptography. [[CSCE 465]] gives it the first full lecture of the applied cryptography unit, and its summary verdict is the reason why: secret key crypto is *(a) good quality, (b) faster to compute than public key crypto, and (c) the most widely used crypto.*

```
plaintext --[Encryption]--> ciphertext --[Decryption]--> plaintext
                 ^                            ^
                key  <------ same key ------> key
```

## Four Applications

The lecture lists four, and the last two are the ones that show the primitive does more than hide data:

| Application | How |
|---|---|
| **Communicating securely over an insecure channel** | Alice encrypts with the shared key; Bob decrypts with the same key |
| **Secure storage on insecure media** | Bob encrypts before storing; Bob decrypts on retrieval with the same key — one party, two points in time |
| **Message integrity** | Alice computes a **[[Message Authentication Code\|message integrity code (MIC)]]** from the message, then encrypts it with the shared key; Bob decrypts the MIC and verifies it agrees with the message contents |
| **Authentication** | Bob can verify that Alice sent the message |

The lecture attaches a question to the fourth: *how is that possible?*

> **Derived, not stated on the slide.** Only two parties hold the key. If Bob receives something that decrypts correctly (or carries a valid MIC) and Bob knows he did not produce it himself, the only other candidate is Alice. The guarantee is exactly as strong as the key's secrecy — and it convinces **only Bob**, since Bob could equally have forged it. That is why symmetric authentication cannot deliver [[Security Services|non-repudiation]]: a third party cannot tell Alice from Bob.

## Notation

Used throughout the rest of the unit:

| Notation | Meaning |
|---|---|
| `X XOR Y` (⊕) | Bit-wise exclusive-or of X and Y |
| `X \| Y` | Concatenation of X and Y |
| `K{m}` | Message `m` encrypted with secret key `K` |

## Key Sizes Over Time

Keys are selected from a large set to prevent [[Cryptanalysis|brute force]]:

| Era | Adequate key size |
|---|---|
| 1970s | 40 bits |
| 1980s | 56 bits ([[DES]]) |
| Now | 128 bits |

The rule of thumb the lecture gives: **if computing power grows 40% per year, you need roughly 5 more key bits per decade** to stay "sufficiently" hard to break. (Check: 1.4¹⁰ ≈ 28.9 ≈ 2⁴·⁸⁵.) This is [[Cipher Security Models|computational security]] made explicit as a moving target — the same cipher with the same key is secure in one decade and not the next, without anything about it changing.

## The Ciphers Covered

| Cipher | Type | Block | Key | Status per the lecture |
|---|---|---|---|---|
| [[DES]] | [[Feistel Cipher]] | 64 bits | 56 bits | Strong enough for non-critical applications |
| [[Triple DES]] | DES applied three times (EDE) | 64 bits | 112 bits effective | Better; widely used; slow |
| [[AES]] | Substitution-permutation (not Feistel) | 128 bits | 128 / 192 / 256 | Stronger *and* much faster |

All three are [[Block Ciphers|block ciphers]] built on [[Confusion and Diffusion|alternating substitution and permutation]]. Using any of them on a message longer than one block requires choosing a [[Block Cipher Modes of Operation|mode of operation]]; the alternative family, [[Stream Ciphers|stream ciphers]], encrypts bit by bit instead.

## The Structural Limitation

The lecture's closing line: secret key crypto **requires "out-of-band", bilateral key negotiation/agreement.** Both parties must hold the same key before the first message, and the cipher provides no way to get it there. This is the [[Cryptography|key distribution problem]] that [[Public Key Cryptography]] exists to solve — and it is why, in practice, public key operations are used to establish a symmetric key which then does the actual work. See [[RSA]] for key negotiation and [[Diffie-Hellman Key Exchange]] for agreement over a public channel.

## See Also

- [[Block Ciphers]]
- [[Confusion and Diffusion]]
- [[Feistel Cipher]]
- [[DES]]
- [[Triple DES]]
- [[AES]]
- [[Block Cipher Modes of Operation]]
- [[Stream Ciphers]]
- [[Message Authentication Code]]
- [[Initialization Vector]]
- [[Side-Channel Attacks]]
- [[Cryptography Taxonomy]]
- [[Public Key Cryptography]]
- [[Cryptography]]
- [[CSCE 465]]
