---
title: "ARP Poisoning"
type: concept
tags: [csce465, security, network-security, arp, spoofing, man-in-the-middle, data-link-layer]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

**ARP poisoning** (also *ARP cache poisoning* or *ARP spoofing*) plants a false IP-to-MAC mapping in another machine's ARP cache, so that frames meant for one host are delivered to a different one. It is [[CSCE 465]]'s link-layer example in the [[Vulnerability Analysis|vulnerability analysis]] lecture.

[[ARP]] from [[CSCE 313]] is the protocol page — the request/reply exchange, the cache, `arp -a`, and a short spoofing section written from the systems side. This page is the attack as CSCE 465 teaches it, and the defences, which the CSCE 313 lecture did not cover.

## What Is Being Abused

> ARP is used by routers extensively to find the destination node. Routers have IP addresses (32-bits). In order to deliver the packet to the destination node, the router broadcasts the IP address of the destination and obtains the MAC address (48-bits).

The deck's figure shows the two halves of the exchange: the **request is broadcast** (*"I am looking for the physical address of a node whose IP address is 141.23.56.23"*) and the **reply is unicast** (*"I am the node you are looking for and my physical address is A46EF45983AB"*). Hosts store the answer in the ARP table.

## The Attack

> ARP Poisoning means that the ARP communication is intercepted by redirection from a router.
>
> - Assume router's IP is 10.1.1.0
> - Host's IP is 10.1.1.1
> - Malicious host with IP 10.1.1.2 **spoofs 10.1.1.1** and replies to requests from 10.1.1.0 with **its** MAC address
> - From this point on all packets meant for 10.1.1.1 is routed to 10.1.1.2 because the router has the MAC address of 10.1.1.2 in its routing table

## The Worked Figure

Two slides show the same three hosts on one switch, before and after:

| Host | IP | MAC |
|---|---|---|
| A | 10.0.0.1 | aa:aa:aa:aa |
| B | 10.0.0.2 | bb:bb:bb:bb |
| Hacker | 10.0.0.3 | cc:cc:cc:cc |

The hacker sends A a **spoofed ARP reply** reading `IP: 10.0.0.2, MAC: cc:cc:cc:cc` — B's address, the hacker's hardware.

| | A's ARP cache | B's ARP cache |
|---|---|---|
| Before | 10.0.0.2 → bb:bb:bb:bb | 10.0.0.1 → aa:aa:aa:aa |
| After | 10.0.0.2 → **cc:cc:cc:cc** | 10.0.0.1 → aa:aa:aa:aa |

> **A's cache is poisoned.**

> **Two things the figure shows without saying, derived.** First, only **one direction** is poisoned. A's traffic for B now goes to the hacker; B's traffic for A is untouched. A full man-in-the-middle poisons B's entry for A as well and forwards in both directions, so neither side notices.
>
> Second, **the switch is not fooled and does not need to be.** It forwards every frame correctly by MAC address. The lie is in the *host's* table, one layer up, which is why a switched network gives no protection here. Lecture 2 asked what a sniffer can see on a switched network; [[Security Attack Taxonomy]] recorded the answer as the reason this attack exists.

## Defenses

> **No universal defense.**

| Defense | How it works | The lecture's catch |
|---|---|---|
| **Static ARP entries** | Cannot be updated; spoofed ARP replies are ignored | Needs a static entry for each machine on the network. **Large overhead** — deploying the tables and keeping them up to date. And: *someone point out that Windows still accepts spoofed ARP replies and updates the static entry with the forged MAC*, sabotaging the purpose |
| **Port security** (port binding, MAC binding) | A feature on some high-end switches; prevents changes to the MAC tables of a switch unless manually performed by a network administrator | Not suitable for large networks and networks using DHCP |
| **Arpwatch** | A free UNIX program that listens for ARP replies, builds a table of IP/MAC associations in a file, and **emails an administrator when a pair changes** (a *flip-flop*) | — |
| **RARP** (Reverse ARP) | Requests the IP of a known MAC; **detects MAC cloning** — cloning shows up as multiple replies to a single RARP | — |

> **The four split two and two, derived.** Static entries and port security are **prevention**: they stop the cache or the switch table from changing. Arpwatch and RARP are **detection**: they let the change happen and report it. That is the [[Security Policy and Mechanism|prevention/detection split]] from Lecture 2 at the scale of one protocol, and the preventive pair fails for the reason prevention usually does — the administrative cost grows with the network. Arpwatch is a small [[Intrusion Detection Systems|intrusion detection system]]: it keeps a record of what normal looks like and raises an alarm on a change.

## How It Relates to the Other Attacks

The lecture calls the [[ICMP Redirect Attack]] *similar ideologically to ARP poisoning*: both corrupt a table a host uses to decide where to send its packets, using a message the protocol never authenticates. [[IP Spoofing]] is the same absence one layer up. All three are **fabrication** in [[Security Attack Taxonomy|the taxonomy]] — a false claim of origin — and the man-in-the-middle position they produce is what makes interception and tampering possible afterwards.

## Deck Wording

Four phrases on these slides are loose and are recorded as written, not corrected in the quotes: the poisoned table is called a *routing table* (it is the ARP table); the last defence bullet says *static routes* (static ARP entries); the example router is given the address `10.1.1.0`; and the one-line definition speaks of *redirection from a router*, where the example that follows shows a forged reply from an ordinary host.

## See Also

- [[ARP]]
- [[Data Link Layer]]
- [[ICMP Redirect Attack]]
- [[IP Spoofing]]
- [[Security Attack Taxonomy]]
- [[Security Policy and Mechanism]]
- [[Intrusion Detection Systems]]
- [[Vulnerability Analysis]]
- [[CSCE 465]]
- [[CSCE 313]]
