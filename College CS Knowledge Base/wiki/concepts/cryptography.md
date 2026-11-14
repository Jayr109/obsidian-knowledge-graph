---
title: "Cryptography"
type: concept
tags: [csce465, security, cryptography, encryption, foundations]
sources: [csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03a-secret-key-cryptography-i]
course: CSCE 465
updated: 2026-10-01
---

Cryptography is **the art of secret writing**: converting data into an unintelligible, random-looking form. [[CSCE 465]] opens its applied cryptography unit here, and the definition carries one requirement that does all the work — the transformation **must be reversible**, recovering the original data without loss or modification. That single constraint separates cryptography from hashing, from compression, and from corruption.

## The Five Terms

| Term | Definition |
|---|---|
| **Plaintext** | A message in its original form |
| **Ciphertext** | A message in the transformed, unrecognized form |
| **Encryption** | The process that transforms plaintext into ciphertext |
| **Decryption** | The process that transforms ciphertext back into the corresponding plaintext |
| **Key** | The value used to control encryption and decryption |

The pipeline, with the key entering at both ends:

```
plaintext --[encryption]--> ciphertext --[decryption]--> plaintext
                 ^                            ^
                key                          key
```

Where those two keys come from — whether they are the same value or a matched pair — is the axis that splits the whole field. See [[Cryptography Taxonomy]].

## Not Compression

Both transform data into something unreadable, but they are different operations with different goals:

- Encryption is usually **n bits in, n bits out**. It does not try to shrink anything.
- Compression removes redundancy. It does not try to hide anything.

They **can** be combined, and the lecture poses the question without answering it: *what's the right order?*

> **Answer, derived rather than stated on the slide:** compress **first**, then encrypt. Good ciphertext is statistically random, and random data has no redundancy left to exploit — compressing after encrypting saves nothing. Compressing first also shrinks the plaintext, which reduces the material an attacker has to work with. (The real-world caveat, beyond this lecture: compressing before encrypting leaks information through *ciphertext length*, which is the basis of the CRIME and BREACH attacks on TLS.)

## Cryptography Is Rarely the Weakest Link

Stated flatly by the lecture, and it is the reason the course spends more time on systems than on algorithms:

- **Implementation of the cipher** — a correct algorithm coded wrongly. [[Side-Channel Attacks]] are the concrete form: timing and power leak the key from an implementation of an algorithm with no known weakness.
- **Distribution or protection of keys** — the problem no algorithm solves for you

The summary slide returns to this: *key distribution and management is a challenge for any cipher.* A perfect cipher with a leaked key protects nothing, and getting the key to the other party is a problem the cipher itself cannot address. This is the same "weakest link" argument from [[Computer Security]] — defense must hold everywhere, and the mathematics is usually the part that already does.

## Secret Keys vs. Secret Algorithms

The lecture reuses the phrase **security by obscurity** from [[Security Assurance|Lecture 2]] and applies it specifically to ciphers.

**Keeping the algorithm secret** is claimed to give better security, but:
- It is hard to keep secret if the cipher is used widely
- Reverse engineering and social engineering both recover it

**Publishing the algorithm** instead means:
- Security depends only on the **secrecy of the keys**
- Fewer unknown vulnerabilities, because all the smart people in the world are examining the algorithm

This is **Kerckhoffs's principle**, and it is the [[Security Design Principles|open design]] principle instantiated for cryptography: *public algorithms with secret parameters.* The design principles page already gives the general form; this is the case that generated it.

### Commercial vs. Military

The lecture notes the two communities genuinely differ:

| | Approach | Rationale |
|---|---|---|
| **Commercial** | Publish | Wide review, and therefore trust |
| **Military** | Keep algorithms secret | Avoid giving the enemy good ideas — and the military has access to public-domain knowledge anyway |

The military position is not a rejection of Kerckhoffs. It is asymmetric information warfare: they get the benefit of public review by *reading* it, while denying the reverse. Note this only works for an actor large enough to run its own review process internally.

## See Also

- [[Cryptanalysis]]
- [[Secret Key Cryptography]]
- [[Side-Channel Attacks]]
- [[Cipher Security Models]]
- [[Cryptography Taxonomy]]
- [[Classical Ciphers]]
- [[One-Time Pad]]
- [[Security Services]]
- [[Security Design Principles]]
- [[CSCE 465]]
