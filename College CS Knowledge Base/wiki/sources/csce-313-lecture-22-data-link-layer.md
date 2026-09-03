---
title: "CSCE 313 Lecture 22 — Network Security: The Data Link Layer"
type: source
tags: [csce313, networking, data-link-layer, arp, mac-addresses, ethernet, network-security]
sources: []
course: CSCE 313
updated: 2026-04-22
---

CSCE 313 Lecture 22 covers the data link layer in the context of network security. It introduces the OSI model, explains the role of the link layer in packet delivery, defines MAC addressing and Ethernet frames, describes how switches operate, explains ARP (Address Resolution Protocol), and ends with ARP spoofing as a network security threat. Instructor: Houngninou (18 slides).

## Extraction Notes

- Page 4 (Internet Layers diagram): visual — TCP/IP 4-layer stack with Ethernet/Fiber/WiFi at physical layer. Text extraction partial.
- Page 5 (Internet Routing diagram): visual-only — shows routing path across nodes (Alice → Ivy → John → Mary → Bob).
- Page 8 (Ethernet frame format): visual-only — frame structure (preamble, MACs, type, payload, CRC) not captured as text.
- Pages 9–12 (Packet switching sequence): visual-only — 4 diagrams showing incremental packet hop from node A to node F.
- Page 16 (ARP broadcast diagram): visual-only — shows ARP request broadcast and unicast reply.
- Page 18: blank/end slide.

## Content Summary

### OSI Model (p.2)
Seven-layer reference model created in 1983 by ISO. Layers (bottom to top): Physical, Data Link, Network, Transport, Session, Presentation, Application. The TCP/IP model collapses this to 4 layers.

### Data Link Layer (p.3)
Layer 2 of OSI. Responsibilities:
- Moves data into and out of physical links.
- Converts data stream to signals bit by bit (transmit side).
- Receives electrical signals, assembles them into frames (receive side).
- Hands completed frames up to the Network layer.

### Intermediate Layer Summary (p.7)
| Layer | Addressing | Protocol | Address Width |
|---|---|---|---|
| Link | MAC addresses | Ethernet, WiFi, Fiber | 48-bit |
| Network | IP addresses | IPv4 / IPv6 | 32-bit / 128-bit |
| Transport | Port numbers | TCP (connection) / UDP (connectionless) | 16-bit |

### Packet Encapsulation (p.6)
Each layer wraps the upper layer's data: Application packet → TCP/UDP header added → IP header added → Data link header + footer (frame).

### MAC Addresses (p.13)
- 48-bit identifier, represented in hex (e.g., `00-1A-92-D4-BF-86`).
- First 3 octets: OUI (Organizationally Unique Identifier), assigned by IEEE (e.g., Cisco `00-1A-A1`, ASUSTek `00-1A-92`).
- Last 3 octets: assigned by the manufacturer, uniqueness required.
- Can be reconfigured via network interface driver software (MAC spoofing possible).

### Switch (p.14)
- Common link-layer network device with multiple ports.
- Learns the MAC address of each connected computer.
- Forwards frames only to the destination computer (unicast, not broadcast).

### ARP — Address Resolution Protocol (pp.15–16)
Connects Network layer to Data Link layer by resolving IP addresses to MAC addresses. Works by broadcasting requests and caching responses.

Request broadcast format: `who has <IP1> tell <IP2>`

Response (unicast to requester): `<IP1> is <MAC>`

Linux/Windows command `arp -a` displays the ARP cache:
```
Internet Address      Physical Address      Type
128.148.31.1          00-00-0c-07-ac-00     dynamic
```

### ARP Spoofing (p.17)
Security vulnerability arising from ARP's lack of authentication:
- ARP table updated on any received ARP response (even unsolicited).
- Gratuitous ARP replies can poison any host's cache.
- Requests are not tracked; responses are not authenticated.
- Hosts implicitly trust each other.
- A rogue machine can impersonate another host → enables MITM attacks.

## See Also

- [[Data Link Layer]]
- [[ARP]]
- [[Computer Networking]]
- [[CSCE 313]]
- [[Houngninou]]
