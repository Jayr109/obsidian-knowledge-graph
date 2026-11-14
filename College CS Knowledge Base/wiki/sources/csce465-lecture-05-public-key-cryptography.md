---
title: "CSCE 465 Lecture 5 — Public Key Cryptography"
type: source
tags: [csce465, cryptography, public-key, rsa, diffie-hellman, pki]
sources: []
course: CSCE 465
updated: 2026-09-26
---

Lecture 5 of [[CSCE 465]] (`raw/CSCE465_05_PublicKeyCrypto.pdf`, 30 PDF pages laid out two slides per page ≈ 59 logical slides, instructor [[Guofei Gu]]). The other half of applied cryptography: asymmetric keys, the two algorithms that make them work, and the infrastructure needed to know whose key is whose. Roadmap: *Introduction, RSA, Diffie-Hellman Key Exchange, Public key infrastructure (PKI) and Certification Authorities (CA)*.

This picks up exactly where [[CSCE 465 Lecture 3a — Secret Key Cryptography (I)|Lecture 3a]] left off — its closing claim was that secret key crypto *requires out-of-band, bilateral key negotiation*, and this lecture is the answer to that requirement.

**Numbering note:** the deck is labelled 05 and follows 3a/3b. There is no Lecture 4 in the KB; whether it exists (hashes, per the course outline) or the numbering simply skips is unknown.

## Structure

| Slides | Section | Content |
|---|---|---|
| 3–14 | **Introduction** | Definition; five applications; the algorithm table; public-key requirements; trapdoor one-way functions |
| 15–32 | **RSA** | Key generation; the four operations; worked example; key negotiation; proof of correctness; security; four attack classes; timing attacks and blinding |
| 33–48 | **Diffie-Hellman** | Protocol; worked example; discrete log; limitations; MITM; authenticating DH; phone-book mode; encryption using DH; picking g and p |
| 49–59 | **PKI and CAs** | What PKI is; CAs; certificates and chains; CA advantages; CA problems; revocation and CRLs; the Comodo attack |

## Pages Derived

| Page | Type | What it holds |
|---|---|---|
| [[Public Key Cryptography]] | concept | Definition, five applications, algorithm table, requirements, trapdoor one-way functions |
| [[RSA]] | algorithm | Key generation, operations, worked examples, correctness proof, security, all four attack classes, blinding |
| [[Diffie-Hellman Key Exchange]] | algorithm | Protocol, examples, discrete log, MITM, authentication, phone-book mode, DH encryption, parameter rules |
| [[Digital Signatures]] | concept | Sign/verify, the key-direction table, non-repudiation |
| [[Public Key Infrastructure]] | concept | CAs, certificates, chains, advantages, revocation, CRLs, Comodo |

## Content Worth Keeping

**Signing and encrypting use opposite keys.** Sign with *your* private key; encrypt with the *recipient's* public key. In RSA they are the same exponentiation, so only the choice of key distinguishes them. → [[Digital Signatures]]

**Non-repudiation is only achievable with public key cryptography.** Stated outright — and it confirms what the KB had already derived from the symmetric side, that a MAC convinces only the other key holder. → [[Digital Signatures]], [[Security Services]]

**The design goal, in one sentence:** *find an appropriate trapdoor one-way function.* RSA and DH are two answers to one search, built on factoring and discrete log respectively. → [[Public Key Cryptography]]

**RSA's security is the hardness of factoring.** Factor `n` → compute `φ(n)` → compute `d` → you have the private key. → [[RSA]]

**RSA is deterministic, and that leaks.** The probable-message attack works by encrypting all candidate plaintexts with the public key and matching. Padding makes encryption non-deterministic — the same fix an [[Initialization Vector]] provides for block cipher modes. → [[RSA]]

**Timing attacks read the private key one bit at a time** from the repeated-squaring loop, because the conditional multiply runs only when the key bit is 1. Blinding is the only countermeasure that removes the correlation rather than adding noise, at <10% cost. → [[RSA]], [[Side-Channel Attacks]]

**DH provides no authentication** — *you can negotiate a key with a complete stranger.* Which is precisely the MITM vulnerability, stated as a feature two slides earlier. → [[Diffie-Hellman Key Exchange]]

**Authenticating DH requires an already-shared secret** — so DH cannot bootstrap trust from nothing, which is what makes PKI necessary. → [[Diffie-Hellman Key Exchange]], [[Public Key Infrastructure]]

**A CA does not need to be online**, because a certificate is a self-contained signed statement. That same property is why **revocation is hard** and why CRLs exist. → [[Public Key Infrastructure]]

**A compromised CA cannot read the past but owns the future.** It holds no private keys, so recorded traffic stays secret — but it can sign a false key binding and impersonate anyone going forward. → [[Public Key Infrastructure]]

## Worked Examples — All Verified

Every numeric example in the deck was recomputed during ingest and **all of them are correct**:

