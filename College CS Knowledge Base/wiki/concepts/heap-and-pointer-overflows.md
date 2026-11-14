---
title: "Heap and Pointer Overflows"
type: concept
tags: [csce465, security, software-security, buffer-overflow, heap, off-by-one, function-pointers]
sources: [csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 465
updated: 2026-10-25
---

The second generation of [[Buffer Overflow|buffer overflow]] attacks, after [[Stack Smashing|stack smashing]] was understood and partly defended: overflows that never touch a return address. [[CSCE 465]] groups three — **off-by-one**, **heap**, and **function pointer** — plus a list of further targets. What they share is that each corrupts a *different* pointer the program will later trust.

## Off-By-One Overflow

The lecture's example is a home-brewed range-checking string copy, which is worse than no range checking because it looks careful:

```c
void notSoSafeCopy(char *input) {
    char buffer[512]; int i;
    for (i = 0; i <= 512; i++)
        buffer[i] = input[i];
}

void main(int argc, char *argv[]) {
    if (argc == 2)
        notSoSafeCopy(argv[1]);
}
```

> This will copy **513** characters into `buffer`. Oops!

The bug is `<=` where `<` was meant. One byte past the end.

**A 1-byte overflow can't change the return address, but it can change the pointer to the previous stack frame:**

- On a **little-endian** architecture, make it point **into the buffer**
- The **return address for the previous function will then be read from the buffer**

> **Why one byte is enough, derived.** The saved frame pointer sits immediately above the local buffer, and on a little-endian machine the byte immediately adjacent is the pointer's **least significant** byte. Overwriting it moves the saved frame pointer by up to 255 bytes — not far, but far enough to land inside the attacker-controlled buffer. The attacker does not redirect execution directly; they redirect the **frame**, and the *calling* function then reads its return address out of the fake frame. It is a two-step hijack, and the whole thing turns on a single `<=`.

## Heap Overflow

Overflowing buffers on the heap can change **pointers that point to important data**.

- Sometimes it can also transfer execution to attack code
- It can cause the program to crash by forcing it to read from an invalid address (segmentation violation)

The more interesting case the lecture gives is **illegitimate privilege elevation**:

> If a program with an overflow has sysadm/root rights, an attacker can use it to **write into a normally inaccessible file** — for example, replace a filename pointer with a pointer into a buffer location containing the name of a system file. Instead of a temporary file, write into `AUTOEXEC.BAT`.

No shellcode, no control-flow hijack. The program keeps running its own code correctly, on the attacker's filename. This is the cleanest example in the deck of an overflow that violates [[CIA Triad|integrity]] without ever violating control flow.

## Function Pointer Overflow

> C uses **function pointers for callbacks**: if a pointer to `F` is stored in memory location `P`, then another function `G` can call `F` as `(*P)(…)`.

The attack shape, from the lecture's diagram:

```
Heap:  [ buffer with attacker-supplied input string ][ callback pointer ]
                           |  overflow -->               |
                           +-----------------------------+
                                     now points at attack code
                                     (legitimate function F lives elsewhere)
```

Same principle as stack smashing — overwrite a stored code address — but the target is a callback pointer on the heap rather than a return address on the stack. This is why [[Stack Canaries|StackGuard]] alone is insufficient and why **PointGuard** extends canaries to function pointers.

## More Buffer Overflow Targets

The lecture's remaining list:

- **Heap management structures used by `malloc()`** — the third-generation target
- **URL validation and canonicalization** — if a web server stores a URL in a buffer with an overflow, an attacker can gain control by supplying a malformed URL. The **Nimda worm** propagated itself using a buffer overflow in Microsoft's Internet Information Server.

### Some Attacks Don't Even Need an Overflow

Filed here by the lecture because the target is the same parsing code:

> Naïve security checks may miss URLs that give an attacker access to forbidden files. For example, `http://victim.com/user/../../autoexec.bat` may pass a naïve check but give access to a system file. Defeat checking for `/` in a URL by using the **hex representation**.

> **The connection to [[Access Control Models|Lecture 7]], derived.** Path traversal is a *canonicalization* failure: the check and the filesystem disagree about what the name means. That is the same structural flaw as Linux's "different paths to the same file are not equivalent" — two names for one object, with the security decision made on the name rather than the object. Checking for a literal `/` is [[Security Design Principles|blacklisting]], and the hex-encoding bypass is the enumerated-badness failure the course has flagged since Lecture 2.

## See Also

- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Format String Vulnerabilities]]
- [[Unsafe C Functions]]
- [[Buffer Overflow Defenses]]
- [[Stack Canaries]]
- [[Security Design Principles]]
- [[Access Control Models]]
- [[CIA Triad]]
- [[CSCE 465]]
