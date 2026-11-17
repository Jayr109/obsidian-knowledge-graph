---
title: "ICMP"
type: concept
tags: [csce465, networking, icmp, ping, traceroute, diagnostics]
sources: [csce465-lecture-10-network-basics, csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

**ICMP** — Internet Control Message Protocol — is how the network reports on itself.

> - Used to report **problems with delivery of IP datagrams** within an IP network
> - Used by **Ping** and **Traceroute** commands

It rides inside [[Internet Protocol|IP]] as protocol number **1**, which makes it structurally odd: a protocol carried by the thing it exists to report on.

Lecture 12 comes back to it as a target and restates it in five lines, one of them with an exclamation mark:

> - Internet Control Message Protocol (**IP management**)
> - Error handling and debugging protocol
> - **Not authenticated!**
> - Encapsulated inside an IP header
> - Message types: **40 assigned, 255 possible, about two dozen in use**

## Message Format

```
+--------------+--------------+--------------+
|  IP Header   | ICMP Header  |  ICMP Data   |
|   20 bytes   |   4 bytes    |              |
+--------------+--------------+--------------+
                      |
         +------+------+----------+
         | Type | Code | Checksum |
         | 1 B  | 1 B  |   2 B    |
         +------+------+----------+
```

A four-byte header on top of the standard twenty-byte IP header. **Type** says what kind of message it is, **Code** sub-classifies it.

## Types and Codes

The four the lecture names:

| Message | Type | Code |
|---|---|---|
| **Echo Request** | 8 | 0 |
| **Echo Reply** | 0 | 0 |
| **Destination Unreachable** | 3 | 0 |
| **Time Exceeded** | 11 | 0 | 

**Time Exceeded** is sent when **Time-to-Live = 0**.

Lecture 12's *Basic ICMP Message Type* slide gives the longer list by type number:

| Type | Message | Type | Message |
|---|---|---|---|
| **0** | **Echo Reply** | 12 | Parameter Problem |
| 3 | Destination Unreachable | 13 | Timestamp |
| 4 | Source Quench | 14 | Timestamp Reply |
| **5** | **Redirect** | 15 | Information Request |
| **8** | **Echo** | 16 | Information Reply |
| 11 | Time Exceeded | | |

The slide sets three in bold — **0, 5 and 8** — and they are the three the attacks below use.

## How Ping and Traceroute Fall Out of This

- **Ping** sends an Echo Request (type 8) and waits for an Echo Reply (type 0). Reachability and round-trip time from two messages.
- **Traceroute** exploits Time Exceeded. Send a datagram with **TTL = 1**; the first router decrements it to zero, discards it, and reports back with type 11 — revealing its own address. Repeat with TTL = 2, 3, and so on, and each router along the path identifies itself in turn.

> **Traceroute is a protocol being used against its purpose, derived.** The TTL field exists to stop datagrams circulating forever in a routing loop, and Time Exceeded exists so a sender learns why its traffic vanished. Traceroute deliberately *causes* that failure, once per hop, and reads the error messages as a map. The lecture presents both as diagnostics; the same property makes ICMP a **reconnaissance tool** — an attacker who can ping and traceroute a network learns which hosts are live and what the topology is, before sending a single packet to the real target. That is why so many networks silently drop ICMP at the border, and why the [[Notable Worms|Welchia counter-worm]] used ICMP to find live addresses before copying itself across.

## Attacks on ICMP

*Not authenticated* is the whole vulnerability: a host acts on an ICMP message without any way to tell who sent it. Lecture 12 gives two attacks, and between them they use the three bolded types above.

| Message abused | Attack | What happens |
|---|---|---|
| Echo (8) and Echo Reply (0) | [[Smurf Attack]] | A ping to a broadcast address with the victim as source; every host replies to the victim |
| Redirect (5) | [[ICMP Redirect Attack]] | A forged "use that gateway instead" sends a host's traffic through the attacker |

TTL comes back once more in the intrusion detection lecture, which lists it as an example of an insertion attack: a packet whose TTL runs out between a monitor and its target is seen by one and not the other. See [[Insertion and Evasion Attacks]].

## See Also

- [[Smurf Attack]]
- [[ICMP Redirect Attack]]
- [[OS Fingerprinting]]
- [[Internet Protocol]]
- [[TCP]]
- [[Computer Networking]]
- [[Notable Worms]]
- [[CSCE 465]]
