import socket
from datetime import datetime

# Hardcoded vulnerability database
vulnerabilities = {
    21: ("FTP", "Anonymous login allowed"),
    22: ("SSH", "Weak password authentication"),
    80: ("HTTP", "Possible XSS vulnerabilities"),
    443: ("HTTPS", "SSL/TLS misconfiguration")
}

# Get target IP
target = input("Enter target IP: ")

ports = [21, 22, 80, 443]
open_ports = []

print(f"\nScanning {target}...\n")

# Scan ports
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)
    
    s.close()

# Generate HTML report
date = datetime.now().strftime("%Y-%m-%d")
filename = f"report_{target}_{date}.html"

with open(filename, "w") as f:
    f.write("<html><head><title>Security Audit Report</title></head><body>")
    f.write(f"<h1>Security Report for {target}</h1>")
    f.write(f"<p>Date: {date}</p>")
    f.write("<table border='1'>")
    f.write("<tr><th>Port</th><th>Service</th><th>Vulnerability</th></tr>")

    for port in open_ports:
        service, vuln = vulnerabilities.get(port, ("Unknown", "None"))
        f.write(f"<tr><td>{port}</td><td>{service}</td><td>{vuln}</td></tr>")

    f.write("</table>")
    f.write(f"<p>Total Open Ports: {len(open_ports)}</p>")
    f.write("</body></html>")

print(f"\nReport saved as {filename}")
