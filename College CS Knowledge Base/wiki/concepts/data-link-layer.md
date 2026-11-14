---
title: "Data Link Layer"
type: concept
tags: [csce313, networking, data-link-layer, ethernet, mac-addresses, frames, switch, osi-model]
sources: [csce-313-lecture-22-data-link-layer]
course: CSCE 313
updated: 2026-04-22
---

The data link layer is Layer 2 of the OSI model. It is responsible for moving data into and out of a single physical link — converting outgoing data into signals bit by bit and reassembling incoming electrical signals into recognizable frame units before handing them to the Network layer.

## Role in the Protocol Stack

In the OSI model (7 layers), the data link layer sits between the Physical layer (raw signal transmission) and the Network layer (IP routing). In the TCP/IP model (4 layers), it is part of the combined "Link" layer.

**Responsibilities:**
- Frame construction and parsing (header + payload + CRC).
- Addressing within a local network segment (via MAC addresses).
- Hop-by-hop delivery — delivers a frame from one device to the next directly connected device (not end-to-end).
- Error detection at the frame level (CRC field).

## Ethernet

Ethernet is the dominant wired link-layer protocol. An Ethernet frame contains:
- **Preamble** — synchronization bytes.
- **Destination MAC** — 6 bytes.
- **Source MAC** — 6 bytes.
- **EtherType/Length** — identifies encapsulated protocol (e.g., 0x0800 = IPv4).
- **Payload** — up to 1500 bytes (MTU).
- **CRC** — 4-byte frame check sequence.

> Note: The full frame diagram in L22 p.8 was a visual-only slide; exact field widths not captured in text extraction.

Other link-layer technologies: WiFi (802.11), optical fiber.

## MAC Addresses

A **MAC (Media Access Control) address** is a 48-bit hardware identifier assigned to a network interface.

- Represented in hex: `00-1A-92-D4-BF-86`
- **First 3 octets** = OUI (Organizationally Unique Identifier), IEEE-assigned.
  - Examples: Cisco `00-1A-A1`, D-Link `00-1B-11`, ASUSTek `00-1A-92`
- **Last 3 octets** = device-specific, assigned by the manufacturer.
- Can be changed via driver software ("MAC spoofing").

MAC addresses are flat (no hierarchy) and only meaningful within a local network segment. Routers strip the frame header at each hop and write a new one — MAC addresses do not survive routing.

## Switch

A **switch** is a link-layer device that interconnects computers within a LAN.

- Operates at Layer 2 (unlike a hub, which broadcasts to all ports).
- Maintains a **MAC address table**: maps MAC addresses to switch ports, learned from observed traffic.
- Forwards incoming frames only to the port connected to the destination MAC.
- Reduces collisions and unnecessary traffic compared to a hub.

## Packet Switching

The Internet uses **packet switching**: data is broken into packets, each forwarded independently through a series of routers/switches. Each hop strips the current frame header, makes a routing/forwarding decision, and writes a new frame header for the next link.

> L22 pp.9–12 were visual-only diagrams showing a packet traversing nodes A → C → B → D → F step by step.

## Packet Encapsulation

Each layer wraps the upper layer's payload:

```
[ Data Link Header | IP Header | TCP/UDP Header | Application Data | Data Link Footer ]
```

At the receiver, each layer strips its own header and passes the inner payload up.

## See Also

- [[ARP]]
- [[Computer Networking]]
- [[CSCE 313 Lecture 22 — Network Security: The Data Link Layer]]
- [[Computer Networking]]
- [[Internet Protocol]]
- [[TCP]]
