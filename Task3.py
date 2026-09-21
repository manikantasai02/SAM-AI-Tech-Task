from datetime import datetime
import socket
import sys


def scan_ports(target_host, start_port, end_port):
    # Resolve target host to IP address
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"\n[!] Error: Hostname '{target_host}' could not be resolved.")
        return

    print("-" * 50)
    print(f"Scanning Target : {target_host} ({target_ip})")
    print(f"Port Range      : {start_port} - {end_port}")
    print(f"Scanning Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = []
    closed_ports = 0

    # Iterate through the specified port range
    for port in range(start_port, end_port + 1):
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a short timeout for fast scanning
        sock.settimeout(0.5)

        # connect_ex returns 0 if the connection succeeded (port is open)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port:5d} : OPEN")
            open_ports.append(port)
        else:
            closed_ports += 1

        sock.close()

    # Generate Scan Summary
    print("-" * 50)
    print("SCAN SUMMARY")
    print("-" * 50)
    print(f"Total Ports Scanned : {end_port - start_port + 1}")
    print(f"Open Ports Count    : {len(open_ports)}")
    print(f"Closed Ports Count  : {closed_ports}")

    if open_ports:
        print(f"Open Ports List     : {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found in the specified range.")
    print("-" * 50)


if __name__ == "__main__":
    # Get user inputs
    target = (
        input("Enter target IP or hostname (default: localhost): ").strip()
        or "localhost"
    )

    try:
        start = int(input("Enter starting port (e.g., 1): "))
        end = int(input("Enter ending port (e.g., 100): "))

        if start < 1 or end > 65535 or start > end:
            print("[!] Invalid port range! Ports must be between 1 and 65535.")
            sys.exit()

        scan_ports(target, start, end)

    except ValueError:
        print("[!] Please enter valid integer numbers for port range.")