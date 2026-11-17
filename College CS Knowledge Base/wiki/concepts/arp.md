---
title: "ARP"
type: concept
tags: [csce313, csce465, networking, arp, arp-spoofing, network-security, data-link-layer, mac-addresses]
sources: [csce-313-lecture-22-data-link-layer, csce465-lecture-12-vulnerability-analysis]
course: CSCE 313
updated: 2026-11-16
---

ARP (Address Resolution Protocol) bridges the Network layer and the Data Link layer by resolving an IP address to its corresponding MAC address. Because IP packets must be encapsulated in Ethernet frames to traverse a LAN, a host must know the MAC address of the next hop before it can send a packet.

## How ARP Works

ARP uses a broadcast-then-cache model:

1. **Request** — host A broadcasts a frame to all LAN members:
   `who has <IP1> tell <IP2>`
2. **Reply** — the host with `<IP1>` (or an ARP proxy) sends a unicast response back to host A:
   `<IP1> is <MAC1>`
3. **Cache** — host A stores `<IP1> → <MAC1>` in its ARP cache for future use.

> L22 p.16 contained a visual diagram of the broadcast/unicast exchange; text was partially extracted.

[[CSCE 465]] Lecture 12 carries the same exchange as a figure that could be read in full, in two panels:

- **a. ARP request is broadcast** — System A sends a request to every machine on the segment: *"I am looking for the physical address of a node whose IP address is 141.23.56.23."*
- **b. ARP reply is unicast** — only System B answers, and only to A: *"I am the node you are looking for and my physical address is A46EF45983AB."*

## Packet Format

Also from CSCE 465 Lecture 12, the ARP message itself:

```
+-------------------------------+-------------------------------+
|    Hardware Type (16 bits)    |    Protocol Type (16 bits)    |
+---------------+---------------+-------------------------------+
|   HA Length   |   PA Length   |      Operation (16 bits)      |
|   (8 bits)    |   (8 bits)    |                               |
+---------------+---------------+-------------------------------+
|             Sender Hardware Address (octets 0-3)              |
+-------------------------------+-------------------------------+
|  Sender Hardware Address      |  Sender Protocol Address      |
|  (octets 4-5)                 |  (octets 0-1)                 |
+-------------------------------+-------------------------------+
|  Sender Protocol Address      |  Target Hardware Address      |
|  (octets 2-3)                 |  (octets 0-1)                 |
+-------------------------------+-------------------------------+
|             Target Hardware Address (octets 2-5)              |
+---------------------------------------------------------------+
|             Target Protocol Address (octets 0-3)              |
+---------------------------------------------------------------+
```

*HA* is the hardware (MAC) address, six octets on Ethernet; *PA* is the protocol (IP) address, four. The **Operation** field says whether the message is a request or a reply. There is no field that ties a reply to a request and none that authenticates the sender — the sender's hardware and protocol addresses are simply whatever the sender wrote, which is the opening the *ARP Spoofing* section below describes.

## Inspecting the ARP Cache

```bash
arp -a          # Linux and Windows
```

Example output:
```
Internet Address      Physical Address      Type
128.148.31.1          00-00-0c-07-ac-00     dynamic
128.148.31.15         00-0c-76-b2-d7-1d     dynamic
```

`dynamic` entries are learned via ARP; `static` entries are manually configured.

## ARP Spoofing

ARP has no authentication mechanism, creating a well-known security vulnerability:

- The ARP cache is updated whenever an ARP reply is received — even without a prior request.
- An attacker can send **gratuitous ARP replies** (unsolicited) to poison any host's cache.
- ARP requests are not tracked, so hosts cannot verify whether a reply corresponds to a legitimate request.
- All hosts on the segment trust each other by default.

**Attack scenario:** A rogue host sends a gratuitous ARP claiming that its MAC address corresponds to the gateway's IP. Victims update their caches, routing their traffic through the attacker → **man-in-the-middle (MITM) attack**.

**Defenses (not covered in L22, general knowledge):**
- Dynamic ARP Inspection (DAI) on managed switches.
- Static ARP entries for critical hosts.
- Network segmentation and VLANs.

**Covered in CSCE 465.** Lecture 12 teaches this attack as *ARP poisoning*, with a worked before-and-after of the two caches and four defences of its own — static entries (and why they do not scale), port security, arpwatch, and RARP — under the heading *no universal defense*. That treatment is on [[ARP Poisoning]]; this page stays the protocol reference.

## See Also

- [[ARP Poisoning]]
- [[Data Link Layer]]
- [[Computer Networking]]
- [[CIA Triad]] — ARP spoofing is an origin-integrity (authentication) failure
- [[Computer Security]]
- [[CSCE 313 Lecture 22 — Network Security: The Data Link Layer]]
- [[Internet Protocol]]
- [[ICMP]]
