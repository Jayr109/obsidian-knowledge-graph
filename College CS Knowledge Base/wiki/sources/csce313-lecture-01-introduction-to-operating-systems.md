---
title: "CSCE 313 Lecture 1 — Introduction to Operating Systems"
type: source
tags: [csce313, operating-systems, processes, virtual-memory, assembly]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 1 of CSCE 313 (Introduction to Computer Systems) introduces the operating system as the software layer between hardware and applications, defines its three core roles (illusionist, referee, glue), and provides an initial look at processes, virtual memory, and the compilation/execution pipeline. Instructor: Sandeep Kumar. Reference: OSSTEP Chapter 4. Some slides adapted from CS162 at UC Berkeley (Crooks & Zaharia).

## Key Concepts Introduced

**Operating System Definition.** An OS is the layer of software that interfaces between diverse hardware resources and the many applications running on the machine. It implements a virtual machine for each application whose interface is more convenient (more secure, reliable, and portable) than the raw hardware.

**Three Hats of the OS:**
- **Illusionist** — provides clean, easy-to-use abstractions of physical resources (e.g., virtual CPUs, virtual memory).
- **Referee** — manages protection, isolation, and fair sharing of resources among competing processes.
- **Glue** — provides a set of common services usable by all programs.

**Process.** A process is an instance of a running program. The `ps aux` command lists processes with attributes: PID (unique process ID), %CPU, %MEM, VSZ (virtual size in KB), RSS (resident set size in KB), STAT (symbolic process state), and CMD.

**Multitasking.** Concurrent (not parallel) execution of multiple processes over time. The CPU switches so fast that it appears all processes run simultaneously.

**Virtual Memory.** An abstraction giving each process the illusion of exclusive access to main memory. The virtual address space on a 64-bit Linux system spans `0x000000000000` to `0xFFFFFFFFFFFF`. Layout (low to high): TEXT (code), DATA, HEAP, UNUSED, STACK, KERNEL. Each process gets a separate page table mapping virtual addresses to physical memory.

## Compilation Pipeline

The GCC compilation of `hello.c` proceeds through four stages: preprocessor (cpp) → compiler (cc1) → assembler (as) → linker (ld), producing the executable. The slides show the generated x86-64 assembly for a simple `printf` call, including frame pointer linkage (`pushq %rbp`, `movq %rsp, %rbp`) and argument passing via `%rdi`.

## Architectural Overview

**Registers in x86-64.** The CPU has general-purpose registers, a program counter (%rip), condition codes (%rflags), and a stack pointer (%rsp). Arguments to functions are passed in registers (%rdi, %rsi, %rdx, %rcx, %r8, %r9).

**Control Flow and the Stack.** A `call f` instruction saves the return address on the stack and jumps to `f`. A `ret` pops the return address from the stack. Each function call creates a stack frame with the return address, saved `%rbp`, local variables, and saved registers.

**Integer Overflow and 2's Complement.** The lecture notes that integer arithmetic wraps modulo 2^n. In 2's complement, `-u = ~u + 1`. Floating-point arithmetic is not associative (e.g., `(1e20 + -1e20) + 3.14 ≠ 1e20 + (-1e20 + 3.14)`).

## Visual Slides

Several slides are diagram-only and text extraction captured little content: virtual memory layout diagrams, stack frame diagrams for control flow, x86-64 register table (URL partially extracted as garbled text), and the analogy slides for virtual memory (ladder/2D space diagrams).

## See Also

- [[Operating Systems]]
- [[Processes]]
- [[Virtual Memory]]
- [[System Calls]]
- [[CSCE 313]]
