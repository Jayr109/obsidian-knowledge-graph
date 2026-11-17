---
title: "Worms"
type: concept
tags: [csce465, security, malware, worms, propagation, scanning, detection]
sources: [csce465-lecture-11-malware]
course: CSCE 465
updated: 2026-11-04
---

> **A worm is code that replicates and propagates across the network**, often carrying a *payload*. Usually spread via **exploiting flaws in open services** — "viruses" require user action to spread.

That contrast with [[Computer Viruses|viruses]] is the whole of it. A worm needs no user, so its speed is bounded by the network rather than by human behaviour, and [[CSCE 465]] spends most of its malware lecture on the consequences. For the specific outbreaks see [[Notable Worms]].

## The First Worm

> First worm: **Robert Morris, November 1988** — **6–10% of all Internet hosts infected** (!). Many more since, but **none on that scale until July 2001**.

That thirteen-year gap is worth noticing: the technique was demonstrated in 1988 and not matched until Code Red. The [[Buffer Overflow|buffer overflow]] lecture gives the same event as *"6,000 machines"* — consistent with 6–10% of an Internet that then had roughly 60,000 hosts.

## What a Worm Has to Do

The lecture's decomposition of the Morris Worm generalizes to every worm since:

> - Determine **where** it could spread
> - **Spread** its infection
> - Remain **undiscovered and undiscoverable**

Each of the three is a design problem with its own literature, and the scanning strategies below are entirely about the first one.

## Designing Fast-Spreading Worms

The lecture presents this from the attacker's side, because the defender's problem is set by it:

| Technique | Idea |
|---|---|
| **Hit-list scanning** | The time to infect the **first 10,000 hosts dominates** total infection time. Solution: reconnaissance in advance — stealthy scans, etc. |
| **Permutation scanning** | Observation: most scanning is **redundant**. Idea: a **shared permutation** of the address space; each worm starts scanning from its own IP address and **re-randomizes when it finds an already-infected machine**. |
| **Internet-scale hit lists** | A **flash worm**: complete infection within **30 seconds**. |

> **Why the first 10,000 dominate, derived.** Infection is exponential, so the curve's shape is fixed by how long the slow early phase lasts. One infected host scanning a 32-bit address space mostly finds nothing; a thousand infected hosts find targets constantly. A pre-computed hit list lets the worm **skip the slow part entirely** by starting with thousands of known-vulnerable addresses — turning the S-curve into something close to a step. Permutation scanning attacks the other end: once many hosts are infected, most scans hit machines already compromised, and the shared permutation lets a worm detect that redundancy and move elsewhere. The two techniques optimize opposite ends of the same curve.
>
> The defensive consequence is uncomfortable. **Every reactive defence has a response-time budget set by the worm's doubling time**, and a flash worm's budget is zero. Human-in-the-loop response stopped being viable somewhere between Code Red (37-minute doubling) and [[Notable Worms|Slammer]] (8.5 seconds).

## Worm Detection and Defense

The lecture's survey, which is largely [[Guofei Gu]]'s own research area:

- **Worm propagation modeling**
- **Automatic signature generation** — e.g. Earlybird, Autograph
- **Detection**
  - **Honeypot-based** — e.g. HoneyStat
  - **Local information based** — e.g. DSC
  - **Global information based** — e.g. Kalman Filter
- **Mitigation and response**

> **Why automatic signature generation is listed first, derived.** [[Computer Viruses|Signature scanning]] works only once a signature exists, and [[Notable Worms|Nimda]] showed that the gap between a worm appearing and a signature being published — *"minutes or hours later"* — is longer than the worm's doubling time. Generating signatures automatically from observed traffic is the attempt to close a race that manual analysis has already lost. Honeypots serve the same end from a different angle: a machine that offers no legitimate service means **any** traffic reaching it is suspect, so detection needs no signature at all.

The detection items on this list get a lecture of their own: see [[Intrusion Detection Systems]], and [[Misuse and Anomaly Detection]] for the signature-versus-behaviour split. The reconnaissance a hit list is built from is [[Port Scanning]].

## See Also

- [[Notable Worms]]
- [[Search Worms]]
- [[Malware]]
- [[Computer Viruses]]
- [[Botnets]]
- [[Stuxnet]]
- [[Buffer Overflow]]
- [[Internet Protocol]]
- [[Port Scanning]]
- [[Intrusion Detection Systems]]
- [[Misuse and Anomaly Detection]]
- [[Guofei Gu]]
- [[CSCE 465]]
