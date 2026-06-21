---
tags: [lab, m1-networking]
aliases: [m1-networking lab]
---
> [[labs/README|⬅ Labs]] | [[HOME|Home]] | [[STUDY_PLAN|Plan]]

# Module 1 — Networking, ports & protocols (hands-on lab)

Run inside **WSL2 Ubuntu**. Goal: understand exactly what happens between a
browser and your app — DNS → TCP → TLS → HTTP — and the tools to inspect each layer.

Install the toolkit first:
```bash
sudo apt install -y iproute2 dnsutils curl netcat-openbsd nmap nginx openssh-client
```

---

## Lab 1 — Find your IP and what's listening

```bash
ip addr                 # your interfaces & IPs. 'lo' = loopback (127.0.0.1),
                        # 'eth0' = your WSL network address (a private IP, 172.x)
ss -tlnp                # TCP (-t) Listening (-l) Numeric (-n) with PID (-p)
ss -ulnp                # same for UDP
```
**Concept — private vs public IP:** `127.0.0.1` = only this machine. `172.x/10.x/192.168.x`
= private LAN, not reachable from the internet. A public IP is internet-routable.
**Ports** are numbered doors on an IP: one process per port. Common: **22** SSH,
**80** HTTP, **443** HTTPS, **8011** your app.

---

## Lab 2 — Make a request and read the raw HTTP

```bash
python3 -m http.server 8000 &          # a throwaway server
curl -v http://localhost:8000          # -v shows the FULL exchange:
#   > GET / HTTP/1.1            <- request line + your headers
#   < HTTP/1.1 200 OK          <- status line + server headers
#   < Content-Type: text/html
kill %1
```
**`0.0.0.0` vs `127.0.0.1`:** bind to `127.0.0.1` and only this box can connect;
bind to `0.0.0.0` and *any* machine that can reach your IP can. (Cloud servers
bind `0.0.0.0`, then a firewall/security-group controls who actually gets in.)
```bash
python3 -m http.server 8000 --bind 127.0.0.1 &   # try curling from Windows: refused
```

**Status codes to know:** 2xx ok, 3xx redirect, 4xx your fault (401 unauth, 403
forbidden, 404 not found), 5xx server's fault (500, 502 bad gateway, 503).

---

## Lab 3 — DNS: name → IP

```bash
dig example.com +short        # the A record (IP)
dig +trace example.com        # watch resolution hop: root -> .com -> authoritative
nslookup example.com          # the classic tool
```
**Concept:** browsers don't know IPs; DNS translates `myapp.com` → `93.184.x.x`
before any connection happens. It's the first step of every web request.

---

## Lab 4 — Raw TCP vs UDP with netcat and the Python demo

```bash
# netcat: a manual TCP pipe. Server in one shell, client in another.
nc -l 9001              # shell A: listen
nc localhost 9001       # shell B: type lines, watch them appear in A (a TCP stream)

# UDP: add -u. No connection is established — bytes are just thrown.
nc -ul 9002             # shell A
nc -u localhost 9002    # shell B
```
Then run the annotated Python version (one shell each):
```bash
python3 sockets_demo.py tcp-server         # then in another shell:
python3 sockets_demo.py tcp-client "hi"    # -> b'echo: hi'
python3 sockets_demo.py udp-server         # then:
python3 sockets_demo.py udp-client "hi"
```
**TCP** does a handshake, guarantees order & delivery (web, SSH). **UDP** doesn't
(DNS, video, games) — faster, lossy.

---

## Lab 5 — Scan ports

```bash
python3 -m http.server 8000 &
nmap localhost            # lists open ports it finds (you'll see 8000)
kill %1
```
**A firewall / security group = an allow-list of ports.** In AWS you'll open only
22 (SSH from your IP) and maybe 443 — nothing else. nmap is how you verify.

---

## Lab 6 — SSH tunnel (reach a remote port as if it were local)

```bash
# Forward local 8080 -> a service on 8011 of a remote box, over the SSH connection:
ssh -L 8080:localhost:8011 user@remote-host
# now http://localhost:8080 on YOUR laptop hits the remote app on 8011.
```
You'll use this constantly to open a cloud worker's UI without exposing it
publicly. (No remote yet? You'll do it for real on the EC2 box in Module 3.)

---

## Lab 7 — TLS / HTTPS: inspect a certificate

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null \
  | openssl x509 -noout -subject -issuer -dates
```
**Concept:** HTTPS = HTTP inside a TLS tunnel. The handshake (1) verifies the
server's identity via a CA-signed certificate and (2) negotiates encryption keys.
That's what the padlock means. Order of a full request:
**DNS → TCP handshake → TLS handshake → HTTP request → response.**

---

## Lab 8 — nginx reverse proxy in front of your app

Use the ready-made `nginx-reverse-proxy.conf` (install steps are in its header
comments). The point: production puts nginx on :80/:443 and keeps the app on
`localhost:8011`, so the app is never exposed directly — nginx handles TLS,
timeouts, and (later) streaming the live progress bar.

```bash
python3 -m http.server 8011 &     # stand-in for your app
# ...install the conf per its header, then:
curl -v http://localhost/         # served via nginx on port 80, proxied to 8011
```

---

**Checkpoint (M1 done):** explain end-to-end what happens when you type
`https://myapp.com:443` (DNS → TCP → TLS → HTTP → response), name 5 ports, tell
TCP from UDP and a public from a private IP. Then tick the boxes in `../../PROGRESS.md`.
Next: **Module 2 — Docker.**
