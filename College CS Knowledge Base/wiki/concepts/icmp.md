---
title: "ICMP"
type: concept
tags: [csce465, networking, icmp, ping, traceroute, diagnostics]
sources: [csce465-lecture-10-network-basics]
course: CSCE 465
updated: 2026-11-04
---

**ICMP** — Internet Control Message Protocol — is how the network reports on itself.

> - Used to report **problems with delivery of IP datagrams** within an IP network
> - Used by **Ping** and **Traceroute** commands

It rides inside [[Internet Protocol|IP]] as protocol number **1**, which makes it structurally odd: a protocol carried by the thing it exists to report on.

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

## How Ping and Traceroute Fall Out of This

- **Ping** sends an Echo Request (type 8) and waits for an Echo Reply (type 0). Reachability and round-trip time from two messages.
- **Traceroute** exploits Time Exceeded. Send a datagram with **TTL = 1**; the first router decrements it to zero, discards it, and reports back with type 11 — revealing its own address. Repeat with TTL = 2, 3, and so on, and each router along the path identifies itself in turn.

> **Traceroute is a protocol being used against its purpose, derived.** The TTL field exists to stop datagrams circulating forever in a routing loop, and Time Exceeded exists so a sender learns why its traffic vanished. Traceroute deliberately *causes* that failure, once per hop, and reads the error messages as a map. The lecture presents both as diagnostics; the same property makes ICMP a **reconnaissance tool** — an attacker who can ping and traceroute a network learns which hosts are live and what the topology is, before sending a single packet to the real target. That is why so many networks silently drop ICMP at the border, and why the [[Botnets|Welchia counter-worm]] used ICMP to find live addresses before copying itself across.

## See Also

- [[Internet Protocol]]
- [[TCP]]
- [[Computer Networking]]
- [[Notable Worms]]
- [[CSCE 465]]
