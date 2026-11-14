---
title: "CSCE 465 Lecture 9 — Software Security: Buffer Overflow"
type: source
tags: [csce465, software-security, buffer-overflow, stack-smashing, aslr, stackguard]
sources: []
course: CSCE 465
updated: 2026-10-25
---

Lecture 9 of [[CSCE 465]] (`raw/CSCE465_09_BufferOverflow.pdf`, 24 PDF pages laid out two slides per page ≈ **47 logical slides**, instructor [[Guofei Gu]]). This opens the **software security** unit — the gap flagged as outstanding after Lectures 7 and 8 — and it is the most hands-on deck of the semester. Roadmap as given: *BO basics; stack smashing; other buffer overflow vulnerabilities; BO defense*.

The companion recitation [[CSCE 465 Recitation — gdb Basics]] was delivered alongside it and teaches the tool the labs need.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–6 | **BO basics** | Definition; impact and the worm list; attack goal; code injection vs. code already there; how to jump to attacker code; attacks on memory buffers and the three generations |
| 7–13 | **Stack smashing** | Process memory regions; what happens when memory outside a buffer is accessed; the stack frame; the `func`/`buf[126]` example; overstuffing; executing attack code; shell code; the attack procedure; buffer overflow issues; guessing the buffer address; NOP sled |
| 14–16 | **Other BO vulnerabilities** | Off-by-one; heap overflow; function pointer overflow; format strings in C; writing the stack with `%n`; more targets including Nimda and path traversal |
| 17–24 | **BO defense** | The five defense families; writing correct code; unsafe C functions; `strncpy` and the Apache `htpasswd` fix; source-code analysis checklist; non-executable buffers and NX; ASLR; array bounds checking; code pointer integrity; Libsafe; StackGuard and canaries |

## Pages Derived

| Page | What it holds |
|---|---|
| [[Buffer Overflow]] | Definition, impact, the attack's two halves, placement and jump strategies, three generations, out-of-bounds outcomes |
| [[Stack Smashing]] | The stack frame, the `buf[126]` example, RET overwrite, attack procedure, address guessing, NOP sled |
| [[Shellcode]] | The `/bin/sh` program, syscalls via `int 0x80`, extraction, why it is written in assembly |
| [[Heap and Pointer Overflows]] | Off-by-one and the frame-pointer hijack, heap overflow, function pointer overflow, further targets, path traversal |
| [[Format String Vulnerabilities]] | `printf(buf)`, the variadic stack walk, `%n` as an arbitrary write |
| [[Unsafe C Functions]] | The unsafe list, `strncpy`, the Apache `htpasswd` case study, the source-analysis checklist |
| [[Buffer Overflow Defenses]] | The five families, NX and return-to-libc, ASLR, bounds checking, pointer integrity, Libsafe |
| [[Stack Canaries]] | StackGuard, random vs terminator canaries, PointGuard, the 8% Apache penalty, the Bulba and Kil3r defeat |

**Deliberately not created:** a process-memory-layout page. [[Processes]] and [[Virtual Memory]] from [[CSCE 313]] already carry the text/data/heap/stack breakdown, and this unit links across to them rather than stating it a third time — the same discipline applied when Lecture 7 met CSCE 313.

## Content Worth Keeping

**Buffer overflow is still the most common source of software vulnerability.** First seen in the **Morris Worm** (1988, **6,000 machines**), and behind Zotob, Sasser, CodeRed, Blaster, SQL Slammer, Conficker and Stuxnet. Twenty-two years of the same mechanism. → [[Buffer Overflow]]

**Every exploit needs two things: code in the address space, and a transfer of execution to it.** Code gets there by **injection** or by **using what's already there**; execution is transferred via **activation records**, **function pointers**, or **longjmp buffers**. The whole unit is a cross product of those two lists. → [[Buffer Overflow]]

**The target is never the code — it is the stored address that decides where code runs next.** Text is read-only; what gets overwritten is a pointer the CPU will later load into the program counter. → [[Buffer Overflow]]

**`strcpy` does not check whether the source is shorter than the destination.** `void func(char *str) { char buf[126]; strcpy(buf, str); }` — a string over 126 bytes overwrites the saved frame pointer and then the return address. → [[Stack Smashing]]

**The attacker must guess where the buffer will be, precisely.** `get_sp()` reads the attacker's own `%esp` and assumes the victim's matches; the **NOP sled** turns one correct address into a range. → [[Stack Smashing]]

**Shellcode is `execve("/bin/sh")` reduced to bytes**, invoking the syscall through software interrupt `0x80`. Root shell if the victim is [[Unix File Permissions|setuid root]]. → [[Shellcode]]

**A one-byte overflow is enough.** Off-by-one (`i <= 512` on `buffer[512]`) cannot reach the return address but can change the **low byte of the saved frame pointer** on a little-endian machine, so the *previous* function reads its return address out of the attacker's buffer. → [[Heap and Pointer Overflows]]

