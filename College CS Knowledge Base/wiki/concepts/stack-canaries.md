---
title: "Stack Canaries"
type: concept
tags: [csce465, security, software-security, stackguard, canary, pointguard, defense]
sources: [csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 465
updated: 2026-10-25
---

A **stack canary** is a known value placed between a function's local variables and its saved return address, checked just before the function returns. [[CSCE 465]] presents it as the concrete instance of [[Buffer Overflow Defenses|code pointer integrity checking]], under its original name **StackGuard** — and then says plainly that it can be defeated.

## The Mechanism

> Embed **"canaries"** in stack frames and verify their integrity **prior to function return**. Any overflow of local variables will **damage the canary**.

The frame layout, with the canary inserted:

```
[ buf ][ canary ][ sfp ][ ret addr ]   [ frame of the calling function ]
  ^        ^        ^        ^
  |        |        |        +-- return execution to this address
  |        |        +----------- pointer to previous frame
  |        +-------------------- checked before every return
  +----------------------------- local variables
```

> **Why position is the entire idea, derived.** The canary does not protect itself and does not detect the overflow when it happens. It works because [[Stack Smashing|stack smashing]] is a **contiguous sequential write** — `strcpy` copies forward byte by byte, so an attacker reaching the return address *must* pass through the canary on the way. The defense converts "detect a corrupted pointer," which is impossible without knowing the correct value, into "detect a changed constant," which is trivial. It is a tripwire, not armor, and everything that follows is about what can step over the wire instead of through it.

## Choosing the Canary Value

Two strategies, defeating two different attackers:

| Kind | Value | Defeats |
|---|---|---|
| **Random canary** | Choose a random canary string on program start | The attacker **can't guess what the value of the canary will be** |
| **Terminator canary** | `\0`, newline, linefeed, EOF | **String functions like `strcpy` won't copy beyond `\0`** |

> **Why both exist, derived.** They cover opposite threats. A random canary stops an attacker who can write arbitrary bytes but cannot read the canary's value. A terminator canary stops an attacker who *knows* the value — it is a published constant — but cannot write it, because the string function doing the copying halts at those very bytes. Neither dominates: a random canary falls to any information leak that discloses it, and a terminator canary falls to any overflow that is not a string copy, such as a `memcpy` with an attacker-controlled length.

## StackGuard in Practice

> - StackGuard requires **code recompilation**
> - Checking canary integrity prior to every function return causes a **performance penalty** — for example, **8% for the Apache web server**
> - **PointGuard** also places canaries next to **function pointers and `setjmp` buffers** — worse performance penalty
> - **StackGuard can be defeated!** — Phrack article by Bulba and Kil3r

PointGuard exists because the plain canary only guards the return address, leaving the [[Heap and Pointer Overflows|function pointer and longjmp]] targets from the attack taxonomy untouched. Extending coverage costs more checks, hence the worse penalty — the same expressiveness-versus-cost trade as everywhere else in the defense list.

> **How the Bulba and Kil3r defeat works, and why it was predictable, derived.** The canary guards the **return address**. It does not guard the other pointers that sit in the same frame — in particular a local **pointer variable** that the function will later write through. An attacker who overflows into such a pointer, and then lets the function perform its own legitimate write, can modify the return address *from the far side of the canary*, never touching it. The tripwire holds; the attacker walks around it. That is the general shape of every canary bypass since: the check is at one location, and the attack moves to another.

## Where It Sits Among the Defenses

| Defense | Coverage | Cost |
|---|---|---|
| [[Buffer Overflow Defenses\|Array bounds checking]] | **Complete** | Every array access |
| **Stack canaries** | Return addresses only | ~8% (Apache), recompilation |
| **PointGuard** | Return addresses + function pointers + setjmp | Higher |
| [[Buffer Overflow Defenses\|Libsafe]] | Return address via `strcpy` only | Low; **no recompilation** |

Canaries are the compromise the industry actually adopted — cheap enough to enable by default, and they turn the overwhelmingly common case into a clean abort rather than a shell. Modern compilers ship this as `-fstack-protector`.

## See Also

- [[Buffer Overflow Defenses]]
- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Heap and Pointer Overflows]]
- [[Unsafe C Functions]]
- [[Shellcode]]
- [[Security Design Principles]]
- [[CSCE 465]]
