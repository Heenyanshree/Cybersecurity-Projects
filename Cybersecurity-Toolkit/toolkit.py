import random
import string
import socket

print("================================")
print("      CYBERSECURITY TOOLKIT V4")
print("================================")

while True:

    print("\nChoose a Tool")
    print("1. Password Generator")
    print("2. Port Scanner")
    print("3. Vulnerability Scanner")
    print("4. Phishing URL Detector")
    print("5. Log Analyzer")
    print("6. Network Scanner")
    print("7. Exit")

    choice = input("Enter Choice: ").strip()

    # PASSWORD GENERATOR
    if choice == "1":

        length = int(input("Enter Password Length: "))

        characters = string.ascii_letters + string.digits + "!@#$%^&*"

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

    # PORT SCANNER
    elif choice == "2":

        target = input("Enter IP Address: ")
        start_port = int(input("Enter Start Port: "))
        end_port = int(input("Enter End Port: "))

        open_ports = []

        print("\nScanning...\n")

        for port in range(start_port, end_port + 1):

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.2)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)

            sock.close()

        with open("port_report.txt", "w") as file:
            file.write("PORT SCAN REPORT\n")
            file.write("================\n")
            file.write(f"Target: {target}\n\n")

            if open_ports:
                for port in open_ports:
                    file.write(f"Port {port} is OPEN\n")
            else:
                file.write("No open ports found.\n")

        print("\nPort Scan Completed!")
        print("Report saved as port_report.txt")

    # VULNERABILITY SCANNER
    elif choice == "3":

        target = input("Enter IP Address: ")

        common_ports = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            80: "HTTP",
            443: "HTTPS",
            445: "SMB",
            3306: "MySQL",
            3389: "RDP"
        }

        open_services = []

        print("\nScanning Common Services...\n")

        for port, service in common_ports.items():

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} OPEN → {service}")
                open_services.append((port, service))

            sock.close()

        with open("vulnerability_report.txt", "w") as file:
            file.write("VULNERABILITY SCAN REPORT\n")
            file.write("=========================\n")
            file.write(f"Target: {target}\n\n")

            if open_services:
                print(f"Port {port} OPEN - {service}")
                file.write(f"Port {port} OPEN - {service}\n")
            else:
                file.write("No vulnerable services detected.\n")

        print("\nVulnerability Scan Completed!")
        print("Report saved as vulnerability_report.txt")

    # PHISHING URL DETECTOR
    elif choice == "4":

        url = input("Enter URL: ")

        risk_score = 0

        if url.startswith("http://"):
            risk_score += 2

        if "@" in url:
            risk_score += 2

        if "-" in url:
            risk_score += 1

        suspicious_words = [
            "login",
            "verify",
            "update",
            "secure",
            "account",
            "bank"
        ]

        for word in suspicious_words:
            if word in url.lower():
                risk_score += 1

        print("\nURL Analysis Report")
        print("-------------------")
        print("Risk Score:", risk_score)

        if risk_score <= 2:
            result = "Safe URL"
        elif risk_score <= 5:
            result = "Suspicious URL"
        else:
            result = "Phishing URL"

        print("Result:", result)

        with open("phishing_report.txt", "w") as file:
            file.write("PHISHING REPORT\n")
            file.write("================\n")
            file.write(f"URL: {url}\n")
            file.write(f"Risk Score: {risk_score}\n")
            file.write(f"Result: {result}\n")

        print("Report saved as phishing_report.txt")

    # LOG ANALYZER
    elif choice == "5":

        log_file = input("Enter log file name: ")

        info_count = 0
        warning_count = 0
        error_count = 0

        try:
            with open(log_file, "r") as file:

                for line in file:

                    if "INFO" in line:
                        info_count += 1

                    elif "WARNING" in line:
                        warning_count += 1

                    elif "ERROR" in line:
                        error_count += 1

            print("\nLog Analysis Report")
            print("-------------------")
            print("INFO Count:", info_count)
            print("WARNING Count:", warning_count)
            print("ERROR Count:", error_count)

            with open("log_report.txt", "w") as report:
                report.write("LOG ANALYSIS REPORT\n")
                report.write("===================\n")
                report.write(f"INFO Count: {info_count}\n")
                report.write(f"WARNING Count: {warning_count}\n")
                report.write(f"ERROR Count: {error_count}\n")

            print("Report saved as log_report.txt")

        except FileNotFoundError:
            print("Log file not found!")

    # NETWORK SCANNER
    elif choice == "6":

        network = input("Enter network prefix like 192.168.1: ")

        print("\nScanning network...\n")

        found = []

        for i in range(1, 255):

            ip = network + "." + str(i)

            try:
                socket.gethostbyaddr(ip)
                print("Device Found:", ip)
                found.append(ip)

            except:
                pass

        with open("network_report.txt", "w") as file:
            file.write("NETWORK SCAN REPORT\n")
            file.write("===================\n")

            for ip in found:
                file.write(ip + "\n")

        print("\nNetwork Scan Completed!")
        print("Report saved as network_report.txt")

    # EXIT
    elif choice == "7":

        print("Goodbye!")
        break

    else:
        print("Invalid Choice")