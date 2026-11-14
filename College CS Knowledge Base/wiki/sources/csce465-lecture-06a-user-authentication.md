---
title: "CSCE 465 Lecture 6a — User Authentication"
type: source
tags: [csce465, authentication, passwords, biometrics, s-key, tokens]
sources: []
course: CSCE 465
updated: 2026-10-08
---

Lecture 6a of [[CSCE 465]] (`raw/CSCE465_06a_AuthenticationUser.pdf`, 23 PDF pages laid out two slides per page ≈ 46 logical slides, instructor [[Guofei Gu]]). **The first lecture after the cryptography unit**, and a change of subject: the thing being verified is a *person*, not a bitstring. Roadmap: *basic concept, password authentication, the S/Key protocol, biometrics, authentication hardware*.

**Numbering note:** the deck is labelled **06a**, which implies a 06b, and there is no Lecture 6 in the KB. Per the course outline the authentication unit also covers *"authentication and security handshake pitfalls"*, so a 6b on protocols and handshakes is the likely companion. Flagged as an open gap rather than assumed.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–9 | **Basic concept** | Authentication vs identification; the four bases; password-, address-, and crypto-based authentication |
| 10–28 | **Password authentication** | Storage via one-way function; brute-force arithmetic and the password study; the three dictionary attacks; salt and whether it helps; Unix; guidelines; other attacks |
| 29–34 | **S/Key** | Disposable passwords; chain generation; authentication; two limitations including the relay attack |
| 35–40 | **Biometrics** | Six desired qualities; assessment; technologies; multifactor arithmetic |
| 41–46 | **Tokens** | Passive vs active; design issues; time-synchronized tokens; the Aladdin eToken; summary |

## Pages Derived

| Page | Type | What it holds |
|---|---|---|
| [[User Authentication]] | concept | Definition, identification vs authentication, the four bases, address- and crypto-based |
| [[Password Authentication]] | concept | Storage, the password study, three dictionary attacks, salt analysed per attack, guidelines, other attacks |
| [[S/Key Protocol]] | algorithm | Chain generation and spending, the dictionary-attack question, both limitations |
| [[Biometrics]] | concept | Six qualities, privacy, technologies, the multifactor formulas worked out |
| [[Authentication Tokens]] | concept | Passive vs active, design issues, time-synchronized tokens, the eToken spec |

## Content Worth Keeping

**Identification is a search; authentication is a comparison.** Identification checks against *all* known entities and must be unique; authentication checks against *one previously identified* entity and need not be. The 1-to-N versus 1-to-1 difference is why a biometric good enough to authenticate can be useless to identify. → [[User Authentication]]

**Four bases, and the right answer is to combine them.** Know / where / are / have. The lecture asks which is best and *best in what way* — the axes genuinely conflict, and factors from *different* bases fail independently. → [[User Authentication]]

**Address-based authentication has no authentication.** `/etc/hosts.equiv`, `.rhosts`, the Berkeley rtools — and source addresses are unauthenticated by design. → [[User Authentication]]

**The password key space is enormous and almost entirely unoccupied.** 10¹⁸ possibilities and 320,000 years of brute force, versus a study where **86% were easily guessed**. Same lesson as mono-alphabetic ciphers: a large key space is necessary but not sufficient. → [[Password Authentication]]

**Three dictionary attacks, and salt only stops one of them.** Online guessing is unaffected; per-file offline attack costs the same against a single chosen target; **precomputation is what salt destroys**. The lecture's own phrasing is honest — *"a bit more difficult."* → [[Password Authentication]]

**S/Key walks the hash chain forwards to build and backwards to spend.** The server holds `x_i`, verifies `x_{i-1}`, and cannot produce it. → [[S/Key Protocol]]

**S/Key does not authenticate the server**, and the relay attack is man-in-the-middle in its purest form: the fake server gets Alice to do the one computation it cannot. → [[S/Key Protocol]]

**Passwords are exact; biometrics are statistical.** That single difference is why biometric matching has error *rates*, and it propagates into every other weakness. Biometrics are also **not revocable**. → [[Biometrics]]

**The multifactor formulas are a caution, not a recommendation.** With TP = AND and FP = OR, **both** rates get worse — combining helps only if combined the right way around. → [[Biometrics]]

**Passive tokens can be cloned by reading them; active tokens cannot.** The processor is the whole security difference. → [[Authentication Tokens]]

## The Lecture's Summary

1. Passwords are **by far the most widely used** form of authentication, despite numerous problems
2. Biometrics **hold promise but are expensive, inconvenient, and compromise privacy**
3. **Two factor authentication** is commonly used for higher security
4. **One-time passwords (S/Key) are attractive, especially if combined with hardware**

## Open Questions the Lecture Poses

| Question | Answered on |
|---|---|
| Which basis is best? *Best in what way?* | [[User Authentication]] |
| Address-based authentication: *benefits?* | [[User Authentication]] |
| What makes a good password? Where is it stored? How is it verified? | [[Password Authentication]] |
| Does password salt help — against **attack 1**? **attack 2**? **attack 3**? | [[Password Authentication]] — no, barely, yes |
| S/Key: *is a dictionary attack still possible?* | [[S/Key Protocol]] — yes, against the master password |
| Biometrics: *which desired qualities are concerns for passwords?* | [[Biometrics]] |

## Connection to Earlier Material

The crypto unit supplies the machinery this lecture assumes. [[Hash Functions|One-way functions]] are what make password storage and the whole S/Key chain work. The **challenge-response** pattern appeared twice already — as `H(R|K)` in [[Hash Function Applications]] and as RSA [[Public Key Cryptography|user authentication]] — and this lecture names it as the general crypto-based approach. [[Security Services]] listed authentication as a service; this is the user-facing half of it, where [[Digital Signatures]] and [[Message Authentication Code|MACs]] were the message-facing half.

And the closing move is the familiar one: the attacks that defeat strong passwords — keylogging, trojan login prompts, MITM, phishing — are not cryptographic. [[Cryptography|"Cryptography is rarely the weakest link"]], again.

## Extraction Note

Text extracted with PyMuPDF. Superscripts flattened as usual (`10¹⁸` appears as `1018`, `2ⁿ` as `2n`); corrected on the derived pages.

**Two genuine visual gaps:**
- Slide 39, *"The Scorecard From One Study"* — a comparison of biometric technologies, image-only. **The ratings are not recoverable.**
- The dictionary-attack and salt slides (17–25) are diagram-driven; the attack mechanics are stated in the bullets and survive, but the per-attack salt answers are conveyed *by the diagrams alone* and were derived rather than read.

The S/Key chain figure and the Aladdin eToken specification table both extracted cleanly.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[User Authentication]]
- [[Password Authentication]]
- [[S/Key Protocol]]
- [[Biometrics]]
- [[Authentication Tokens]]
- [[CSCE 465 Lecture 5 — Public Key Cryptography]]
- [[Hash Function Applications]]
- [[Classical Ciphers]]
- [[Diffie-Hellman Key Exchange]]
