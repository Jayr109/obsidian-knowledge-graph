---
title: "Side-Channel Attacks"
type: concept
tags: [csce465, security, cryptography, side-channel, timing-attack, power-analysis]
sources: [csce465-lecture-03a-secret-key-cryptography-i, csce465-lecture-05-public-key-cryptography, csce465-lecture-07-operating-system-security]
course: CSCE 465
updated: 2026-10-08
---

A side-channel attack recovers secrets not from a cipher's inputs and outputs but from the **physical behavior of the machine computing it** — how long it takes, how much power it draws. [[CSCE 465]] closes the secret key lecture with two of them, and the placement is deliberate: after establishing that [[AES]] has no known successful attacks and [[DES]] falls only to brute force, the lecture points out that none of that protects an *implementation*.

This is the concrete form of Lecture 3's claim that [[Cryptography|cryptography is rarely the weakest link]] — the implementation is.

## Timing Attacks

**Measure the time it takes to do operations.**

Some operations, with some operands, are much faster than the same operations with other operand values. Timing therefore provides clues about *what internal operations are being performed* and *what internal data values are being produced.* If a multiplication takes longer when a key bit is 1 than when it is 0, an attacker with a stopwatch reads the key one bit at a time, without ever touching the ciphertext.

Table lookups are a classic source: an S-box entry that is already in the CPU cache returns faster than one that is not, and which entries are cached depends on which inputs were recently used — which depends on the key.

## Power Attacks

**Measure the power consumed to do operations.**

Changing one bit requires considerably less power than changing many bits in a byte. A power trace over time therefore reveals the **Hamming weight** of intermediate values as they are written — and intermediate values in a cipher are functions of the key. With enough traces, statistical analysis (differential power analysis) recovers the key outright.

## The Worked Case: RSA Timing

Lecture 5 develops a timing attack in full. The repeated-squaring loop that computes `m = c^d mod n` performs an extra multiply **only when the current key bit is 1**, so the running time leaks `d` one bit at a time — and the attacker needs no weakness in RSA itself. Of the three countermeasures the lecture lists, only **blinding** removes the correlation between the secret and the observable; fixed delays cost worst-case latency on every operation and random delays only add noise that averaging defeats. See [[RSA]].

## A Physical One: the Cold Boot Attack

Lecture 7 adds a side channel that is not about timing or power but about **matter**. DRAM contents decay after power is cut, but **cooling to −50 °C leaves < 0.2% decay after a minute** — long enough to reboot into a minimal loader and read the encryption key out of RAM. Demonstrated against dm-crypt, LoopAES, BitLocker, FileVault, and TrueCrypt (Halderman et al., USENIX Security 2008): **five full-disk encryption systems, no cipher broken.** The abstract model says memory clears at power-off; the device disagrees for a few seconds. See [[Operating System Security]].

## Why They Matter Structurally

Side channels break an assumption every [[Cipher Security Models|security model]] silently makes: that the attacker sees **only** the inputs and outputs. The abstract cipher is a function from `(plaintext, key)` to `ciphertext`; the physical cipher is a function from `(plaintext, key)` to `(ciphertext, time, power, electromagnetic emission, ...)`. The security proof covers the first function. The attacker gets the second.

Two connections to earlier material:

- **Least common mechanism.** [[Security Design Principles]] listed *side channels* as a reason to minimize shared mechanism — a shared cache, a shared power rail, a shared CPU are all channels between the victim's computation and the attacker's measurement. Timing attacks across a shared cache are exactly that principle's failure mode.
- **Confidentiality of configuration.** [[CIA Triad]] split confidentiality into data, existence, and configuration. Side channels leak *what the machine is doing*, which is configuration confidentiality — the same category as traffic analysis, arriving through the hardware instead of the network.

## Defense

Not covered in the lecture, but implied by the attack descriptions: make the implementation's time and power **independent of the secret**. Constant-time code avoids key-dependent branches and key-dependent memory addresses; hardware countermeasures add noise or balance the power draw. Both are properties of the *implementation*, not the algorithm, which is why a correct AES can still be a broken AES.

## See Also

- [[Block Ciphers]]
- [[Operating System Security]]
- [[RSA]]
- [[AES]]
- [[DES]]
- [[Cryptography]]
- [[Cipher Security Models]]
- [[Security Design Principles]]
- [[Secret Key Cryptography]]
- [[CSCE 465]]