| Example | Check |
|---|---|
| RSA `p=23, q=11` | `n=253`, `φ=220`, `gcd(39,220)=1`, `d=79`, `39·79 ≡ 1 mod 220` ✓ |
| RSA encrypt / decrypt | `80^39 mod 253 = 37`; `37^79 mod 253 = 80` ✓ |
| RSA sign / verify | `80^79 mod 253 = 224`; `224^39 mod 253 = 80` ✓ |
| Key negotiation | Bob's `589 = 19·31`, `φ=540`, `23·47 ≡ 1 mod 540`; all four exchange values ✓ |
| Diffie-Hellman `p=353, g=3` | `T_A=40`, `T_B=248`, both sides reach `K=160` ✓ |
| DH encryption `<401,5,51>` | `5^17=173`, `51^17=360`, `173^58=360`, and `T_B = 5^58 mod 401 = 51` ✓ |

**One internal mismatch worth knowing.** The DH example uses `p = 353`, which satisfies the deck's own later rule `g^((p-1)/2) ≡ -1 mod p` (`3^176 mod 353 = 352`) but **violates** the rule that `(p-1)/2` be prime — `176 = 2⁴ × 11`. Toy examples are chosen for arithmetic that fits on a slide. Recorded on [[Diffie-Hellman Key Exchange]] so the mismatch does not read as an error.

## Open Questions the Lecture Poses

The pattern continues. All answered on the derived pages inside blockquotes marked as derived:

| Question | Answered on |
|---|---|
| RSA correctness: `m^(ed) = m mod n` **(why?)** | [[RSA]] — Euler's theorem, `ed = 1 + kφ(n)` |
| Timing countermeasure 1 (fixed delay) — *disadvantage: ?* | [[RSA]] — every operation pays worst-case latency |
| Timing countermeasure 2 (random delay) — *disadvantage?* | [[RSA]] — noise, not removal; averaging defeats it |
| DH: *possible timing attacks??* | [[Diffie-Hellman Key Exchange]] — yes, same modular exponentiation |
| DH MITM: **Solution???** | [[Diffie-Hellman Key Exchange]] — authenticate the messages |
| Phone-book mode: reliability of published values — *how accomplished???* | [[Diffie-Hellman Key Exchange]] — signed certificates |
| CA: *The CA does not need to be online. [Why?]* | [[Public Key Infrastructure]] — certificates are self-contained |
| *Can a compromised CA decrypt a conversation?* | [[Public Key Infrastructure]] — no |
| *Can a compromised CA impersonate Bob to Alice?* | [[Public Key Infrastructure]] — yes |
| Unexpired revoked certificate — *what kind of harm can this do?* | [[Public Key Infrastructure]] |
| Comodo: **"The future?"** | Left open; it is the closing slide |

## Connection to Earlier Material

The lecture completes the [[Cryptography Taxonomy|three-family taxonomy]] from Lecture 3 — one key, two keys, no key — by developing the two-key family that had been a map entry until now. It answers [[Secret Key Cryptography]]'s closing limitation, and it confirms a claim the KB had derived rather than read: that non-repudiation is unavailable symmetrically.

It also supplies the course's **second real-world post-mortem**. Where [[Content Scrambling System|CSS]] failed with weak cryptography *and* bad key management, Comodo failed with **intact** cryptography — the HSMs held, the root keys never leaked, and nine fraudulent certificates for Google, Yahoo, Skype, Live, and Mozilla were issued anyway. Together they make [[Cryptography|"cryptography is rarely the weakest link"]] concrete from both directions.

## Extraction Note

Text extracted with PyMuPDF. **No image-only slides.**

**Notation losses to be aware of:** superscript exponents are flattened throughout, so `m^e` appears as `me`, `8039 mod 253` means `80^39 mod 253`, and `f -1k(Y)` means `f_k^-1(Y)`. The Greek φ (phi) alternates between `φ` and `f` in the text layer depending on the slide. All formulas on the derived pages were reconstructed with explicit `^` and verified numerically against the deck's own answers.

**The PKCS #1 v1 padding figure** extracts as `00 | 02 | R1..R8 | data… | 00`, placing the `00` separator *after* the data. The actual standard puts it between the padding and the data. This may be a figure-ordering artifact of extraction rather than a slide error; flagged on [[RSA]] with both readings.

Several protocol diagrams (the DH exchange table, the MITM diagram, the CA network figure) extract as label lists without their arrows; the tables and diagrams on the derived pages were reconstructed from the labels plus the accompanying prose.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Public Key Cryptography]]
- [[RSA]]
- [[Diffie-Hellman Key Exchange]]
- [[Digital Signatures]]
- [[Public Key Infrastructure]]
- [[CSCE 465 Lecture 3b — Secret Key Cryptography (II): Modes of Operation]]
- [[Secret Key Cryptography]]
- [[Cipher Security Models]]
- [[Message Authentication Code]]
