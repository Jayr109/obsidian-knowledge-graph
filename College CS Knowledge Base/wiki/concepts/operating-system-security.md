---
title: "Operating System Security"
type: concept
tags: [csce465, security, os, boot, cold-boot, tcb, hibernation]
sources: [csce465-lecture-07-operating-system-security]
course: CSCE 465
updated: 2026-10-08
---

[[CSCE 465]] opens its OS unit from a security angle on material the KB already holds from the systems side. The mechanics of [[Operating Systems|what an OS is]], [[Processes|processes]], [[Virtual Memory|virtual memory]], and [[File Systems|file systems]] come from [[CSCE 313]]; this page is about **where the OS is attacked**, and the lecture's answer is mostly: *before and around it, not inside it.*

The framing it reuses: an OS **provides the interface between the users of a computer and that computer's hardware**, managing how applications access the disk, CPU, main memory, input and output devices, and network interfaces — and managing **multiple users** and **multiple programs**. Every item in that list is a resource to be mediated, and mediation is where access control lives. See [[Access Control Models]].

## The Boot Chain Is the Attack Surface

> Loading an operating system into memory from a powered-off state is **booting** or **bootstrapping**. A computer first executes code stored in firmware known as the **BIOS** (basic input/output system). On modern systems the BIOS loads the **second-stage boot loader**, which loads the rest of the OS and passes control to it.

```
power on -> BIOS (firmware) -> second-stage boot loader -> operating system
```

> **A malicious user could potentially seize execution of a computer at several points in the boot process.**

That sentence is the unit's thesis. Every OS protection mechanism — permissions, ACLs, user separation — is code that *runs once the OS is running*. Anything executing earlier in the chain is outside all of it. The defenses below each address one link.

### BIOS Passwords

To stop an attacker from initiating the first stages of booting, many computers feature a **BIOS password** that does not allow a second-stage boot loader to execute without proper authentication.

This is [[User Authentication|authentication]] moved below the OS, because the OS is not there yet to do it.

### Hibernation

> Modern machines can enter a powered-off state known as **hibernation**. Going into hibernation, the OS stores the contents of the machine's memory into a **hibernation file** (such as `hiberfil.sys`) on disk, so the computer can be restored quickly.
>
> But without additional security precautions, **hibernation exposes a machine to potentially invasive forensic investigation.**

The attack, as the lecture draws it:

```
1. User closes a laptop, putting it into hibernation.
2. Attacker copies hiberfil.sys to discover any unencrypted passwords
   that were in memory when the machine hibernated.
```

The failure is a **change of threat model without a change of protection**. Data in RAM is implicitly protected by [[Virtual Memory|process isolation]] and by being volatile; writing it to disk strips both guarantees at once, and nothing in the OS's permission model was asked about it.

### Cold Boot Attack

> **Capture residual data on RAM** — but it will decay after cutting power. **Slow the decay by cooling:** at **−50 °C, less than 0.2% decay after one minute.**

**Demonstrated against:** Linux dm-crypt, Linux LoopAES, Windows BitLocker, Mac OS FileVault, TrueCrypt.

Citation on the slide: **J. Alex Halderman et al., *Lest We Remember: Cold Boot Attacks on Encryption Keys*, USENIX Security 2008.**

This is the sharpest item in the lecture, and the reason is what it defeats: **full-disk encryption, all five major implementations, without breaking any cipher.** The key must be in RAM for the disk to be readable, so the attacker cools the DRAM, cuts power, reboots to a minimal loader, and reads the key out of the surviving bits.

Note where this sits in the course's running argument. It is a physical [[Side-Channel Attacks|side channel]] — the abstract model says RAM contents vanish at power-off, and the physical device disagrees for a few seconds. And it is another confirmation of [[Cryptography|"cryptography is rarely the weakest link"]]: BitLocker's AES is not what failed.

### Measured / Trusted Boot with a TCB

The lecture's answer to the whole chain:

> **Trusted Compute Base (TCB): root of trust.**

> **Derived, since the slide is a diagram with little text.** The idea is to make each stage of the boot chain *measure* (hash) the next before transferring control, anchoring the chain in a small piece of hardware that cannot be rewritten. Because each link verifies the one after it, tampering anywhere produces a measurement that does not match the expected value, and the chain can refuse to proceed or refuse to release secrets.
>
> The TCB is the part you have to trust because nothing else can check it — making it **small** is the whole design goal, which is [[Security Design Principles|economy of mechanism]] applied to trust itself. The less code in the root of trust, the less there is to verify by hand and the less there is to get wrong.

> **Visual gap:** the measured/trusted boot slide is a diagram whose text layer carries only the TCB definition. The specific stages and measurement flow it depicts are not recoverable.

## Event Logging

> Keeping track of what processes are running, what other machines have interacted with the system over the Internet, and whether the OS has experienced unexpected or suspicious behavior can leave important clues — not only for troubleshooting ordinary problems, but **for determining the cause of a security breach.**

This is [[Security Design Principles|compromise recording]] at the OS level, and [[Security Policy and Mechanism|detection]] rather than prevention. The caveat from Lecture 2 applies directly: detection *requires that the audit trail be protected from alteration*, so a log an attacker can edit after gaining root detects nothing.

## What This Unit Covers

| Topic | Page |
|---|---|
| Access control models and policy | [[Access Control Models]] |
| Unix/Linux permissions, special bits, octal notation | [[Unix File Permissions]] |
| Windows NTFS permissions and inheritance | [[NTFS Permissions]] |

## See Also

- [[Access Control Models]]
- [[Buffer Overflow]]
- [[Buffer Overflow Defenses]]
- [[Security Models]]
- [[Safety Problem]]
- [[Unix File Permissions]]
- [[NTFS Permissions]]
- [[Operating Systems]]
- [[Virtual Memory]]
- [[File Systems]]
- [[Side-Channel Attacks]]
- [[Security Design Principles]]
- [[Host-Based Intrusion Detection]]
- [[CSCE 465]]
