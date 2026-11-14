---
title: "Search Worms"
type: concept
tags: [csce465, security, malware, worms, search-engines, mydoom, santy, anomaly-detection]
sources: [csce465-lecture-11-malware]
course: CSCE 465
updated: 2026-11-04
---

A **search worm** solves [[Worms|the "where to spread" problem]] by letting a search engine find its targets. Instead of scanning the address space — the approach every worm on [[Notable Worms]] takes — it issues queries and reads the results as a target list. [[CSCE 465]] treats it as a distinct propagation model, and it is the one where the defence ends up sitting with a third party.

## The Method

> - **Generate a search query**
>   - Search for **version numbers of vulnerable software** to find exploitable targets
>   - Search for **popular domains** to harvest email addresses
> - **Analyze search results**
>   - Remove duplicates and URLs belonging to the search engine
> - **Infect identified targets**
>   - **Reformat URLs to include the exploit** — for example, append exploit code instead of a username
>   - The exploit code downloads the actual infection and joins the machine to a [[Botnets|botnet]]

> **Why this beats scanning, derived.** Random scanning spends almost all its packets on addresses where nothing is listening — the reason [[Notable Worms|hit-list and permutation scanning]] exist is to cut that waste. A search engine has already done the work: it has crawled the web and indexed which hosts run which software at which version. Querying it converts a blind sweep of 2³² addresses into a list of hosts **known** to be vulnerable, with no packets sent to the targets beforehand. The worm also becomes quieter, because the reconnaissance traffic goes to Google rather than to the victims' networks, where an intrusion detector might notice it.

## MyDoom

- Spreads by **email**
- **MyDoom** searches the local hard drive for addresses; **MyDoom.O** uses **web search engines**
- Queries split between **Google (45%), Lycos (22.5%), Yahoo (20%) and Altavista (12.5%)**

Google's own measurements, as the lecture presents them: **60,000 hosts infected in 8 hours**, a peak scan rate of **30,000 queries per second**, and the number of served queries **dropping as Google's anomaly detection kicked in**.

The four-way query split is worth noting as deliberate design — spreading load across engines both increases capacity and keeps any single provider's view of the worm below the threshold that would trigger a response.

## Santy

- Written in **Perl**, exploits a bug in the **phpBB** bulletin board system (prior to version 2.0.11), allowing **injection of arbitrary code** into the web server running phpBB
- Uses **Google to find sites running phpBB**
- Once injected, downloads the actual worm code from a **central site**, asks Google for more targets, and connects the infected machine to an **IRC [[Botnets|botnet]]**
- **Polymorphism:** the actual Perl code **changes from infection to infection**, so filtering worm traffic is difficult

Polymorphism here is the same countermeasure [[Computer Viruses|viruses]] use against signature scanners, applied to network traffic instead of files.

## Evading Anomaly Detection

The arms race, as the lecture lays it out:

| Move | By |
|---|---|
| Google will **refuse worm-generated queries** | Defender |
| Different Santy variants **generate different search terms**, or take them from an **IRC botmaster** | Attacker |
| If an IP address generates many **"rare" queries**, ask it to solve a **CAPTCHA** | Defender |
| Do not return a query's results if it contains **(a)** pages from many hosts and **(b)** a high percentage of them tagged as vulnerable | Defender |

> **The last countermeasure is the unusual one, derived.** The first two are *requester*-side: identify the client as suspicious by how it behaves, then challenge it. The fourth is **result**-side — the engine declines to answer because **the answer itself would be a target list**, regardless of who asked. That is a different and stronger idea: it does not require detecting the attacker at all, and it survives an attacker who distributes queries across many innocent-looking clients, which is precisely what taking search terms from a botmaster achieves.
>
> It generalizes past worms. Any service that aggregates information can be asked a question whose *answer* is dangerous even when the *question* is not, and filtering on the response is sometimes the only point where that is visible.

## What Makes Search Worms Structurally Different

Every other worm in the lecture is a problem for the owners of the vulnerable machines. A search worm routes its reconnaissance through **one intermediary**, which means a single party sees the entire population's targeting behaviour at once and can act on it unilaterally.

That is the same **centralized-versus-distributed** trade [[Botnets]] makes explicit: routing through one point buys the attacker enormous reach and hands the defender a vantage point they would otherwise never have. Santy's reply — take the search terms from the botmaster instead of generating them — is the attacker moving back toward distribution to close that view.

## See Also

- [[Notable Worms]]
- [[Worms]]
- [[Botnets]]
- [[Malware]]
- [[Computer Viruses]]
- [[HTTP]]
- [[CSCE 465]]
