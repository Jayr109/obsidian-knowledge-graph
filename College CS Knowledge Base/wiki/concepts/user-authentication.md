---
title: "User Authentication"
type: concept
tags: [csce465, security, authentication, identification, challenge-response]
sources: [csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

**Authentication is the process of reliably verifying certain information.** [[CSCE 465]] opens a new unit here — the first after cryptography — and the lecture's framing matters because "authentication" has been used loosely up to this point. Two kinds:

- **User authentication** — allow a user (the **supplicant**) to prove their identity to another entity (the **verifier**: a system, a device)
- **Message authentication** — verify that a message has not been altered without proper authorization

The second is what [[Message Authentication Code|MACs]] and [[Digital Signatures|signatures]] deliver. This lecture is about the first, and it is a different problem: the thing being verified is a *person*, not a bitstring.

## Identification Is Not Authentication

A distinction the lecture draws in four parts, and it is the sharpest thing on the slide:

| | Identification | Authentication |
|---|---|---|
| What is checked | The presented information against **all entities the verifier knows about** | The information against a **single, previously identified** entity |
| Uniqueness | **Must** uniquely identify a given entity, by definition | Does **not** necessarily require uniqueness |

**Identification is a search; authentication is a comparison.** "Who is this?" against a database of everyone versus "is this the person they claim to be?" against one record. The computational shapes differ (1-to-N versus 1-to-1), the error modes differ, and — as [[Biometrics]] shows — a technology good enough for authentication can be useless for identification, because a false-positive rate that is tolerable once becomes a certainty across a million comparisons.

## Four Bases for User Authentication

| Basis | Examples |
|---|---|
| **What the user knows** | Passwords, personal information, a key, a credit card number |
| **Where the user is or can be reached** | Email address, IP address |
| **Physical characteristics of the user** | Fingerprints, voiceprint, signature dynamics, iris pattern, DNA |
| **What the user has in their possession** | Smart card, physical key, USB token |

The lecture asks: *which of the above is best? Best in what way?*

> **Derived.** There is no best, and the second half of the question is the point — the axes genuinely conflict. Knowledge is cheap, revocable, and transmissible (which is also its weakness: it can be shared, stolen, or guessed). Possession cannot be guessed but can be lost or stolen, and costs money per user. Physical characteristics cannot be lost or forgotten but **cannot be revoked** — a leaked fingerprint is leaked permanently — and they raise privacy problems a password does not. Location is the weakest, because network addresses are spoofable.
>
> The practical answer is the lecture's own summary: **combine them.** Two factors drawn from *different* bases fail independently, which is why "a biometric technique with passwords" or a token plus a PIN is the standard for higher security. Two factors from the *same* basis (two passwords) buy much less.

Each basis gets its own treatment: [[Password Authentication]] (what you know), [[Biometrics]] (what you are), [[Authentication Tokens]] (what you have), and the two below.

## Address-Based Authentication

Associates identity with a network or email address — *assume the identity of the source can be inferred from the network address the packets arrive from.* Used by many web services, and by several early OS tools:

- **Berkeley rtools** (`rsh`, `rlogin`, …)
- `/etc/hosts.equiv` — a list of trusted computers
- Per-user `.rhosts` — a list of `<computer, account>` pairs

The lecture asks about benefits and threats, and answers the second itself: **spoofing of network addresses**, because there is **no authentication of source addresses**.

> **The benefit, derived:** convenience and transparency — no password prompt, nothing for the user to remember or type, and it works for automated jobs with no interactive session. That is exactly why the rtools were popular and exactly why they are gone.

This is the same structural flaw as [[Security Attack Taxonomy|fabrication]]: the channel delivers a claim about origin that nothing verifies. IP source addresses are unauthenticated by design in [[Computer Networking|TCP/IP]] — the lecture on [[Cryptography|why security is hard]] named exactly this, *most TCP/IP protocols were not built with security in mind*.

Lecture 12 carries the threat out. [[IP Spoofing]] is the forged address, and [[TCP Session Hijacking]] is the attack that gets a connection accepted under it — exactly what a host trusting `.rhosts` cannot afford.

## Crypto-Based Authentication

> The user performs a requested cryptographic operation on a value (a **challenge**) that the verifier supplies.

Usually reduced to **knowledge of a key** — secret or private. Examples: [[RSA]], zero-knowledge proofs.

This is the **challenge-response** pattern, and the KB has already met it twice: [[Hash Function Applications|the H(R|K) protocol]] from Lecture 4, where `R` is the challenge and `K` the shared secret, and [[Public Key Cryptography|RSA user authentication]], where the private key does the operation. The point of a challenge is freshness — it is what stops a recorded response from being replayed, and it is the one mechanism that proves knowledge of a secret **without transmitting it**.

## The Lecture's Summary

1. **Passwords are by far the most widely used form of authentication, despite numerous problems**
2. **Biometrics hold promise but are expensive, inconvenient, and compromise privacy**
3. **Two factor authentication is commonly used for higher security**
4. **One-time passwords ([[S/Key Protocol|S/Key]]) are attractive, especially if combined with hardware**

## See Also

- [[Password Authentication]]
- [[S/Key Protocol]]
- [[Biometrics]]
- [[Authentication Tokens]]
- [[Hash Function Applications]]
- [[Public Key Cryptography]]
- [[Security Services]]
- [[IP Spoofing]]
- [[TCP Session Hijacking]]
- [[CSCE 465]]
