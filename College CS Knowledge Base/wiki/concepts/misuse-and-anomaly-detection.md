---
title: "Misuse and Anomaly Detection"
type: concept
tags: [csce465, security, intrusion-detection, misuse-detection, anomaly-detection, signatures, false-positives]
sources: [csce465-lecture-14-intrusion-detection-system]
course: CSCE 465
updated: 2026-11-16
---

**Misuse detection** and **anomaly detection** are the two ways an [[Intrusion Detection Systems|intrusion detection system]] can decide that something is an attack. One knows what attacks look like; the other knows what normal looks like. [[CSCE 465]] introduces them as the two *analysis approaches* — the ways of *piecing the evidences together* — and gives each one slide and one sentence of weakness.

## Misuse Detection

Also called **signature-based** detection; the lecture's examples are **Snort** and **Bro**.

```
   Intrusion Patterns  ---->  pattern matching  ---->  intrusion
                                     ^
                                     |
                                 activities
```

Observed activity is matched against a store of known intrusion patterns, and a match is an intrusion. The slide's example rule:

> **if** (src_ip == dst_ip) **then** "land attack"

and its verdict:

> **Can't detect new attacks.**

> **About the example, derived.** A *land attack* is a packet whose source address has been [[IP Spoofing|forged]] to equal its destination address. The slide does not explain it; the point of choosing it is that the rule is one comparison on two header fields, which is as cheap and as certain as a signature gets. No legitimate packet has that property, so the rule never fires by mistake — and it also only ever catches that one thing.

## Anomaly Detection

The lecture's example of the approach is *statistical-based*.

The slide is a bar chart: a monitored system produces **activity measures** (the axis labels that survive are *CPU* and *Process Size*), and each measure is drawn twice, as its **normal profile** and as the **abnormal** value just observed. The normal bars sit at roughly 20 to 45; the abnormal ones at roughly 43 to 90. The output arrow is labelled **probable intrusion**.

> **Relatively high false positive rate — anomalies can just be new normal activities.**

So the method is: build a profile of normal behaviour, measure current behaviour, and raise an alarm when the two are far apart. Note the word *probable*. A misuse detector says *this is attack X*; an anomaly detector can only say *this is unusual*.

## Side by Side

| | Misuse detection | Anomaly detection |
|---|---|---|
| What is modelled | Known attacks — *intrusion patterns* | Normal behaviour — the *normal profile* |
| Alarm when | Activity **matches** a pattern | Activity **deviates** from the profile |
| Stated weakness | *Can't detect new attacks* | *Relatively high false positive rate* |
| Lecture's examples | Snort, Bro; the land-attack rule | Statistical-based; Forrest's system-call sequences |
| What an alarm says | Which attack | Only that something is unusual |

> **The weaknesses are mirror images, derived.** Each approach fails on exactly what it has no model of. Misuse detection has no model of the unknown attack, so it misses it — a **false negative**. Anomaly detection has no model of the unknown *normal*, so it flags it — a **false positive**. In the terms of [[IDS Performance Metrics]], one approach starts from a low false-alarm rate and gives up detection of the new; the other starts from being able to detect the new and pays in false alarms. The [[Base-Rate Fallacy]] says which price is harder to live with.

## Hand-Coded or Learned

The same slide lists a separate choice under *development and maintenance*:

> - Hand-coding of **"expert knowledge"**
> - **Learning** based on audit data

This is independent of the misuse/anomaly split. A signature can be written by an analyst or generated automatically; a normal profile can be a hand-set threshold or a model fitted to a training period. [[Host-Based Intrusion Detection|Forrest's system]] is anomaly detection with a learned profile.

## The Same Split Elsewhere in the Course

The pair is not new in Lecture 14. It has appeared four times already under other names.

- **Antivirus.** [[Computer Viruses]] gives four generations of scanner. The first, *simple scanners using signatures of known viruses*, is misuse detection; the later activity- and behaviour-based ones are the move toward anomaly detection.
- **Worms.** [[Notable Worms|Nimda]] beat signature defences by being new, and the lecture named the gap: a worm's *signature is not extracted until minutes or hours later*. That is *can't detect new attacks* with a clock on it. The *automatic signature generation* on [[Worms]] is an attempt to shorten it.
- **Search worms.** [[Search Worms]] records Google's *anomaly detection* cutting off worm queries, and the attackers' reply of varying the search terms from one variant to the next so that no fixed pattern matches.
- **ARP.** [[ARP Poisoning|Arpwatch]] keeps a table of IP/MAC pairs and raises an alarm when one changes — a one-rule anomaly detector.

## See Also

- [[Intrusion Detection Systems]]
- [[IDS Performance Metrics]]
- [[Base-Rate Fallacy]]
- [[Host-Based Intrusion Detection]]
- [[Network Intrusion Detection]]
- [[Computer Viruses]]
- [[Worms]]
- [[Search Worms]]
- [[IP Spoofing]]
- [[CSCE 465]]
