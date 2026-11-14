---
title: "Notable Worms"
type: concept
tags: [csce465, security, malware, worms, code-red, nimda, slammer, mydoom, case-studies]
sources: [csce465-lecture-11-malware]
course: CSCE 465
updated: 2026-11-04
---

[[CSCE 465]] teaches [[Worms|worm]] propagation through a chronology rather than a model, because each outbreak introduced one new idea. This page is that chronology. The general mechanics are on [[Worms]]; [[Stuxnet]] and the Storm worm are treated separately on [[Stuxnet]] and [[Botnets]].

## The Morris Worm — November 1988

> 1988: **No malicious payload**, but bogged down infected machines by **uncontrolled spawning**. Infected **10% of all Internet hosts** at the time.

**Multiple propagation vectors:**

- **Remote execution using `rsh` and cracked passwords** — tried to crack passwords using a small dictionary and the publicly readable password file; targeted hosts from `/etc/hosts.equiv`
- **Buffer overflow in `fingerd` on VAX** — a standard [[Stack Smashing|stack smashing]] exploit
- **DEBUG command in Sendmail** — in early versions it was possible to execute a command on a remote machine by sending an SMTP message

**Effect:** resource exhaustion from **repeated infection due to a programming bug**, and servers disconnected from the Internet by sysadmins to stop the spread.

**How it stayed hidden:** loaded code in memory, encrypted it, removed the file, and periodically changed its name and process ID.

> **The bug is the lesson, derived.** The worm carried no payload — the damage was entirely an accident of re-infecting machines it had already compromised. [[Computer Viruses|A virus avoids this with an infection mark]], and the Morris Worm's equivalent check was too weak. The thing that made it visible was also the only thing that made it harmful: a silent worm would have spread further and been noticed later. Note also that its three vectors are **a weak password, a buffer overflow, and a trapdoor** — three of the course's own topics, in 1988.

Two of the three also connect to earlier KB material: the readable `/etc/passwd` is exactly the exposure [[Password Authentication|the authentication lecture]] covers, and `fingerd` is the canonical [[Buffer Overflow|buffer overflow]].

## Summer of 2001 — Three Major Outbreaks

### Code Red I — July 13, 2001

> The **first worm of the modern era**. Exploited a buffer overflow in Microsoft's **Internet Information Server (IIS)**.

Behaviour was calendar-driven:

- **1st–20th of each month: spread** — find new targets by **random scan of the IP address space**, spawning **99 threads** to generate addresses and look for IIS
- **21st to end of month: attack** — deface websites with *"HELLO! Welcome to http://www.worm.com! Hacked by Chinese!"*

> The creator **forgot to seed the random number generator**, so every copy scanned the same set of addresses.

### Code Red I v2 — July 19, 2001

> Same codebase, but **fixed the random IP address generation bug**.

- Compromised **all vulnerable IIS servers on the Internet**; the large vulnerable population meant fast spread
- Scanned address space grew exponentially — **350,000 hosts infected in 14 hours**
- **Payload:** a distributed packet flooding (denial of service) attack on `www.whitehouse.gov`
- A coding bug caused it to die on the 20th of each month — *but if the victim's clock was wrong, it resurrected on the 1st*

> **One line of code separates the two, derived.** v1 and v2 are the same worm; the only change is seeding the PRNG. Unseeded, every copy generated an identical address sequence, so a thousand infected machines scanned the same thousand addresses and the worm could not outgrow its own first wave. Seeded, the copies cover the space independently and the growth becomes genuinely exponential — **350,000 hosts in 14 hours**. This is the sharpest demonstration in the course that a worm's danger is a property of its **scanning strategy**, not its exploit: identical vulnerability, identical payload, one missing function call.

### Code Red II — August 4, 2001

> Same IIS vulnerability, **completely different code**, and it **kills Code Red I**. Known as "Code Red II" because of a comment in the code. Worked only on Windows 2000, **crashed NT**.

**Scanning algorithm preferred nearby addresses:**

| Target | Probability |
|---|---|
| Same class A | **1/2** |
| Same class B | **3/8** |
| Random from the entire Internet | **1/8** |

- **Payload:** installed a **root backdoor** in IIS servers for unrestricted remote access
- **Died by design on October 1, 2001**

> **Why locality beats uniform random scanning, derived.** Vulnerable hosts are not spread evenly across the address space — they cluster, because one organization runs many similar machines on adjacent addresses. Scanning nearby addresses therefore has a far higher hit rate than scanning uniformly, and the packets stay inside the local network where they are fast and often unfiltered. The 1/8 random share is what stops the worm from getting trapped in one subnet. It is a deliberate exploration-versus-exploitation split.

The lecture also shows the Paxson measurement of the two together: **Code Red II dies off as programmed, and with its predator gone, Code Red I comes back — still exhibiting its monthly pattern.**

### Nimda — September 18, 2001

> A **multi-modal worm** using several propagation vectors:

