---
title: "CSCE 465 Lecture 10 — Network Basics"
type: source
tags: [csce465, networking, tcp-ip, http, smtp, icmp, background]
sources: []
course: CSCE 465
updated: 2026-11-04
---

Lecture 10 of [[CSCE 465]] (`raw/CSCE465_10_NetworkBasics.pdf`, 13 PDF pages laid out two slides per page = **26 logical slides**, instructor [[Guofei Gu]]). This opens the **network security** unit by first establishing the protocols it will attack. There is almost no security content in the deck itself — it is deliberate background, and the shortest CSCE 465 lecture so far.

It overlaps [[CSCE 313]] heavily, which is handled below.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–5 | **Naming and applications** | Naming in a networked environment (where/who/how/what mapped onto layers); protocols for that environment; client-server model; standard application protocols and the telnet multiple-choice question |
| 7–10 | **Application protocols by hand** | Fetching a web page with telnet; the Alice-to-Bob mail scenario; a sample SMTP interaction; sending email with telnet |
| 12–18 | **TCP/IP basics** | OSI vs the TCP/IP hierarchy; packet encapsulation; Ethernet; ARP; IP and the protocol field; IP routing; ICMP |
| 20–22 | **TCP** | Header format; connection establishment and close; data transfer and retransmission |
| 23–26 | **HTTP and a worked trace** | HTTP transaction steps; methods and response codes; end-to-end trace of accessing `www.cse.tamu.edu`; references |

## Pages Derived

| Page | What it holds |
|---|---|
| [[Internet Protocol]] | Unreliable connectionless delivery, the protocol field (1/6/17), routing tables, the per-hop two-layer router |
| [[TCP]] | Header format, three-way handshake, four-message close, retransmission timer |
| [[ICMP]] | Message format, the four type/code pairs, how ping and traceroute fall out of them |
| [[HTTP]] | Transaction steps, methods, response-code categories, `GET /` over telnet, the end-to-end trace |
| [[SMTP]] | The MUA/MTA path, the wire transcript, sending mail by hand, and what that demonstrates about authentication |

## What Was Deliberately Not Created

Five slides of this deck are already in the KB from [[CSCE 313]], and **no page was created or duplicated for them**:

| Slide content | Already covered by |
|---|---|
| OSI vs TCP/IP layering | [[Computer Networking]] — *Protocol Layering* |
| Client-server model | [[Computer Networking]] — *Client-Server Model* |
| IP addresses, ports | [[Computer Networking]] — *IP Addresses*, *Ports* |
| Ethernet frames, MAC addresses, packet encapsulation | [[Data Link Layer]] |
| ARP, ARP cache | [[ARP]] |

Those three CSCE 313 pages instead gained short cross-links into the new protocol pages. This is the same discipline applied when Lecture 7 and Lecture 9 met CSCE 313 — the 465 pages carry the **protocol mechanics the later attacks target**, and the 313 pages keep the programming-level treatment.

## Content Worth Keeping

**IP is unreliable and connectionless, and that is a design choice with consequences.** Routers hold no per-connection state and nothing authenticates the source address — the enabling condition for spoofing and for reflection attacks. → [[Internet Protocol]]

**A router implements only the bottom two layers.** It reads the IP header, consults its routing table, forwards, and never sees the transport or application layers. → [[Internet Protocol]]

**The TCP three-way handshake is a reachability proof — and a state allocation.** Completing it requires receiving a number the other side chose, which is why spoofing a full TCP conversation is hard; but the responder allocates state on the SYN, before the handshake completes, which is the SYN flood. → [[TCP]]

**Traceroute works by deliberately causing a failure.** Send TTL = 1, read the Time Exceeded (type 11) that comes back, repeat. The same property makes ICMP a reconnaissance tool. → [[ICMP]]

**HTTP is just text over a TCP connection.** `telnet httpforever.com 80` then `GET /` with two carriage returns is a complete request. Everything a client claims about itself is client-supplied. → [[HTTP]]

**SMTP authenticates nothing.** `HELO` and `MAIL FROM:` are strings the client types; the server's *"Sender ok"* means well-formed, not genuine. The telnet exercise is a demonstration of email spoofing. → [[SMTP]]

**The deck answers its own telnet question by example.** It asks whether telnet can access terminals, access services, send email, or fetch a web page — then demonstrates sending email and fetching a web page. → [[SMTP]]

## Connection to the Rest of the KB

- **This is the third 465 lecture to overlap [[CSCE 313]]** (after 7 and 9), and the heaviest. The split held: 313 keeps the socket API and byte-order mechanics, 465 takes the protocol formats and handshakes.
- **[[ARP]] was already in the KB with its spoofing section**, written from the CSCE 313 side. [[Internet Protocol]] now gives the structural reason the same class of attack works one layer up.
- **[[SMTP]] connects to [[CIA Triad|origin integrity]]** more directly than anything since the hash unit: the protocol provides data integrity of a sort and no origin integrity whatsoever.
- **The protocols here are the targets of the rest of the unit.** The deck is background for malware, firewalls, intrusion detection and web security — and [[Notable Worms|Lecture 11's worms]] already exercise several: Slammer is a single UDP packet to port 1434, Nimda arrives over SMTP, Welchia uses ICMP to find live hosts.

## Extraction Note

Text extracted with PyMuPDF and essentially complete: the SMTP transcript, the TCP header field layout, the ICMP type/code list, the Ethernet frame byte counts and the HTTP response categories all survived intact.

**Figures extract as label clouds** — boxes and arrows lost, labels preserved. This affects the handshake diagrams (slides 21–22), the IP routing figure (17), the packet encapsulation bar (13) and the end-to-end trace (25). All were reconstructed from the labels **plus** the accompanying prose, which states each relationship; the raw deck remains authoritative for exact figure geometry.

**Encapsulation byte counts cross-checked:** the encapsulation slide gives 22 / 20 / 20 / 4 / 64–1500 bytes, and the Ethernet slide independently gives preamble 8 + destination 6 + source 6 + type 2 = **22**, with CRC 4 and data 64–1500. The two slides agree, and 20 + 20 is the IP and TCP headers.

**Deck erratum:** the TCP data-transfer diagram reads **"Send AXK 1"** for *ACK 1*. Corrected silently on [[TCP]] and recorded here.

**Oddity in the handshake diagrams:** both label their columns *"Host"* and *"Client"* rather than client and server, with the left-hand column initiating. The derived page uses **initiator / responder** to avoid the ambiguity, which is a presentation change, not a content one.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Internet Protocol]]
- [[TCP]]
- [[ICMP]]
- [[HTTP]]
- [[SMTP]]
- [[Computer Networking]]
- [[Data Link Layer]]
- [[ARP]]
- [[CSCE 313]]
- [[CSCE 465 Lecture 11 — Malware]]
