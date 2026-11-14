---
title: "Stack Smashing"
type: concept
tags: [csce465, security, software-security, buffer-overflow, stack, return-address, nop-sled]
sources: [csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 465
updated: 2026-10-25
---

**Stack smashing** is the first-generation [[Buffer Overflow|buffer overflow]] attack and the one the rest are measured against: overflow a local buffer until the write reaches the **saved return address**, and replace it with an address pointing back into the buffer. When the function returns, the CPU jumps to the attacker's data and executes it.

## The Stack Frame

The stack is composed of **frames**, and it usually **grows toward lower memory addresses**. The **stack pointer (SP, `%esp`)** points to the top of the stack — usually the last valid address.

A frame, from high addresses down:

```
        Parameters              <- arguments to the function
        Return address          <- where to resume after the call
        Stack frame pointer     <- pointer to the previous frame
        Local variables
                                <- SP (%esp)
   |
   v  stack growth
```

The layout itself is [[CSCE 313]] material — see [[Processes|the process address space]] and [[Process Attributes]] for registers and the PCB. What matters here is one consequence of it: **the return address sits at a higher address than the local buffers**, and buffers are written **upward**. So overflowing a local buffer walks straight into the saved frame pointer and then the return address.

## The Vulnerable Function

The lecture's example, a function in a hypothetical web server:

```c
void func(char *str) {
    char buf[126];
    strcpy(buf, str);
}
```

- `char buf[126]` allocates a local buffer — **126 bytes reserved on the stack**
- `strcpy(buf, str)` copies the argument into the local buffer

When `func` is invoked, a new frame with local variables is pushed. The frame looks like this, with the stack growing left to right in the lecture's diagram:

```
[ buf ][ sfp ][ ret addr ][ str ]
  ^      ^        ^          ^
  |      |        |          +-- argument
  |      |        +------------- execute code at this address after func() finishes
  |      +---------------------- pointer to previous frame
  +----------------------------- local buffer (126 bytes)
```

## Overstuffing It

> **`strcpy` does NOT check whether the string at `*str` contains fewer than 126 characters.**

If a string longer than 126 bytes is copied in, it overwrites adjacent stack locations — the saved frame pointer first, then the return address. Whatever bytes land in the return-address slot **will be interpreted as the return address**.

That alone is a crash. The attack comes from controlling those bytes.

## Executing Attack Code

> Suppose the buffer contains an attacker-created string — for example, `*str` contains a string received from the network as input to some network service daemon.

The attacker puts **actual assembly instructions** into the input string — the binary encoding of `execve("/bin/sh")`, see [[Shellcode]] — and arranges that in the overflow, **a pointer back into the buffer appears in the location where the system expects to find the return address**.

```
[ code ][ ... ][ ret -> points back into buffer ][ str ]
```

When the function exits, the code in the buffer is executed, **giving the attacker a shell — a root shell if the victim program is [[Unix File Permissions|setuid root]]**.

## The Attack Procedure

The lecture's high-level recipe:

1. Compile the attack code
2. Extract the binary for the piece that actually does the work — the [[Shellcode|shell code]]
3. Insert the compiled code into the buffer
4. Figure out **where** the overflow code should jump
5. Place that address in the buffer at the proper location so the normal return address gets overwritten

Steps 4 and 5 are where real exploits fail.

## The Hard Part: Guessing the Buffer Address

> The value in the RET position **must point to the beginning of the attack assembly code** in the buffer. Otherwise the application will crash with a segmentation violation.

And the attacker must correctly guess **in which stack position the buffer will be** when the function is called. The lecture is blunt that this is usually unknown:

- In most cases the address of the buffer is not known
- It has to be **guessed**, and the guess must be **very precise**
- Given the same environment, and knowing the size of the command-line arguments, the address of the stack can be **roughly** guessed
- The attacker must also guess the **offset of the buffer with respect to the stack pointer**

The stack address of a program can be obtained with:

```c
unsigned long get_sp(void) {
    __asm__("movl %esp, %eax");
}
```

> **Why this helper works at all, derived.** It reads the attacker's *own* `%esp` on the *same machine and environment*, then assumes the victim's stack starts in the same place. That assumption held for decades because the stack base was a fixed constant per platform — the same program loaded at the same address on every machine. It is precisely this assumption that [[Buffer Overflow Defenses|ASLR]] destroys, and the reason the lecture's answer to "same address on many machines" is **artificial diversity**.

## The NOP Sled

The fix for an imprecise guess:

> Use a series of **NOPs** at the beginning of the overflowing buffer so that the jump **does not need to be exactly precise**. This technique is called a **no-op sled**.

```
[ NOP NOP NOP ... NOP ][ shellcode ][ ... ][ ret -> anywhere in the NOPs ]
```

> **What the sled actually buys, derived.** It converts a single correct address into a **range** of correct addresses. Landing anywhere in the NOP region causes the CPU to slide forward instruction by instruction — each NOP does nothing — until it reaches the real payload. A 200-byte sled turns a one-in-a-million guess into a one-in-five-thousand guess. It does not make the attack reliable so much as make it **repeatable**, which for a worm is the same thing.

## See Also

- [[Buffer Overflow]]
- [[Shellcode]]
- [[Heap and Pointer Overflows]]
- [[Unsafe C Functions]]
- [[Buffer Overflow Defenses]]
- [[Stack Canaries]]
- [[GDB]]
- [[Processes]]
- [[Process Attributes]]
- [[Unix File Permissions]]
- [[CSCE 465]]
