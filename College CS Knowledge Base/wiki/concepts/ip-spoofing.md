---
title: "IP Spoofing"
type: concept
tags: [csce465, security, network-security, ip, spoofing, ingress-filtering, tcp-ip]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

**IP spoofing** is sending a datagram whose source address is not your own. [[CSCE 465]] puts it first among the TCP/IP vulnerability examples for a reason it states in two lines:

> - **A common first step to many threats**
> - **Source IP address cannot be trusted!**

Nothing about it is clever. The [[Internet Protocol|IP header]] has a 32-bit source field, the sender fills it in, and nobody checks. The lecture's example header reads `SRC: 18.31.10.8, DST: 128.194.7.237`, over the question *"Is it really from MIT?"*

## Why It Is Possible

> **Current IPv4 infrastructure: no authentication for the source.**

**The mail analogy.** The slide draws an envelope — *From: Guofei Gu, TAMU. To: William Smith, M.I.B. Corp.* — and notes that the return address is whatever the sender wrote. Then the caveat:

> US mail maybe better in the sense that there is a **stamp** put on the envelope at the **location** (e.g., town) of collection...

A postmark records where the letter actually entered the system. IP has no postmark.

**Most routers only care about the destination address.** The lecture's figure has three networks and one header:

```
  Columbia  128.59.10.xx  --[Rtr]--\
                             |      \
                             |       [Rtr]-- TAMU  128.194.xx.xx
                             |      /
  Stanford  36.190.0.xx   --[Rtr]--/

  the same header on both paths:   src: 128.59.10.8   dst: 128.194.7.237
```

A packet claiming to be from Columbia is delivered to TAMU whether it left Columbia or Stanford. Forwarding reads the destination field; the source field is cargo.

## Why Should I Care?

> - Attack packets with spoofed IP address help **hide the attacking source**.
> - A **smurf attack** launched with your host IP address could bring your host and network to their knees.
> - Higher protocol layers (e.g., TCP) help to protect applications from direct harm, **but not enough**.

Those are three different uses, and they map onto the rest of the lecture:

| Use of the forged source | Attack |
|---|---|
| Hide where the packets come from | [[SYN Flooding]] |
| Make someone else receive the replies | [[Smurf Attack]] and its DNS variant |
| Be mistaken for a trusted host | [[TCP Session Hijacking]], [[TCP Reset Attack]] |

## Defense 1: Router Filtering

> Decide whether this packet, with certain source IP address, **should come from this side of network.** — Local policy.

In the figure the Stanford router looks at a packet with source `128.59.10.8` leaving the `36.190.0.xx` network and says *"Hey, you shouldn't be here!"*

> - **Very effective for some networks (ISP should always do that!)** — at least be sure that this packet is from some particular subnet
> - Problems:
>   - Hard to handle frequent add/delete hosts/subnets or mobileIP
>   - Upsets customers should legitimate packets get discarded
>   - **Need to trust other routers**

> **Why the last problem is the real one, derived.** The network that can do this filtering is the *attacker's* network, and the network that benefits is the victim's. The filter costs its operator effort and the occasional angry customer, and protects somebody else. So it only works if nearly everyone does it, which is what *need to trust other routers* means. A router can check its own customers' addresses; it cannot check a packet that has already crossed three other networks. The usual name for this, which the slide does not use, is ingress filtering.

## Defense 2: The TCP Handshake

The lecture reuses the three-network figure with the attacker at Stanford. The forged SYN reaches TAMU, and TAMU's reply, `seq=y, ACK x+1`, goes to the address in the source field — Columbia. The attacker never sees `y`.

> The handshake prevents the attacker from establishing a TCP connection pretending to be 128.59.10.8.

> - **Very effective** for stopping most such attacks
> - Problems:
>   - The attacker can succeed if **"y" can be predicted**
>   - Other DoS attacks are still possible (e.g., **TCP SYN-flood**)

So the handshake turns spoofing from *free* into *blind*: the attacker can still send, and cannot receive. Both stated problems are attacks that need no reply — [[TCP Session Hijacking|guessing `y`]] and [[SYN Flooding|never completing the handshake at all]].

## A Prediction Closed

[[Internet Protocol]] recorded on 2026-11-04, from the Lecture 10 routing slide alone, that a source address *"is never verified by anyone along the path"* and that this was *"the enabling condition for the reflection and amplification attacks the network security unit builds toward"*. Lecture 12 is that unit. The same absence was named a month earlier still, on [[User Authentication]], as the stated threat to address-based authentication: *no authentication of source addresses*.

## See Also

- [[Internet Protocol]]
- [[TCP]]
- [[SYN Flooding]]
- [[TCP Session Hijacking]]
- [[TCP Reset Attack]]
- [[Smurf Attack]]
- [[ARP Poisoning]]
- [[User Authentication]]
- [[Packet Filtering]]
- [[Vulnerability Analysis]]
- [[CSCE 465]]
