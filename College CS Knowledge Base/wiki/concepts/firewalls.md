---
title: "Firewalls"
type: concept
tags: [csce465, security, network-security, firewall, access-control, dmz, vpn]
sources: [csce465-lecture-13-firewall]
course: CSCE 465
updated: 2026-11-16
---

A **firewall**, in [[CSCE 465]]'s definition, is a

> **Device that provides secure connectivity between networks** (internal/external; varying levels of trust), used to **implement and enforce a security policy for communication between networks**.

The second half is the part to hold on to. A firewall is a [[Security Policy and Mechanism|mechanism]]; it enforces whatever policy its rules encode and nothing else. The lecture's roadmap is four items — basic concept, filtering firewall, proxy firewall, network address translation — and this page is the first of them plus the comparison that ties the rest together.

## The Picture

```
   Trusted networks                                     Untrusted networks & servers
   ( Intranet ) ------ [ Firewall ] ---- [ Router ] ---- ( Internet ) ---- untrusted users
                            |                                 |
                            |                                 +----------- trusted users
                         (  DMZ  )                                         (outside)
            publicly accessible servers & networks
```

Three zones at three levels of trust. The **DMZ** holds the servers outsiders are supposed to reach, so that reaching them does not mean reaching the intranet. Note the *trusted users* drawn out on the Internet side: trust and location are not the same thing, which is what the VPN slide at the end of the deck is for.

## A Moat, Not a Wall

> - From Webster's Dictionary: *a wall constructed to prevent the spread of fire*
> - Internet firewalls are **more the moat around a castle** than a building firewall
> - **Controlled access point**

A building firewall is passive and stops everything. A moat stops nothing by itself; it forces all traffic over one bridge where it can be inspected. That is the function — a single choke point.

## What Firewalls Can and Cannot Do

| Firewalls can | Firewalls cannot protect… |
|---|---|
| **Restrict incoming and outgoing traffic** by IP address, ports, or users | **Traffic that does not cross it** — routing around it, and internal traffic |
| **Block invalid packets** | …**when misconfigured** |
| Convenient extras: insight into the traffic mix via **logging**; **Network Address Translation**; **encryption** | |

> **Both limits are structural, derived.** A choke point only sees what goes through it, so an insider, a second link that bypasses the firewall, or an attack between two inside hosts never meets a rule. And *misconfigured* is not a footnote: a firewall is exactly as good as its rule set, which nobody can see from outside. [[Computer Security]] already records this as the usual failure of mechanism without assurance — *the system has a firewall, and no one has checked what it enforces.*

The lecture states the requirement the device is there to meet, under the heading **Access Control**:

> - Control access to network information and resources
> - Protect the network from attacks

## The Four Types

```
Firewall
├── Filtering firewall        "packets checked then passed"
│   ├── Packet filtering      Access Control Lists
│   └── Session filtering     Dynamic Packet Filtering / Stateful Inspection /
│                             Context Based Access Control
└── Proxy firewall            "relay for connections"
    ├── Application level     application gateways
    └── Circuit level         e.g. SOCKS
```

A filter looks at traffic and lets it through or not; a proxy ends the connection and starts another one. For a filter, *inbound and outbound affect when policy is checked* — a rule is attached to a direction on an interface. Each type has its own page: [[Packet Filtering]], [[Session Filtering]], [[Proxy Firewalls]].

## The Comparison

The deck compares the four across three slides. Merged into one table:

| | Packet filter | Session filter | Circuit GW | App. GW |
|---|---|---|---|---|
| **Security** | 3 | 2 | 2 | **1** |
| **Performance** | **1** | 2 | 3 | 4 |
| **Service support** | No dynamic w/o holes | Dependent on vendor for dynamic support | Dependent on vendor for dynamic support | Typically < 20 |
| **Modify client applications?** | No | No | Typical, SOCKS-ify client applications | Unless transparent, client application must be proxy-aware & configured |
| **ICMP** | Yes | Yes | (SOCKS v5) | No |
| **Fragmentation** | No | Maybe | Yes | Yes |

> *Lower is better for security & performance.*

Two notes on reading it. *Dependent on vendor for dynamic support* is one merged cell on the slide, spanning the session filter and circuit gateway rows. And the last two columns have no caption; read with the proxy slides (*ICMP difficult* for application gateways; circuit-level gateways *protect against fragmentation problem*), **ICMP** is whether the type can carry ICMP traffic at all and **Fragmentation** is whether it protects against fragmentation tricks. That reading is inferred.

> **The table is one trade-off, derived.** Security runs 3, 2, 2, 1 and performance runs 1, 2, 3, 4 — nearly mirror images. The more of each packet a firewall understands, the more it can enforce and the more it costs: a packet filter reads a few header fields and is fast; an application gateway understands the whole protocol and needs a process per connection and a separate proxy per protocol, hence *typically < 20* services. Nothing in the table is best at everything, which is the same shape as the centralized/distributed table on [[Botnets]].
>
> The *dynamic* in the service-support row means protocols that negotiate a port at run time. [[FTP]] is the lecture's example, and each type's answer to it is the clearest way to tell the four apart.

## Extras: NAT and VPN

[[Network Address Translation]] has its own page. The deck's last slide is the other convenience from the "can" list:

> **Encryption (VPNs)**
> - Allows **trusted users to access sensitive information while traversing untrusted networks**
> - Useful for remote users/sites
> - IPSec

That is the answer to the trusted users drawn outside the perimeter in the first figure.

## Firewall Versus IDS

The next lecture sets the two side by side: a firewall is **active filtering** and **fail-close**; a network IDS is **passive monitoring** and **fail-open**. See [[Network Intrusion Detection]]. They are the *prevent* and *detect* layers of the same [[Intrusion Detection Systems|layered defence]].

## See Also

- [[Packet Filtering]]
- [[Session Filtering]]
- [[Proxy Firewalls]]
- [[FTP]]
- [[Network Address Translation]]
- [[Network Intrusion Detection]]
- [[Intrusion Detection Systems]]
- [[Security Policy and Mechanism]]
- [[Security Design Principles]]
- [[Computer Security]]
- [[Access Control Models]]
- [[Vulnerability Analysis]]
- [[CSCE 465]]
