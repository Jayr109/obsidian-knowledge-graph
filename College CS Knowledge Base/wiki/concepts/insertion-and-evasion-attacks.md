---
title: "Insertion and Evasion Attacks"
type: concept
tags: [csce465, security, network-security, intrusion-detection, nids, evasion, insertion, fragmentation]
sources: [csce465-lecture-14-intrusion-detection-system]
course: CSCE 465
updated: 2026-11-16
---

**Insertion** and **evasion** are the two ways to get an attack past a [[Network Intrusion Detection|network IDS]] without the IDS seeing it for what it is. Both rest on one sentence from [[CSCE 465]]:

> **What the IDS sees may not be what the end system gets.**

A network IDS is not the destination of the traffic. It watches packets go by and has to work out what the host that finally receives them will reconstruct. If the attacker can make those two reconstructions differ, the IDS is matching signatures against a byte stream the target never sees.

## The Problem

> - Insertion and evasion attacks.
>   - IDS needs to perform **full reassembly** of packets.
> - But there are still **ambiguities in protocols and operating systems**:
>   - E.g. **TTL, fragments**.
>   - Need to **"normalize"** the packets.

Both of the lecture's figures use the same setup. The attacker wants the end system to receive the string `ATTACK`, sends it as single-letter packets **out of order**, and the IDS has a signature for `ATTACK`.

## Insertion Attack

```
attacker's data stream (as sent):    T  X  T  C  A  A  K

IDS sees:                            A  T  X  T  A  C  K      "ATXTACK"
end system sees:                     A  T  T  A  C  K         "ATTACK"
```

> **Examples: bad checksum, TTL.**

The attacker adds a packet — the `X` — that the **IDS accepts and the end system does not**. The IDS reassembles a stream with an extra letter in the middle and its signature for `ATTACK` no longer matches. The end system never had the `X` and assembles the attack intact.

> **How the two examples work, derived.** The slide names them and does not explain them. *Bad checksum:* the `X` packet carries an invalid checksum. A host discards it on arrival; an IDS that does not verify checksums on every packet keeps it. *TTL:* the `X` packet is given a time-to-live large enough to pass the IDS and too small to reach the host, so it expires at a router in between. This is the mechanism of traceroute on [[ICMP]] — choosing a TTL so that a packet dies at a known hop — used to make a packet exist for one observer and not the other.

## Evasion Attack

```
attacker's data stream (as sent):    T  T  C  A  A  K

IDS sees:                            A  T  T  C  K            "ATTCK"
end system sees:                     A  T  T  A  C  K         "ATTACK"
```

> **Example: fragmentation overlap.**

The reverse case: a packet the **end system accepts and the IDS does not**. The IDS's stream is missing a letter, and again nothing matches.

> **How the example works, derived.** [[Internet Protocol|IP]] lets a datagram be split into fragments, each labelled with an offset. If two fragments claim the same bytes with different contents, the standard does not say which wins, and operating systems resolve it differently — some keep the first copy, some the last. An IDS that resolves the overlap one way, watching a host that resolves it the other way, ends up with different data from the host.

## Side by Side

| | Insertion | Evasion |
|---|---|---|
| The disagreement | IDS **accepts** a packet the end system rejects or never receives | IDS **misses** a packet the end system accepts |
| IDS's stream in the figure | `ATXTACK` — one letter too many | `ATTCK` — one letter too few |
| End system's stream | `ATTACK` | `ATTACK` |
| Lecture's examples | Bad checksum, TTL | Fragmentation overlap |

## Why It Cannot Be Fully Fixed

The first slide gives the fix and the reason it is not enough in consecutive lines: *full reassembly* is necessary, *but there are still ambiguities in protocols and operating systems*.

> **Where the ambiguity comes from, derived.** It is the same fact [[OS Fingerprinting]] depends on, two lectures earlier: *each OS implements their TCP stack differently.* There the differences identified the host. Here they mean a passive monitor cannot know what a given host will do with an overlapping fragment or a borderline packet unless it knows that host's operating system, and cannot know whether a packet will survive the hops to the host unless it knows the topology. One property of TCP/IP stacks, used once for reconnaissance and once for evasion.
>
> **What "normalize" means.** If the monitor cannot predict the host's interpretation, remove the choice: put something in the path that rewrites traffic into one unambiguous form before either sees it. That works, and it changes what the IDS is. A normalizer is in line and active, which is a [[Firewalls|firewall's]] position, not a passive monitor's. It is also what a [[Proxy Firewalls|proxy firewall]] does without trying — it terminates the connection and builds a clean one — which is why the firewall lecture credits circuit-level gateways with protecting against *the fragmentation problem*.

This is the *"resilience to attacks upon the IDS itself!"* on the lecture's requirements list, made concrete. These attacks do not exploit a bug in the target. They exploit the monitor's distance from it, and a [[Host-Based Intrusion Detection|host-based IDS]], which watches the real execution, is not exposed to them.

## Where the Framework Comes From

The insertion/evasion terminology and the letter-box figures follow Ptacek and Newsham's 1998 report *Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection*. The slides do not cite it; the attribution is recorded here, not taken from the deck.

## See Also

- [[Network Intrusion Detection]]
- [[Intrusion Detection Systems]]
- [[Host-Based Intrusion Detection]]
- [[OS Fingerprinting]]
- [[Internet Protocol]]
- [[ICMP]]
- [[Proxy Firewalls]]
- [[Firewalls]]
- [[Misuse and Anomaly Detection]]
- [[CSCE 465]]
