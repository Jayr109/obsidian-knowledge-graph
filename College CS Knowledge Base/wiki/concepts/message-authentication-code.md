---
title: "Message Authentication Code"
type: concept
tags: [csce465, security, cryptography, mac, mic, integrity, cbc-residue]
sources: [csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation, csce465-lecture-05-public-key-cryptography, csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

A **MAC (Message Authentication Code)**, also called a **MIC (Message Integrity Code)**, is a short value computed from a message under a shared key that lets the receiver detect any modification. [[CSCE 465]] introduces it immediately after the [[Block Cipher Modes of Operation|modes of operation]], and the placement is the argument: **none of the five modes provides integrity.** Every one of them permits some targeted modification of the plaintext. A MAC is the mechanism that closes that gap.

This is the [[CIA Triad|data integrity]] half of the triad, delivered by [[Secret Key Cryptography|symmetric]] means — and, per [[Security Services]], it convinces only the other key holder, never a third party. Lecture 5 states the contrast directly: **non-repudiation is only achievable with public key cryptography**, so where a third party must be convinced, a MAC is the wrong tool and a [[Digital Signatures|digital signature]] is the right one.

## CBC Residue

The lecture's construction reuses machinery already on hand:

> Only send the **last block of CBC** (the *CBC residue*) — and send the plaintext.

```
IV -> M1 -> [E] -> C1
            |
      M2 -> [E] -> C2
            |
      M3 -> [E] -> C3
            |
      M4 -> [E] -> C4  <- residue: this block only
      (M4 = 46 bytes + pad)

Transmit:  plaintext M1..M4  +  residue C4
```

Because [[Block Cipher Modes of Operation|CBC]] chains every block into the next, the final block depends on **every** plaintext block and on the key. **Any modification in the plaintext modifies the CBC residue** — so the receiver recomputes the chain over the received plaintext and compares. A mismatch means tampering.

Note what is and is not sent: the *plaintext* travels in the clear and only the residue is appended. This construction provides **integrity alone**, not confidentiality. The intermediate ciphertext blocks `C1..C3` are computed and discarded.

## Getting Both Confidentiality and Integrity

The lecture is careful here, and leads with what does **not** work:

> **Replicating the last CBC block doesn't work.**

> **Derived, not explained on the slide.** If you CBC-encrypt the message and then send `C_n` again as the "MAC", you have appended a value the receiver already has. It is a function of the ciphertext the attacker also holds, computed under the same key, so it adds no information and no assurance — an attacker who alters the ciphertext simply recomputes nothing, because the last block *is* the ciphertext. Encryption and authentication must not collapse into the same computation under the same key.

The two approaches given:

| Approach | How |
|---|---|
| **P+I** | Use **separate (but maybe related) secret keys** for encryption and for the MIC — **two encryption passes** over the data |
| **CBC(message \| hash)** | Append a hash of the message to the message, then CBC-encrypt the whole thing |

The cost of the first is explicit: two passes, so twice the work. The parenthetical "but maybe related" is doing quiet work — the keys may be derived from one master key, but they must not be *the same* key, for the reason above.

> **Worth flagging.** Modern practice has largely settled this debate in favor of **encrypt-then-MAC** (encrypt, then MAC the ciphertext under a separate key) over the MAC-then-encrypt shape the second option suggests, and in favor of dedicated authenticated-encryption modes (GCM, CCM) that do both in one pass. The lecture predates that consensus; the *principle* it teaches — separate keys, do not reuse one computation for two jobs — is the part that survived.

## The Other Construction: HMAC

Lecture 4 supplies the second MAC in the course, built on a [[Hash Functions\|hash]] rather than a block cipher. [[HMAC]] exists because the naive keyed hash `H(K|M|padding)` — which is exactly what the [[Hash Function Applications\|message authentication application]] uses — falls to an **extension attack**: a Merkle–Damgard digest is a resumable intermediate state, so anyone holding `H(K|M1|pad)` can compute `H(K|M1|pad|M2|newpad)` **without knowing K**. HMAC's nested digest-inside-a-digest defeats it.

Both constructions give integrity and authentication under a shared key, and **neither gives non-repudiation**. HMAC dominates in practice because hashing is far cheaper than block encryption.

## Why This Follows the Modes Lecture

Reading the [[Block Cipher Modes of Operation|mode comparison table]] with a MAC in mind reorganizes it. Every mode answers "can ciphertext be manipulated profitably?" with some version of *yes*:

- **ECB** — blocks can be reordered wholesale
- **CBC** — a targeted bit flip in one block, at the cost of garbling the previous one
- **OFB / CFB / CTR** — a targeted bit flip with **no collateral damage at all**, which is the worst case, because nothing signals that anything happened

The keystream modes are the clearest demonstration. [[Stream Ciphers]] have **no integrity** as a structural property of XOR: `(M1 XOR PRNG) XOR M2 = (M1 XOR M2) XOR PRNG`, so an attacker who knows anything about the plaintext can flip precisely the bits he wants. Confidentiality and integrity are independent properties, and a mode that delivers the first delivers nothing about the second.

## See Also

- [[Block Cipher Modes of Operation]]
- [[Stream Ciphers]]
- [[Initialization Vector]]
- [[CIA Triad]]
- [[Security Services]]
- [[HMAC]]
- [[Hash Functions]]
- [[Digital Signatures]]
- [[Secret Key Cryptography]]
- [[CSCE 465]]
