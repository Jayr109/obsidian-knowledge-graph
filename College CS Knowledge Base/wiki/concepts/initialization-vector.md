---
title: "Initialization Vector"
type: concept
tags: [csce465, security, cryptography, iv, cbc, modes]
sources: [csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation]
course: CSCE 465
updated: 2026-09-22
---

An **initialization vector (IV)** is the starting value that seeds a [[Block Cipher Modes of Operation|chained or keystream mode]] — CBC, OFB, CFB, and CTR all need one. [[CSCE 465]] states its two defining properties in one line, and the second is the one students get wrong:

- **Used along with the key** — it enters the computation the way key material does
- **Not secret** — it may be transmitted in the clear alongside the ciphertext

The IV is not a second key. It is a *uniqueness* parameter, and it must be handled by rules about repetition rather than rules about secrecy.

## What It Buys

> For a given plaintext, changing **either the key or the IV** will produce a different ciphertext.

The lecture asks: *why is that useful?*

> **Derived, not stated on the slide.** Without an IV, encrypting the same message twice under the same key produces identical ciphertext — so an eavesdropper learns that the two messages are the same without decrypting either. That is real leakage: "the general sent the same order again" is often the whole intelligence. Worse, an attacker who ever learns one plaintext can recognize it forever, and short predictable messages ("ATTACK", "YES") become a lookup table.
>
> A fresh IV per message makes encryption **non-deterministic from the attacker's view**: the same plaintext under the same key produces unrelated ciphertext every time. This is exactly the property listed as "identical plaintext blocks produce different ciphertext blocks" on the CBC, OFB, CFB, and CTR property slides — and it is what [[Block Cipher Modes of Operation|ECB]], which has no IV, fails at.

## Generating and Sharing It

The lecture gives two approaches:

| Approach | How it is shared |
|---|---|
| **Random** | May be transmitted with the ciphertext |
| **Incremental** | Predictable by receivers — no transmission needed |

Both work because the IV is not secret. The trade is bandwidth against predictability, and the right choice depends on the mode.

> **Worth knowing, and not in this lecture:** *unique* and *unpredictable* are different requirements, and modes differ in which they need. CBC needs the IV to be **unpredictable** — an attacker who can guess the next IV before choosing a plaintext can mount a chosen-plaintext attack (this is the BEAST attack on TLS 1.0, which used the previous message's last ciphertext block as the next IV). CTR needs only **uniqueness**, since its counter is expected to be predictable by design. So "incremental" is fine for CTR and dangerous for CBC.

## The Absolute Rule for Keystream Modes

For [[Block Cipher Modes of Operation|OFB, CFB, and CTR]] the lecture states the consequence flatly:

> If you know one plaintext/ciphertext pair, you can easily derive the one-time pad that was used — i.e., **should not reuse a one-time pad.** **Conclusion: IV must be different every time.**

In a keystream mode the IV determines the entire keystream. Reusing an IV reuses the pad, and reusing the pad reproduces the [[One-Time Pad|one-time pad's]] catastrophic failure exactly: `C1 XOR C2 = M1 XOR M2`, and the key cancels. See [[Stream Ciphers]] for the same failure in its native setting — and WEP, which repeated IVs on a 24-bit counter, for what it costs in practice.

**An IV is public but must never repeat under the same key.** Both halves of that sentence are load-bearing, and they are the halves people reverse.

## See Also

- [[Block Cipher Modes of Operation]]
- [[Stream Ciphers]]
- [[One-Time Pad]]
- [[Message Authentication Code]]
- [[Secret Key Cryptography]]
- [[CSCE 465]]
