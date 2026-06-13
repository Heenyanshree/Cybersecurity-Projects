import tkinter as tk
import random
import string
import socket

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"Generated Password:\n{password}")

def scan_ports():
    target = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Scanning...\n\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((target, port))

        if result == 0:
            output_box.insert(tk.END, f"Port {port} is OPEN\n")

        sock.close()

    output_box.insert(tk.END, "\nPort Scan Completed!")

def vulnerability_scan():
    target = vuln_ip_entry.get()

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

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Vulnerability Scan Started...\n\n")

    found = False

    for port, service in common_ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target, port))

        if result == 0:
            found = True
            output_box.insert(tk.END, f"Port {port} OPEN - {service}\n")

            if port == 23:
                output_box.insert(tk.END, "HIGH RISK: Telnet is insecure.\n")
            elif port == 21:
                output_box.insert(tk.END, "MEDIUM RISK: FTP may expose files.\n")
            elif port == 445:
                output_box.insert(tk.END, "HIGH RISK: SMB should not be public.\n")
            elif port == 3389:
                output_box.insert(tk.END, "HIGH RISK: RDP can be dangerous if exposed.\n")

        sock.close()

    if not found:
        output_box.insert(tk.END, "No common vulnerable services detected.\n")

    output_box.insert(tk.END, "\nVulnerability Scan Completed!")

def check_phishing():
    url = url_entry.get()
    risk_score = 0

    if url.strip() == "":
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a URL.")
        return

    if url.startswith("http://"):
        risk_score += 2
    if "@" in url:
        risk_score += 2
    if "-" in url:
        risk_score += 1
    if url.count(".") > 3:
        risk_score += 1
    if len(url) > 75:
        risk_score += 2

    suspicious_words = [
        "login", "verify", "update", "secure",
        "account", "bank", "free", "password"
    ]

    for word in suspicious_words:
        if word in url.lower():
            risk_score += 1

    if risk_score <= 2:
        result = "Safe URL"
    elif risk_score <= 5:
        result = "Suspicious URL"
    else:
        result = "Phishing URL"

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Phishing URL Analysis\n")
    output_box.insert(tk.END, "---------------------\n")
    output_box.insert(tk.END, f"URL: {url}\n")
    output_box.insert(tk.END, f"Risk Score: {risk_score}\n")
    output_box.insert(tk.END, f"Result: {result}\n")

def clear_output():
    output_box.delete("1.0", tk.END)

def save_report():
    content = output_box.get("1.0", tk.END)

    with open("gui_report.txt", "w") as file:
        file.write(content)

    output_box.insert(tk.END, "\n\nReport saved as gui_report.txt")

window = tk.Tk()
window.configure(bg="#1e1e1e")
window.title("Cybersecurity Toolkit GUI")
window.geometry("700x900")

tk.Button(
    window,
    text="Generate Password",
    command=generate_password,
    bg="#0f766e",
    fg="white"
).pack(pady=8)

tk.Label(window, text="Password Length:").pack()
length_entry = tk.Entry(window)
length_entry.pack(pady=5)
tk.Button(window, text="Generate Password", command=generate_password).pack(pady=8)

tk.Label(window, text="Port Scanner - IP Address:").pack()
ip_entry = tk.Entry(window)
ip_entry.pack(pady=5)

tk.Label(window, text="Start Port:").pack()
start_port_entry = tk.Entry(window)
start_port_entry.pack(pady=5)

tk.Label(window, text="End Port:").pack()
end_port_entry = tk.Entry(window)
end_port_entry.pack(pady=5)

tk.Button(window, text="Scan Ports", command=scan_ports).pack(pady=8)

tk.Label(window, text="Vulnerability Scanner - IP Address:").pack()
vuln_ip_entry = tk.Entry(window)
vuln_ip_entry.pack(pady=5)

tk.Button(window, text="Run Vulnerability Scan", command=vulnerability_scan).pack(pady=8)

tk.Label(window, text="URL:").pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

tk.Button(window, text="Check Phishing URL", command=check_phishing).pack(pady=8)
tk.Button(window, text="Clear Output", command=clear_output).pack(pady=8)
tk.Button(window, text="Save Report", command=save_report).pack(pady=8)

output_box = tk.Text(window, height=15, width=80)
output_box.pack(pady=10)

window.mainloop()