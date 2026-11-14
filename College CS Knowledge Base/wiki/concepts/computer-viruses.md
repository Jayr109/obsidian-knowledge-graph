---
title: "Computer Viruses"
type: concept
tags: [csce465, security, malware, virus, macro-virus, antivirus, polymorphism]
sources: [csce465-lecture-11-malware]
course: CSCE 465
updated: 2026-11-04
---

A **virus** infects a program by modifying it, copying itself into that program so it runs whenever the host does. [[CSCE 465]] places it on the *needs a host program* side of the [[Malware|malware taxonomy]], and the defining constraint follows from that: **a virus requires user action to spread.**

## The Four Stages

> - **Dormant** phase
> - **Propagation** phase — e.g. attachment to email
> - **Triggering** phase
> - **Execution** phase

Not every virus uses all four; the dormant and triggering phases are what make a virus a [[Malware|logic bomb]] as well.

## Virus Structure

The lecture's pseudo-structure, which is worth reading as a program:

> - **First line:** go to "main" of virus program
> - **Second line:** a special mark (infected or not)
> - **Main:**
>   - find uninfected programs — **infect and mark them**
>   - do something damaging to the system
>   - now "go to" the first line of the original program — **appear to do the normal work**
> - Avoid detection by looking at size of program: **compress/decompress the original program**

Three design decisions are visible here, and each is a response to a way of being caught:

| Feature | Defeats |
|---|---|
| The **special mark** | Re-infecting the same file, which wastes time and makes the infection obvious |
| Jumping back to the **original program** | The user noticing that the program stopped working |
| **Compressing** the host | The user or a checksum noticing the file grew |

> **The mark is also the weakness, derived.** The infection marker exists so the virus can tell infected files from clean ones — but it is a constant the virus writes into every file it touches, which makes it exactly the **signature** a scanner looks for. The feature that keeps the virus efficient is the feature that makes it detectable, and **polymorphism** below is the response to that. Note too what the lecture flags about repeated infection: when the Morris Worm's equivalent check failed, the result was resource exhaustion that gave the whole thing away. See [[Notable Worms]].

## Types

- **Parasitic virus** — searches for and infects executable files
- **Memory-resident virus** — infects running programs
- **Boot sector virus** — spreads whenever the system is booted
- **Polymorphic virus** — **encrypts part of the virus program using a randomly generated key**, so the bytes differ between copies and no fixed signature matches

## Macro Viruses

> A **macro** is an executable program (e.g. opening a file, starting an application) embedded in a word processing document, e.g. MS Word.

The spreading technique:

1. A virus macro is attached to a Word document
2. The document is loaded and opened on the local system
3. When the macro executes, it **copies itself to the global macro file**
4. The global macro can be activated and spread when **new documents are opened**

> **Why macro viruses mattered so much, derived.** They broke the assumption users had been taught to rely on — that *documents* are data and only *programs* are dangerous. Once a document format is also an execution format, the distinction collapses, and the infection travels through exactly the files people email each other without thinking. The step that does the damage is step 3: jumping from one document into the **global** macro file turns a single opened attachment into an infection of the application itself. It is the same structural error as a [[Buffer Overflow|buffer overflow]] — attacker-supplied *data* being treated as *code* — one layer up.

## Truths and Myths

The lecture lists these together, deliberately unlabelled, as a *"truth and myths"* slide:

> - Can only infect Microsoft Windows
> - Can modify hidden and read-only files
> - Spread only on disks or in email
> - Cannot remain in memory after reboot
> - Cannot infect hardware
> - Can be malevolent, benign, or benevolent

> **Which are which, derived — the deck does not mark them.** *Can only infect Windows* is false; Windows is the biggest target, not the only possible one. *Can modify hidden and read-only files* is **true** — those attributes are advisory metadata, not an access control check, and malware running with the user's rights can simply clear them. *Spread only on disks or in email* is false: network shares, documents, boot sectors and open services all carry infections. *Cannot remain in memory after reboot* is false — anything that writes itself into the boot path survives, which is what a boot sector virus is for. *Cannot infect hardware* is false in the sense that matters: firmware is writable, and [[Stuxnet]] is the course's own demonstration that code can reach programmable controllers. *Can be malevolent, benign, or benevolent* is **true**, and the Welchia counter-worm on [[Notable Worms]] is the cautionary case — written to patch machines, it did more damage than the worm it hunted.

## The Antivirus Approach

> - **Prevention** — limit contact with the outside world
> - **Detection and identification**
> - **Removal**

And four generations of antivirus software:

| Generation | Technique |
|---|---|
| 1 — **Simple scanners** | Use **signatures** of known viruses |
| 2 — **Heuristic scanners** | **Integrity checking**: checksum, encrypted hash |
| 3 — **Activity / behavior** | Watch what the program does |
| 4 — **Full-featured protection** | Combination of the above |

The progression is a direct response to the evasion techniques above. Signatures fail against polymorphism, so generation 2 checks whether files *changed* rather than what they contain — note that this is [[Hash Functions|hashing]] used for [[CIA Triad|integrity]], and that the hash must itself be protected, the same caveat [[Security Policy and Mechanism|Lecture 2]] attached to audit logs. Integrity checking fails against malware that infects before the baseline is taken, so generation 3 watches behaviour instead.

[[Notable Worms|Nimda]] is where this chain visibly breaks: a brand-new infection has no signature, and the lecture names **zero-day detection** as the resulting open problem.

## See Also

- [[Malware]]
- [[Worms]]
- [[Notable Worms]]
- [[Botnets]]
- [[Stuxnet]]
- [[Buffer Overflow]]
- [[Hash Functions]]
- [[CIA Triad]]
- [[CSCE 465]]
