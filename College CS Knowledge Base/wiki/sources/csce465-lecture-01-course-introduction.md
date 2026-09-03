---
title: "CSCE 465 Lecture 1 — Course Introduction"
type: source
tags: [csce465, introduction, security, logistics, foundations]
sources: []
course: CSCE 465
updated: 2026-08-27
---

Lecture 1 of [[CSCE 465]] (`raw/CSCE465_01_courseIntro.2026.pdf`, 20 PDF pages laid out two slides per page = 39 logical slides, instructor [[Guofei Gu]]). This is the framing and logistics lecture. Roughly two thirds of it is course administration — outline, grading, homework, project ideas — and one third is real content: the definition of security, the goals of security, and the [[CIA Triad]]. No mechanisms are introduced yet; the cryptography, OS, and network units start later.

## Structure

| Slides | Content |
|---|---|
| 1–4 | Instructor and SUCCESS Lab; "about you" discussion prompts |
| 5–9 | Why this course: incident volume and the named threat list |
| 10–18 | **Image-only** — news headlines, incident screenshots, botnet diagram (slide 15) |
| 19–21 | What is security; goals of security; components of security |
| 22–26 | Course objectives, styles, outline, prerequisites |
| 27–30 | Textbooks, resources, grading, homework/labs |
| 31–32 | How to succeed; ethics and academic integrity |
| 33–39 | Mini-research project: rules, prior examples, idea list |

## Content Worth Keeping

**The definition.** Security is the prevention of certain intentional actions. Threats are potential actions; attacks are threats carried out; attackers carry them out; assets are what they are aimed at. → [[Computer Security]]

**Four goals.** Prevention, detection, recovery, survivability — only the first assumes defense works, which is why the course spends a full unit on intrusion detection. → [[Computer Security]]

**Three components.** Confidentiality, integrity, availability, with integrity split into data integrity and origin integrity (= authentication). → [[CIA Triad]]

**The threat list.** Malware, spam, botnet, DDoS, phishing, ransomware, AI/agentic attacks. → [[Security Threat Landscape]]

**Course objectives as stated.** Understand the basic issues, concepts, principles, and mechanisms of information security — security goals and threats to networking infrastructure and applications, network security, system security, and an introduction to cryptography — and be able to *choose* appropriate mechanisms for protecting a given system. The second objective is the one that makes this a design course rather than a catalogue.

## Textbooks

Suggested primary text: **van Oorschot, *Computer Security and the Internet: Tools and Jewels from Malware to Bitcoin*, 2nd ed., Springer 2021** — freely available at `https://people.scs.carleton.ca/~paulv/toolsjewels.html`.

References:
- Wenliang Du, *Computer Security: A Hands-on Approach* (2017) — matches the lab-heavy structure of the homework
- Goodrich & Tamassia, *Introduction to Computer Security* (Addison-Wesley Pearson)
- Kaufman, Perlman & Speciner, *Network Security — Private Communication in a Public World*, 2nd ed. (Prentice Hall, 2002)
- *Handbook of Applied Cryptography* — free at `https://cacr.uwaterloo.ca/hac/`

Two of the five are legally free online, which is worth noting before buying anything. Others are reachable through TAMU library ebook links.

## Prior-Year Project Examples

Listed to calibrate scope, not as assignments: blockchain data inference (Bitcoin/Ethereum), webcam hacking and defense, forgery detection, phishing email detection, anti-cheat vulnerability analysis, security-education games, Bluetooth sniffing, USB attack and defense, phishing and TikTok user studies, a mouse-based trojan delivery method, GAN-based deepfake detection, offline machine attestation via smartphone, AI-powered fake news detection, adaptive phishing detection in messaging platforms, and a terminal-based SIEM. The instructor's own idea list adds social network privacy, smartphone/console security, underground economy monitoring, cloud security, cyber deception (honeypots/honeynets/honeyPatch/honeyDocument), wireless and cellular security, online game security, malware analysis, spam and phishing measurement, authentication security, web security and click fraud, SDN-based network security, botnet/ransomware detection and evasion-hardness analysis, DNS security (fast flux, scam hosting, cache poisoning), new cryptography applications, virtualization for security, DDoS attack and defense, IoT/CPS/smart grid security, and both directions of AI security.

The pattern across the list: almost every entry is *measure or build something real*, not *survey the literature*.

## Extraction Note

Text was extracted with PyMuPDF (the harness PDF reader cannot do page-ranged reads in this environment — poppler is unavailable). **Slides 7–18 carry no text layer at all** — PDF pages 4–9 contain only images, averaging 3 images per page with fewer than 15 characters of text. These are the news-headline and incident-screenshot slides that motivate the course, plus a botnet architecture diagram on slide 15. The specific incidents cited in lecture are therefore *not* recoverable from this ingest; if they matter for an exam, they need to come from lecture notes or the slides viewed directly.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Computer Security]]
- [[CIA Triad]]
- [[Security Threat Landscape]]
