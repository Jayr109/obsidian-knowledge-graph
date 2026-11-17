---
title: "TCP Reset Attack"
type: concept
tags: [csce465, security, network-security, tcp, rst, denial-of-service, sequence-numbers]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

The **TCP reset (RST) attack** tears down somebody else's connection with one forged packet. A [[TCP]] segment carrying the `RST` flag tells the receiver to abandon the connection immediately; the attack is to send one that looks as though it came from the other endpoint. [[CSCE 465]] presents it as the second of three TCP attacks, between [[SYN Flooding]] and [[TCP Session Hijacking]].

## The Attack

> - Send a **RST (TCP RESET flag) packet with a spoofed IP address** to either side of a valid connection
>   - Need to guess a sequence number **inside the appropriate window**
>     - Or sniff traffic to know which number to use
>   - The range can be guessed fairly efficiently for RST attacks
>   - Sequence numbers: **32 bits**
>   - Window size: **up to 16 bits**
>   - Number of guesses 32−16 = **16 bit address space**
>     - **65535 RST attempts, ~ 4 min on DSL connection**
>     - Faster connection or zombies, faster RST
>     - This is the **brute force RST attack**

## The Arithmetic

The receiver does not require the forged segment to carry the exact next sequence number, only one that falls **inside its current window**. So the attacker does not search a 32-bit space one value at a time. It steps through it one window at a time:

```
sequence space        2^32
window (up to)        2^16
guesses needed        2^32 / 2^16  =  2^16  =  65,536
```

> **Verified during ingest.** 2³² / 2¹⁶ = 65,536; the slide's 65535 is the same figure, one short. The *~4 minutes on DSL* is consistent with it: 65,536 packets in 240 seconds is about 273 packets per second, and at 40 bytes each (a 20-byte IP header and a 20-byte TCP header) that is roughly 87 kbit/s — an ordinary DSL uplink. A faster link, or many machines (*zombies*) splitting the range, shortens it in proportion.

## Why the Window Matters

Two slides earlier the lecture introduced the window as a performance feature:

> **TCP "Window"** — with every ACK, the receiver indicates how many more bytes it is prepared to receive. *The more can be sent, the more efficient the network is.*

and stated the rule that protects a connection:

> TCP packets with sequence numbers **outside the window are ignored** — this makes attacks on TCP applications harder than if they used UDP.

> **The same field does both jobs, derived.** The window is what makes blind injection hard (2³² possibilities) and what makes it feasible (anything in-window is accepted). A bigger window means better throughput and fewer guesses for the attacker. That is a real trade-off between performance and security sitting in one 16-bit header field.
>
> The count also assumes the attacker already knows which connection to hit: both addresses and both ports. The server's port is usually well known; the client's has to be guessed or observed, which multiplies the work unless the attacker can sniff the traffic, as the slide notes. So the realistic targets are long-lived connections between known endpoints, where four minutes is short compared with the connection's lifetime.

## How It Compares

| Attack | What the attacker must know about sequence numbers |
|---|---|
| [[SYN Flooding]] | Nothing |
| **TCP reset** | Any value inside the window — about 1 chance in 2¹⁶ per guess |
| [[TCP Session Hijacking]] | The exact initial sequence number the server will choose |

All three use a [[IP Spoofing|forged source address]], and all three are *blind*: the attacker sends and never needs a reply. The reset attack is an **interruption** in [[Security Attack Taxonomy|the taxonomy]] — it destroys a connection without reading or altering a byte of it.

## See Also

- [[TCP]]
- [[IP Spoofing]]
- [[SYN Flooding]]
- [[TCP Session Hijacking]]
- [[Security Attack Taxonomy]]
- [[Vulnerability Analysis]]
- [[CSCE 465]]
