---
title: "Public Key Infrastructure"
type: concept
tags: [csce465, security, cryptography, pki, certificates, ca, revocation]
sources: [csce465-lecture-05-public-key-cryptography, csce465-lecture-04-hash-functions]
course: CSCE 465
updated: 2026-10-01
---

**PKI is, informally, the infrastructure supporting the use of [[Public Key Cryptography|public key cryptography]].** It exists because public key crypto solves key *secrecy* but not key *authenticity*: a public key is useless if you cannot tell whose it is. Every attack in this unit that survives good mathematics — [[Diffie-Hellman Key Exchange|DH man-in-the-middle]], phone-book substitution — is an authenticity failure, and PKI is the answer [[CSCE 465]] gives.

A PKI consists of:

- A **Certificate Authority (CA)**
- **Certificates**
- A **repository** for retrieving certificates
- A method of **revoking** certificates
- A method of **evaluating a chain** of certificates from known public keys to the target name

## Certification Authorities

> A CA is a **trusted node that maintains the public keys for all nodes.** Each node maintains its own private key.

The scaling property is the point:

> If a new node is inserted in the network, **only that new node and the CA** need to be configured with the public key for that node.

Without a CA, adding one node to an *n*-node network means updating *n* configurations. With one, it means updating one. The CA converts an O(n²) key-distribution problem into an O(n) one by making everyone trust a single point.

## Certificates

> A **certificate is a signed message vouching that a particular name goes with a particular public key.**

The lecture's notation, where `[...]X` means "signed by X":

```
1.  [Alice's public key is 876234]carol

2.  [Carol's public key is 676554]Ted  &  [Alice's public key is 876234]carol
```

Line 1 is a single certificate. **Line 2 is a chain** — if you know Ted's key, you learn Carol's; knowing Carol's, you learn Alice's. That is the "evaluating a chain of certificates from known public keys to the target name" bullet, and it is how trust reaches names you have never heard of from a small set of roots you have.

Knowing the CA's public key, users can verify the certificate and authenticate Alice's public key.

**Practical properties:**
- Certificates can hold an **expiration date and time**
- Alice keeps the same certificate as long as she has the same public key and it has not expired
- Alice can **append the certificate to her messages** so others know her public key for sure

## CA Advantages

The lecture lists three, the first as a question:

**1. The CA does not need to be online. [Why?]**

> **Derived.** A certificate is a *signed statement*, complete in itself. Verification requires only the certificate and the CA's public key — both of which the verifier already has. Nothing in the check is a query to the CA. This makes the CA an offline, air-gappable machine, which is exactly what you want for the most security-critical private key in the system.

**2. If a CA crashes**, nodes that already have their certificates can still operate. (The same property from the availability side — the CA is not on the critical path.)

**3. Certificates are not security sensitive** in terms of confidentiality. They are meant to be published; there is nothing in one to keep secret.

The lecture then poses two questions that test whether that third claim is understood:

**Can a compromised CA decrypt a conversation between two parties?**

> **Derived: no** — not retroactively, and not passively. The CA never holds anyone's private key; it only signs statements about public keys. A recorded conversation stays secret.

**Can a compromised CA fool Alice into accepting an incorrect public key for Bob, and then impersonate Bob to Alice?**

> **Derived: yes.** The CA can sign "Bob's public key is *(the attacker's key)*" and Alice will accept it, because the signature is valid. This is the [[Diffie-Hellman Key Exchange|man-in-the-middle attack]] again, now authorized by the entity everyone trusts.
>
> The pair of answers is the real lesson: **a compromised CA cannot read the past, but it owns the future.** Trust in a PKI is not distributed — it is concentrated in the CA, which is [[Security Design Principles|least common mechanism]] deliberately violated for the sake of scalability. The system buys O(n) key distribution by accepting a single point of total failure.

## CA Problems and Revocation

**What if Alice is given a certificate with an expiration time and then is revoked (fired) from the system?**

- Alice **can still use her certificate** until the expiration time passes
- *What kind of harm can this do?* — Alice can still exchange messages with Bob using her unexpired certificate

> **Derived.** A certificate is an offline, self-contained assertion — the property that made the CA offline-capable is exactly the property that makes revocation hard. Nothing consults the CA at verification time, so nothing learns that the CA changed its mind. Expiration times are *typically in the order of months*, which is far too long to wait when a key is compromised or an employee is dismissed.

Real reasons a certificate needs revoking, per the lecture: **someone is fired, someone graduated, someone's certificate (card) is stolen.**

**Solution: a Certificate Revocation List (CRL)** maintained at the CA. A CRL is **issued periodically** and contains all revoked certificates; each transaction is checked against it.

**A certificate is valid if and only if:**
1. It has a **valid CA signature**
2. It has **not expired**
3. It is **not listed in the CA's CRL**

Note what the CRL costs: verifiers must now obtain a reasonably fresh list, which partially gives back the offline property that was advantage #1. The gap between "revoked" and "everyone knows it is revoked" is the CRL's publication period, and that window is a permanent structural weakness of the design.

## Real-World Attack on a CA

The lecture closes on the **Comodo** incident. Nine fraudulently issued certificates covering:

`mail.google.com` · `www.google.com` · `login.yahoo.com` · `login.skype.com` · `login.live.com` · `addons.mozilla.org` · "global trustee"

> **The master CA private keys in its Hardware Security Modules (HSMs) were not compromised.**

That sentence is the whole case study. The cryptography held perfectly — the HSMs did their job, the root keys never leaked. The attacker obtained the ability to *request* certificates and the CA signed them correctly. A valid signature on a false statement is indistinguishable from a valid signature on a true one.

This is the second confirmed instance in the course of [[Cryptography|"cryptography is rarely the weakest link"]], after [[Content Scrambling System|CSS]] — and a cleaner one, because here the cryptography was not even weak. The failure was in *authorization and process* around an intact cryptographic core, and the targets were the login pages of every major service at once.

The lecture ends with two words: **"The future?"**

## A Third Way to Break a CA: the Hash

Comodo was broken by process. A CA can also be broken **at the hash layer** without any process failure: in 2005 two X.509 certificates with different public keys and the **same [[MD5]] hash** were constructed, so a CA signature over one validates the other. The CA behaves perfectly, the signature verifies, and the binding is still false — because a [[Digital Signatures\|signature]] covers `H(m)`, not `m`. See [[Birthday Attack]] for why collision resistance is the property that matters here.

## See Also

- [[Public Key Cryptography]]
- [[Digital Signatures]]
- [[RSA]]
- [[Diffie-Hellman Key Exchange]]
- [[Security Design Principles]]
- [[MD5]]
- [[Hash Functions]]
- [[Content Scrambling System]]
- [[Cryptography]]
- [[CSCE 465]]
- [[Stuxnet]]
