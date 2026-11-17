---
title: "Security Attack Taxonomy"
type: concept
tags: [csce465, security, attacks, threats, eavesdropping, mitm]
sources: [csce465-lecture-02-security-overview, csce465-hw1-build-and-threat-model-an-ai-agent, csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

[[CSCE 465]] classifies attacks by **which security property they violate**, giving one attack family per component of the [[CIA Triad]] plus authenticity. This is the organizing move that makes the [[Security Threat Landscape|catalogue of real threats]] analyzable: any concrete attack can be placed by asking what it breaks, not how it works.

## Threats vs. Attacks

- A **threat** is a *potential* violation of security, arising from flaws in design, implementation, or operation.
- An **attack** is any *action* that violates security.

Lecture 12 names the thing in between: those flaws are **vulnerabilities**. See [[Vulnerability Analysis]].

Attacks divide into **passive** and **active**. A passive attack observes without altering; an active attack modifies, injects, or destroys. The distinction is practical rather than academic: passive attacks are far harder to detect, because by construction they leave the system's behavior unchanged. Prevention is the only real defense against a purely passive attacker.

## The Four Attack Families

| Attack | Violates | What it does |
|---|---|---|
| **Interception** (eavesdropping) | Confidentiality | Unauthorized access to information |
| **Tampering** | Integrity | Stop, delay, and optionally modify a message, then release it |
| **Fabrication** | Authenticity | Assume another's identity and generate objects under it |
| **Interruption** | Availability | Destroy, corrupt, or overwhelm so service cannot be delivered |

### Interception — Attack on Confidentiality

Unauthorized reading: packet sniffers and wiretappers, illicit copying of files and programs. Passive by nature.

The lecture's hardware example is **full packet capture** — an OC3Mon-style rack-mounted PC with an optical splitter and a Data Acquisition and Generation (DAG) card, tapping a fiber link without participating in it. The software example is `tcpdump` on a promiscuous network interface, with a pointed question attached: *on a switched network, what can you actually see?* (Switching limits a passive tap to broadcast traffic and the attacker's own segment — which is why [[ARP]] spoofing exists, to make a switched network behave like a shared one.)

The lecture then asks what different traffic types reveal even when you cannot read the contents: DNS lookups and replies, IP headers without payloads, and payloads. The answer is the point of the next section.

### Does Cryptography Guarantee Confidentiality?

No — and this is the sharpest idea in the lecture. **Who is talking to whom is itself important information.** Encryption protects payload content and nothing else. The metadata survives: the parties involved, where they are, how they communicate, and how often.

This is why [[CIA Triad|confidentiality]] is defined in the course to cover more than data. A perfectly encrypted channel still discloses *existence* ("this person contacts a divorce lawyer daily") and *pattern*. Traffic analysis operates entirely on what cryptography leaves behind.

### Tampering — Attack on Integrity

The attacker sits in the path: stop the flow of a message, delay it, optionally modify it, then release it again. Unlike interception this is necessarily active, and therefore in principle detectable — which is why integrity mechanisms can choose between preventing and detecting.

### Fabrication — Attack on Authenticity

Unauthorized assumption of another's identity, then generating and distributing objects under that identity. The masquerader sends messages "from A" that A never wrote. This attacks **origin integrity** rather than data integrity: the content may be perfectly well-formed and unaltered in transit.

### Interruption — Attack on Availability

Ranges from crude to subtle:
- Destroy hardware (cutting fiber) or software
- Modify software in a subtle way (aliasing commands)
- Corrupt packets in transit
- Blatant **denial of service**: crash the server, or overwhelm it until its resources are exhausted

## Man-in-the-Middle

The MITM position generalizes the taxonomy rather than sitting inside it, because occupying the path enables all four families at once:

- **Passive tapping** — listen without altering contents (interception)
- **Active wire tapping** — modify data in transit (tampering), or take over the user's identity after authentication completes (fabrication)

The lecture's example is an intruder who waits for a legitimate user to log in, injects a `logoff` to the user while telling the server everything is `fine!`, and inherits the authenticated session. This is why authenticating *once* at connection setup is insufficient — it is [[Security Design Principles|complete mediation]] stated as an attack.

## Where Prompt Injection Fits (and Does Not)

[[Prompt Injection]], introduced with the first homework, sits awkwardly in this taxonomy — which is worth noticing rather than forcing. An indirect injection is closest to **fabrication**: the attacker causes an action to be attributed to the operator, who never requested it. But the mechanism is neither identity spoofing nor message tampering. The poisoned page is delivered honestly, over a channel working exactly as designed, and is treated as authoritative because the receiving architecture has no way to record that it was not.

The connection to this lecture's sharpest claim is direct. Encryption defeats the on-path attacker — eavesdropping, tampering, replay. Indirect injection is **not on-path**: the payload is authored into content the agent is legitimately asked to read, so a perfectly confidential and authenticated pipe delivers it intact. *"Did this arrive unmodified?"* is the wrong question; *"should the agent act on it?"* is an authorization question, not an integrity one.

## Impact

The lecture closes the section with a list and a warning:

- Theft of confidential information
- Unauthorized use of network bandwidth or computing resource
- Spread of false information
- Disruption of legitimate services

**All attacks can be related and are dangerous.** The families are analytical categories, not independent risks — a fabrication attack enables interception, which enables a more targeted interruption.

## Worked Instances

Lecture 12 supplies protocol-level examples for most of the table above:

| Family | Worked in the KB |
|---|---|
| Interruption | [[SYN Flooding]], [[TCP Reset Attack]], [[Smurf Attack]] |
| Fabrication | [[IP Spoofing]], [[ARP Poisoning]], [[ICMP Redirect Attack]], [[TCP Session Hijacking]] |
| Man-in-the-middle position | [[ARP Poisoning]], [[ICMP Redirect Attack]] |

## See Also

- [[CIA Triad]]
- [[Computer Security]]
- [[Security Threat Landscape]]
- [[Security Services]]
- [[Prompt Injection]]
- [[AI Agent Security]]
- [[ARP]]
- [[Vulnerability Analysis]]
- [[IP Spoofing]]
- [[ARP Poisoning]]
- [[SYN Flooding]]
- [[CSCE 465]]
