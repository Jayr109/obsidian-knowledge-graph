---
title: "FTP"
type: concept
tags: [csce465, networking, ftp, firewall, application-protocol, active-mode, passive-mode]
sources: [csce465-lecture-13-firewall]
course: CSCE 465
updated: 2026-11-16
---

**FTP**, the File Transfer Protocol, appears in [[CSCE 465]] as the worked example of the [[Firewalls|firewall]] lecture, and it was chosen for being awkward. It uses **two connections**, and the second is arranged *inside* the first: the two sides agree on a port at run time and then one of them opens a new connection to it. The lecture calls protocols like this **dynamic**, and how a firewall copes with one is the fastest way to tell the firewall types apart.

It joins [[HTTP]] and [[SMTP]] as the third application protocol the course walks through.

## Two Channels

| Channel | Server port | Carries |
|---|---|---|
| **Command** | 21 | The client's commands and the server's answers |
| **Data** | 20 in active mode; a port the server picks in passive mode | The files |

In both of the lecture's diagrams the client uses port **5150** for the command channel and **5151** for data.

## Active Mode

```
  FTP Server                                           FTP Client
  20 (data)     21 (command)                      5150          5151
      |              |<------ (1) "PORT 5151" ------|              |
      |              |------- (2) "OK" ------------>|              |
      |------------------- (3) DATA CHANNEL ---------------------->|
      |<------------------ (4) TCP ACK ----------------------------|
```

1. **Client opens command channel to server; tells server second port number.**
2. **Server acknowledges.**
3. **Server opens data channel to client's second port.**
4. **Client acknowledges.**

Step 3 is the unusual one: the **server** starts a connection **to the client**.

## Passive Mode

```
  FTP Server                                           FTP Client
  3267 (data)   21 (command)                      5150          5151
      |              |<------ (1) "PASV" -----------|              |
      |              |------- (2) "OK 3267" ------->|              |
      |<------------------ (3) DATA CHANNEL -----------------------|
      |------------------- (4) TCP ACK --------------------------->|
```

1. **Client opens command channel to server; requests passive mode.**
2. **Server allocates port for data channel; tells client port number.**
3. **Client opens data channel to server's second port.**
4. **Server acknowledges.**

Now both connections are opened by the client.

## Who Opens What

| | Active | Passive |
|---|---|---|
| Client says | `PORT 5151` | `PASV` |
| Server answers | `OK` | `OK 3267` |
| Data connection opened by | The **server**, from port 20 | The **client** |
| Port that has to be reachable | A high port on the **client** | A high port on the **server** |

(The replies `OK` and `OK 3267` are the slide's shorthand for the server's responses.)

## Why Firewalls Hate It

> **Derived, pulling together what each slide says about FTP.** The port for the data connection is chosen while the session is running and announced **in the payload** of the command channel. A firewall that reads only headers cannot know it; a firewall that wants to know it has to understand FTP.

| Firewall type | What happens with FTP | Lecture's words |
|---|---|---|
| [[Packet Filtering\|Packet filter]] | Cannot see the `PORT` command, so it permits the server's port 20 to reach **every** port above 1023 | *Entire ranges of ports must be allowed*; *no dynamic w/o holes* |
| [[Session Filtering\|Session filter]] | Follows the command channel and opens only the negotiated port, for that session | *Allowed only if supported*; two rules instead of four |
| [[Proxy Firewalls\|Circuit-level gateway]] | Relays bytes without reading them, so it misses the announcement | *Hard to handle protocols like FTP* |
| [[Proxy Firewalls\|Application gateway]] | Runs a dedicated FTP proxy | FTP is one of the three proxies in the figure |

> **What passive mode changes.** It does not make the dynamic port go away; it moves it. In active mode the hole has to be in the firewall in front of the **client**, because that is where the unsolicited inbound connection arrives. In passive mode the client only ever connects outward, and the high port that must be reachable is on the **server**. The lecture's packet-filter example is explicitly for *"FTP (not passive FTP)"*.

## See Also

- [[Firewalls]]
- [[Packet Filtering]]
- [[Session Filtering]]
- [[Proxy Firewalls]]
- [[HTTP]]
- [[SMTP]]
- [[TCP]]
- [[Computer Networking]]
- [[CSCE 465]]
