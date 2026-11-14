---
title: "TCP"
type: concept
tags: [csce465, networking, tcp, transport-layer, handshake, reliability]
sources: [csce465-lecture-10-network-basics]
course: CSCE 465
updated: 2026-11-04
---

**TCP** is the transport layer that makes [[Internet Protocol|IP]]'s unreliable datagram service usable. [[CSCE 465]] characterizes it in three words — **connection-oriented, reliable, byte stream service** — and then shows the three mechanisms that deliver each: a handshake, acknowledgements with retransmission, and sequence numbers.

[[Computer Networking]] from [[CSCE 313]] covers the **socket API** that programs use to speak TCP. This page is the protocol underneath it.

## The Protocol in Three Steps

> 1. Set up connection
> 2. Transfer data
> 3. Close connection

## Header Format

The lecture's 32-bit-wide header diagram:

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-------------------------------+-------------------------------+
|          Source Port          |       Destination Port        |
+---------------------------------------------------------------+
|                        Sequence Number                        |
+---------------------------------------------------------------+
|                     Acknowledgement Number                    |
+-------+-------+---------------+-------------------------------+
| Data  |       |               |                               |
| Offset|   -   |     flags     |            Window             |
+-------+-------+---------------+-------------------------------+
|           Checksum            |        Urgent Pointer         |
+-------------------------------+-------------------------------+
|            Options (0 to 10 Words of 32 Bits)                 |
+---------------------------------------------------------------+
|                         TCP Payload                           |
+---------------------------------------------------------------+
```

The two **port** fields plus the two IP addresses are what identify a connection; see [[Computer Networking|the 4-tuple]]. The **sequence** and **acknowledgement** numbers are what make the byte stream reliable and ordered.

## Establishing a Connection — the Three-Way Handshake

```
  Initiator                               Responder
      |                                       |
      |------ SYN, seq = x ------------------>|
      |                                       |  receives SYN
      |<----- SYN, seq = y, ACK = x+1 --------|
      |  receives SYN+ACK                     |
      |------ ACK = y+1 --------------------->|
      |                                       |  receives ACK
```

Each side chooses an initial sequence number (`x`, `y`) and each acknowledges the other's by returning it **plus one**. After three messages both sides know the other is reachable and both know where the other's byte stream starts.

> **Two things the handshake is quietly doing, derived.** First, it is a **reachability proof**: completing it requires receiving a number the other side chose, which an attacker who can send but not receive at a spoofed address cannot do. That is why [[Internet Protocol|IP source spoofing]] is easy for a single datagram and hard for a full TCP conversation. Second, the responder must **allocate state** when it receives the SYN, before the handshake completes — it has to remember `x` and its own `y`. An attacker who sends many SYNs and never completes the third step consumes that state without ever proving reachability. That is the SYN flood, and it follows directly from the shape of the diagram above.
>
> It also follows that the security of the first property depends entirely on `y` being **unguessable**. If initial sequence numbers are predictable, an attacker can forge the third message without ever seeing the second — the classic sequence-number prediction attack.

## Closing a Connection

Close is symmetric and takes four messages, because each direction of the byte stream is shut down independently:

```
  Initiator                               Responder
      |------ FIN, seq = x ----------------->|
      |                                      |  receives FIN
      |<----- ACK = x+1 ---------------------|
      |<----- FIN, seq = y, ACK = x+1 -------|
      |  receives FIN+ACK                    |
      |------ ACK = y+1 -------------------->|
      |                                      |  receives ACK
```

## Data Transfer and Retransmission

Reliability is an acknowledgement plus a timer, and the lecture's diagram shows the loss case:

```
  Sender                                  Receiver
      |--- Packet 1 ---X  (lost)              |
      |  start timer                          |
      |                                       |  ACK would normally
      |                                       |  arrive about here
      |  time expires                         |
      |--- Retransmit Packet 1 -------------->|  receives Packet 1
      |  start timer                          |  sends ACK 1
      |<-- ACK 1 -----------------------------|
      |  cancel timer                         |
```

The sender starts a timer on transmission, cancels it on acknowledgement, and retransmits if it expires. Nothing in the protocol tells the sender *why* a packet was lost — congestion, corruption, or a dropped link all look identical, which is why the timer is the only recovery mechanism.

## See Also

- [[Internet Protocol]]
- [[ICMP]]
- [[HTTP]]
- [[SMTP]]
- [[Computer Networking]]
- [[Data Link Layer]]
- [[CSCE 465]]
- [[CSCE 313]]
