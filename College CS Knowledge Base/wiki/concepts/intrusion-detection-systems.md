---
title: "Intrusion Detection Systems"
type: concept
tags: [csce465, security, network-security, intrusion-detection, ids, detection, monitoring]
sources: [csce465-lecture-14-intrusion-detection-system]
course: CSCE 465
updated: 2026-11-16
---

An **intrusion detection system (IDS)** watches a system or network for attacks in progress or already done. [[CSCE 465]] starts from two definitions:

> - **Intrusion** — a set of actions aimed to compromise the security goals, namely **integrity, confidentiality, or availability**, of a computing and networking resource
> - **Intrusion detection** — the process of **identifying and responding to** intrusion activities

The first is the [[CIA Triad]] restated as a target. The second has two verbs, and the second verb matters: detection that nobody acts on is a log file.

This is the unit the course has been pointing at since Lecture 2, where [[Security Policy and Mechanism]] argued that detection is sometimes the only option and [[Security Design Principles|compromise recording]] made it a design principle.

## Why It Is Necessary

The slide is three brick walls of decreasing size, labelled **Prevent**, **Detect**, **React/Survive**, with attack arrows hitting the first, a few getting through its holes to the second, and one reaching the third. The caption:

> **Security principles: layered mechanisms**

> **Reading the picture, derived.** No wall is solid. Prevention — [[Firewalls|firewalls]], [[Access Control Models|access control]], [[Cryptography|cryptography]] — stops most attacks and has holes; detection exists for what gets through; and reaction and survival exist for what detection catches too late. These are the prevention, detection and recovery [[Computer Security|goals]] from Lecture 1 drawn as a sequence, and the lecture before this one is the first wall.

## Two Assumptions

> **Primary assumptions:**
> - System activities are **observable**
> - Normal and intrusive activities have **distinct evidence**

Everything else in the lecture rests on these, and the lecture's own list of weaknesses is the list of ways they fail.

| Assumption | How it fails | Where |
|---|---|---|
| Activities are observable | The traffic is encrypted; the monitor drops packets under load | [[Network Intrusion Detection]] |
| Activities are observable *as the target sees them* | The monitor and the end host reconstruct different data | [[Insertion and Evasion Attacks]] |
| Normal and intrusive are distinct | New normal behaviour looks anomalous; a new attack matches no pattern | [[Misuse and Anomaly Detection]] |

## Components

The lecture describes an IDS from two angles.

**Algorithmic:**

- **Features** — capture intrusion evidences
- **Models** — piece evidences together

**System architecture:** audit data processor, knowledge base, decision engine, alarm generation and responses. As a pipeline, with the slide's two annotations marking where each assumption is needed:

```
        Audit Records              <- "system activities are observable"
              |
              v
     Audit Data Preprocessor
              |  Activity Data
              v
       Detection Engine  <------ Detection Models
              |                    <- "normal and intrusive activities
              |  Alarms               have distinct evidence"
              v
        Decision Engine  <------ Decision Table
              |
              v
        Action / Report
```

The detection engine turns activity into alarms; the decision engine turns alarms into actions. Keeping those two apart is the *identifying and responding* of the definition.

## The Design Space

One slide lays out the choices, and they are three independent axes:

| Axis | Options | Page |
|---|---|---|
| **Analysis approach** | **Misuse detection** (signature-based, e.g. Snort, Bro) or **anomaly detection** (e.g. statistical-based) | [[Misuse and Anomaly Detection]] |
| **Deployment** | **Network-based** or **host-based** | [[Network Intrusion Detection]], [[Host-Based Intrusion Detection]] |
| **Development and maintenance** | **Hand-coding of "expert knowledge"** or **learning based on audit data** | — |

The two deployments have different raw material. The *Monitoring Networks and Hosts* slide names one tool for each: **`tcpdump`** for network packets, **BSM** for operating system events.

## How Good Is It?

The lecture measures an IDS by its detection rate and false positive rate, then shows why those two numbers are not enough: see [[IDS Performance Metrics]] and the [[Base-Rate Fallacy]], which is the most quantitative idea in the deck.

## Firewall and IDS

| | [[Firewalls\|Firewall]] | Network IDS |
|---|---|---|
| Role | **Active filtering** | **Passive monitoring** |
| When it fails | **Fail-close** | **Fail-open** |

The two are different layers of the same defence, not alternatives. Detail on [[Network Intrusion Detection]].

## Connection to the Instructor's Work

[[Botnets]] recorded the paper Lecture 11 closed on: *BotHunter: Detecting Malware Infection Through **IDS-Driven** Dialog Correlation* (Gu, Porras, Yegneswaran, Fong and Lee). This lecture supplies the vocabulary that title assumes. BotHunter takes the alarms of an ordinary IDS as its input and looks for the *sequence* an infection produces, which is one answer to the false-alarm problem the base-rate slide raises: any single alarm is weak evidence, a correlated chain of them is not.

## See Also

- [[Misuse and Anomaly Detection]]
- [[IDS Performance Metrics]]
- [[Base-Rate Fallacy]]
- [[Host-Based Intrusion Detection]]
- [[Network Intrusion Detection]]
- [[Insertion and Evasion Attacks]]
- [[Firewalls]]
- [[Security Policy and Mechanism]]
- [[Security Design Principles]]
- [[Computer Security]]
- [[CIA Triad]]
- [[Botnets]]
- [[Worms]]
- [[Guofei Gu]]
- [[CSCE 465]]
