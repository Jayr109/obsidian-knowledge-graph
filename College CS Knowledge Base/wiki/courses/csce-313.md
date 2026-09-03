---
title: "CSCE 313"
type: course
tags: [csce313, operating-systems, systems-programming, posix]
sources: [csce313-lecture-01-introduction-to-operating-systems, csce313-lecture-02-architectural-support-for-os, csce313-lecture-05-ipc-pipes-and-fifo, csce313-lecture-06-process-api-part-i, csce313-lecture-07-process-api-part-ii, csce313-lecture-08-process-attributes, csce313-lecture-09-unix-file-io, csce313-lecture-10-file-descriptors-redirection-stdio, csce313-lecture-11-file-systems-ii, csce313-lecture-12-threads-introduction, csce313-lecture-14-thread-synchronization-i-mutexes, csce313-lecture-15-thread-synchronization-ii, csce313-lecture-16-thread-synchronization-iii-semaphores, csce313-lecture-18-introduction-to-networking, csce-313-lecture-22-data-link-layer]
updated: 2026-04-22
---

CSCE 313: Introduction to Computer Systems is a Texas A&M University course that teaches systems programming from the programmer's perspective. It focuses on the POSIX API, operating system concepts, and low-level Unix programming in C/C++. It is a prerequisite for CSCE 410 (Operating Systems).

## Course Information

| Field | Value |
|-------|-------|
| **Course** | CSCE 313 — Introduction to Computer Systems |
| **University** | Texas A&M University |
| **Instructors** | [[Sandeep Kumar]]; [[Houngninou]] (L22) |
| **Textbooks** | OSSTEP (Operating Systems: Three Easy Pieces); APUE (Advanced Programming in the UNIX Environment) |
| **Language** | C / C++ on Linux (GCP VM) |
| **Tools** | gdb/lldb, git, vi, strace |

## Course Philosophy

CSCE 313 is explicitly not an OS design course. It covers OS concepts at a coarser level than CSCE 410, focusing on the programmer's POV — essentially the POSIX API. Students learn how Unix is structured, how programs execute, how they read/write files, communicate with each other, and deal with events (signals, timers, network packets).

## Topic Arc

| Phase | Topics | Lectures |
|-------|--------|---------|
| OS Foundations | What is an OS; three hats; hardware support (interrupts, privilege levels, virtual memory) | L1, L2 |
| IPC | Pipes, FIFO, fork/exec intro | L5 |
| Process API | fork, exec, wait, exit; exec family; zombie processes | L6, L7 |
| Process Attributes | PCB, states, context switch, signals, signal API | L8, L12 |
| File I/O | Unix I/O syscalls; file descriptors; the three-table model; redirection; stdio | L9, L10 |
| File Systems | On-disk layout; inodes; indexed allocation; hard/soft links; directory API | L11 |
| Concurrency | Threads vs processes; pthreads API; race conditions | L12, L14 |
| Synchronization | Mutexes; condition variables; semaphores; producer-consumer | L14, L15, L16 |
| Networking | Internet; TCP/IP; sockets API; client-server; DNS | L18 |
| Network Security | Data link layer; Ethernet; MAC addresses; ARP; ARP spoofing | L22 |

## Concept Pages

### Operating System Internals
- [[Operating Systems]] — three hats: illusionist, referee, glue
- [[Processes]] — process model, PCB, lifecycle states
- [[Virtual Memory]] — per-process address spaces, page tables
- [[System Calls]] — traps, mode switches, calling convention
- [[Interrupts and Exceptions]] — hardware interrupts, faults, aborts, traps

### IPC and Process Management
- [[Inter-Process Communication]] — message passing vs. shared memory
- [[Pipes and FIFO]] — anonymous pipes, named pipes, dup2
- [[Process API]] — fork, exec, wait, exit, zombie prevention
- [[Process Attributes]] — PID/UID/GID, signals, context switch, signal mask

### File I/O and Storage
- [[UNIX File I/O]] — open/read/write/close/lseek; everything is a file
- [[File Descriptors]] — DT/FT/vnode model; fork/dup sharing semantics
- [[File Systems]] — on-disk layout; inodes; hard and symbolic links

### Concurrency and Synchronization
- [[Threads]] — thread model, pthreads API, C++ threads
- [[Thread Synchronization]] — race conditions, critical sections, atomicity
- [[Mutexes and Locks]] — pthread_mutex, unique_lock, coarse/fine grained
- [[Condition Variables]] — wait/signal/broadcast, producer-consumer
- [[Semaphores]] — counting semaphores, bounded buffer

### Networking
- [[Computer Networking]] — TCP/IP, sockets, DNS, client-server
- [[Data Link Layer]] — OSI layer 2; Ethernet frames; MAC addresses; switch
- [[ARP]] — IP→MAC resolution; ARP spoofing

## Source Pages (Lectures Ingested)

- [[CSCE 313 Lecture 1 — Introduction to Operating Systems]] (36 pages)
- [[CSCE 313 Lecture 2 — Architectural Support for Operating Systems]] (28 pages)
- [[CSCE 313 Lecture 5 — Inter-Process Communication: Pipes and FIFO]] (45 pages)
- [[CSCE 313 Lecture 6 — Process API Part I]] (24 pages)
- [[CSCE 313 Lecture 7 — Process API Part II]] (22 pages)
- [[CSCE 313 Lecture 8 — Process Attributes]] (28 pages)
- [[CSCE 313 Lecture 9 — UNIX File I/O]] (35 pages)
- [[CSCE 313 Lecture 10 — UNIX I/O: File Descriptors, Redirection, and Standard I/O]] (23 pages)
- [[CSCE 313 Lecture 11 — File Systems II]] (39 pages)
- [[CSCE 313 Lecture 12 — Threads Introduction]] (35 pages; also covers signals)
- [[CSCE 313 Lecture 14 — Thread Synchronization I: Mutexes and Locks]] (31 pages)
- [[CSCE 313 Lecture 15 — Thread Synchronization II]] (31 pages)
- [[CSCE 313 Lecture 16 — Thread Synchronization III: Condition Variables and Semaphores]] (21 pages)
- [[CSCE 313 Lecture 18 — Introduction to Networking/Internet]] (51 pages)
- [[CSCE 313 Lecture 22 — Network Security: The Data Link Layer]] (18 slides; instructor: Houngninou)

## Lectures Not Yet Ingested

Lectures 3, 4, 13, 17, and others not in the extracted text set. These likely cover additional process/threading topics and advanced file system design.

## See Also

- [[CSCE 411]] — companion algorithms course
- [[CSCE 465]] — Computer & Network Security; lists CSCE 313 as its prerequisite
- [[Overview]]
