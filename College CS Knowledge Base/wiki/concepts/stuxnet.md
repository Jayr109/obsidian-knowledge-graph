---
title: "Stuxnet"
type: concept
tags: [csce465, security, malware, stuxnet, ics, scada, zero-day, critical-infrastructure]
sources: [csce465-lecture-11-malware]
course: CSCE 465
updated: 2026-11-04
---

**Stuxnet** gets its own section at the end of [[CSCE 465]]'s malware lecture, and the lecture's closing claim says why:

> Many experts say it is **the most complex malicious software created in the history of cyber security**. Highlights that it is **possible to attack critical infrastructures in places other than Hollywood movies**.

It is simultaneously a [[Worms|worm]], a [[Botnets|botnet]], and a rootkit, which is why it sits apart from the chronology on [[Notable Worms]].

## The Target

> **Primary target: industrial control systems.**
>
> - Reprogram **Industrial Control Systems (ICS)**
> - On **Programmable Logic Controllers (PLCs)** — specific **Siemens Simatic (Step 7)** PLCs
> - **Code changes are hidden**

> **Why this is a different kind of malware, derived.** Every other sample in the lecture attacks *computation* — files, credentials, bandwidth, CPU time. Stuxnet attacks a **physical process**, by rewriting the logic of the controller that drives it. That breaks the assumption running under the whole course, that the asset being protected is information. Here the [[CIA Triad|integrity]] violation propagates out of the computer and into machinery, and the hidden code changes mean the operators' own instrumentation reports normal operation — the control system lies to the people watching it. That is why the lecture gives it the last word.

## The Component List

> Vast array of components used:
>
> - **Zero-day exploits**
> - **Windows rootkit**
> - **PLC rootkit** — *the first ever*
> - **Antivirus evasion**
> - **Peer-to-peer updates**
> - **Signed driver with a valid certificate**
> - **Command and control interface**

The **signed driver** is the item worth pausing on: code signing is the defence that is supposed to make the others moot, and it was defeated not by breaking the cryptography but by obtaining valid certificates. The summary slide records **2 compromised digital certificates**. This is [[Public Key Infrastructure|PKI]] failing the same way the Comodo breach did in Lecture 5 — the signature verified correctly and attested to the wrong thing.

## Propagation

> **Network**
>
> - Peer-to-peer communication and updates
> - Infecting WinCC machines via a **hardcoded database server password**
> - Propagating through **network shares**
> - Propagating through the **MS10-061 Print Spooler** zero-day vulnerability
> - Propagating through the **MS08-067 Windows Server Service** vulnerability
>
> **USB**

> **USB is in the list because the target is not on the Internet, derived.** Industrial control networks are normally air-gapped, which defeats every propagation vector on [[Notable Worms]]. A removable drive crosses that gap, carried by a person — so the worm needs the network vectors to spread *inside* the plant once it arrives, and a physical vector to arrive at all. The hardcoded database password is the same observation from another angle: control-system software ships with credentials that cannot be changed, so the air gap is doing the security work that authentication is not.

## Command and Control

> Stuxnet contacts the command and control server:
>
> - Tests whether it can connect to `www.windowsupdate.com` and `www.msn.com`, on **port 80**
> - Sends some basic information about the compromised computer to the attacker
> - C&C hosts: `www.mypremierfutbol.com` and `www.todaysfutbol.com` — these two URLs previously pointed to servers in **Malaysia** and **Denmark**

The connectivity test is the detail worth keeping: before calling home, the malware checks whether it has general Internet access by reaching two innocuous, universally reachable sites. Traffic to those is unremarkable in any log, and the result tells it whether it is inside the air gap or outside it.

## Summary, as the Lecture Gives It

> Stuxnet achieved many things in the malicious code realm:
>
> - **First to exploit 4 zero-day vulnerabilities**
> - **Compromised 2 digital certificates**
> - **Injected code into industrial control systems and hid the code from operators**

Four zero-days in one sample is the figure that signals resourcing rather than opportunism: zero-days are expensive, and spending four on a single target implies the target was chosen first and the exploits acquired to reach it — the opposite of the [[Notable Worms|random-scanning worms]] that take whatever is vulnerable.

Stuxnet also appeared earlier in the course: [[Buffer Overflow|Lecture 9]] lists it among the worms built on memory-corruption bugs, at the end of a line that starts with the Morris Worm in 1988.

## See Also

- [[Malware]]
- [[Worms]]
- [[Notable Worms]]
- [[Botnets]]
- [[Computer Viruses]]
- [[Buffer Overflow]]
- [[Public Key Infrastructure]]
- [[CIA Triad]]
- [[Security Threat Landscape]]
- [[CSCE 465]]
