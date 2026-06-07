import socket

print("================================")
print("         PORT SCANNER")
print("================================")

target = input("Enter IP Address: ")

for port in range(1, 101):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)  # Fast timeout

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()

print("\nScan Completed!")