- Exploit the **same IIS buffer overflow** as Code Red I and II
- **Bulk-email itself** as an attachment to addresses harvested from infected machines
- Copy itself across **open network shares**
- Add exploit code to **web pages on compromised sites** to infect visiting browsers
- **Scan for backdoors left by Code Red II**

**Payload:** turned-off code that would have deleted all data on infected hard drives.

**Why signature-based defences did not help:**

> Nimda **leaped firewalls**. Many firewalls passed mail untouched, relying on mail servers to filter out infections — and most filters simply scan attachments for **signatures of known viruses and worms**. Nimda was a brand-new infection with an unknown signature.
>
> **Big challenge: detection of zero-day attacks.** When a worm first appears in the wild, its signature is not extracted until **minutes or hours later**.

That last line is the quantitative statement of the problem [[Worms|automatic signature generation]] exists to solve, and the reason the final vector above matters: reusing *another worm's* backdoor means Nimda inherited Code Red II's installed base for free.

## Slammer (Sapphire) — January 24/25, 2003

> A **UDP worm** exploiting a buffer overflow in Microsoft's **SQL Server**. The overflow was **already known and patched by Microsoft** — but not everybody installed the patch.

- The **entire code fits into a single 404-byte UDP packet** — worm binary followed by an overflow pointer back to itself
- Classic [[Stack Smashing|buffer overflow]] combined with random scanning: once control passes to the worm, it randomly generates IP addresses and sends a copy of itself to **port 1434**, where MS-SQL listens

**Propagation figures:**

- Scan rate of **55,000,000 addresses per second**; up to **30,000 single-packet worm copies per second**
- Initial infection **doubling in 8.5 seconds** — Code Red's doubling time was **37 minutes**
- Worm-generated packets **saturated the carrying capacity of the Internet in 10 minutes**
- **75,000 SQL servers compromised** — in spite of a broken pseudo-random number generator

**Impact — $1.25 billion of damage**, temporarily knocking out elements of critical infrastructure:

- Bank of America ATM network
- The entire cell phone network in South Korea
- Five root DNS servers
- Continental Airlines' ticket processing software

> The worm **did not even have a malicious payload** — simply bandwidth exhaustion on the network and resource exhaustion on infected machines.

**The secret of Slammer's speed**, as the lecture puts it:

| | Old-style (Code Red) | Slammer |
|---|---|---|
| Transport | Spawn a thread, establish a **[[TCP\|TCP]] connection**, send a copy over it | **Connectionless UDP** — just send a 404-byte packet |
| Bounded by | **Latency** of the network | **Bandwidth** of the network |

> **Why that distinction is worth more than the figures, derived.** A TCP worm must wait for a [[TCP|three-way handshake]] to complete before it can send anything, so each infection attempt costs at least one round trip and a thread blocked waiting on it. Latency does not improve with a faster link. A single-packet UDP worm never waits for anything — it is **fire-and-forget**, so the only limit is how fast the host can put packets on the wire. Fitting into one packet is what makes that possible, and it is why 404 bytes is the most important number on the slide. Slammer also confirms [[Buffer Overflow Defenses|the ASLR argument]]: it worked because the **same code worked on every machine**.

## Blaster and Welchia/Nachia — August 11, 2003

> A **scanning worm** exploiting the **RPC service** in Microsoft Windows XP and 2000 — first address at random, then a **sequential upward scan**. Easy to detect, yet propagated widely and leaped firewalls.
>
> **Payload:** denial of service against MS Windows Update, plus a remotely accessible backdoor.

**Welchia/Nachia was intended as a counter-worm:**

> Random-start sequential scan, use **[[ICMP]]** to determine if an address is live, then copy itself over, **patch the RPC vulnerability**, and **remove Blaster if found**.
>
> **Did more damage by flooding networks with traffic.**

> **The benevolent-worm problem, derived.** Welchia is the concrete case behind the [[Computer Viruses|"malevolent, benign, or benevolent"]] line in the virus myths. Its intent was repair, and it still caused more harm than its target — because the *propagation* mechanism is the damaging part regardless of payload, and because nobody consented to it. Patching a machine you do not own, by exploiting it, is still exploitation; the course's own [[Security Policy and Mechanism|policy framing]] applies cleanly — the system entered an unauthorized state, and good intentions are not in the policy.

## Search Worms

A different answer to the "where to spread" problem: instead of scanning the address space, **query a search engine for vulnerable hosts**. **MyDoom** and **Santy** are the lecture's examples, and the countermeasures are a genuine arms race — up to a search engine declining to return results whose *answer* would be a target list. Covered on [[Search Worms]].

## See Also

- [[Worms]]
- [[Search Worms]]
- [[Malware]]
- [[Computer Viruses]]
- [[Botnets]]
- [[Stuxnet]]
- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Buffer Overflow Defenses]]
- [[TCP]]
- [[ICMP]]
- [[SMTP]]
- [[Password Authentication]]
- [[CSCE 465]]
