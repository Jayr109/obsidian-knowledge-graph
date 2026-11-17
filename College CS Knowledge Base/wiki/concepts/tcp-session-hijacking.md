---
title: "TCP Session Hijacking"
type: concept
tags: [csce465, security, network-security, tcp, spoofing, sequence-prediction, hijacking]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

**TCP session hijacking**, as [[CSCE 465]] presents it, is what happens when [[IP Spoofing]] meets a predictable sequence number. The slide is titled *IP Spoofing & TCP Session Hijacking*, and its one sentence is the whole goal:

> **X establishes a TCP connection with B assuming A's IP address.**

It is the third of the lecture's three TCP attacks and the one that defeats the defence the others left standing — the [[TCP|three-way handshake]] itself.

## The Five Steps

The slide is a single figure with three hosts and five numbered arrows:

```
            (4)  SYN(seq=n) ACK(seq=m+1)
     A  <---------------------------------  B
     ^                                     ^ ^
     |                                     | |
     | (1) SYN flood     (3) SYN(seq=m),   | |  (5) ACK(seq=n+1)
     |                       src = A       | |
     |                                     | |
     +---------------  X  -----------------+-+
               (2) predict B's TCP seq. behavior
```

1. **X SYN-floods A.**
2. **X predicts B's TCP sequence behaviour.**
3. X sends B a `SYN(seq=m)` with **source = A**.
4. B answers **A**, not X: `SYN(seq=n), ACK(seq=m+1)`.
5. X sends B `ACK(seq=n+1)`, again as A. B now believes it holds an open connection with A.

## Why Each Step Is There

> **Derived; the slide gives the arrows and no explanation.**
>
> **Step 4 is the problem the attacker has to solve.** B's reply goes to the address in the source field, so X never sees `n`. That is the protection [[IP Spoofing]] described: *the handshake prevents the attacker from establishing a TCP connection* under a forged address.
>
> **Step 2 is the solution.** The same slide named the exception — *the attacker can succeed if "y" can be predicted*. If B chooses its initial sequence numbers in a guessable way, X can first open ordinary connections to B under its own address, watch the numbers B hands out, and work out what `n` will be next. Then step 5 can be sent blind.
>
> **Step 1 keeps A out of it.** A did not send the SYN in step 3, so when B's `SYN, ACK` arrives A would answer with a reset and B would drop the half-open connection. A [[SYN Flooding|SYN-flooded]] host is too busy to respond. This is the second attack of the lecture used as a component of the third.

After step 5 the attack is still **blind**: X can send data to B as A and cannot read what B sends back, because that also goes to A. So it is only worth doing where one unanswered message is enough.

## What It Is Good For

It is enough where B **trusts A by address**. [[User Authentication]] recorded the Berkeley r-tools — `rsh`, `rlogin`, `/etc/hosts.equiv`, per-user `.rhosts` — as address-based authentication: *assume the identity of the source can be inferred from the network address the packets arrive from*, with the lecture naming *spoofing of network addresses* as the threat. This is that threat carried out. A single blind command to a host that trusts A's address needs no reply.

## A Note on the Name

The figure shows X opening a **new** connection in A's name. It does not show X taking over a connection A already had, which would need the live sequence numbers of that connection (by [[TCP Reset Attack|guessing into the window]] or by sniffing). The page keeps the deck's title.

## Defences

> **Derived from the conditions the attack needs.** Each step fails if one thing changes: [[IP Spoofing|router filtering]] at X's network stops the forged source in step 3; **unpredictable initial sequence numbers** defeat step 2 (the same requirement [[SYN Flooding|SYN cookies]] put on their `rand`); and not treating an IP address as an identity removes the reason to try. That last one is the durable fix, and it is why the r-tools were replaced by cryptographic authentication.

## A Prediction Closed

When Lecture 10 was ingested, [[TCP]] recorded as a derived consequence that the handshake's protection *"depends entirely on `y` being unguessable"* and called the result *the classic sequence-number prediction attack*. This slide is that attack, drawn.

## See Also

- [[TCP]]
- [[IP Spoofing]]
- [[SYN Flooding]]
- [[TCP Reset Attack]]
- [[User Authentication]]
- [[Security Attack Taxonomy]]
- [[Vulnerability Analysis]]
- [[CSCE 465]]
