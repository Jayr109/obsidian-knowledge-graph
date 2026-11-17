---
title: "Network Address Translation"
type: concept
tags: [csce465, security, network-security, nat, firewall, ip-addresses]
sources: [csce465-lecture-13-firewall]
course: CSCE 465
updated: 2026-11-16
---

**Network Address Translation (NAT)** rewrites the addresses in packets as they cross a boundary, so that hosts inside a network can use addresses the outside never sees. It is the fourth and last item on the [[CSCE 465]] [[Firewalls|firewall]] lecture's roadmap, and one of the conveniences the lecture lists under what firewalls can do.

## Why Use It

> - Useful if organization **does not have enough real IP addresses**
> - **Extra security measure** if internal hosts do not have valid IP addresses (harder to trick firewall)
> - Only really need real IP addresses for **services outside networks will originate connections to**

The lecture's figure is a single translating device with an address on each side:

```
  ( Internet server )
          ^
          |
          v
   external IP address                      internal IP address
       172.19.19.5      [ NAT device ]          10.1.1.5       <------->   L A N
```

## Mappings

> - **Many-to-1** (n-to-m) mapping
> - **1-to-1** (n-to-n) mapping
> - **Proxies provide many-to-1**
> - NAT **not required** on filtering firewalls

| Mapping | Meaning |
|---|---|
| **1-to-1** | Each inside host has its own outside address; only the address is rewritten |
| **Many-to-1** | Many inside hosts share one outside address (or a small pool, the *n-to-m* in the parenthesis) |

## What It Does for Security

> **Reading the three bullets, derived.** The first is the original purpose: address shortage. The second is a side effect. An inside host with no valid outside address **cannot be named** by an outsider, so an unsolicited inbound packet has nowhere to go unless a mapping already exists. That is why it is *harder to trick the firewall*: an attacker cannot aim at a host it cannot address.
>
> The third bullet is the design rule that follows. The only machines that need real addresses are the ones outsiders are meant to **start** connections to — the public servers, which is the population of the DMZ in the first figure of [[Firewalls]]. Everything else can sit behind the translation.
>
> **Why a many-to-1 NAT looks like a stateful firewall.** If many hosts share one address, the device has to remember which inside host each outbound connection belongs to in order to deliver the replies. That is a per-connection table, the same structure as the state table in [[Session Filtering]], with the same limits. It also explains the last two slide bullets. A [[Proxy Firewalls|proxy]] gets many-to-1 for nothing, since every outbound connection is opened by the proxy itself. A filtering firewall passes the original packets through and has no need to rewrite them, so NAT is an optional extra there.

NAT is a side effect being used as protection, not a policy. It hides inside hosts from *unsolicited* inbound traffic and does nothing about a connection an inside host opens to a hostile server.

## Where the Course Uses It

The [[CSCE 465|lab safety rules]] for every homework require the VM's network to be **NAT only, never bridged**. That is this property used as a safety control: the lab VM can reach out, and nothing on the campus network can address it.

## See Also

- [[Firewalls]]
- [[Session Filtering]]
- [[Proxy Firewalls]]
- [[Packet Filtering]]
- [[Internet Protocol]]
- [[Computer Networking]]
- [[CSCE 465]]
