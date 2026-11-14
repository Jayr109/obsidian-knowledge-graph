---
title: "Cipher Security Models"
type: concept
tags: [csce465, security, cryptography, entropy, provable-security]
sources: [csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-05-public-key-cryptography]
course: CSCE 465
updated: 2026-09-26
---

Three standards for what "this cipher is secure" can mean, in decreasing order of strength. [[CSCE 465]] introduces them in one slide, but the distinction governs how every later claim in the cryptography unit should be read — a cipher described as "secure" is almost always secure in the *third* sense.

## 1. Unconditionally Secure (Perfectly Secure)

Defined by an entropy equation:

```
H(p) = H(p | c)
```

The uncertainty about the plaintext `p` is **unchanged** by knowing the ciphertext `c`. Observing the ciphertext gives the attacker literally zero information about the message — not "not enough information," but none. An attacker with infinite computing power gains nothing, because there is nothing in the ciphertext to gain.

This is the strongest possible claim, and it is achievable: the [[One-Time Pad]] meets it, by Shannon's theorem. The price is a key as long as the message, used once — which is why perfect security is real but almost never practical.

**Why the equation is the right definition:** it does not mention attackers, algorithms, or running time at all. It is a statement about information, so no advance in computing or mathematics can weaken it.

## 2. Provably Secure

Breaking the cipher is **as difficult as solving a well-known and supposedly difficult problem** — factoring large integers, computing discrete logarithms.

Read the wording carefully, because it is doing something subtle. This is a **reduction**, not a proof of security: it shows *if you can break my cipher, you can also solve this famous problem nobody has solved.* It inherits its confidence from the reputation of the hard problem, and that reputation is empirical. The word "supposedly" in the lecture's own phrasing is honest — nobody has proven factoring is hard. A polynomial-time factoring algorithm (or a large enough quantum computer) would collapse the guarantee without any flaw ever being found in the cipher itself.

This is the same logical shape as [[Karp Reductions|NP-hardness reductions]] in [[CSCE 411]]: *this problem is at least as hard as that one.* Reduction arguments transfer difficulty; they do not create it.

Lecture 5 supplies the two canonical instances. [[RSA]] rests on **factoring** — recover `p` and `q` and the private key follows immediately. [[Diffie-Hellman Key Exchange]] rests on the **discrete logarithm problem**, and the lecture attaches an unusually honest caveat: *as always, to the best of our knowledge; doesn't mean there isn't a method out there waiting to be found.*

## 3. Computationally Secure

The weakest and by far the most common. The cost of breaking the cipher exceeds the value of the information, or the time to break it exceeds the useful lifetime of the information.

Lecture 3a gives the concrete cases. [[DES]]: *no attacks significantly better than brute force* — a sound algorithm whose 2⁵⁶ key space is simply too small now. [[AES]]: *no known successful attacks on the full cipher*, 2⁷² times more brute-force effort than DES. Both are computational-security claims, and neither says anything about [[Side-Channel Attacks|the implementation]].

The lecture leaves this bullet bare, but it is the standard nearly every deployed cipher actually meets — and it is the standard the [[Cryptanalysis|brute force cost table]] is arguing about. A 128-bit key is computationally secure because 5.6 × 10²⁶ processors is not a thing anyone has, not because anything is proven impossible.

Note that computational security is the cryptographic form of the **work factor** [[Security Design Principles|design principle]]: compare the cost of circumventing the mechanism against the resources of the expected attacker. It is explicitly relative to an adversary and to a moment in time.

## Summary

| Model | Guarantee rests on | Survives unlimited computation? |
|---|---|---|
| **Unconditionally secure** | Information theory | **Yes** |
| **Provably secure** | An unproven hardness assumption | No — falls if the assumption falls |
| **Computationally secure** | Current cost of attack vs. value of data | No — erodes over time |

The lecture's closing summary makes the practical verdict: *"perfectly secure" ciphers are possible, but too expensive in practice.* The field lives in row three and manages the risk with key length.

## See Also

- [[One-Time Pad]]
- [[DES]]
- [[AES]]
- [[RSA]]
- [[Diffie-Hellman Key Exchange]]
- [[Side-Channel Attacks]]
- [[Cryptography]]
- [[Cryptanalysis]]
- [[Security Design Principles]]
- [[CSCE 465]]
