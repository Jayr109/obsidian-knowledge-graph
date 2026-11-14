---
title: "Cryptography Taxonomy"
type: concept
tags: [csce465, security, cryptography, symmetric, public-key, hash-functions]
sources: [csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation, csce465-lecture-05-public-key-cryptography, csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

[[CSCE 465]] classifies cryptographic constructions along **two independent axes**. The first — how many keys — is the one that determines what a primitive can *do*, and it organizes the rest of the applied cryptography unit.

## Axis 1: Number of Keys

| Keys | Family | What it provides |
|---|---|---|
| **None** | [[Hash Functions\|Hash functions]] | Integrity, not confidentiality — nothing to decrypt with |
| **One** | Secret key cryptography | Confidentiality between parties who already share a secret |
| **Two** | Public key cryptography | Confidentiality and authentication without a pre-shared secret |

The key count is not a detail of implementation — it decides which [[Security Services|security service]] the primitive can deliver. A construction with no key cannot keep a secret; a construction with one key cannot prove *who* sent something to a third party, since either holder could have produced it.

## Axis 2: How the Plaintext Is Processed

- **[[Stream Ciphers|Stream cipher]]** — encrypt the input message **one symbol at a time**
- **[[Block Ciphers|Block cipher]]** — divide the input into **blocks of symbols** and process the blocks in sequence. *May require padding*, since the last block is rarely full. How the blocks are chained is the [[Block Cipher Modes of Operation|mode of operation]].

This axis is orthogonal to the first: secret key cryptography contains both kinds. It is also softer than it looks — [[Block Cipher Modes of Operation|OFB, CFB, and CTR]] run a block cipher as a keystream generator, producing a stream cipher out of block-cipher parts.

## Secret Key Cryptography

*Developed in full on [[Secret Key Cryptography]]; the ciphers are [[DES]], [[Triple DES]], and [[AES]].*

**The same key is used for encryption and decryption.**

```
plaintext --[encryption]--> ciphertext --[decryption]--> plaintext
                 ^                            ^
                key  <------ same key ------> key
```

Also called **symmetric** or **conventional** cryptography. Ciphertext is approximately the same length as plaintext.

Examples the lecture names:
- **Stream cipher:** RC4
- **Block ciphers:** DES, IDEA, AES

The unsolved problem is visible in the diagram: both parties must already hold the same key. Getting it there is [[Cryptography|key distribution]], which the lecture repeatedly flags as the hard part.

## Public Key Cryptography

*Developed in full on [[Public Key Cryptography]]; the algorithms are [[RSA]] and [[Diffie-Hellman Key Exchange]], and the infrastructure is [[Public Key Infrastructure|PKI]].*

A **public/private key pair** is used — encrypt with one, decrypt with the other.

```
plaintext --[encryption]--> ciphertext --[decryption]--> plaintext
                 ^                            ^
            public key                   private key
```

- The **public key** can be publicly known
- The **private key** is kept secret by the key's owner
- **Much slower** than secret key cryptography

Also called **asymmetric** cryptography. The lecture dates its invention/publication to **1975**; the commonly cited landmark is Diffie & Hellman's *New Directions in Cryptography* in **1976**, with Merkle's related work from 1974–75 — recorded here because the deck's date and the standard one differ slightly.

Why this matters despite being slow: it removes the pre-shared secret. Two parties who have never met can establish confidentiality, and because only the owner holds the private key, a third party can be convinced of origin — which is what [[Security Services|non-repudiation]] requires and symmetric cryptography cannot provide. In practice the speed problem is solved by using public key cryptography to establish a symmetric key, then switching.

## Hash Algorithms

*Developed in full on [[Hash Functions]]; the standards are [[MD5]] and [[SHA-1]], and the keyed construction is [[HMAC]].*

```
message of arbitrary length --[Hash H]--> fixed-length short message
```

Also known as **message digests**, **one-way transformations**, **one-way functions**, or simply **hash functions**.

- The length of `H(m)` is **much shorter** than the length of `m`
- Usually a **fixed length: 128 or 160 bits**

Two consequences of "shorter" and "one-way," neither drawn out in this lecture but both load-bearing later:
- Because the output is shorter than the input, **collisions must exist** — infinitely many messages map to each digest. Security comes from them being infeasible to *find*, not from their absence.
- Because there is no key and the function is not reversible, hashing provides **integrity**, not confidentiality. It answers "has this changed?" and never "what does this say?"

## How the Families Map to the Services

| Family | [[CIA Triad]] component | [[Security Services]] delivered |
|---|---|---|
| Secret key | Confidentiality | Confidentiality; integrity with a shared secret |
| Public key | Confidentiality, origin integrity | Confidentiality, authentication, non-repudiation |
| Hash | Integrity (data) | Integrity; a building block for the other two |

Each family gets developed in its own part of the course; this page is the map, not the territory.

## See Also

- [[Cryptography]]
- [[Secret Key Cryptography]]
- [[Stream Ciphers]]
- [[Block Cipher Modes of Operation]]
- [[Hash Functions]]
- [[HMAC]]
- [[Public Key Cryptography]]
- [[RSA]]
- [[Diffie-Hellman Key Exchange]]
- [[Block Ciphers]]
- [[One-Time Pad]]
- [[Cipher Security Models]]
- [[Security Services]]
- [[CIA Triad]]
- [[CSCE 465]]
