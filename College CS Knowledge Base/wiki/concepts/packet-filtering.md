---
title: "Packet Filtering"
type: concept
tags: [csce465, security, network-security, firewall, packet-filter, acl, stateless]
sources: [csce465-lecture-13-firewall]
course: CSCE 465
updated: 2026-11-16
---

**Packet filtering** is the simplest kind of [[Firewalls|firewall]]: look at one packet, compare its header to a list of rules, pass it or drop it, and forget it. [[CSCE 465]] gives it three defining lines:

> - Decisions made on a **per-packet basis**
> - **No state information saved**
> - Typical configuration
>   - **Ports > 1024 left open**
>   - If dynamic protocols are in use, *entire ranges of ports must be allowed* for the protocol to work

The lecture's figure draws the filter inside a **router**, at the network layer. The application and transport layers appear only on the two end hosts; the filter is not a party to the conversation and sees each packet once, in isolation.

## Access Control Lists

The rules are an **access control list**. The format the lecture gives:

```
access-list <rule number> <permit|deny> <protocol>
            <SOURCE host with IP address | any | IP address and mask> [<gt|eq port number>]
            <DEST host with IP address   | any | IP address and mask> [<gt|eq port number>]
```

So a rule can test five things — **protocol, source address, source port, destination address, destination port** — plus the direction it is applied in. That is the entire vocabulary. The protocol is the one-byte field in the [[Internet Protocol|IP header]]; the ports come from the [[TCP]] or UDP header behind it.

## Worked Example: FTP

> The following allows a user to FTP (not passive FTP) from any IP address to the FTP server (172.168.10.12):

```
access-list 100 permit tcp any gt 1023 host 172.168.10.12 eq 21
access-list 100 permit tcp any gt 1023 host 172.168.10.12 eq 20
! Allows packets from any client to the FTP control and data ports

access-list 101 permit tcp host 172.168.10.12 eq 21 any gt 1023
access-list 101 permit tcp host 172.168.10.12 eq 20 any gt 1023
! Allows the FTP server to send packets back to any IP address with TCP ports > 1023

interface Ethernet 0
 access-list 100 in     ! Apply the first rule to inbound traffic
 access-list 101 out    ! Apply the second rule to outbound traffic
```

Line by line:

| Rule | Reads as |
|---|---|
| 100, line 1 | Inbound TCP from **any host, port above 1023**, to the server's port **21** (command) |
| 100, line 2 | The same, to the server's port **20** (data) |
| 101, line 1 | Outbound TCP from the server's port 21 to **any host, port above 1023** |
| 101, line 2 | Outbound TCP from the server's port 20 to **any host, port above 1023** |

[[FTP]] explains why there are two ports and why the server ends up opening a connection of its own.

> **What the four lines cannot say, derived.** In active FTP the client announces, inside the command channel, which of its ports the server should connect back to. A packet filter never reads that — it sees headers, not the conversation. So the last rule cannot say *"to the port that client just named"*; it has to say *"to any port above 1023 on any host, at any time"*, whether or not an FTP session exists. And line 2 of list 100 admits a packet to port 20 from anyone, with no way to tell a reply from an unsolicited probe.
>
> That is the slide's *entire ranges of ports must be allowed*, and it is the comparison table's verdict on this type: **no dynamic [protocols] without holes**. The same weakness cuts the other way when the filter protects clients instead of a server. To let inside users run active FTP, it must admit inbound connections from any outside host whose **source port is 20** — and the source port is a number the sender chooses.

The slide writes `access-list 100 in` to attach a list to an interface. That is schematic; the point is that each list is bound to **one direction** on one interface.

## Where It Stands

From the lecture's [[Firewalls|comparison]]: **worst security (3) and best performance (1)**. It needs no change to client applications, it passes ICMP, and it does **not** protect against fragmentation.

> **Why those go together, derived.** It is fast for the reason it is weak: a handful of header comparisons per packet, no memory, no parsing. The fragmentation entry follows from the same per-packet view. The ports a rule tests live in the TCP or UDP header, which is only in the *first* fragment of a fragmented datagram; the later fragments carry no ports for a rule to match.
>
> The typical configuration — high ports open — is a blacklist in spirit, which is the losing side of the firewall example on [[Security Design Principles]] (*deny port 23, allow port \**). [[Session Filtering]] inverts it.

## The Same Idea Elsewhere

*Router filtering* against [[IP Spoofing]] in Lecture 12 is packet filtering with one rule: does this source address belong on this side of the network? And the word *ACL* is the same one [[Access Control Models]] uses for files — a list of entries naming who may do what, checked on every access.

## See Also

- [[Firewalls]]
- [[Session Filtering]]
- [[Proxy Firewalls]]
- [[FTP]]
- [[Internet Protocol]]
- [[TCP]]
- [[IP Spoofing]]
- [[Access Control Models]]
- [[Security Design Principles]]
- [[CSCE 465]]
