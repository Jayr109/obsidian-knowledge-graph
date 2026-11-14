---
title: "Buffer Overflow"
type: concept
tags: [csce465, security, software-security, buffer-overflow, memory-safety, exploitation]
sources: [csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 465
updated: 2026-10-25
---

A **buffer overflow** occurs when a program writes data outside the bounds of allocated memory. [[CSCE 465]] opens its **software security** unit here, and the reason is stated flatly on the second slide: buffer overflow is **still the most common source of software vulnerability**. This page is the unit's hub — the anatomy of the attack and the taxonomy of its variants; the mechanics live on [[Stack Smashing]], [[Heap and Pointer Overflows]], [[Format String Vulnerabilities]], and [[Buffer Overflow Defenses]].

## The Definition, and Why It Is Exploitable

> A buffer overflow occurs when a program writes data **outside the bounds of allocated memory**.
>
> Buffer overflow vulnerabilities are exploited to **overwrite values in memory to the advantage of the attacker**.

A **buffer** is a data storage area inside memory — on the stack or the [[Virtual Memory|heap]] — intended to hold a pre-defined amount of data. If more data is stuffed into it, **it spills into adjacent memory**. And if executable code is supplied as "data," the victim's machine may be fooled into executing it.

> **The one-sentence version, derived.** C does not store the length of an array alongside it, so a write past the end is not an error the language can detect — it is just a write to whatever happens to live next. The vulnerability is not that the write *fails*; it is that it **succeeds against the wrong memory**. Everything else on this page is a consequence of which memory sits next to the buffer.

## Impact

- First widely seen in the first computer worm — the **Morris Worm** (1988, **6,000 machines infected**)
- Behind some of the most devastating worms and viruses in recent history: **Zotob, Sasser, CodeRed, Blaster, SQL Slammer, Conficker, Stuxnet**

That list spans 1988 to 2010 and the mechanism did not change. It is the strongest argument in the course for [[Security Design Principles|designing against a class of bug rather than patching instances]].

## The Attack's Goal

> **Goal:** subvert the function of a **privileged** program so that the attacker can take control of that program — and if the program is sufficiently privileged, thence **control the host**.

The word *privileged* is doing the work. Overflowing a program that has no more rights than the attacker already holds buys nothing. This is why [[Unix File Permissions|setuid root]] binaries are the classic target: the lecture's payoff is a **root shell if the victim program is setuid root**.

## The Two Halves of Every Exploit

Every buffer overflow attack involves exactly two things:

1. **Code present in the program's address space**
2. **Transfer of execution to that code**

### Half One — Getting Code Into the Address Space

Two strategies, and the second is the one that defeats most naive defenses:

| Strategy | How |
|---|---|
| **Inject user code** | Provide a string as input which the program stores in a buffer. The string contains **native CPU instructions** for the platform being attacked. Works with buffers stored anywhere. See [[Shellcode]]. |
| **Use what's already there** | The code of interest is already part of the program. The attacker only needs to **call it with the desired arguments** before jumping to it. |

The lecture's example of the second: an attacker who wants a shell may find that some library already contains a call to `exec(arg)`. The attacker needs only to pass a pointer to the string `"/bin/sh"` and jump to the `exec` call. **No injected code at all** — which is why [[Buffer Overflow Defenses|marking the stack non-executable]] does not end the problem.

### Half Two — Transferring Execution

Three targets, all of them pointers the program will later dereference:

| Target | Technique |
|---|---|
| **Activation records** | The stack frame stores the **return address** of a function. The attacker modifies it to point at their code. This is **[[Stack Smashing\|stack smashing]]**. |
| **Function pointers** | Same idea against an arbitrary function pointer rather than a return address. See [[Heap and Pointer Overflows]]. |
| **Longjmp buffers** | The attacker modifies the `setjmp`/`longjmp` buffer so the jump lands in their code. |

> **The unifying observation, derived.** None of these three overwrite *instructions* — the text section is read-only and modifying it faults. They all overwrite a **stored address that the CPU will later load into the program counter**. A buffer overflow is therefore best understood not as "corrupting code" but as **corrupting the data that decides where code runs next**. That reframing is what makes [[Stack Canaries|canaries]] and code-pointer-integrity checking the natural defenses: they guard the pointer, not the buffer.

## Three Generations

The lecture gives the attack classes in the order they were discovered, which is also roughly the order of difficulty:

| Generation | Techniques |
|---|---|
| **First** | [[Stack Smashing\|Stack smashing]] |
| **Second** | Heaps, function pointers, off-by-one |
| **Third** | Format strings and heap management structures |

Each generation appeared after defenses blunted the one before it — a pattern the course has already shown in cryptography, where every broken cipher was replaced by one designed against the specific break.

## What Happens When Memory Outside a Buffer Is Accessed

Not every overflow is exploitable; the lecture enumerates the outcomes:

- **If memory doesn't exist** — bus error
- **If memory protection denies access** — page fault, segmentation fault, or general protection fault
- **If access is allowed** — the memory next to the buffer **can be accessed**: heap, stack, and so on

Only the third case is a vulnerability. The first two are crashes, which are availability problems rather than control-flow ones. The attacker's craft is largely in arranging to land in case three.

For the address-space layout this depends on — text, data, heap, stack — see [[Processes|the process address space]] and [[Virtual Memory]] from [[CSCE 313]]; this unit does not restate it.

## See Also

- [[Stack Smashing]]
- [[Shellcode]]
- [[Heap and Pointer Overflows]]
- [[Format String Vulnerabilities]]
- [[Unsafe C Functions]]
- [[Buffer Overflow Defenses]]
- [[Stack Canaries]]
- [[GDB]]
- [[Operating System Security]]
- [[Security Design Principles]]
- [[Processes]]
- [[Virtual Memory]]
- [[CSCE 465]]
- [[Malware]]
- [[Notable Worms]]
