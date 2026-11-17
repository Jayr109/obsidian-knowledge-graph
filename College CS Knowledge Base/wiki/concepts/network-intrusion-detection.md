---
title: "Network Intrusion Detection"
type: concept
tags: [csce465, security, network-security, intrusion-detection, nids, snort, bro, monitoring]
sources: [csce465-lecture-14-intrusion-detection-system]
course: CSCE 465
updated: 2026-11-16
---

A **network intrusion detection system (NIDS)** watches traffic on the wire and looks for attacks in it. It is the second deployment of an [[Intrusion Detection Systems|IDS]] in [[CSCE 465]], beside [[Host-Based Intrusion Detection]], and the one the lecture spends longest on: what it does, how it is built, how it differs from a [[Firewalls|firewall]], what it must be able to survive, and how it is fooled.

## What a NIDS Does

> - **Deploying sensors at strategic locations**
>   - E.g., packet sniffing via `tcpdump` at routers
> - **Inspecting network traffic**
>   - Watch for violations of protocols and unusual connection patterns
> - **Monitoring user activities**
>   - Look into the data portions of the packets for malicious command sequences
> - **May be easily defeated by encryption**
>   - Data portions and some header information can be encrypted
> - Other problems …

The slide carries the Snort logo. The first three bullets go progressively deeper into the packet: where to listen, then headers and connection patterns, then payloads.

> **The sniffer changes sides, derived.** `tcpdump` on a tapped link is exactly the equipment Lecture 2 presented as an *attack* on confidentiality ([[Security Attack Taxonomy]]). A NIDS is authorised interception. And the encryption bullet is the mirror image of that lecture's sharpest point: encryption hides payloads and leaves metadata, so a NIDS facing encrypted traffic is reduced to what a traffic analyst has — who is talking to whom, how often, and how much.

## Architecture

```
       Policy script                          Alerts/notifications
            |                                          ^
            v                                          |
    +----------------------------------------------------------+
    |                 Policy Script Interpreter                |
    +----------------------------------------------------------+
            |  Event control                           ^  Event stream
            v                                          |
    +----------------------------------------------------------+
    |                       Event Engine                       |
    +----------------------------------------------------------+
            |  tcpdump filters                         ^  Filtered packet stream
            v                                          |
    +----------------------------------------------------------+
    |                         libpcap                          |
    +----------------------------------------------------------+
                                                       ^  Packet stream
    +----------------------------------------------------------+
    |                         Network                          |
    +----------------------------------------------------------+
```

Data flows **up** the right-hand side and gets smaller and more meaningful at each layer: every packet, then only the packets a filter selects, then *events*, then alerts. Control flows **down** the left: the policy decides which events it cares about, and the event engine decides which packets it needs.

> **What the layering buys, derived.** The cheapest test runs on the most data. A capture filter discards most packets with a few comparisons; only what survives is parsed into events, and only events reach the expensive, site-specific policy code. That is how the first requirement below is met at all.
>
> The top two boxes are also the fourth requirement, **mechanism separate from policy**, built as architecture. The event engine knows protocols and holds no opinion about what is bad; the policy scripts hold the opinions and know nothing about packets. It is the [[Security Policy and Mechanism|policy/mechanism split]] from Lecture 2, here as two layers of one program.

The slide does not name the system. The layering, and the requirements list that follows, are those of **Bro**, which the lecture named earlier as a signature-based example. That attribution is recorded here, not taken from the slide.

## Firewall Versus Network IDS

| | Firewall | Network IDS |
|---|---|---|
| Role | **Active filtering** | **Passive monitoring** |
| When it fails | **Fail-close** | **Fail-open** |
| In the figure | In line — traffic goes *through* it | To one side — traffic passes, a copy goes to the IDS |

> **What fail-close and fail-open mean, derived.** The figure explains the words. A firewall sits in the path, so if it stops working nothing gets through: availability is lost and the policy is not violated. An IDS sits beside the path, so if it stops working traffic carries on unwatched: availability is kept and detection is lost, *silently*.
>
> That is the blacklist/whitelist choice from [[Security Design Principles|fail-safe defaults]] made in hardware. It also tells an attacker which device to aim at. Crashing the firewall cuts off the attacker's own access; overloading the IDS removes the witness.

## Requirements of a Network IDS

> - **High-speed, large volume monitoring** — no packet filter drops
> - **Real-time notification**
> - **Mechanism separate from policy**
> - **Extensible**
> - **Broad detection coverage**
> - **Economy in resource usage**
> - **Resilience to stress**
> - **Resilience to attacks upon the IDS itself!**

The first two are about keeping up; the next four are engineering; the last two treat the monitor as a target. *No packet filter drops* connects them: a monitor that drops packets under load has a blind spot, and an attacker who can create load can choose when it is blind.

## How It Is Fooled

The *other problems…* on the first slide are the last three slides of the lecture: a NIDS has to predict what the end host will make of a packet stream, and an attacker can arrange for the two to disagree. See [[Insertion and Evasion Attacks]].

## See Also

- [[Intrusion Detection Systems]]
- [[Host-Based Intrusion Detection]]
- [[Insertion and Evasion Attacks]]
- [[Misuse and Anomaly Detection]]
- [[IDS Performance Metrics]]
- [[Firewalls]]
- [[Security Policy and Mechanism]]
- [[Security Design Principles]]
- [[Security Attack Taxonomy]]
- [[Port Scanning]]
- [[CSCE 465]]
