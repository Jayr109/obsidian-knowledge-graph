---
title: "Session Filtering"
type: concept
tags: [csce465, security, network-security, firewall, stateful-inspection, session-filter, state-table]
sources: [csce465-lecture-13-firewall]
course: CSCE 465
updated: 2026-11-16
---

**Session filtering** is the second kind of filtering [[Firewalls|firewall]] in [[CSCE 465]]: it judges each packet **in the context of the connection it belongs to**. The lecture lists three other names for the same thing — **Dynamic Packet Filtering**, **Stateful Inspection**, and **Context Based Access Control** — and *stateful firewall* is the usual one outside the course. It is [[Packet Filtering]] with a memory.

## How It Decides

> - Packet decision made **in the context of a connection**
> - If packet is a **new connection**, check against security policy
> - If packet is part of an **existing connection**, match it up in the **state table** & update table
> - Typical configuration
>   - **All denied unless specifically allowed**
>   - Dynamic protocols (FTP, RealAudio, etc.) allowed **only if supported**

So the rule base is consulted once per connection, not once per packet. Everything after the first packet is a table lookup.

## The State Table

The second slide is the vendor's pitch, three verbs in bold:

> - **Screens** ALL attempts, **Protects** All applications
> - **Extracts** & **maintains** 'state' information
> - **Makes** an intelligent **security** / **traffic** decision

In its figure the inspection point sits low in the firewall's stack, between the data link and network layers, with arrows reaching up through transport and application and out to a box labelled **Dynamic State Tables**. The filter intercepts packets where a packet filter would, and unlike one it reads as far up the packet as it needs to.

## Worked Example: FTP

The packet filter needed four ACL lines and a permanent hole to allow [[FTP]]. The session filter's slide is a screenshot of a rule base with two rows:

| No. | Source | Destination | Service | Action |
|---|---|---|---|---|
| 1 | Local_Net | Any | ftp | **accept** |
| 2 | Any | Any | Any | **drop** |

> **Why two rows are enough, derived.** Rule 1 names a *service*, not a pair of port ranges. The filter knows what FTP is: it watches the command channel, sees the `PORT` or `PASV` exchange, and adds the negotiated data connection to the state table for as long as that session lasts. Nothing else is opened. This is what *"allowed only if supported"* means — the convenience depends on the firewall containing a parser for each dynamic protocol, which is the comparison table's *dependent on vendor for dynamic support*.
>
> Rule 2 is the default. It is written out here, and it is the typical configuration from the first slide: **all denied unless specifically allowed**.

The screenshot is image-only. Its tab labels read *Security Policy - ftp*, *Address Translation - ftp*, *Bandwidth Policy - VPN* and *Compression Policy - VPN*.

## Against the Packet Filter

| | [[Packet Filtering\|Packet filter]] | Session filter |
|---|---|---|
| Unit of decision | Each packet alone | A packet in the context of its connection |
| Memory | None | State table, updated per packet |
| Typical default | Ports > 1024 left open | All denied unless specifically allowed |
| Dynamic protocols | Entire port ranges must be allowed | Allowed only if supported |
| Security / performance (lower is better) | 3 / 1 | 2 / 2 |
| Fragmentation | No | Maybe |

Neither needs any change to client applications, and both pass ICMP.

> **The default is the real difference, derived.** A packet filter that cannot tell a reply from a probe has to leave the high ports open, so it is permissive by construction. A filter that can recognise replies does not need the hole and can afford to deny everything else. That is [[Security Design Principles|fail-safe defaults]] — the whitelist from Lecture 2's own firewall example — made practical by state.

## UDP and ICMP

A later slide asks why UDP and ICMP are not proxied as much as TCP, and ends:

> **Session filters determine which packets appear to be replies.**

TCP announces its connections with a handshake. UDP and ICMP have none, so *each packet is a separate transaction* and the filter has to infer a session: an outbound request, then an inbound packet from the same host that looks like its answer within a short time.

## What State Costs

> **Derived.** The state table is a finite resource that outsiders can fill. A [[SYN Flooding|SYN flood]] aimed through the firewall creates a half-open entry in the firewall's table as well as the server's, so the device inherits the weakness of the host it protects. And each protocol parser is code reading attacker-supplied data, with the same ambiguity problems as a network IDS trying to reconstruct what a host will see; see [[Insertion and Evasion Attacks]].

## See Also

- [[Firewalls]]
- [[Packet Filtering]]
- [[Proxy Firewalls]]
- [[FTP]]
- [[TCP]]
- [[SYN Flooding]]
- [[Security Design Principles]]
- [[Network Address Translation]]
- [[CSCE 465]]
