import socket

print("================================")
print("        NETWORK SCANNER")
print("================================")

network = input("Enter network prefix like 192.168.1: ")

print("\nScanning network...\n")

for i in range(1, 255):
    ip = network + "." + str(i)

    try:
        socket.gethostbyaddr(ip)
        print(f"Device Found: {ip}")
    except:
        pass

print("\nScan Completed!")