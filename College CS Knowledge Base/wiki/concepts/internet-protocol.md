---
title: "Internet Protocol"
type: concept
tags: [csce465, networking, ip, routing, datagram, network-layer]
sources: [csce465-lecture-10-network-basics, csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

**IP** is the network layer of the TCP/IP stack: it moves datagrams from one host to another across intermediate networks. [[CSCE 465]] introduces it as background for the network security unit, and the two words that matter are the two it opens with — **unreliable** and **connectionless**.

> - **Unreliable … connectionless datagram delivery service**
> - Responsible for **routing** of data through intermediate networks and computers

[[Computer Networking]] from [[CSCE 313]] already covers IP *addresses* — dotted-decimal notation, network byte order, `htonl`/`inet_pton`. This page is about IP the *protocol*; that page is not repeated here.

## What "Unreliable and Connectionless" Commits To

- **Unreliable** — no guarantee a datagram arrives, arrives once, or arrives in order. IP will not retransmit.
- **Connectionless** — each datagram is routed independently. There is no state at the endpoints tying one datagram to the next.

> **Why the network was built this way, derived.** Everything IP declines to do is pushed to the endpoints, where [[TCP]] implements it with sequence numbers, acknowledgements and timers. That is the end-to-end argument, and it is what let the Internet scale: routers hold no per-connection state, so adding a connection costs the core nothing. The security consequence follows immediately and shapes the rest of the unit — **a router does not know which datagrams belong together, and nothing in IP authenticates the source address**. Both facts are assumptions attackers rely on, and neither is a bug.

## The Header

Lecture 12 shows the header itself — **20 bytes** before any options:

```
+-----------------------------------------+-----------------------------------------+
| version, header length, type of service |     16-bit total length (in bytes)      |
+-----------------------------------------+-------+---------------------------------+
|          16-bit identification          | flags |     13-bit fragment offset      |
+--------------------+--------------------+-------+---------------------------------+
| 8-bit time to live |   8-bit protocol   |         16-bit header checksum          |
+--------------------+--------------------+-----------------------------------------+
|                             32-bit source IP address                              |
+-----------------------------------------------------------------------------------+
|                           32-bit destination IP address                           |
+-----------------------------------------------------------------------------------+
|                                 options (if any)                                  |
+-----------------------------------------------------------------------------------+
|                                       data                                        |
+-----------------------------------------------------------------------------------+
```

The lecture draws it to make one point — the **source address** is a field the sender fills in, and *"source IP address cannot be trusted!"* That is [[IP Spoofing]].

> **Most of the other fields get used against the protocol too, derived.** The **time to live** differs by operating system and so identifies it ([[OS Fingerprinting]]), and a packet can be given just enough of it to pass a monitor and die before its target ([[Insertion and Evasion Attacks]]). The **identification** field is what nmap's *IPID sampling* reads. The **flags and fragment offset** are how one datagram is split, and overlapping fragments are the lecture's example of an evasion attack. The **protocol** byte is the next section.

## The Protocol Field

The IP header carries a protocol number naming what it is wrapping:

| Value | Protocol |
|---|---|
| `1` | [[ICMP]] |
| `6` | [[TCP]] |
| `17` | UDP |

This one byte is how the receiving host's network layer knows which transport layer to hand the payload to, and it is also the first thing a firewall rule or a packet filter looks at.

## IP Routing

A host or router decides where to send a datagram by consulting its **routing table**, whose entries the lecture gives as:

- **Destination IP address**
- **IP address of a next-hop router**
- **Flags**
- **Network interface specification**

The path through the network, in the lecture's diagram:

```
Source                 Router                Destination
-----------            -----------           -----------
Application                                  Application
Transport                                    Transport
Network      <----->   Network    <----->    Network
Link                   Link                  Link
```

The point the figure is making is that an intermediate router implements **only the bottom two layers**. It reads the IP header, consults its table, forwards, and never looks at the transport or application layers above. Each hop is a fresh next-hop decision; no router knows the whole route.

> **The attack surface this creates, derived.** Because forwarding is per-hop and stateless, a datagram's **source address is never verified by anyone along the path** — routers forward on the *destination* field, and checking the source would require knowing which addresses legitimately originate on which link. That is IP spoofing, and it is the enabling condition for the reflection and amplification attacks the network security unit builds toward. It is also why [[ARP|ARP spoofing]] works one layer down for the same structural reason: a protocol designed when every host on the network was trusted.
>
> **Confirmed by Lecture 12.** *"Most routers only care about destination address"* is a slide title there, and the attacks this paragraph predicted are worked in full: [[IP Spoofing]], the [[Smurf Attack]] and its DNS amplification variant, and [[ARP Poisoning]].

## Where It Sits

Below IP is the [[Data Link Layer|link layer]], which carries the datagram one hop using [[ARP]] to translate the next-hop IP address into a MAC address. Above it are [[TCP]] and UDP. [[ICMP]] is unusual — it rides *inside* IP (protocol 1) but exists to report on IP itself.

## See Also

- [[IP Spoofing]]
- [[OS Fingerprinting]]
- [[Packet Filtering]]
- [[Network Address Translation]]
- [[TCP]]
- [[ICMP]]
- [[Computer Networking]]
- [[Data Link Layer]]
- [[ARP]]
- [[HTTP]]
- [[CSCE 465]]
- [[CSCE 313]]
