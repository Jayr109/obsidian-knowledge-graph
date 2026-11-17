---
title: "CSCE 465 Lecture 13 — Firewall"
type: source
tags: [csce465, firewall, network-security, packet-filter, stateful-inspection, proxy, nat, ftp]
sources: []
course: CSCE 465
updated: 2026-11-16
---

Lecture 13 of [[CSCE 465]] (`raw/CSCE465_13_Firewall.pdf`, 17 PDF pages laid out two slides per page = **34 logical slides**, instructor [[Guofei Gu]]). The first *defence* deck of the network security unit: [[CSCE 465 Lecture 12 — Vulnerability Analysis|Lecture 12]] showed what unauthenticated protocols allow, and this one puts a checkpoint in front of them. Roadmap: *basic firewall concept; filtering firewall; proxy firewall; network address translation*.

The deck is a taxonomy with one running example. It defines four firewall types, pushes [[FTP]] through each of them, and closes with a three-slide comparison table.

## Structure

The slides carry no printed numbers, so they are numbered here by position (PDF page *p* holds slides 2*p*−1 and 2*p*).

| Slides | Section | Content |
|---|---|---|
| 3–8 | **Basic firewall concept** | Roadmap; definition and the intranet/DMZ/Internet figure; the moat analogy; what firewalls can do; what they cannot protect; the access control requirement |
| 9–14 | **Filtering firewall** | Packets checked then passed; packet filtering vs session filtering and their other names; packet filtering; session filtering and the state table figure |
| 15–18 | **The FTP example** | Active FTP; the packet-filter ACL; passive FTP; the session-filter rule base |
| 19–25 | **Proxy firewall** | Relay for connections; application gateways (three slides); circuit-level gateways; SOCKS |
| 26–30 | **Comparison** | Security, performance and service support; client modification; ICMP and fragmentation; proxying UDP/ICMP; circuit-level gateways at user level |
| 31–34 | **NAT and VPN** | Why NAT; mappings; encryption (VPNs) |

## Pages Derived

| Page | What it holds |
|---|---|
| [[Firewalls]] | Definition, the three zones, the moat analogy, can and cannot, the four-type taxonomy, the merged comparison table, VPNs |
| [[Packet Filtering]] | Per-packet stateless decisions, the ACL format, the four-line FTP example read line by line |
| [[Session Filtering]] | Decisions in the context of a connection, the state table, the two-rule FTP policy, UDP and ICMP "replies" |
| [[Proxy Firewalls]] | Application gateways, circuit-level gateways, SOCKS, and why TCP proxies well |
| [[FTP]] | Command and data channels, active vs passive mode, and what each firewall type does with it |
| [[Network Address Translation]] | Why it is used, the two mappings, and what it does and does not do for security |

[[Security Design Principles]] took content from this deck as well: the two filters' typical configurations are its fail-safe-defaults example in a real device.

## Content Worth Keeping

**A firewall enforces a policy; it is not one.** *Device that provides secure connectivity between networks… used to implement and enforce a security policy.* → [[Firewalls]]

**A moat, not a wall.** It works by forcing traffic through a controlled access point. So it cannot protect traffic that does not cross it — routing around, internal traffic — or anything at all *when misconfigured*. → [[Firewalls]]

**Filters pass packets; proxies relay connections.** That one distinction generates the whole taxonomy. → [[Firewalls]], [[Proxy Firewalls]]

**A packet filter decides per packet and saves no state**, so its typical configuration leaves ports above 1024 open, and a dynamic protocol forces *entire ranges of ports* open. → [[Packet Filtering]]

**A session filter decides once per connection and then matches the state table.** Typical configuration: *all denied unless specifically allowed*. → [[Session Filtering]]

**FTP is the test case because the server opens the data connection.** In active mode the client says `PORT 5151` and the server connects back from port 20. In passive mode the client says `PASV`, the server answers with a port, and the client connects. → [[FTP]]

**Four ACL lines against two rules.** The packet filter permits the FTP server's port 20 to reach every high port on every host; the session filter's rule base is *Local_Net → Any, ftp, accept* and *Any → Any, Any, drop*. → [[Packet Filtering]], [[Session Filtering]]

**An application gateway impersonates both sides of the connection.** Most secure, slowest, a process per connection, a new proxy for every protocol — *not trivial!* → [[Proxy Firewalls]]

**A circuit-level gateway supports more services with less control over data**, finds FTP hard, and protects against fragmentation. → [[Proxy Firewalls]]

**The comparison is one trade-off.** Security 3/2/2/1 against performance 1/2/3/4, lower is better. → [[Firewalls]]

**UDP and ICMP are harder to proxy because each packet is a separate transaction.** → [[Proxy Firewalls]]

