---
title: "ICMP Redirect Attack"
type: concept
tags: [csce465, security, network-security, icmp, redirect, man-in-the-middle, routing]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

An **ICMP redirect** is a legitimate [[ICMP]] message (type 5) by which a gateway tells a host that a better first hop exists for some destination. The **ICMP redirect attack** is forging one. [[CSCE 465]] sums up the protocol's side of the conversation in two lines:

> "Really, you should send your packets to that gateway first, it will be faster"
>
> "Uh, OK, I'll send them there then if you say so"

The host obeys because nothing in the message proves who sent it.

## The Message

```
+---------------+---------------+-------------------------------+
| Type (1 byte) | Code (1 byte) |      Checksum (2 bytes)       |
+---------------+---------------+-------------------------------+
|              Gateway Internet Address (4 bytes)               |
+---------------------------------------------------------------+
|       Internet Header and 8 bytes of Original Datagram        |
+---------------------------------------------------------------+
```

**Type 5.** The *Gateway Internet Address* is the router the host is being told to use from now on.

## The Attack

> The attacker can forge ICMP redirect packet in order to **redirect traffic to himself**.

The lecture's figure is a LAN containing a host **H**, its real gateway **G1** and an attacker **AT**, with the target **T** outside:

```
                              T   (outside the LAN)
                              ^
   +--------------------------|---------------------+
   |  LAN                     |                     |
   |           G1 <-----------+------------ AT      |
   |            :                           ^       |
   |            :  forged "ICMP redirect    |       |
   |            :   to AT"                  |       |
   |            v                           |       |
   |            H --------------------------+       |
   +------------------------------------------------+

   before:   H -> G1 -> T
   after:    H -> AT -> G1 -> T
```

The forged redirect reaches H looking as if it came from G1 and names AT as the better gateway. H updates its route, and its traffic for T now passes through the attacker.

> Typically used as a scam to perpetrate **man-in-the-middle attack or DoS**.

> **Which of the two it becomes, derived.** It depends on what AT does with the packets. Forward them on to G1 and nothing looks broken, so AT reads or alters everything in transit: man-in-the-middle. Drop them and H simply loses its route to T: denial of service.

## Similar Ideologically to ARP Poisoning

That phrase is the lecture's. Side by side:

| | [[ARP Poisoning]] | ICMP redirect attack |
|---|---|---|
| Forged message | ARP reply | ICMP redirect (type 5) |
| Table corrupted | The host's **ARP cache** (IP → MAC) | The host's **route** to a destination |
| Layer | Data link | Network |
| The lie | "That IP address is at my MAC" | "Send packets for that destination through me" |
| Result | Frames for the victim's peer go to the attacker | Packets for the destination go via the attacker |

Both work for the same reason: a host changes where it sends traffic on the strength of an unauthenticated message from the local network.

## Countermeasures

> - **YES** — Disable the ICMP REDIRECT
> - **NO** — Linux has the "secure redirect" options but it seems to be ineffective against this attack

> **What the YES costs, derived.** Almost nothing. A host with one gateway has no better first hop to be told about, so ignoring redirects loses no function. That makes this the rare case in the lecture where the fix is to switch the feature off — compare [[ARP Poisoning]], where *no universal defense* exists because hosts cannot stop using ARP.

## See Also

- [[ICMP]]
- [[ARP Poisoning]]
- [[Smurf Attack]]
- [[IP Spoofing]]
- [[Internet Protocol]]
- [[Security Attack Taxonomy]]
- [[Vulnerability Analysis]]
- [[CSCE 465]]
