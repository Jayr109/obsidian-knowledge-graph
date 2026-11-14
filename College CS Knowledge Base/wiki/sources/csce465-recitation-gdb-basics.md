---
title: "CSCE 465 Recitation — gdb Basics"
type: source
tags: [csce465, gdb, debugging, recitation, tools, lab]
sources: []
course: CSCE 465
updated: 2026-10-25
---

A recitation deck for [[CSCE 465]] (`raw/CSCE465_GDB_Basics.pdf`, **11 pages, one slide per page** — not two-up like the lecture decks). Titled simply *CSCE 465: Computer & Network Security (gdb basics)*. It carries no instructor attribution and reads as TA-delivered; the screenshots were taken under WSL on a machine whose user directory is `Hayoung`, which matches the TA naming pattern rather than [[Guofei Gu]]'s lecture decks.

It accompanies [[CSCE 465 Lecture 9 — Software Security: Buffer Overflow]] and exists to make the lab work possible: the attacks in that lecture are about stack frames, and this is the tool that shows them.

## Structure

| Slides | Content |
|---|---|
| 1–3 | What gdb is; the four-step debugging loop |
| 4–6 | Commonly used commands, in three batches — compile/start/run, breakpoints and stepping, then `bt` and `info frame` with a worked recursive example |
| 7–10 | A four-step walkthrough in screenshots: compile, start gdb, debug, quit |
| 11 | References |

## Pages Derived

| Page | What it holds |
|---|---|
| [[GDB]] | The debugging loop, the full command table, both worked examples, and the link from `info frame` output to the stack-smashing target |

One page only. The deck is a tool reference, not a concepts lecture, and splitting it would produce stubs.

## Content Worth Keeping

**`bt` and `info frame` are the two commands this course actually needs.** The rest of the deck is generic debugging; these two print the function chain and the frame internals. → [[GDB]]

**`info frame` prints the exploit target directly.** Its output names `saved rip` (the return address an overflow overwrites), the address that value is stored at, and `rbp` eight bytes below it. The recitation presents this as debugging output; read against [[Stack Smashing]] it is a map of the attack surface. → [[GDB]]

**`s` versus `n`.** Both step, but `s` descends into functions — the screenshot shows it landing inside `strlen` at `../sysdeps/x86_64/strlen.S:66` with "No such file or directory", which is the normal and confusing result of stepping into a libc routine with no source installed. → [[GDB]]

**`q` discards everything.** Breakpoints and settings are not saved between sessions. → [[GDB]]

**Pressing Enter repeats the previous command** — flagged in red on the slide, so presumably asked about often.

## Worked Examples Recovered

Both live in screenshots and were read by rendering the pages at 2×:

- **A recursive `test(level)` program** counting down from 5 to `level0()`, with the resulting eight-frame `backtrace` and the `info frame` dump for the innermost frame. Frames `#2`–`#6` share the return address `0x4005af` because every recursive call returns to the same line; `#1` differs at `0x4005bb` because that is the other branch.
- **A `b main` / `run` / `s` session** on a `hello world` program, stepping into `strlen`.

Both are reproduced on [[GDB]].

## Connection to the Rest of the KB

- **[[Stack Smashing]]** is the reason this deck exists. The offset from a local buffer to the saved return address is the quantity an attacker spends most of their effort guessing, and `info frame` prints it.
- **[[Process Attributes]]** from [[CSCE 313]] already covers `%rip`, `%rsp` and `%rbp` as PCB/register state. This page is the *observation* of those registers at runtime, not a second description of them.
- **A caveat worth carrying into the lab:** the frame addresses in these screenshots are stable across runs because **gdb disables [[Buffer Overflow Defenses|ASLR]] by default**. An exploit developed entirely under the debugger will often fail outside it, which is a standard first-lab surprise.

## Extraction Note

The text layer is thin — **3,870 characters across 11 pages** — because slides 6 through 10 are **terminal and editor screenshots**. All five were rendered at 2× and read; the command tables, both worked examples and the full `info frame` output were recovered. Nothing on this deck is unrecoverable.

The reference URLs on slide 11 were transcribed as given and **not visited**.

## See Also

- [[CSCE 465]]
- [[GDB]]
- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Buffer Overflow Defenses]]
- [[Process Attributes]]
- [[CSCE 465 Lecture 9 — Software Security: Buffer Overflow]]
