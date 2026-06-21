#!/usr/bin/env python3
"""sockets_demo.py — feel TCP vs UDP by running real sockets.

TCP = connection-oriented, reliable, ordered (a phone call).
UDP = connectionless, fire-and-forget, may drop/reorder (a postcard).

Run a server in one shell and a client in another:

    # TCP (reliable stream)
    python3 sockets_demo.py tcp-server          # shell A
    python3 sockets_demo.py tcp-client hello     # shell B  -> echoed back

    # UDP (datagram, no connection)
    python3 sockets_demo.py udp-server          # shell A
    python3 sockets_demo.py udp-client hello     # shell B

Then inspect with:  ss -tlnp   (TCP listeners)   /   ss -ulnp   (UDP)
"""
import socket
import sys

HOST = "127.0.0.1"   # localhost; change to 0.0.0.0 to accept from other machines
PORT = 9000


def tcp_server():
    # SOCK_STREAM = TCP. We accept a connection, then read/echo a stream of bytes.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[tcp] listening on {HOST}:{PORT} — Ctrl-C to stop")
        while True:
            conn, addr = s.accept()                 # blocks until a client connects
            with conn:
                data = conn.recv(1024)              # read up to 1024 bytes
                print(f"[tcp] {addr} sent: {data!r}")
                conn.sendall(b"echo: " + data)      # send it back


def tcp_client(msg: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))                     # 3-way handshake happens here
        s.sendall(msg.encode())
        print(f"[tcp] server replied: {s.recv(1024)!r}")


def udp_server():
    # SOCK_DGRAM = UDP. No accept(), no connection — just receive datagrams.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[udp] waiting for datagrams on {HOST}:{PORT} — Ctrl-C to stop")
        while True:
            data, addr = s.recvfrom(1024)
            print(f"[udp] {addr} sent: {data!r}")
            s.sendto(b"echo: " + data, addr)


def udp_client(msg: str):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(msg.encode(), (HOST, PORT))        # no handshake — just fire it off
        s.settimeout(2)
        try:
            print(f"[udp] server replied: {s.recvfrom(1024)[0]!r}")
        except socket.timeout:
            print("[udp] no reply (this is normal for UDP — delivery isn't guaranteed)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    mode = sys.argv[1]
    msg = sys.argv[2] if len(sys.argv) > 2 else "ping"
    {
        "tcp-server": tcp_server,
        "tcp-client": lambda: tcp_client(msg),
        "udp-server": udp_server,
        "udp-client": lambda: udp_client(msg),
    }.get(mode, lambda: (print(__doc__), sys.exit(1)))()


if __name__ == "__main__":
    main()
