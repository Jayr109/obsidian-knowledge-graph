---
title: "Port Scanning"
type: concept
tags: [csce465, security, network-security, reconnaissance, nmap, tcp, ports]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

**Port scanning** is the first half of what [[CSCE 465]] calls *identifying targets*: probing a host to learn which ports have a process listening behind them. It comes before any attack in the [[Vulnerability Analysis|vulnerability analysis]] lecture because every later step needs its answer — you cannot exploit a service you have not found. The second half is [[OS Fingerprinting]].

## Ports, as the Lecture States Them

> - Ports dynamically address ("**bind**") IP packets to a process
>   - Socket data structures keep the mapping information
>   - Need to "bind" a socket (port) to a process
> - Ports range from **0 to 65535**
> - Ports **0–1023** are reserved for well-known services
>   - Require **root** (in UNIX) access to listen on those ports
> - UDP and TCP ports
>   - Usually the same port number is assigned to a service for both UDP and TCP (if the service can use both)

The socket side of this — `bind()`, the 4-tuple, well-known port numbers — is on [[Computer Networking]] from [[CSCE 313]].

## The Tool

> Tools: **NMAP**… e.g. run `nmap -sS 192.168.1.102` — does a **SYN scan**. More: TCP connect, FIN, Ping, UDP…

## The SYN ("Stealth") Scan

The deck's figure shows the two cases side by side, each with its packet capture.

| Port state | Scanner sends | Target answers | Scanner then |
|---|---|---|---|
| **Open** (port 22 in the figure) | `SYN` | `SYN, ACK` | `RST` |
| **Closed** (port 3389 in the figure) | `SYN` | `RST, ACK` | nothing |

```
open port                                  closed port
  scanner                  target            scanner                  target
     |--- SYN (port 22) ----->|                 |--- SYN (port 3389) --->|
     |<-- SYN, ACK -----------|                 |<-- RST, ACK -----------|
     |--- RST --------------->|
```

The captures behind the figure (the target is `192.168.1.102`, the scanner `192.168.1.113`):

```
open:    65008 -> 22    [SYN]       Seq=0 Win=1024  Len=0 MSS=1460
         22    -> 65008 [SYN, ACK]  Seq=0 Ack=1 Win=29200 Len=0 MSS=1460
         65008 -> 22    [RST]       Seq=1 Win=0 Len=0

closed:  45014 -> 3389  [SYN]       Seq=0 Win=29200 Len=0 MSS=1460 SACK_PERM=1 ...
         3389  -> 45014 [RST, ACK]  Seq=1 Ack=1 Win=0 Len=0
```

> **Why it is called stealth, derived.** The scanner learns everything it needs from the **second** message of the [[TCP|three-way handshake]] and never sends the third. The connection is therefore never established, the listening application never sees it, and nothing reaches an application log — the scanner answers the `SYN, ACK` with a `RST` and moves on. That is also why it is called a *half-open* scan: it leaves the target in exactly the state a [[SYN Flooding|SYN flood]] does, once per port instead of thousands of times on one.
>
> A `connect` scan (the "TCP connect" on the slide) finishes the handshake instead. It needs no special privilege, and it is logged.

> **A detail in the two captures, derived.** The two probe SYNs are not built the same way. The first is 58 bytes with `Win=1024` and only an MSS option; the second is 74 bytes with `Win=29200` and `SACK_PERM`. Different window, different options, different length — which is the kind of difference [[OS Fingerprinting]] reads. The slide labels both captures as stealth scans and does not comment on it.

## What the Answer Is Worth

> **Why this comes first, derived.** A list of open ports is a list of running services, and each service is a candidate for a known flaw — a [[Buffer Overflow|buffer overflow]] in the daemon behind it, a weak password, an unauthenticated protocol. [[Worms|Worms]] automate exactly this step, and their *hit-list scanning* is a port scan done in advance. The same scan is how a defender takes inventory, which is the [[Vulnerability Analysis|attacker/defender symmetry]] the lecture closes on.
>
> It is also the first thing the other two decks of this unit react to. A [[Firewalls|firewall]] decides which ports can be probed at all, and a scan is the textbook input to an [[Intrusion Detection Systems|intrusion detection system]] — one host touching many ports in sequence is hard to mistake for normal use.

## See Also

- [[OS Fingerprinting]]
- [[Vulnerability Analysis]]
- [[TCP]]
- [[SYN Flooding]]
- [[Computer Networking]]
- [[Worms]]
- [[Firewalls]]
- [[Intrusion Detection Systems]]
- [[CSCE 465]]
