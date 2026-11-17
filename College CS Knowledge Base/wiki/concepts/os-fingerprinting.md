---
title: "OS Fingerprinting"
type: concept
tags: [csce465, security, network-security, reconnaissance, nmap, tcp, ttl]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

**OS fingerprinting** is, in [[CSCE 465]]'s words, *a method of detecting the remote host's operating system using information leaked by that host's TCP stack*. It is the second half of target identification, after [[Port Scanning]]: the scan says which services are running, the fingerprint says what they are running on.

> These methods are possible because **each OS implements their TCP stack differently**. OS fingerprinting **(ab)uses** these differences.

## Active and Passive

| Mode | How |
|---|---|
| **Active** | Send **carefully crafted packets** and read the responses — *usually with an invalid/strange set of options (which is where OS vendors usually differ in implementation), and see what happens* |
| **Passive** | **Observe captured network traffic** and send nothing |

## Methods Used in Nmap

The lecture names four and explains one:

- **The FIN probe** — *Send a FIN packet (or any packet without an ACK or SYN flag) to an open port and wait for a response. The correct RFC 793 behavior is to NOT respond, but many broken implementations such as MS Windows, BSDI, CISCO, and IRIX send a RESET back.*
- **IPID sampling**
- **TCP Initial Window**
- **TCP Options**

> **What the other three measure, derived.** The slide only names them. *IPID sampling* looks at how a host fills the 16-bit identification field of the [[Internet Protocol|IP header]] from one packet to the next (a counter, a per-destination counter, random). *TCP initial window* is the window size a stack advertises in its first segment. *TCP options* is which options it sends and in what order. None is a bug; each is a place where the specification leaves a choice and vendors chose differently.
>
> The FIN probe shows the general shape: the RFC defines what a correct stack does, and **the fingerprint lives in the deviations**.

## TTL as a Fingerprint

One slide is a single table, *List of TTL values that represent specific OS* (credited to gbhackers.com), with columns Device/OS, Version, Protocol, TTL. It is an image with no text layer; the rows below were read from the rendered slide.

| Initial TTL | Systems listed (selection) |
|---|---|
| **64** | Linux (2.0.x kernel; Red Hat 9), FreeBSD 5, MacOS X 10.5.6, Juniper, Foundry, Compaq Tru64 v5.0 |
| **128** | Windows 98, NT 4.0, 2000, XP, Vista, 7, Server 2003, Server 2008, 10 |
| **255** | Solaris 2.5.1–2.8, AIX 3.2/4.1, BSDI, FreeBSD 3.4/4.0, NetBSD, OpenBSD 2.6 & 2.7, Linux 2.2.14 and 2.4 kernels, HP-UX 10.2 and 11 — all for **ICMP** |
| **254** | Cisco (ICMP) |
| **32** | Windows 95, Windows for Workgroups, NT 3.51 |
| **30 / 60** | Older Unix stacks: AIX (TCP 60, UDP 30), Irix (60), Ultrix (TCP 60, UDP 30), SunOS 4.1.3 (60) |

The table lists the protocol separately because **one OS can use different values for different protocols** — it gives Solaris 2.8 as 255 for ICMP but 64 for TCP, and HP-UX 11 the same way. It is not perfectly consistent with itself: Windows 98 over ICMP appears once as 128 and once as 32. Treat it as a rule of thumb, which is how the slide uses it.

> **How it is used, derived.** A receiver sees the TTL *after* each router on the path has decremented it, not the initial value. But the initial values cluster at a few numbers, so the observed TTL rounds up to the nearest cluster and the remainder is the hop count. A packet arriving with TTL 116 almost certainly started at 128 — probably Windows, 12 hops away.

## Two SYNs Side by Side

Another image-only slide shows two captured SYN packets, both to port 80, from two hosts on the same LAN:

| | Capture 1 | Capture 2 |
|---|---|---|
| Source | `172.16.16.100` (Dell NIC) | `172.16.16.104` (VMware NIC) |
| Frame on the wire | 66 bytes | 74 bytes |
| TCP header length | 32 bytes | 40 bytes |
| Window size | **8192** | **5840** |
| Options | 12 bytes: MSS 1460, NOP, window scale 2 (×4), NOP, NOP, SACK permitted | 20 bytes: MSS 1460, SACK permitted, timestamps, NOP, window scale 6 (×64) |
| TTL (from the hex dump) | `0x80` = **128** | `0x40` = **64** |

Same destination port, same MSS, and they agree on almost nothing else.

> **Reading the slide, derived.** The slide carries no caption, but this is the passive mode from above made concrete: nobody probed either host, and the two SYNs still give themselves away. The TTL bytes are visible in the hex dumps — `80` and `40` — and by the table on the previous slide those are a Windows stack and a Linux/Unix stack. The window sizes and the option lists differ the same way the Nmap list says they will.

## Why It Matters

> **For the attacker and for the defender, derived.** An exploit is OS-specific — the [[Stack Smashing|stack layout]], the [[Shellcode|shellcode]], the service version — so knowing the OS turns a list of open ports into a list of exploits worth trying. Defenders run the same technique as asset inventory.
>
> The less obvious consequence shows up two lectures later. The differences fingerprinting reads are the same *"ambiguities in protocols and operating systems"* that let an attacker show a network IDS one byte stream and the end host another: see [[Insertion and Evasion Attacks]]. One fact about TCP/IP stacks, used once for reconnaissance and once for evasion.

## See Also

- [[Port Scanning]]
- [[Vulnerability Analysis]]
- [[TCP]]
- [[Internet Protocol]]
- [[ICMP]]
- [[Insertion and Evasion Attacks]]
- [[CSCE 465]]
