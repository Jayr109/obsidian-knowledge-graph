---
title: "SYN Flooding"
type: concept
tags: [csce465, security, network-security, tcp, denial-of-service, syn-flood, syn-cookies]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

A **SYN flood** is a denial-of-service attack on the [[TCP]] three-way handshake: send the first message many times and never send the third. [[CSCE 465]] gives it as the first of three TCP attacks, with one statistic attached — **90% of DoS attacks use TCP SYN floods**.

## The Attack

The lecture describes it twice. First as a mechanism:

> - This exploits how the 3-way handshake of TCP services for opening a session works.
> - SYN packets are sent to the target node with **incomplete source IP addresses**
> - The node under attack sends an ACK packet and **waits for response**
> - Since the request has not been processed, it **takes up memory**
> - Many such SYN packets clog the system and take up memory
> - Eventually the attacked node is unable to process any requests as it runs out of memory storage space

Then as a summary:

> - Streaming **spoofed** TCP SYNs
> - Takes advantage of three way handshake
> - Server start **"half-open"** connections
> - These build up… until **queue is full** and all additional requests are blocked

```
  attacker (source forged)                 server
      |--- SYN, src = bogus_1 ------------->|  allocate entry 1, send SYN+ACK to bogus_1
      |--- SYN, src = bogus_2 ------------->|  allocate entry 2, send SYN+ACK to bogus_2
      |--- SYN, src = bogus_3 ------------->|  allocate entry 3, ...
      |            ...                      |  queue full
  real client                               |
      |--- SYN ---------------------------->|  refused
```

(*Incomplete source IP addresses* means [[IP Spoofing|spoofed]] ones, and the *ACK packet* the victim sends is the handshake's `SYN+ACK`.)

## Why It Works

> **The asymmetry, derived.** The server commits memory on the *first* packet of the handshake; the attacker commits nothing. A real client would answer the `SYN+ACK` and turn the half-open entry into a connection. A forged source never answers — the reply went to an address that is not the attacker's — so each entry sits until it times out. The spoofed source does two jobs at once: it keeps the entry half-open, and it hides who is sending.
>
> [[TCP]] recorded this as a derived consequence of the handshake diagram when Lecture 10 was ingested (*"the responder must allocate state when it receives the SYN, before the handshake completes"*). Lecture 12 confirms it as course content.

In [[Security Attack Taxonomy|the taxonomy]] this is **interruption**, an attack on availability, of the *overwhelm until resources are exhausted* kind. It needs no vulnerability in the server's code and no knowledge of sequence numbers.

## The Fix: SYN Cookies

The slide that states the problem ends on *"Solution?"* The next one answers:

> **TCP SYN cookies — general idea**
> - Client sends SYN w/ ACK number
> - Server responds to Client with **SYN-ACK cookie**
>   - `sqn = f(src addr, src port, dest addr, dest port, rand)`
>   - **Server does not save state**
> - Honest client responds with `ACK(sqn+1)`
> - Server checks response
> - If matches SYN-ACK, establishes connection

```
  client                                   server
     |--- SYN ----------------------------->|  sqn = f(src addr, src port, dst addr, dst port, rand)
     |<-- SYN+ACK, seq = sqn ---------------|  stores NOTHING
     |--- ACK = sqn + 1 ------------------->|  recompute f; does ACK - 1 equal it?
     |                                      |  yes: allocate the connection now
```

> **What the cookie is, derived.** The server's own initial sequence number *becomes* the half-open entry. Instead of remembering *"I sent `y` to this client"*, the server picks a `y` it can recompute later from the packet in front of it plus a secret. A forged SYN now costs one computation and one outgoing packet, and **zero memory**. Nothing is left to fill.
>
> The handshake's protection is kept, and moved earlier. Only a client that actually received the `SYN+ACK` can return `sqn+1`, so reachability is still proved before any state exists. This depends on `rand` staying secret: if `f` were predictable, an attacker could forge the third message without seeing the second, which is the [[TCP Session Hijacking|sequence-prediction attack]] under another name.

**Deck wording:** the first bullet says the client sends a SYN *"w/ ACK number"*. A SYN carries a sequence number, not an acknowledgement number. Recorded as written.

## Where Else It Shows Up

- [[TCP Session Hijacking]] uses a SYN flood as its **first step**, to keep the impersonated host quiet.
- A [[Port Scanning|SYN scan]] leaves one half-open connection per probed port — the same state, used to ask a question instead of to exhaust a queue.
- A [[Session Filtering|stateful firewall]] keeps a connection table of its own, so it inherits this problem along with the server it protects.

## See Also

- [[TCP]]
- [[IP Spoofing]]
- [[TCP Session Hijacking]]
- [[TCP Reset Attack]]
- [[Smurf Attack]]
- [[Port Scanning]]
- [[Security Attack Taxonomy]]
- [[Security Threat Landscape]]
- [[Vulnerability Analysis]]
- [[CSCE 465]]
