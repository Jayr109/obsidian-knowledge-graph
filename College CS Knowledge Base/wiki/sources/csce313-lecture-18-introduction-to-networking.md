---
title: "CSCE 313 Lecture 18 — Introduction to Networking/Internet"
type: source
tags: [csce313, networking, tcp-ip, sockets, dns, ip-addresses, client-server]
sources: []
course: CSCE 313
updated: 2026-04-10
---

Lecture 18 introduces computer networking from the programmer's perspective: the Internet architecture, protocol layering (OSI and TCP/IP), IP addresses and DNS, and the POSIX socket API for TCP client-server programming. References: Kurose & Ross "Computer Networking: A Top-Down Approach" 8th ed.; Tanenbaum & Wetherall "Computer Networks."

## The Internet: Structure

The Internet is a network of networks connecting billions of computing devices (hosts/end systems). Key components:
- **Hosts** — end systems running applications at the Internet's "edge."
- **Packet switches** — routers and switches that forward packets (chunks of data).
- **Communication links** — fiber, copper, radio, satellite; characterized by **bandwidth** (transmission rate).
- **Networks** — collections of devices, routers, and links managed by an organization (ISPs, home networks, enterprise, data centers).

**What networking provides:**
- Name endpoints (addressing).
- Make/break connections.
- Route packets through the network.
- Transfer information reliably (TCP) or unreliably (UDP).
- Handle arbitrary-length messages.
- Share bandwidth fairly.
- Secure information in transit.

## Protocol Layering

A **protocol** defines the format and order of messages and the actions taken on send/receive. Layers encapsulate protocols, with each layer providing services to the layer above and using services of the layer below.

**OSI 7-layer model:** Physical, Data Link, Network, Transport, Session, Presentation, Application. (Diagram-only slide — visual.)

**TCP/IP model (4 layers):**
| Layer | Examples |
|-------|----------|
| Application | HTTP, FTP, SMTP, DNS |
| Transport | TCP, UDP |
| Network/Internet | IP |
| Link | Ethernet, 802.11 (Wi-Fi) |

TCP/IP layers loosely align with the OSI model.

## Client-Server Model

Most network applications use the client-server model:
1. Client sends a request.
2. Server handles the request (manages a resource).
3. Server sends a response.
4. Client handles the response.

Both client and server are **processes** running on hosts (possibly the same machine).

## IP Addresses

IPv4 addresses are 32-bit unsigned integers, stored in **network byte order** (big-endian — most significant byte first).

```c
struct in_addr {
    in_addr_t s_addr;  /* network byte order (big-endian) */
};
```

**Byte order conversion functions:**
```c
uint32_t htonl(uint32_t hostlong);   // host → network (32-bit)
uint16_t htons(uint16_t hostshort);  // host → network (16-bit)
uint32_t ntohl(uint32_t netlong);    // network → host (32-bit)
uint16_t ntohs(uint16_t netshort);   // network → host (16-bit)
```

**Dotted-decimal notation:** `0x8002C2F2` = `128.2.194.242` (each byte as decimal, separated by `.`).

```c
inet_pton(AF_INET, "128.2.194.242", &addr.sin_addr); // string → binary
char buf[INET_ADDRSTRLEN];
inet_ntop(AF_INET, &addr.sin_addr, buf, sizeof buf);  // binary → string
```

## Domain Name System (DNS)

DNS maps human-readable domain names to IP addresses via a worldwide distributed database.

```c
#include <netdb.h>
struct addrinfo *result, hints;
memset(&hints, 0, sizeof hints);
hints.ai_family = AF_INET;         // IPv4
hints.ai_socktype = SOCK_STREAM;   // TCP
getaddrinfo("www.google.com", NULL, &hints, &result);
// result is a linked list of struct addrinfo
```

`struct addrinfo` fields: `ai_family`, `ai_socktype`, `ai_protocol`, `ai_addrlen`, `ai_addr` (→ `sockaddr`), `ai_canonname`, `ai_next`.

`getnameinfo()` performs the reverse mapping (IP → name).

## Socket Address Structures

```c
struct sockaddr {          // base type
    sa_family_t sa_family;
    char sa_data[14];
};

struct sockaddr_in {       // IPv4 specific
    short sin_family;           // AF_INET
    unsigned short sin_port;    // port number (network byte order)
    struct in_addr sin_addr;    // 32-bit IP address
    char sin_zero[8];           // padding
};
```

## TCP Socket API (POSIX)

A socket is a file descriptor representing a network endpoint.

```c
int socket(int family, int type, int protocol);
// family: AF_INET (IPv4), AF_INET6 (IPv6)
// type: SOCK_STREAM (TCP), SOCK_DGRAM (UDP)
// protocol: typically 0
// Returns fd, or -1 on error.

int bind(int sockfd, struct sockaddr *myaddr, socklen_t addrlen);
// Assign local IP + port to socket.
// IP = INADDR_ANY → all local addresses; port = 0 → kernel assigns.

int listen(int sockfd, int backlog);
// Put socket in passive state; backlog = queue length for unaccepted connections.

int accept(int sockfd, struct sockaddr *cliaddr, socklen_t *addrlen);
// Block until a client connects; returns new connected socket fd.

int connect(int sockfd, struct sockaddr *servaddr, socklen_t addrlen);
// Client: initiate connection to server.
```

**Data transfer (TCP):**
```c
ssize_t send(int sockfd, const void *buf, size_t len, int flags);
ssize_t recv(int sockfd, void *buf, size_t len, int flags);
// (or use write/read — same semantics for SOCK_STREAM)
```

**Server flow:** `socket()` → `bind()` → `listen()` → loop: `accept()` → `recv()`/`send()` → `close(connfd)`.  
**Client flow:** `socket()` → `connect()` → `send()`/`recv()` → `close()`.

**setsockopt:** Avoid "Address already in use" error after restart:
```c
int optval = 1;
setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof optval);
```

## Ports

A port (16-bit) identifies a service on a host. Well-known ports:
| Port | Service |
|------|---------|
| 23 | Telnet |
| 25 | SMTP (mail) |
| 80 | HTTP |
| 443 | HTTPS |

A connection is identified by the 4-tuple: `(client IP, client port, server IP, server port)`.

## Connection Lifecycle (TCP)

```
Server:  socket → bind → listen → accept (blocks)
Client:              socket → connect (sends SYN)
Server: accept returns → read/write data
Client: sends data via write/send
Server: echoes back
Both: close → FIN/ACK exchange
```

## Short-Count I/O

`read()`/`write()` on sockets may transfer fewer bytes than requested (network buffering). Robust programs loop:
```c
ssize_t writen(int fd, const void *ptr, size_t n) {
    size_t nleft = n;
    while (nleft > 0) {
        ssize_t nwritten = write(fd, ptr, nleft);
        if (nwritten <= 0) break;
        nleft -= nwritten; ptr += nwritten;
    }
    return n - nleft;
}
```

## Visual Slides

Routing and forwarding diagrams (slides p7–p8), OSI model table (slide p10), IP datagram header layout (slide p16), TCP header (slide p17), and DNS hierarchy tree (slide p22) were visual-only or minimally captured.

## See Also

- [[Computer Networking]]
- [[UNIX File I/O]]
- [[File Descriptors]]
- [[CSCE 313]]
