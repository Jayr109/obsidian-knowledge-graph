---
title: "Chinese Wall Model"
type: concept
tags: [csce465, security, chinese-wall, conflict-of-interest, hybrid-policy, commercial]
sources: [csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

The **Chinese Wall model** is a **hybrid policy** — it refers equally to confidentiality and integrity — and it is the only model in [[CSCE 465]]'s security-theory lecture whose permissions **change as the subject acts**. It targets **conflict of interest**, the commercial problem that [[Bell-LaPadula Model|BLP]] and [[Biba Integrity Model|Biba]] cannot express, because the thing being protected is not a level but a *history*.

## The Problem

> - Tony advises American Bank about investments
> - He is asked to advise Toyland Bank about investments
> - **Conflict of interest** to accept, because his advice for either bank would affect his advice to the other

Nothing here is a clearance question. Tony is cleared for both banks' data; the issue is that holding both at once is itself the violation. No static label can encode that, because whether Tony may read Toyland's file depends entirely on **what he has already read**.

## Organization

> - Organize entities into **"conflict of interest" classes**
> - Control subject accesses to each class
> - Control **writing** to all classes to ensure information is not passed along in violation of rules
> - Allow **sanitized** data to be viewed by everyone

## Definitions

- The **objects** are items of information related to a company
- A **company dataset (CD)** contains objects related to a single company
- A **conflict of interest (COI) class** contains the datasets of companies **in competition**
- **CD(O)** — the company dataset containing object *O*; **COI(O)** — the COI class containing object *O*

The lecture's example, two COI classes:

| COI class | Company datasets |
|---|---|
| **Bank** | Bank of America, Citibank, Bank of the West |
| **Gasoline Company** | Shell Oil, Union '76, Standard Oil, ARCO |

A consultant may advise one bank and one oil company — those are different COI classes. Two banks is the violation.

## CW-Simple Security Condition

> If Anthony reads any CD in a COI, he can **never** read another CD in that COI — it is possible that information learned earlier may allow him to make decisions later.

Formally, *s* can read *o* if and only if **any** of the following holds:

1. There is an object *o′* such that *s* has accessed *o′* and `CD(o′) = CD(o)` — *s* is already inside this company's dataset
2. For all objects *o′* in `PR(s)`, `COI(o′) ≠ COI(o)` — *s* has read nothing in this conflict class
3. *o* is a **sanitized** object

where `PR(s)` is the **set of objects *s* has read**.

> **The model has state, derived.** `PR(s)` is the whole difference from every other model in the lecture. BLP's matrix cell is a pure function of two labels, so the same request always gets the same answer; Chinese Wall's depends on the subject's access history, so **permissions shrink irreversibly as the subject works**. On day one every CD is readable; after one read, an entire COI class closes forever. That also means the model cannot be enforced by a stateless reference monitor — the system has to remember, per subject, everything ever read.

## Writing, and Why a Second Rule Is Needed

The read rule alone leaks through a shared dataset:

> - Anthony and Susan work in the same trading house
> - Anthony can read Bank 1's CD and Gas' CD
> - Susan can read Bank 2's CD and Gas' CD
> - If Anthony could write to Gas' CD, **Susan can read it** — hence, indirectly, she can read information from Bank 1's CD, a clear conflict of interest

Both subjects individually satisfy CW-simple. The violation is built out of two legal accesses plus a shared object, which is the same structural lesson as BLP's [[Bell-LaPadula Model|\*-property]]: a read rule without a matching write rule only stops the *direct* path.

## CW-*-Property

> *s* can write to *o* iff **both** of the following hold:
>
> 1. The CW-simple security condition permits *s* to read *o*; **and**
> 2. For all unsanitized objects *o′*, if *s* can read *o′*, then `CD(o′) = CD(o)`
>
> Says that *s* can write to an object if **all** the (unsanitized) objects it can read are in the **same dataset**.

This is severe. Anthony, who can read both Bank 1's CD and Gas' CD, may write to **neither** — the moment he holds unsanitized data from two datasets, every write is blocked. Writing requires having confined yourself to a single company's data.

> **Which is why sanitization is load-bearing, derived.** Without it the model grinds to a halt: any consultant useful enough to work two accounts is forbidden to write anything at all. Sanitized objects — aggregated or anonymized so they no longer carry a single company's information — are exempt from both rules, and they are the only way analysis ever gets published. The model therefore relies on a step it does not itself specify: deciding when data has been sanitized *enough* is a human judgment outside the formalism, and it is where real Chinese Walls fail.

## See Also

- [[Security Models]]
- [[Bell-LaPadula Model]]
- [[Biba Integrity Model]]
- [[Role-Based Access Control]]
- [[Access Control Matrix]]
- [[Access Control Models]]
- [[CIA Triad]]
- [[CSCE 465]]
