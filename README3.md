# Simple TCP Port Scanner

A lightweight, concurrent-capable **Python-based TCP Port Scanner** that resolves hostnames, checks a specific range of ports, and provides a clear scan summary.

## Features
* **Hostname Resolution:** Automatically converts domain names (e.g., `localhost` or `google.com`) into target IP addresses.
* **Custom Scan Ranges:** Allows users to input exact starting and ending port limits (between `1` and `65535`).
* **Timeout Optimized:** Uses a standard `0.5` second socket connection timeout for rapid discovery.
* **Comprehensive Summary:** Outputs total scanned ports, total closed ports, and a comma-separated list of all open ports discovered.

## Prerequisites
* **Python 3.x** installed on your system.
* No external libraries are required (uses standard built-in modules: `socket`, `datetime`, and `sys`).

## How It Works
The script utilizes standard **TCP 3-Way Handshake** connection attempts (`socket.connect_ex`). 
* A return value of `0` indicates a successful handshake, meaning the target port is **OPEN**.
* Any other return value signifies that the port is **CLOSED** or filtered.

## Usage Guide

1. Run the Python script in your terminal:
   ```bash
   python port_scanner.py
   ```

2. **Provide the Target Host:** Enter an IP address or domain name when prompted. Press `Enter` without typing to default to `localhost`.
3. **Define Port Boundaries:** Input your desired starting and ending port numbers.

### Sample Execution
```text
Enter target IP or hostname (default: localhost): localhost
Enter starting port (e.g., 1): 79
Enter ending port (e.g., 100): 81
--------------------------------------------------
Scanning Target : localhost (127.0.0.1)
Port Range      : 79 - 81
Scanning Started: 2026-09-21 15:33:00
--------------------------------------------------
Port    80 : OPEN
--------------------------------------------------
SCAN SUMMARY
--------------------------------------------------
Total Ports Scanned : 3
Open Ports Count    : 1
Closed Ports Count  : 2
Open Ports List     : 80
--------------------------------------------------
```

## Disclaimer
*This tool is intended for educational, network management, and authorized security assessment purposes only. Scanning targets without explicit permission may violate local computer misuse legislation.*
