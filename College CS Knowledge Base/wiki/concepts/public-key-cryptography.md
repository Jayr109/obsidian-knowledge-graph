---
title: "Public Key Cryptography"
type: concept
tags: [csce465, security, cryptography, asymmetric, public-key, trapdoor]
sources: [csce465-lecture-05-public-key-cryptography, csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

Public key cryptography uses a **public/private key pair** instead of one shared secret: the public key can be announced to everyone, and the private key is kept secret by its owner. Also called **asymmetric** cryptography. [[CSCE 465]] gives it a full lecture, and the reason it exists is the limitation [[Secret Key Cryptography]] ended on — symmetric crypto requires out-of-band, bilateral key agreement before the first message, and public key crypto is what removes that requirement.

Two properties frame everything else:

- **Invented and published in 1975** (as the deck states; the commonly cited landmark is Diffie & Hellman 1976 — see [[Cryptography Taxonomy]] for the discrepancy, which both CSCE 465 crypto lectures repeat consistently)
- **Much slower to compute** than secret key cryptography

That second point is why public key crypto is almost never used to encrypt bulk data. It is used to establish a symmetric key, which then does the work.

## Five Applications

The lecture lists five, and they are not variations on one idea — the first and fourth do things symmetric cryptography structurally cannot.

**1. Message integrity with digital signatures.** Alice computes a hash and signs it with her *private* key; Bob verifies with Alice's *public* key.

```
Plaintext --[Alice signs, Alice's PRIVATE key]--> Plaintext + signature
          --[Bob verifies, Alice's PUBLIC key]--> Valid / Not Valid
```

See [[Digital Signatures]]. The critical consequence: the signature is **verifiable by anybody**, and only one person could have produced it — **non-repudiation**, which the lecture states outright is *only achievable with public key cryptography*.

**2. Communicating securely over an insecure channel.** Alice encrypts with **Bob's public key**; Bob decrypts with **his private key**. No one else can decrypt, because no one else has Bob's private key.

```
Plaintext --[encrypt, Bob's PUBLIC key]--> Ciphertext --[decrypt, Bob's PRIVATE key]--> Plaintext
```

Note the direction reverses between applications 1 and 2. **Signing uses your own private key; encrypting uses the recipient's public key.** Getting that backwards is the most common conceptual error in this material.

**3. Secure storage on insecure medium.** Alice encrypts with her own public key and decrypts later with her private key. (One party, two points in time — the same shape as symmetric secure storage, but she need not protect an encryption key on the storing machine.)

**4. User authentication.** Bob proves his identity to Alice by performing an operation with his private key **without divulging it**; Alice verifies with Bob's public key. See [[User Authentication]] for where this sits among the alternatives, and [[Authentication Tokens]] for the hardware that holds such a private key. This is a zero-disclosure proof of possession, which a shared secret cannot provide — with symmetric keys, proving you know the secret means showing something that Alice could equally have produced.

**5. Key exchange for secret key crypto.** Alice and Bob use public key crypto to negotiate a shared secret key. See [[Diffie-Hellman Key Exchange]] and the RSA-based negotiation on [[RSA]].

## The Algorithms

| System | Encryption / Decryption? | Digital Signatures? | Key Exchange? |
|---|---|---|---|
| **[[RSA]]** | Yes | Yes | Yes |
| **[[Diffie-Hellman Key Exchange\|Diffie-Hellman]]** | — | — | Yes |
| **DSA** | — | Yes | — |

RSA is the only one of the three that does all three jobs, which is most of why it dominates. Diffie-Hellman does key exchange *only* — it is not an encryption algorithm, a point the lecture returns to under its limitations.

## Public-Key Requirements

It must be computationally:

- **easy** to generate a public/private key pair
- **hard** to determine the private key given the public key
- **easy** to encrypt using the public key
- **easy** to decrypt using the private key
- **hard** to recover the plaintext from the ciphertext plus the public key alone

Five requirements, and the two "hard" ones are what make the scheme possible at all. Note the asymmetry is not about secrecy of the algorithm — it is a *computational* gap between operations that are mathematically inverse.

## Trapdoor One-Way Functions

The abstraction that delivers those requirements:

```
Y = f_k(X)        easy to compute if k and X are known
X = f_k^-1(Y)     easy to compute if k and Y are known
X = f_k^-1(Y)     HARD if Y is known but k is unknown
```

The middle and third lines are the same computation; the only difference is whether you hold `k` — the **trapdoor**. A function that is hard to invert *in general* but easy to invert *with a secret* is exactly what a private key is for.

> **The goal of designing a public-key algorithm is to find an appropriate trapdoor one-way function.**

That sentence reframes the rest of the lecture. [[RSA]] and [[Diffie-Hellman Key Exchange]] are not two unrelated inventions; they are two answers to the same search, built on two different hard problems — **factoring** and **discrete logarithm**. Both are [[Cipher Security Models|provably secure]] in the lecture's sense: breaking them reduces to a famous problem nobody has solved, which is confidence by reputation rather than proof.

## See Also

- [[RSA]]
- [[Diffie-Hellman Key Exchange]]
- [[Digital Signatures]]
- [[Public Key Infrastructure]]
- [[Cryptography Taxonomy]]
- [[Secret Key Cryptography]]
- [[Security Services]]
- [[User Authentication]]
- [[Authentication Tokens]]
- [[CSCE 465]]
