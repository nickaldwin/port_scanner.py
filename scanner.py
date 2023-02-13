import socket

def scan_ports(host, start, end):
    open_ports = []
    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

host = input("Enter the host to scan: ")
start = int(input("Enter the start port: "))
end = int(input("Enter the end port: "))

open_ports = scan_ports(host, start, end)
if len(open_ports) > 0:
    print("Open ports:", open_ports)
else:
    print("No open ports found.")