**Heap overflow can elevate privilege without hijacking control flow** — replace a filename pointer and a root-privileged program writes the attacker's file. → [[Heap and Pointer Overflows]]

**`printf(buf)` instead of `printf("%s", buf)` is an arbitrary memory write.** `printf` trusts the format string to say how many arguments it has; `%n` writes the character count to an address taken from the stack. → [[Format String Vulnerabilities]]

**The published fix for the Apache `htpasswd` overflow was itself wrong.** Three `strncpy`/`strncat` calls each bounded by `MAX_STRING_LEN-1` can write nearly twice the buffer, because a per-call bound is not a per-buffer bound. → [[Unsafe C Functions]]

**Non-executable stack does not stop return-to-libc.** The attacker executes only code that was already executable. NX defeats one of the two placement strategies and nothing else. → [[Buffer Overflow Defenses]]

**Slammer infected 75,000 MS-SQL servers using the same code on every machine** — the argument for ASLR in one number. Listed attacks on ASLR: repetitive guessing and spraying. → [[Buffer Overflow Defenses]]

**Libsafe needs no recompilation** because it substitutes a bound it can compute — `|frame-pointer − dest| > strlen(src)` — for the buffer size it cannot know. → [[Buffer Overflow Defenses]]

**Canaries are a tripwire, and StackGuard can be defeated** (Phrack, Bulba and Kil3r). Random canaries defeat a guesser; terminator canaries (`\0`, newline, linefeed, EOF) defeat a string copy. 8% penalty on Apache; recompilation required. → [[Stack Canaries]]

## Connection to the Rest of the KB

- **This closes the loop from [[Access Control Models|Lecture 7]] and [[Security Models|Lecture 8]].** Lecture 7 gave the mechanisms, Lecture 8 the policy models and the proof that safety is undecidable in general — and Lecture 9 is what undecidability looks like in practice: the model says the program may read its own buffer, and the implementation lets it write past the end. This is the **[[Safety Problem|"a safe model does not ensure a secure system"]]** bullet, instantiated.
- **[[CSCE 313]] supplies the mechanics.** [[Processes]] and [[Virtual Memory]] carry the address-space layout; [[Process Attributes]] carries `%rsp`, `%rip` and the PCB. The security pages link rather than restate.
- **[[Security Design Principles]] gets its sharpest instances yet** — *least privilege* (why setuid root turns an overflow into host compromise), *fail-safe defaults* and the whitelist argument (the path-traversal hex-encoding bypass is enumerated badness failing again), and *economy of mechanism* (the Apache fix failed because the safe function moved a bound into the programmer's head).
- **[[GDB]] is the practical bridge**: `info frame` prints the saved return address and its storage location, which is the object every attack on this page targets.

## Extraction Note

Text extracted with PyMuPDF; code listings, the unsafe-function list and the defense bullets all survived intact.

**One slide was font-mangled and was recovered by rendering.** Slide 40 (*"Bugs to Detect in Source Code Analysis"*) extracted as a substitution cipher — `! "#$%&'"$(%)*+',-.-/0%` — because the list is set in a font with a scrambled encoding. Rendered at 2.4× and read directly: all **20 defect classes** recovered and recorded on [[Unsafe C Functions]]. The mapping is not a simple shift and was not reconstructed by hand.

**Diagrams** for the stack frame (slide 18), the overflow (19–20), Libsafe (45) and the StackGuard canary (47) extract as label clouds — boxes and arrows lost, labels intact. The layouts on the derived pages were rebuilt from the labels **plus** the surrounding prose, which states each relationship explicitly; the raw deck remains authoritative for exact figure geometry.

**Deck erratum:** the slide reads *"To stop buffer overflow, exploits, the data section has to be marked non-executable"* — a stray comma. Quoted as written.

**Note on `buf[126]`:** the vulnerable example uses **126** bytes, not the more common 128. Kept as the deck has it, including in the prose that follows ("a string longer than 126 bytes").

## Open Gaps

- **No Lecture 6, and 6a still implies a 6b** — unchanged since Lecture 7, likely *authentication and security handshake pitfalls*.
- **Software security is now open but probably not complete.** This deck covers memory corruption only; the course outline's software-security entry would normally also reach integer overflows, race conditions and input validation generally.
- **Network security and web security remain entirely outstanding**, along with malware, vulnerability analysis, firewalls and intrusion detection.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Shellcode]]
- [[Heap and Pointer Overflows]]
- [[Format String Vulnerabilities]]
- [[Unsafe C Functions]]
- [[Buffer Overflow Defenses]]
- [[Stack Canaries]]
- [[GDB]]
- [[Processes]]
- [[Virtual Memory]]
- [[CSCE 465 Recitation — gdb Basics]]
- [[CSCE 465 Lecture 8 — Security Theory: Security Policies and Models]]
