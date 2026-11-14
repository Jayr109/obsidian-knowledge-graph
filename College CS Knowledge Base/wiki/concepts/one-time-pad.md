---
title: "One-Time Pad"
type: concept
tags: [csce465, security, cryptography, shannon, xor, perfect-secrecy]
sources: [csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation]
course: CSCE 465
updated: 2026-09-22
---

The one-time pad is the cipher that is **perfectly secure** and almost never usable. [[CSCE 465]] presents it as the existence proof for [[Cipher Security Models|unconditional security]] — and as the demonstration of what that guarantee costs.

## Shannon's Requirements

By a theorem of Shannon, a perfectly secure cipher requires:

1. A **key at least as long as the message** to be encrypted
2. The key can be used **only once** — every message needs a new key

Both conditions are necessary. Neither is negotiable, and together they are why the pad has *very limited use*: you must negotiate and distribute long, random keys for every message. Note the circularity that makes it impractical — to send an *n*-bit secret you must first securely deliver an *n*-bit key, which is the same problem you started with. The pad does not solve key distribution; it converts a confidentiality problem into a logistics problem.

## The Construction

```
1. Generate a random bit string (the key) as long as the plaintext,
   and share it with the other party.

2. Encrypt:  ciphertext = plaintext XOR key
3. Decrypt:  plaintext  = ciphertext XOR key
```

```
plaintext --(XOR key)--> ciphertext --(XOR key)--> plaintext
```

The same operation encrypts and decrypts, because XOR is its own inverse: `(p XOR k) XOR k = p`.

**Why this achieves `H(p) = H(p|c)`:** with a uniformly random key, every plaintext of the right length is an equally likely candidate for any given ciphertext. Given ciphertext `c`, the key `c XOR p` maps it to *any* plaintext `p` you like, and all such keys are equally probable. The ciphertext therefore rules nothing out. An attacker with unlimited computation can enumerate all keys and obtain every possible message — including the true one — with no way to tell which is which. This is the [[Cryptanalysis|recognition problem]] made permanent by design.

## Why the Key Cannot Be Reused

The lecture poses this as a question over a worked XOR example. The answer:

> **Derived, not stated on the slide.** If two messages are encrypted with the same key `k`:
> ```
> c1 = p1 XOR k
> c2 = p2 XOR k
> c1 XOR c2 = (p1 XOR k) XOR (p2 XOR k) = p1 XOR p2
> ```
> **The key cancels.** The attacker now holds the XOR of two plaintexts with no key involved at all — and two natural-language messages XORed together are readily separable by *crib-dragging*, exactly the kind of statistical structure [[Classical Ciphers|frequency analysis]] exploits. One reuse converts a perfect cipher into a solvable puzzle.

This is why the "one-time" is in the name rather than being a recommendation. The security claim is void on the second use, and it degrades further with each additional message under the same key.

## Where the Reuse Failure Reappears

The one-time pad is not a historical aside — its key-reuse catastrophe is the single most repeated result in the cryptography unit. Lecture 3b hits it three separate times:

- **[[Block Cipher Modes of Operation|OFB mode]]** — *if you know one plaintext/ciphertext pair, you can easily derive the pad; should not reuse a one-time pad*
- **[[Initialization Vector|IVs]]** — the conclusion drawn from that: *the IV must be different every time*
- **[[Stream Ciphers]]** — the same algebra as a structural weakness: `(M1 XOR PRNG) XOR (M2 XOR PRNG) = M1 XOR M2`

Any construction that XORs a keystream against plaintext inherits it, which is every keystream mode and every stream cipher.

## What It Teaches

The pad is rarely deployed, but it fixes the ceiling for everything else:

- **Perfect secrecy is real**, not a theoretical fiction — so "unbreakable" is a meaningful category.
- **It costs exactly what Shannon says** — no cheaper construction achieves it. Any cipher with a key shorter than its message is at best [[Cipher Security Models|computationally secure]].
- The failure mode is **operational, not mathematical**. The pad is broken by reusing a key, mishandling key material, or using a non-random generator — never by cryptanalysis of the algorithm. That is [[Cryptography|the weakest link argument]] in its purest form: the math is flawless and the system still fails.

The lecture's summary: *"perfectly secure" ciphers are possible, but too expensive in practice.*

## See Also

- [[Cipher Security Models]]
- [[Stream Ciphers]]
- [[Block Cipher Modes of Operation]]
- [[Initialization Vector]]
- [[Classical Ciphers]]
- [[Cryptanalysis]]
- [[Cryptography]]
- [[Cryptography Taxonomy]]
- [[CSCE 465]]
