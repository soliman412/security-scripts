import socket

def check_port(host, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        s.close()

if __name__ == "__main__":
    for port in [22, 80, 443, 8080]:
        status = "open" if check_port("127.0.0.1", port) else "closed"
        print(f"Port {port}: {status}")