**Only services that outsiders originate connections to need real IP addresses.** → [[Network Address Translation]]

## Connection to the Rest of the KB

- **Lecture 2's firewall example has become two firewall types.** [[Security Design Principles]] illustrated fail-safe defaults with a blacklist (*deny port 23, allow port \**) and a whitelist (*allow port 80, deny port \**). The packet filter's typical configuration is the first; the session filter's is the second, and it is state that makes the second affordable.
- **Router filtering in [[IP Spoofing|Lecture 12]] is packet filtering** keyed on the source address.
- **[[Access Control Models|Lecture 7]]'s ACL and this lecture's ACL are the same idea**: an ordered list of entries naming who may do what, checked at the point of access. There the subject was a user and the object a file; here the subject is an address and port and the object is a network.
- **[[Computer Security]] already warned about this mechanism by name**: mechanisms without assurance are the normal failure mode — *the system has a firewall, and no one has checked what it enforces*. *When misconfigured* is the deck's own version.
- **[[HTTP]] and [[SMTP]] from Lecture 10 are single-connection protocols** and pass a packet filter easily; [[FTP]] is the first protocol in the course that does not.
- **The course's own [[CSCE 465|lab safety rules]] rest on NAT.** *NAT networking only, never bridged* uses the property this deck describes: the VM can reach out, and nothing outside can address it.
- **[[SYN Flooding]] reaches the firewall.** A stateful filter keeps a connection table, so the Lecture 12 attack on a server's memory applies to it as well.
- **Forward link.** [[Network Intrusion Detection|Lecture 14]] sets the firewall beside the network IDS: active and fail-close against passive and fail-open.

## Extraction Note

Text extracted with PyMuPDF and clean. The bullets, the ACL listing and both FTP step lists came through intact; the circled step numbers on the FTP slides extract as the letters `u v w x` and the arrows on the proxy slide as the digit `1` (*"Client 1 Proxy 1 Server"*), both confirmed against the rendered slides.

**The three comparison tables needed the renders.** Their cells extract as a loose column of values with the blank and merged cells lost, so which value belongs to which row cannot be recovered from text alone. Read from the rendered slides, they are merged into one table on [[Firewalls]].

**Slide 18 is image-only** — a screenshot of a firewall rule base. Its two rules were read from the render and are on [[Session Filtering]].

Three small figures were recovered by zooming: the NAT diagram's addresses (external `172.19.19.5`, internal `10.1.1.5`), the circuit-level gateway figure (outside host, outside connection, gateway, inside connection, inside host), and the VPN figure, whose labels include *Check Point VPN-1 Gateway*.

The layered-stack figures on the filtering and gateway slides are images; what each shows is described on the derived pages. The remaining pictures are decorative (a brick wall on fire, a castle moat, a firewall appliance, a coffee filter) and carry no content.

**Provenance.** The PDF's internal title is `12_Firewall` and its creation date is **2021-11-17**, where the Lecture 12 deck was created on 2026-11-06. The likeliest reading is that this deck was number 12 in an earlier offering and was renumbered when the vulnerability analysis lecture was placed before it. Lecture 12, exported this semester, prints slide numbers; this deck and Lecture 14 (exported 2024) do not. Inferred from metadata, not stated anywhere.

## Deck Oddities

- **The ACL example's server is `172.168.10.12`.** It reads like a private address, but the private block is 172.16–172.31; 172.168 is public space. Kept as written.
- **The NAT figure's *external* address is `172.19.19.5`**, which is inside that private block. Kept as written.
- **`access-list 100 in`** under `interface Ethernet 0` is schematic syntax for binding a list to a direction.
- **Slide 15** spells *acknowledges* as *acknowleges*.
- **The comparison's last two column headings, ICMP and Fragmentation, are not explained.** The reading on [[Firewalls]] is inferred from the proxy slides.
- **IPSec is named on the last slide and nowhere explained.** No VPN or IPSec material is in the KB.

## Open Gaps

- **Web security is still outstanding** from the course outline's network security row, and is the hypothesis for Lecture 15.
- **No Lecture 6, and 6a still implies a 6b.** Unchanged.
- **Homework position unchanged** — only HW1, and only its briefing deck.

## See Also

- [[CSCE 465]]
- [[Guofei Gu]]
- [[Firewalls]]
- [[Packet Filtering]]
- [[Session Filtering]]
- [[Proxy Firewalls]]
- [[FTP]]
- [[Network Address Translation]]
- [[Security Design Principles]]
- [[Access Control Models]]
- [[CSCE 465 Lecture 12 — Vulnerability Analysis]]
- [[CSCE 465 Lecture 14 — Intrusion Detection System]]
