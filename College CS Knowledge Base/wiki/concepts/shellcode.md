---
title: "Shellcode"
type: concept
tags: [csce465, security, software-security, exploitation, shellcode, syscalls]
sources: [csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 465
updated: 2026-10-25
---

**Shellcode** is the payload of a [[Stack Smashing|stack smashing]] attack: a short sequence of native CPU instructions, supplied to the victim as ordinary input data, whose effect is to hand the attacker a shell. [[CSCE 465]] presents it as the C program an attacker *starts* from, then the extraction step that turns it into bytes.

## The Program

```c
void main() {
    char *name[2];
    name[0] = "/bin/sh";
    name[1] = NULL;
    execve(name[0], name, NULL);
    exit(0);
}
```

That is the whole payload: replace the current process image with `/bin/sh`. If the exploited program was [[Unix File Permissions|setuid root]], the shell inherits root.

## From C to Bytes

Shellcode is not shipped as C. The [[Stack Smashing|attack procedure]] is to **compile the attack code, then extract the binary for the piece that actually does the work** and paste those bytes into the overflowing input.

The mechanism the extracted bytes rely on:

> System calls in assembly are invoked by saving parameters either **on the stack or in registers** and then calling the **software interrupt (`0x80` in Linux)**.

So the real payload is a handful of instructions that load the `execve` syscall number and its arguments into registers and issue `int 0x80`. No libraries, no loader, no relocation — which is exactly why it survives being pasted into the middle of a string.

> **Why shellcode is written the way it is, derived.** The lecture gives the C and the syscall mechanism but not the constraints that make real shellcode look strange, and they follow directly from where it is being delivered. It arrives inside a **string** being copied by [[Unsafe C Functions|`strcpy`]], and `strcpy` stops at the first `\0` — so the payload **may not contain a zero byte** anywhere, which rules out the obvious `mov eax, 0` encodings and forces tricks like `xor eax, eax`. It is also injected at an address nobody knew at compile time, so it must be **position-independent**: it cannot reference `"/bin/sh"` by absolute address and instead pushes the string onto the stack and uses the stack pointer. Those two constraints — no nulls, position-independent — are why shellcode is hand-written assembly rather than compiler output, even though the lecture starts from a C program.

## Where It Sits

The injected code lives **on the stack, inside the buffer containing the attacker's string**. The lecture flags the oddity directly:

> Stack memory is supposed to contain only **data**, but…

That "but" is the entire premise of the attack, and it is also the opening for the defense: since **no legitimate program has code in the stack**, the stack segment can simply be marked non-executable. See [[Buffer Overflow Defenses]].

## The Alternative: Don't Inject Anything

Shellcode is only needed if the attacker chooses the **inject user code** strategy. The other half of [[Buffer Overflow|the taxonomy]] — *use what's already there* — skips this page entirely: if a library already contains a call to `exec(arg)`, the attacker passes a pointer to `"/bin/sh"` and jumps to it. That is the **return-to-libc** attack, and it is the reason a non-executable stack is not a complete defense.

## See Also

- [[Stack Smashing]]
- [[Buffer Overflow]]
- [[Buffer Overflow Defenses]]
- [[Unsafe C Functions]]
- [[Unix File Permissions]]
- [[Operating System Security]]
- [[Host-Based Intrusion Detection]]
- [[CSCE 465]]
