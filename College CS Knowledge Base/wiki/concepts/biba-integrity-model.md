---
title: "Biba Integrity Model"
type: concept
tags: [csce465, security, biba, integrity, low-water-mark, information-flow]
sources: [csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

**Biba** is the integrity dual of [[Bell-LaPadula Model|Bell-LaPadula]]: the same lattice machinery, the rules turned upside down. Where BLP asks *who may read this*, Biba asks *who may write this* — and [[CSCE 465]] motivates the swap with one line worth keeping: *you may not care who can read DNS records, but you better care who writes to them.* Its slogan is **"no read down, no write up."**

## Integrity Levels Are Not Security Levels

> **I** is a set of **integrity levels**, with a function `i: S ∪ O → I`.
>
> **Important point: integrity labels are different from security labels.**
>
> - Security labels limit the **flow** of information
> - Integrity labels inhibit **modification** of information

Both label the same subjects and objects, and a real system carries both independently. A document can be highly classified and completely untrustworthy.

**The higher the level, the more confidence:**

- that a program will execute correctly
- that data is accurate and/or reliable

The lecture flags the relationship directly: **integrity level is trustworthiness**. That reframing is what makes the rules read naturally.

## The Rules

> Biba defined a **dual of secrecy for integrity** — a lattice policy with **"no read down, no write up."**

The lecture's monastic example, which is the clearest statement of both halves:

| Rule | Statement | Example |
|---|---|---|
| **No write up** | Users can only **create** content at or **below** their own integrity level | A monk may write a prayer book that can be read by commoners, but not one to be read by a high priest |
| **No read down** | Users can only **view** content at or **above** their own integrity level | A monk may read a book written by the high priest, but may not read a pamphlet written by a lowly commoner |

> **Why "no read down" is the strange one, derived.** Forbidding write-up is intuitive — a low-trust subject must not touch a high-trust file. Forbidding *read*-down is not, because reading changes nothing. The justification is **contamination**: a high-integrity process that reads low-integrity data and acts on it has laundered untrusted input into a trusted context. That is not an abstraction. It is exactly a trusted program parsing attacker-controlled input, which is where most of the [[Operating System Security|software security]] unit's bugs live. Biba's answer is to forbid the read outright; the real-world answer is input validation, which is the same rule enforced by hand and usually enforced badly.

## Biba Against BLP

| | [[Bell-LaPadula Model\|BLP]] | **Biba** |
|---|---|---|
| Protects | [[CIA Triad\|Confidentiality]] | [[CIA Triad\|Integrity]] |
| Read | No read **up** | No read **down** |
| Write | No write **down** | No write **up** |
| Information flows | **Up** the lattice | **Down** the lattice |

The two are exact mirrors, which has a consequence the lecture leaves implicit: **run both at once over one lattice and nothing can move at all.** A subject could then read and write only at its own exact level. Practical systems avoid this by using two *separate* lattices — a secrecy lattice and an integrity lattice, labelled independently — which is why the "integrity labels are different from security labels" slide is not a pedantic aside.

## Example Left Open

Slide 35 re-poses the BLP cast — Alice, Bob, Charlie over DocA, DocB, DocC — under the integrity rules and asks **"which users can modify what documents?"**, answering only with `?????`. It is an in-class exercise; the deck records no answer, and none is invented here. Note that it reuses the *confidentiality* labels from slide 28, so working it requires first deciding whether those pairs are being read as integrity levels — which is the point the exercise is probably making.

## Low-Water Mark Integrity

A dynamic variant that relaxes the read rule instead of enforcing it:

> - Change integrity level based on **actual dependencies**
> - A subject is initially at the **highest** integrity
> - But the integrity level **can change** based on objects accessed
> - Ultimately, the subject has the integrity of the **lowest object read**

So rather than forbidding a read-down, the system permits it and **demotes the reader** to match. The subject's level only ever falls — hence "low-water mark."

> **The trade, derived.** Strict Biba fails closed: the read is refused and the program breaks. Low-water mark fails open and tracks the damage: the program runs, but having touched untrusted data it is now itself untrusted and loses the right to write anywhere high. That is taint tracking, built into the access control model. The cost is monotonic decay — a long-running process that reads one low-integrity file is permanently demoted, which in practice means a daemon can poison itself and need a restart to recover.

## See Also

- [[Bell-LaPadula Model]]
- [[Multi-Level Security]]
- [[Security Models]]
- [[Chinese Wall Model]]
- [[Access Control Matrix]]
- [[CIA Triad]]
- [[Operating System Security]]
- [[CSCE 465]]
