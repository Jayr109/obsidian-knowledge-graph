---
title: "Computer Networking"
type: concept
tags: [csce313, networking, tcp-ip, sockets, dns, ip-addresses, osi-model]
sources: [csce313-lecture-18-introduction-to-networking]
course: CSCE 313
updated: 2026-04-10
---

Computer networking is the discipline of connecting computing devices so they can exchange data. From a systems programming perspective, the key abstractions are IP addresses (endpoint names), TCP (reliable byte streams), and the socket API (the programmer's interface to the network stack).

## The Internet Architecture

The Internet is a network of networks — a global collection of interconnected **hosts** (end systems), **routers** (forward packets), and **communication links** (fiber, copper, wireless). Applications run at the edges (hosts); the interior routes packets.

**Key functions provided by networking:**
- Name endpoints (IP addresses, DNS).
- Establish and tear down connections (TCP handshake).
- Route packets through the network (IP routing).
- Transfer data reliably (TCP) or unreliably (UDP).
- Share bandwidth fairly (TCP congestion control).
- Secure information in transit (TLS).

## Protocol Layering

Protocols are organized in layers; each layer provides services to the layer above using the layer below.

**TCP/IP Model (4 layers):**

| Layer | Protocols | Purpose |
|-------|-----------|---------|
| Application | HTTP, FTP, SMTP, DNS | End-user services |
| Transport | TCP, UDP | Process-to-process delivery |
| Network/Internet | IP | Host-to-host routing |
| Link | Ethernet, 802.11 | Single-hop delivery |

The OSI model has 7 layers (Physical, Data Link, Network, Transport, Session, Presentation, Application); TCP/IP collapses Session and Presentation into Application. For link-layer detail (Ethernet frames, MAC addresses, switches, ARP), see [[Data Link Layer]].

## IP Addresses

A 32-bit (IPv4) or 128-bit (IPv6) identifier for a network interface. Stored in **network byte order** (big-endian).

**Dotted-decimal notation:** `0x8002C2F2` = `128.2.194.242`.

**Byte order conversion:**
```c
uint32_t htonl(uint32_t);  // host → network (32-bit)
uint16_t htons(uint16_t);  // host → network (16-bit)
uint32_t ntohl(uint32_t);  // network → host (32-bit)
uint16_t ntohs(uint16_t);  // network → host (16-bit)
```

**String ↔ binary:**
```c
inet_pton(AF_INET, "128.2.194.242", &addr);  // string → binary
inet_ntop(AF_INET, &addr, buf, buflen);       // binary → string
```

## DNS

The Domain Name System (DNS) maps human-readable hostnames to IP addresses via a worldwide distributed database.

```c
struct addrinfo hints = {0};
hints.ai_family = AF_INET;
hints.ai_socktype = SOCK_STREAM;
struct addrinfo *result;
getaddrinfo("www.google.com", NULL, &hints, &result);
// result is linked list; each entry has ai_addr (sockaddr)
```

## TCP Socket API

A socket is a file descriptor representing one endpoint of a network connection. The POSIX socket API:

**Server:**
```
socket() → bind() → listen() → accept() [blocks] → recv()/send() → close(connfd)
```

**Client:**
```
socket() → connect() → send()/recv() → close()
```

**Key functions:**
```c
// Create socket
int sockfd = socket(AF_INET, SOCK_STREAM, 0);

// Bind to local address (server)
bind(sockfd, (struct sockaddr*)&server, sizeof(server));

// Put in passive mode (server)
listen(sockfd, backlog);

// Accept incoming connection (server; blocks; returns new fd)
int connfd = accept(sockfd, (struct sockaddr*)&client, &len);

// Initiate connection (client)
connect(sockfd, (struct sockaddr*)&server, sizeof(server));

// Transfer data
ssize_t send(int fd, const void *buf, size_t len, int flags);
ssize_t recv(int fd, void *buf, size_t len, int flags);

// Close
close(fd);
```

## Ports

A 16-bit port number identifies a specific process/service on a host. Combined with an IP address, it forms a **socket address** (`IP:port`). A TCP connection is uniquely identified by the 4-tuple `(client IP, client port, server IP, server port)`.

Well-known ports: 23 (Telnet), 25 (SMTP), 80 (HTTP), 443 (HTTPS).

## Client-Server Model

Most network applications use the client-server model:
1. Server is a long-running daemon (started at boot) listening on a well-known port.
2. Client connects, sends a request.
3. Server processes and sends a response.
4. Connection closed.

## Short-Count I/O

TCP `read()`/`write()`/`recv()`/`send()` may transfer fewer bytes than requested. Robust code loops:
```c
while (nleft > 0) {
    nread = read(fd, ptr, nleft);
    if (nread <= 0) break;
    nleft -= nread; ptr += nread;
}
```

## Practical Tips

- `SO_REUSEADDR`: Prevents "Address already in use" error when restarting a server quickly:
  ```c
  int opt = 1;
  setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof opt);
  ```
- Use `INADDR_ANY` for the server's IP to listen on all local interfaces.
- `htons(port)` converts the port number to network byte order before storing in `sin_port`.

## See Also

- [[Data Link Layer]]
- [[ARP]]
- [[File Descriptors]]
- [[Inter-Process Communication]]
- [[UNIX File I/O]]
- [[System Calls]]
- [[CSCE 313]]
- [[CSCE 465]] — builds network security on top of this material
