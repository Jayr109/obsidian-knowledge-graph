---
title: "Buffer Overflow Defenses"
type: concept
tags: [csce465, security, software-security, defense, nx, aslr, bounds-checking, libsafe]
sources: [csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 465
updated: 2026-10-25
---

[[CSCE 465]] closes the software security unit with five defense families against [[Buffer Overflow|buffer overflow]]. None of them is complete, and the lecture says so for each in turn — which makes this the clearest worked example in the course of **defense in depth** being a consequence of individual defenses failing differently.

> - Writing correct code
> - Non-executable buffers
> - Randomize stack location, or encrypt the return address on the stack by XORing with a random string
> - Array bounds checking
> - Code pointer integrity checking

## 1. Writing Correct Code

Covered on [[Unsafe C Functions]]: safe languages, compiler warnings, static analysis, black-box testing with long strings, and replacing `gets`/`strcpy` with `getline`/`strlcpy`. The unanswered question the lecture itself raises is **"what about legacy C code?"** — which is why the other four exist.

## 2. Non-Executable Buffers

> Works by marking a region of memory as **non-executable**. To stop buffer overflow exploits, the data section has to be marked non-executable.
>
> Problem with recent systems, since they emit executable code within the data section — but **more applicable to the stack segment, since no legitimate program has code in the stack**.

### Non-Executable Stack

- **NX bit** on every page table entry — AMD Athlon 64, Intel P4 "Prescott", **but not 32-bit x86**
- Code patches marking the stack segment non-executable exist for Linux, Solaris, OpenBSD

Three stated limitations:

- **Some applications need an executable stack** — for example, LISP interpreters
- **Does not defend against return-to-libc exploits** — overwrite the return address with the address of an *existing* library function, which can still be harmful
- **Nor against heap and function pointer overflows**

> **Why return-to-libc defeats NX by construction, derived.** NX enforces a partition between "memory that holds data" and "memory that holds code." Return-to-libc never violates it: the attacker executes **only code that was already marked executable** — `libc` itself — and supplies only data. The defense assumes the attacker must bring their own code, and the [[Buffer Overflow|*use what's already there*]] strategy was in the attack taxonomy from the start. NX raises the cost of one of two strategies and does nothing to the other.

## 3. Address Randomization

### The Motivation

> Buffer overflow and return-to-libc exploits need to know the **virtual address** to which to pass control — the address of attack code in the buffer, or the address of a standard kernel library routine. **The same address is used on many machines.**
>
> **Slammer infected 75,000 MS-SQL servers using the same code on every machine.**
>
> Idea: introduce **artificial diversity** — make stack addresses, addresses of library routines, and so on unpredictable and different from machine to machine.

That Slammer figure is the argument in one number: a monoculture of addresses is what makes one working exploit into a worm.

### ASLR

> **Address Space Layout Randomization** — arranging the positions of key data areas randomly in a process's address space: the base of the executable and the position of libraries (libc), heap, and stack.
>
> **Effect:** for return-to-libc, the attacker needs to know the address of the key functions.
>
> **Attacks:** repetitively guess the randomized address; spray injected attack code.
>
> **Almost all modern operating systems** (Windows / Linux / Mac) have implemented ASLR.

The lecture also mentions the related trick of **encrypting the return address on the stack by XORing it with a random string**, so the attacker cannot write a usable value even knowing the target.

> **What ASLR actually changes, derived.** It does not make the exploit impossible — it makes it **probabilistic**, and it interacts directly with the [[Stack Smashing|NOP sled]]. A sled widens the target; randomization moves the target. The two are in direct tension, and the winner depends on how many bits of entropy the OS can afford versus how large a sled the input buffer can hold. This is also why "repetitively guess" is listed as an attack: against a network service that **restarts after a crash**, the attacker gets unlimited retries and randomization only costs time. ASLR is strongest exactly where crashes are noticed.

## 4. Array Bounds Checking

> - **Completely stops BO attacks**
> - All reads and writes to arrays will be bounds-checked. This is the case with memory-safe languages like **Java and .NET languages**
> - **Solves the problem at the cost of performance**

The only defense on the list the lecture describes as complete. It is also the only one that cannot be retrofitted to a C binary.

## 5. Code Pointer Integrity Checking

> Works by **detecting whether a code pointer — e.g. a return address — has been corrupted before dereferencing it**.
>
> - Prevents only BO attacks exploiting **automatic** (stack) buffers
> - **Much better performance** than array bounds checking
> - E.g. **StackGuard**

The trade against bounds checking is explicit: bounds checking validates **every array access** and stops everything; pointer integrity validates **one word per function return** and stops the subset that goes through a return address. See [[Stack Canaries]].

## Run-Time Checking: Libsafe

A sixth mechanism the lecture presents separately, notable because it needs **no recompilation**:

> - A **dynamically loaded library**
> - Intercepts calls to `strcpy(dest, src)`
> - Checks if there is sufficient space in the current stack frame: `|frame-pointer – dest| > strlen(src)`
> - If yes, does the `strcpy`; else **terminates the application**

```
   libsafe interposes here
        |
  [ buf ][ sfp ][ ret-addr ]   <- current frame
   dest  ^
         +-- distance from dest to the frame pointer is the real space available
```

> **The insight and its limit, derived.** Libsafe cannot know how big `buf` is — that information is gone by the time the binary runs. So it substitutes a bound it *can* compute: the distance from the destination to the **frame pointer**, which is an upper bound on any local buffer's size. That is enough to guarantee the return address is never reached, which is precisely the [[Stack Smashing|stack smashing]] condition. The cost of the approximation is that it permits overflows *within* the frame — one local buffer may still clobber another — so Libsafe protects the control flow without protecting the data.

## See Also

- [[Buffer Overflow]]
- [[Stack Canaries]]
- [[Stack Smashing]]
- [[Shellcode]]
- [[Unsafe C Functions]]
- [[Heap and Pointer Overflows]]
- [[Format String Vulnerabilities]]
- [[Security Design Principles]]
- [[Operating System Security]]
- [[Virtual Memory]]
- [[CSCE 465]]
- [[Notable Worms]]
