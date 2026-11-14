---
title: "HTTP"
type: concept
tags: [csce465, networking, http, application-layer, web, telnet]
sources: [csce465-lecture-10-network-basics]
course: CSCE 465
updated: 2026-11-04
---

**HTTP** — Hyper Text Transfer Protocol — is the application-layer protocol of the web, and [[CSCE 465]] teaches it the useful way: by having you speak it yourself, over [[TCP]], by hand.

## The Transaction

> 1. Establish connection
> 2. **Request** — `Method <URL> <CR>`
> 3. **Response** — `Response Code <Data> <CR>`
> 4. Close connection

## Methods and Response Codes

**Common request methods:** `GET`, `PUT`, `POST`

**Response categories**, by leading digit:

| Range | Category |
|---|---|
| `100` | Informational |
| `200` | Successful |
| `300` | Redirection |
| `400` | Client Error — e.g. **404 Not Found** |
| `500` | Server Error |

## Fetching a Web Page With Telnet

The lecture's exercise, which is the whole point of the slide:

```
telnet httpforever.com 80
```

> Opens a TCP connection to **port 80** (the default HTTP server port). Anything typed in is sent to port 80.

Then type the request and **hit carriage return twice**:

```
GET /
```

> By typing this in you send this **minimal (but complete)** GET request to the http server. Look at the response message sent back.

> **Why this exercise is worth doing, derived.** It establishes that HTTP is **just text over a TCP connection** — there is no magic in the browser, and a server cannot tell a hand-typed request from a real one. Everything a client claims about itself (`User-Agent`, `Referer`, cookies, the request line) is supplied by the client and is therefore attacker-controlled input. That is the premise of the entire web security unit, and it is cheaper to learn by typing `GET /` into telnet than by reading it.

## End to End: Accessing `www.cse.tamu.edu`

The lecture's closing slide traces one page load down and back up the stack, which is the summary of the whole deck:

| Layer | Client | Router(s) | Server |
|---|---|---|---|
| Application | HTTP — `GET "http://www.cse.tamu.edu"<CR>` | — | Assemble response: `200 "" <CR> <html file in MIME format>` |
| Transport | TCP — initiate connection (handshake), package data by adding the TCP header | — | Break the response into several packets |
| Network | IP | **Relay data** | IP |
| Link | Ethernet — [[ARP]] provides IP/MAC translation | Send data to next hop | Ethernet |

Then the connection is closed with another handshake. Note again that the router implements **only the bottom two layers** — see [[Internet Protocol|IP routing]].

## See Also

- [[TCP]]
- [[SMTP]]
- [[Internet Protocol]]
- [[Computer Networking]]
- [[ARP]]
- [[Heap and Pointer Overflows]]
- [[CSCE 465]]
