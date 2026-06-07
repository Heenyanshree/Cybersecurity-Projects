import socket

print("================================")
print("      ADVANCED PORT SCANNER")
print("================================")

target = input("Enter IP Address: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

open_ports = []

print("\nScanning...")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)

    sock.close()

with open("scan_report.txt", "w") as file:
    file.write("PORT SCAN REPORT\n")
    file.write("================\n")
    file.write(f"Target: {target}\n")
    file.write(f"Port Range: {start_port}-{end_port}\n\n")

    if open_ports:
        file.write("Open Ports:\n")
        for port in open_ports:
            file.write(f"Port {port} is OPEN\n")
    else:
        file.write("No open ports found.\n")

print("\nScan Completed!")
print("Report saved as scan_report.txt")