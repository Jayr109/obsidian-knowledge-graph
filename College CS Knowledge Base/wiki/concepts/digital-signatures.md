---
title: "Digital Signatures"
type: concept
tags: [csce465, security, cryptography, public-key, signatures, non-repudiation]
sources: [csce465-lecture-05-public-key-cryptography, csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

A digital signature is a value only the holder of a private key could have produced, verifiable by anyone holding the matching public key. [[CSCE 465]] presents it as the **first application of [[Public Key Cryptography]]**, and it is the one that delivers something symmetric cryptography structurally cannot.

## The Construction

```
Plaintext --[Alice SIGNS with Alice's PRIVATE key]--> Plaintext + digital signature
                                |
          --[Bob VERIFIES with Alice's PUBLIC key]--> Valid / Not Valid
```

Alice computes a **hash** of the message and signs the hash with her private key — *no one else can do this without her key*. Bob verifies the hash on receipt using Alice's public key and the verification equation.

Signing the **hash** rather than the message is not incidental, and Lecture 4 is where the hash side gets developed — see [[Hash Functions]]. [[RSA]] requires `m < n`, so a long message cannot be signed directly; a fixed-length digest can. It is also far cheaper, since public key operations are slow.

## The Direction Is the Whole Idea

The key usage is exactly **reversed** from encryption, and confusing the two is the standard error in this material:

| | Key used to produce | Key used to consume | Who can produce | Who can consume |
|---|---|---|---|---|
| **Encryption** | Recipient's **public** key | Recipient's **private** key | Anyone | Only the recipient |
| **Signing** | Signer's **private** key | Signer's **public** key | Only the signer | Anyone |

Encryption restricts *reading*; signing restricts *writing*. In [[RSA]] they are literally the same exponentiation — `m^d` is both "decrypt" and "sign" — so nothing in the arithmetic distinguishes them. Only the choice of whose key, and what the result is taken to mean, does.

## The Signature Is Only as Strong as the Hash

Because what gets signed is `H(m)` and not `m`, **a collision in the hash is a forgery in the signature scheme**: if `H(m1) = H(m2)`, a signature over `m1` is equally valid over `m2`. [[MD5]] made this concrete — in 2005 **two X.509 certificates with different public keys and the same MD5 hash** were constructed, meaning a certificate authority's signature on the benign one validated the malicious one too. That is [[Public Key Infrastructure\|PKI]] broken at the hash layer, and it is why [[Birthday Attack\|collision resistance]] rather than preimage resistance is the property signatures depend on.

## Non-Repudiation

Two properties the lecture states directly:

- **The digital signature is verifiable by anybody**
- **Only one person can sign the message**

Together these give **non-repudiation** — and the lecture makes the strong claim explicitly:

> **Non-repudiation is only achievable with public key cryptography.**

This confirms what the [[Secret Key Cryptography|symmetric authentication]] discussion implied: a [[Message Authentication Code|MAC]] convinces the other key holder and nobody else, because *either* holder of the shared key could have produced it. There is no way for a third party — a judge, an auditor, a protocol peer — to attribute it. Asymmetry is what makes attribution possible at all, since only one party ever holds the signing key.

The distinction maps onto [[Security Services]]:

| Service | Symmetric | Asymmetric |
|---|---|---|
| Integrity (data unchanged) | Yes, via MAC | Yes, via signature |
| Authentication (convinces the peer) | Yes, via MAC | Yes, via signature |
| **Non-repudiation (convinces a third party)** | **No** | **Yes** |

## Which Algorithms Sign

From the lecture's algorithm table:

| System | Digital signatures? |
|---|---|
| [[RSA]] | **Yes** |
| [[Diffie-Hellman Key Exchange\|Diffie-Hellman]] | No — key exchange only |
| DSA | **Yes** — and *only* signatures |

DSA is named but not developed in this lecture.

## See Also

- [[Public Key Cryptography]]
- [[RSA]]
- [[Hash Functions]]
- [[MD5]]
- [[Public Key Infrastructure]]
- [[Message Authentication Code]]
- [[Security Services]]
- [[CIA Triad]]
- [[CSCE 465]]
