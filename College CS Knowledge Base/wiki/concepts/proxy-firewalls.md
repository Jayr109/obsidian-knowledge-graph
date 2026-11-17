---
title: "Proxy Firewalls"
type: concept
tags: [csce465, security, network-security, firewall, proxy, application-gateway, circuit-level-gateway, socks]
sources: [csce465-lecture-13-firewall]
course: CSCE 465
updated: 2026-11-16
---

A **proxy firewall** does not pass packets; it **relays connections**. [[CSCE 465]] puts it in three lines:

> - Relay for connections
> - **Client ↔ Proxy ↔ Server**
> - Two flavors: **application level** and **circuit level**

Where a [[Packet Filtering|filtering firewall]] inspects traffic on its way through, a proxy ends the client's connection at itself and opens a second one to the server. The client and server never exchange a packet directly.

## Application Gateways

The application-level flavor is a proxy that speaks one specific protocol.

> - **Understands specific applications**
>   - Limited proxies available
>   - Proxy **'impersonates' both sides** of connection
> - **Resource intensive** — process per connection
> - HTTP proxies may cache web pages

> - More appropriate to **TCP**
> - ICMP difficult
> - **Block all unless specifically allowed**
> - Must write a **new proxy application** to support new protocols — *Not trivial!*

> - Clients configured for proxy communication
> - **Transparent proxies**

The figure shows the gateway with a full protocol stack and three separate proxies at its application layer: **Telnet, FTP, HTTP**. A connection comes up through the gateway's stack, is handled by the proxy for that protocol, and goes back down the other side as a new connection.

> **Why this is the most secure and the slowest, derived.** To the client the proxy *is* the server, and to the server it *is* the client. So it can apply policy to the protocol itself — which commands, which URLs, which users — and not just to addresses and ports. That is what earns it the **1** for security in the [[Firewalls|comparison table]]. It pays for it three ways, all on the slides: a process per connection (the **4** for performance), a separate program per protocol (*typically < 20* services), and clients that have to know the proxy is there unless it is transparent.
>
> The default is the secure one. *Block all unless specifically allowed* is not a configuration choice here; a protocol with no proxy written for it simply cannot cross.

## Circuit-Level Gateways

The circuit-level flavor relays connections without understanding what is inside them.

> - **Support more services** than application-level gateway — **less control over data**
> - **Hard to handle protocols like FTP**
> - Clients must be aware they are using a circuit-level proxy
> - **Protect against fragmentation problem**

> - Operate at **user level in OS**
> - Have circuit program **'route' packets between interfaces** instead of OS routing code

```
  outside host  <--- outside connection --->  [ circuit-level gateway ]  <--- inside connection --->  inside host
                                                 out <-------> in
```

> **The trade against the application gateway, derived.** A circuit-level gateway copies bytes from one connection to the other and does not parse them. One program therefore serves any TCP service (*support more services*), and for the same reason it cannot object to anything in the data (*less control*). [[FTP]] is hard for it because the port for FTP's second connection is announced *inside* the first one, in data this gateway does not read.
>
> **Why it protects against fragmentation.** Nothing from the outside packet reaches the inside host. The gateway's own TCP stack reassembles what arrives and the inside connection is built from fresh, well-formed packets. Odd fragments, overlapping fragments and strange header options die at the gateway. That is the property a [[Packet Filtering|packet filter]] lacks, and it is also why the ambiguities behind [[Insertion and Evasion Attacks]] do not survive a proxy.

## Example: SOCKS

> - Circuit level gateway
> - Support TCP
> - **SOCKS v5 supports UDP**, earlier versions did not
> - See `http://www.socks.nec.com`

*SOCKS-ify* is the comparison table's verb for what has to be done to a client application so that it talks to the gateway.

## Why TCP Proxies Well and UDP and ICMP Do Not

> **Why isn't UDP or ICMP proxied as much as TCP?**
> - TCP's **connection-oriented** nature easier to proxy
> - UDP & ICMP harder (but not impossible) since **each packet is a separate transaction**
> - Session filters determine which packets appear to be replies

A proxy relays *connections*, and [[TCP]] is the protocol that has them. This is the reason for the comparison table's ICMP column: **No** for application gateways, **(SOCKS v5)** for circuit gateways.

## The Two Flavors Compared

| | Application gateway | Circuit-level gateway |
|---|---|---|
| Understands the application protocol | **Yes** | No |
| Control over data | Full | Less |
| Services supported | Typically < 20; a new proxy per protocol | More |
| Security / performance (lower is better) | 1 / 4 | 2 / 3 |
| Client changes | Proxy-aware and configured, unless transparent | Typically SOCKS-ified |
| FTP | Has its own proxy | Hard |
| Fragmentation | Yes | Yes |

The deck adds one more property under NAT: **proxies provide many-to-1** address mapping. Every outbound connection originates from the proxy's own address, so [[Network Address Translation|address translation]] comes for free.

## See Also

- [[Firewalls]]
- [[Packet Filtering]]
- [[Session Filtering]]
- [[FTP]]
- [[Network Address Translation]]
- [[HTTP]]
- [[TCP]]
- [[Insertion and Evasion Attacks]]
- [[CSCE 465]]
