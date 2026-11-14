---
title: "Authentication Tokens"
type: concept
tags: [csce465, security, authentication, tokens, smart-card, two-factor]
sources: [csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

A **token is a physical device that can be interfaced to the computer, and carries identifying information** — the "what the user *has*" basis of [[User Authentication]]. [[CSCE 465]] closes the authentication lecture here, and the reason is in its summary: one-time passwords are *attractive, especially if combined with hardware.*

## Passive vs. Active

| Type | Capability |
|---|---|
| **Passive tokens** | Just **store** information |
| **Active tokens** | Have **processors** and can perform **cryptographic operations** |

That line is the whole security difference. A passive token is a container — whatever it holds can be read out and copied, so it is only as strong as the secrecy of its contents. An active token **never reveals its secret**; it performs an operation with it and returns the result, which is the [[User Authentication|challenge-response]] pattern moved into hardware. A cloned passive token is as good as the original; an active token cannot be cloned by reading it.

**Examples:** cards with magnetic strips, smart cards, USB storage devices, RFID tags.

Note that list spans both types — a magnetic strip and a USB stick are passive, a smart card is active.

## Design Issues

- **Cost**
- **Size**
- **Capabilities**
- **Robustness**
- **Resistance to tampering**
- **Usefulness if stolen or lost**

The last two are the security-relevant pair, and they pull against the first. *Resistance to tampering* is what keeps an active token's key from being extracted in a lab — and it is expensive, which is why cheap tokens are passive. *Usefulness if stolen* is the argument for pairing a token with a PIN: possession alone should not authenticate, because possession is exactly what is lost. That is two-factor authentication arising from a design constraint rather than from a policy.

## Time-Synchronized Tokens

The lecture's worked example. The token contains:

- an **internal clock**
- a **display**
- a **secret key**

```
token computes a one-way function of (current time + key)  -->  displays the result
value changes about once per minute
user reads the value and types it in to authenticate to the server
```

**Requirement: the server and token clocks must stay synchronized.**

> **What makes this work, and what it costs.** The server holds the same key and computes the same function, so it can check the displayed value without the token ever transmitting anything — there is no channel between token and server at all, which is why a purely optical, battery-powered device suffices. The time *is* the challenge, which removes the round trip that [[Hash Function Applications|challenge-response]] normally needs.
>
> The price is the clock. Drift must be tolerated (so the server accepts a window of values, slightly widening the guess space), and a token whose clock has drifted too far stops working entirely. Compare [[S/Key Protocol|S/Key]], which needs no clock but does need a finite chain and a counter the two sides agree on: **one trades a synchronization requirement for a state requirement.**

This is also why a time-synchronized token resists everything in the [[Password Authentication|other attacks]] list that a password does not. Keylogging a value that expires in sixty seconds is nearly worthless; so is phishing one.

## Aladdin eToken

The deck's concrete product specification, recorded as given:

| | |
|---|---|
| **API / standards** | PKCS#11 v2.01, CAPI (Microsoft Crypto API), Siemens/Infineon APDU commands, PC/SC, X.509 v3 certificate storage, SSL v3, IPSec/IKE |
| **Security algorithms** | RSA 1024-bit / 2048-bit, DES, 3DES, SHA1 |
| **Power source** | Battery, 5-year lifetime |
| **LCD** | 6 characters |
| **Data retention** | 10 years |

Worth reading as a snapshot of the era: the algorithm list is precisely the set this course has covered — [[RSA]], [[DES]], [[Triple DES]], [[SHA-1]] — and **X.509 v3 certificate storage** means the token is a [[Public Key Infrastructure|PKI]] endpoint, holding a private key that never leaves the device. That is the active-token argument in product form.

## See Also

- [[User Authentication]]
- [[S/Key Protocol]]
- [[Password Authentication]]
- [[Biometrics]]
- [[Public Key Infrastructure]]
- [[Hash Function Applications]]
- [[CSCE 465]]
