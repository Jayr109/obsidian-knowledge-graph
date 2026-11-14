---
title: "Virtual Memory"
type: concept
tags: [csce313, virtual-memory, page-tables, address-space, memory-management]
sources: [csce313-lecture-01-introduction-to-operating-systems, csce313-lecture-02-architectural-support-for-os, csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 313
updated: 2026-10-25
---

Virtual memory is an OS abstraction that provides each process with the illusion that it has exclusive, contiguous use of the entire physical memory. In reality, multiple processes share physical RAM, and the OS uses page tables and hardware support (MMU/TLB) to translate each process's virtual addresses to physical addresses transparently.

## Purpose

Virtual memory serves three goals:

1. **Isolation** — each process has its own address space; one process cannot read or write another process's memory (enforced by the MMU).
2. **Convenience** — every process sees the same large, contiguous address space regardless of how much physical memory is installed or how it is fragmented.
3. **Demand paging** — physical memory pages are allocated only when first accessed, allowing programs larger than physical RAM.

## Virtual Address Space Layout (64-bit Linux)

A 64-bit Linux process uses a 48-bit virtual address space (`0x000000000000` – `0xFFFFFFFFFFFF`):

```
0xFFFFFFFFFFFF
  KERNEL            (kernel virtual addresses — always mapped, inaccessible to user)
0x800000000000
  STACK             (grows downward; local variables, function call frames)
  [UNUSED]
  HEAP              (grows upward; malloc, new, mmap anonymous)
  DATA              (initialized + uninitialized globals and statics; BSS)
  TEXT (CODE)       (read-only; program machine instructions)
0x000000000000
```

## Page Tables

The OS maintains a **page table** per process that maps virtual page numbers (VPN) to physical frame numbers (PFN). A virtual address is split into:
- VPN: high bits → index into page table.
- Page offset: low bits → offset within the 4 KB page.

When a process accesses a virtual address:
1. MMU looks up the VPN in the page table.
2. If the page is present (valid bit set), adds the physical frame number to the offset → physical address.
3. If the page is not present → **page fault**: the OS allocates a physical frame, loads the page from disk (if needed), updates the page table, and restarts the instruction.

## Page Fault Handling

- **Recoverable fault (demand paging):** Virtual address is valid but page not yet mapped. OS allocates a page, updates the page table, and the faulting instruction succeeds on retry.
- **Invalid access (SIGSEGV):** Virtual address is not in any valid mapping (e.g., `a[5000]` when only 1000 elements). OS sends `SIGSEGV` to the process → "Segmentation fault."

## Memory Isolation Enforcement

Each process has its own page table (controlled by the OS). The page table for process A does not contain valid mappings to process B's physical frames. Any access to unmapped or foreign addresses generates a fault trapped by the OS.

## Security View

Memory isolation above protects one process from another. It does **not** protect a process
from itself, and [[CSCE 465]]'s [[Buffer Overflow|buffer overflow]] unit lives entirely inside
that gap: every write in a stack-smashing attack is to the process's own, properly mapped,
writable memory. No page fault occurs because nothing illegal happens at the page level.

The page table is nonetheless where two of the defenses live:

- **The NX bit** is a per-page-table-entry permission marking a region non-executable.
  Marking the stack NX stops injected [[Shellcode|shellcode]] — but not **return-to-libc**,
  which executes only pages that were already executable.
- **ASLR** randomizes the base addresses of the executable, libraries, heap and stack, so the
  absolute addresses an exploit hard-codes differ per machine.

See [[Buffer Overflow Defenses]]. The three outcomes of an out-of-bounds access — bus error,
page fault, or a successful write into adjacent memory — are decided by the page tables
described above; only the third is a vulnerability.

## Relationship to Process

When `fork()` is called:
- The OS creates a new page table for the child, initially sharing the same physical pages (copy-on-write).
- Writes by either parent or child trigger a copy of the modified page into a new physical frame.

When `exec()` is called:
- The OS replaces the current process's page table (and virtual address space) with the new program's image.

## See Also

- [[Processes]]
- [[Buffer Overflow]]
- [[Buffer Overflow Defenses]]
- [[Operating Systems]]
- [[System Calls]]
- [[Interrupts and Exceptions]]
- [[CSCE 313]]
