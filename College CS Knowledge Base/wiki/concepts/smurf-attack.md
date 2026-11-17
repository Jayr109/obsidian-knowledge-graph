---
title: "Smurf Attack"
type: concept
tags: [csce465, security, network-security, icmp, denial-of-service, amplification, reflection, ddos, dns]
sources: [csce465-lecture-12-vulnerability-analysis]
course: CSCE 465
updated: 2026-11-16
---

A **smurf attack** floods a victim with [[ICMP]] echo replies that the attacker never sent it. The attacker pings a network's broadcast address with the victim's address in the source field, and every host on that network answers the victim. It is [[CSCE 465]]'s first ICMP attack, and the cleanest example in the course of two ideas that outlive it: **reflection** and **amplification**.

## Ping, Then Smurf

The lecture's figure puts the ordinary case above the attack:

```
ping     host  ---- ICMP echo request ---->  host
         host  <--- ICMP echo reply -------  host

smurf    attacker ---- ICMP echo request to a BROADCAST address,
                       "from" the victim ------------------------>  [ a whole network ]

         victim  <==== ICMP echo reply from every host there =====  [ a whole network ]
```

## The Mechanism

> - Generate *ping* stream (ICMP echo request) to a network *broadcast address* with a *spoofed source IP* set to a victim host
> - **Every host on the ping target network will generate a ping reply** (ICMP echo reply) stream, all towards the victim host
> - Amplified ping reply stream can easily overwhelm the victim's network connection
> - *Fraggle* and *Pingpong* exploit UDP in a similar way

The lecture had already warned about this from the victim's side, on [[IP Spoofing]]: *a smurf attack launched with your host IP address could bring your host and network to their knees.*

## Three Ingredients

The slide describes one attack. Taken apart, it is three separate things, and the table is derived from the mechanism above:

| Ingredient | In the smurf attack | What it buys |
|---|---|---|
| **Spoofing** | Source address = the victim | The replies go to someone who never asked |
| **Reflection** | An innocent network does the sending | The victim sees the reflectors' addresses, not the attacker's |
| **Amplification** | One request to a broadcast address, one reply per host | A small stream in, a large stream out |

> **What follows from that, derived.** The attacker is hidden twice over: once by the forged source, and again because the packets that arrive are genuine replies from machines that did nothing wrong. And none of the reflectors has been compromised. They are answering a ping, which is what [[ICMP]] is for. This is the unauthenticated-control-message problem again — the lecture's own note on ICMP is *Not authenticated!*

## The Same Pattern With DNS

One slide later, under *Others: DDoS Using DNS*:

> **Botnets increasingly used for amplified distributed reflective attacks.**

```
  Attacker
     |  commands
     v
  Zombies ... ----- DNS request for a large TXT record -----> Open recursive DNS servers
                    UDP, ~60 bytes, source = victim            (anyone can query)
                                                                      |
  Victim <------------- large DNS TXT RR, 1500+ bytes ----------------+
```

The figure labels the result with three words, one per ingredient: **Amplified, Distributed, Reflective.**

| | Smurf | DNS |
|---|---|---|
| Reflector | Every host on a network | Open recursive DNS servers |
| Trigger | ICMP echo request to a broadcast address | DNS request for a large TXT record |
| Amplification | One reply per host on the network | ~60 bytes in, 1500+ bytes out — about **25×** |
| Who sends the trigger | The attacker | A [[Botnets\|botnet]]'s zombies |

> **Verified during ingest:** 1500 / 60 = 25. The slide gives the two sizes and leaves the ratio to the reader.
>
> **Why DNS and UDP, derived.** UDP has no handshake, so the [[TCP|reachability proof]] that stops a forged TCP connection is simply absent: one forged datagram gets one full-sized answer. That is also why the slide's *Fraggle* and *Pingpong* variants are UDP attacks. And the botnet adds the word *distributed* — the attacker's own bandwidth stops being the limit, which is the "canonical use of a botnet" recorded on [[Security Threat Landscape]].

## Defences

> **Derived; the deck gives none for this attack.** Each ingredient can be removed separately. Stop the **spoofing** at the attacker's own network, which is the router filtering on [[IP Spoofing]] and has the incentive problem described there. Stop the **amplification** by not answering pings sent to a broadcast address and not forwarding them into the network. Stop the **reflection** in the DNS case by not running resolvers that *anyone can query* — the parenthesis on the slide is the vulnerability.

## Deck Erratum

On the figure slide the lower arrow is labelled *"icmp echo request from all hosts to victim"*. It should read echo **reply**, as the text slide that follows has it. Corrected in the diagram above.

## See Also

- [[ICMP]]
- [[IP Spoofing]]
- [[ICMP Redirect Attack]]
- [[SYN Flooding]]
- [[Botnets]]
- [[Security Threat Landscape]]
- [[Security Attack Taxonomy]]
- [[Vulnerability Analysis]]
- [[CSCE 465]]
