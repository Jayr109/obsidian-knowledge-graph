---
title: "SMTP"
type: concept
tags: [csce465, networking, smtp, email, application-layer, spoofing]
sources: [csce465-lecture-10-network-basics]
course: CSCE 465
updated: 2026-11-04
---

**SMTP** — Simple Mail Transfer Protocol — moves email between mail servers over [[TCP]] port 25. [[CSCE 465]] walks the delivery path, shows the wire protocol as a plain-text transcript, and then has you send a message by hand with telnet. That last step is the security lesson, though the slide does not say so.

## The Delivery Path

The lecture's scenario — Alice sends a message to `bob@tamu.edu`:

1. Alice uses her **MUA** (mail user agent) to compose the message and address it to `bob@tamu.edu`
2. Alice's MUA sends the message to **her mail server**; the message is placed in a message queue
3. The **client side of SMTP** opens a TCP connection with **Bob's mail server**
4. The **MTA** (Message Transfer Agent) in the mail server sends Alice's message over the TCP connection
5. Bob's mail server places the message in **Bob's mailbox**
6. Bob invokes his user agent to read the message

```
Alice                                               Bob
 MUA  ---1,2--->  mail server  ---3,4--->  mail server  ---5,6--->  MUA
```

Note that steps 3 and 4 are **server to server**. The protocol below governs that hop.

## The Wire Protocol

The lecture's sample interaction, with `S:` the server and `C:` the client:

```
S: 220 hamburger.edu
C: HELO crepes.fr
S: 250  Hello crepes.fr, pleased to meet you
C: MAIL FROM: <alice@crepes.fr>
S: 250 alice@crepes.fr... Sender ok
C: RCPT TO: <bob@hamburger.edu>
S: 250 bob@hamburger.edu ... Recipient ok
C: DATA
S: 354 Enter mail, end with "." on a line by itself
C: Do you like ketchup?
C:   How about pickles?
C: .
S: 250 Message accepted for delivery
C: QUIT
S: 221 hamburger.edu closing connection
```

Plain text, line oriented, with three-digit reply codes in the same style as [[HTTP]]. The message body is terminated by **a line containing only a period**.

## Sending Mail By Hand

> ```
> telnet servername 25
> HELO/EHLO "your own domain name"
> MAIL FROM: <your own email address>
> RCPT TO: <recipient address>
> DATA
> QUIT
> ```

## What the Exercise Actually Demonstrates

> **SMTP authenticates nothing, derived.** Read the transcript again and ask what the server verified. `HELO crepes.fr` is a domain the client typed. `MAIL FROM: <alice@crepes.fr>` is an address the client typed. The server's reply — *"Sender ok"* — means the address is **well-formed**, not that it belongs to whoever is connected. Nothing in the exchange proves the sender is Alice, or is at `crepes.fr`, or exists.
>
> So the telnet exercise is not only a protocol demo: **it is a demonstration that anyone who can open a TCP connection to port 25 can claim to be anyone.** That is email spoofing, and it is a property of the protocol as designed, not a defect in any implementation. It is the clearest instance in the course of a failure of [[CIA Triad|origin integrity]] — the content may arrive intact (data integrity) while the claimed source is fiction.
>
> Everything layered on afterwards — SPF, DKIM, DMARC, and the [[Digital Signatures|signatures]] of S/MIME and PGP — exists to retrofit the authentication this transcript shows is absent. It is also why [[Security Threat Landscape|phishing]] is a protocol-level problem and not only a user-education one, and why bulk email worked as a propagation vector for [[Notable Worms|Nimda, MyDoom and the Storm worm]].

## Why Telnet Appears Three Times in This Lecture

The deck poses a multiple-choice question — *telnet can be used to:* **A.** remotely access terminals, **B.** remotely access services, **C.** send an email, **D.** fetch a web page — and then spends the following slides doing **D** (see [[HTTP]]) and **C** (above).

> **The answer the deck demonstrates is all four, derived.** Telnet's advertised purpose is A, but what it actually provides is a raw TCP connection to an arbitrary port with a terminal attached. Since SMTP and HTTP are both plain-text line-oriented protocols, that is sufficient to speak either by hand. The pedagogical point is that **application protocols are not opaque** — and the security point is that a protocol you can drive from a terminal is one an attacker can drive from a script.

## See Also

- [[HTTP]]
- [[FTP]]
- [[TCP]]
- [[Computer Networking]]
- [[CIA Triad]]
- [[Digital Signatures]]
- [[Security Threat Landscape]]
- [[Notable Worms]]
- [[CSCE 465]]
