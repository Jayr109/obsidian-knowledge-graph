---
title: "Botnets"
type: concept
tags: [csce465, security, malware, botnet, command-and-control, irc, p2p, bothunter]
sources: [csce465-lecture-11-malware]
course: CSCE 465
updated: 2026-11-04
---

A **botnet** is a population of compromised machines under a common **command-and-control (C&C)** channel. [[CSCE 465]] gives it the final third of the malware lecture, and the organizing question throughout is architectural: **where does the C&C live?** It is also the part of the course closest to [[Guofei Gu]]'s own research — the detection system presented is his.

Where a [[Worms|worm]] is about *propagation*, a botnet is about *control* afterwards. The two compose: several worms on [[Notable Worms]] end by joining the infected machine to one.

## Centralized Botnets

The classic design: every bot connects to a C&C server, historically over **IRC**.

The lecture's **life-cycle of an IRC-based botnet infection** annotates the stages:

- Initial exploit over **port 445** and similar service ports
- Use a **domain name** rather than a fixed IP **to keep flexibility**
- The C&C channel may be **any protocol**
- The later stages **include an authentication procedure** — the botmaster must prove to the bot that commands are genuine

> **Why the botmaster authenticates to the bots, derived.** It looks backwards — the compromised machines are the attacker's own. But a C&C channel that accepts unauthenticated commands can be **taken over by anyone who finds it**, including a rival botmaster or a researcher. Authentication protects the attacker's *investment*, and it is a real instance of [[CIA Triad|origin integrity]] mattering to whoever holds the asset, regardless of which side they are on. It also means a defender who merely *locates* the channel cannot necessarily shut the botnet down.
>
> The **domain name** note is the same logic applied to resilience: a hard-coded IP dies when that host is seized, while a domain can be re-pointed. This is the pressure that led to fast-flux and domain-generation algorithms.

### Malware Collection

The lecture shows a data-collection architecture used to study botnets, with its design notes:

- **Longitudinal tracking** of collected samples
- **Graybox testing** — extract network and IRC-related features, and **learn the dialect** each botnet family speaks
- **Reduce the number of downloads**
- The harness runs **its own IRC client**, behind a **firewall**

Cited to *A Multifaceted Approach to Understanding the Botnet Phenomenon*.

> **"Learn the dialect" is the interesting phrase, derived.** C&C traffic is usually not a documented protocol but a family-specific convention layered over one — which is why detection cannot be a fixed signature and must infer structure from observed exchanges. The firewall and the purpose-built client are the ethics-and-safety half of the same setup: you study a botnet by joining it, which means containing it. The same constraint governs the course's own [[CSCE 465|lab safety rules]] — everything in a VM, NAT only, no real command-and-control.

## Distributed Botnets

The alternative: no central server, with bots forming a peer-to-peer overlay.

### Storm Worm / Peacomm (2007)

> Uses **P2P communication: Kademlia**. Spreads by a cleverly designed **spam campaign**.

Arrives as an email with a catchy subject — the first instance was *"230 dead as storm batters Europe"*, which gave it its name; others included *"Condoleeza Rice has kicked German Chancellor"*, *"Saddam Hussein alive!"* and *"Fidel Castro dead"*. The attachment or URL carries the payload: `FullVideo.exe`, `MoreHere.exe`, `ReadMore.exe`, and it also masqueraded as flash postcards. Once opened, it installs a **Trojan (`wincom32`) and a rootkit**.

**Characteristics:**

- Infected machines join the botnet — **between 1 and 5 million machines infected (September 2007)**
- **Obfuscated peer-to-peer control structure** — not like Agobot, which uses a simple IRC control channel; interacts with peers via the **eDonkey protocol**
- **Obfuscated code and anti-debugging defences** — goes into an **infinite loop if it detects VMware or Virtual PC**, and a large number of spurious probes (evidence of external analysis) **triggers a distributed DoS attack**
- The **spambot binary is used to spread new infections** in subsequent campaigns, looking for email addresses and mailing lists in files on infected machines

> **Storm attacks the researcher, not just the target, derived.** The VM check and the DoS-on-probing response are defences against *analysis* rather than against the victim — the malware treats being studied as an attack and retaliates. That is a direct answer to the collection architecture above, and it is why the "firewall" in that diagram is load-bearing. It also inverts the [[Computer Viruses|antivirus generations]]: behaviour-based detection requires running the sample, and this sample declines to behave when it thinks it is being watched.

**Stated weaknesses** of the P2P design:

- **Initial peer list** — a new bot must bootstrap from somewhere
- **Sybil attack** — flood the overlay with fake peers
- **Index poisoning** — corrupt the lookup structure so bots cannot find each other

## Centralized vs Distributed

The lecture's comparison table:

| Communication system | Security | Design complexity | Channel type | Message latency | Detectability | Resilience |
|---|---|---|---|---|---|---|
| **Centralized** | Low | Low | Bidirectional | Low | **High** | **Low** |
| **Distributed** | High | High | Unidirectional | High | **Low** | **High** |

> **The trade in one line, derived.** Centralized C&C is cheap to build and fast to command, and it has a single point of failure that is also a single point of *observation* — find the server and you see and stop everything. P2P removes that point, at the cost of complexity and latency: commands propagate hop by hop, so the botmaster loses the immediate bidirectional channel. Note that *security* here means **the attacker's** security. Every row is written from the botmaster's point of view, and the Storm weaknesses above are exactly where the "high security" column is softer than it looks.

## Detection: BotHunter

> **BotHunter: Detecting Malware Infection Through IDS-Driven Dialog Correlation** — Guofei Gu, Phillip Porras, Vinod Yegneswaran, Martin Fong, and Wenke Lee.
>
> Also cited: *A Multi-perspective Analysis of the Storm (Peacomm) Worm* — Phillip Porras, Hassen Saïdi and Vinod Yegneswaran.

**Dialog correlation** is the idea in the title: rather than matching a signature for any single event, BotHunter looks for the **sequence** of events that an infection life-cycle necessarily produces — inbound scan, exploit, binary download, C&C coordination, outbound scanning — and correlates them per host. Any one of those alone is weak evidence; in order, they are not.

This is the [[Guofei Gu|BotHunter]] work the KB has referenced since Lecture 1, now arriving as course content. It is also why [[Security Threat Landscape|the Lecture 2 threat survey]] gave botnets their own slide.

## Open Research Questions

The lecture closes the section with its own open problems:

- **Botnet detection and defense** — under various datasets (packet traces, varying numbers of vantage points), and *can the botnet operation be disabled?*
- **Click fraud detection**
- **Phishing detection**

## See Also

- [[Malware]]
- [[Worms]]
- [[Notable Worms]]
- [[Search Worms]]
- [[Computer Viruses]]
- [[Stuxnet]]
- [[Security Threat Landscape]]
- [[Guofei Gu]]
- [[CIA Triad]]
- [[SMTP]]
- [[CSCE 465]]
