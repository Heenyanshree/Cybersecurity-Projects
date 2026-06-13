import streamlit as st
import re

st.title("AI Threat Intelligence Dashboard")

uploaded_file = st.file_uploader("Upload Threat Feed", type=["txt"])

if uploaded_file is not None:
    feeds = uploaded_file.read().decode("utf-8").splitlines()

    ioc_count = 0
    malware_count = 0
    suspicious_count = 0
    ip_addresses = []
    domains = []
    malware_names = []

    for item in feeds:
        ip_match = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", item)
        domain_match = re.findall(r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", item)

        ip_addresses.extend(ip_match)

        if "MALWARE" in item:
            malware_count += 1
            malware_name = item.replace("MALWARE", "").replace("detected", "").strip()
            malware_names.append(malware_name)
        elif "IOC" in item:
            ioc_count += 1
            domains.extend(domain_match)
        elif "SUSPICIOUS" in item:
            suspicious_count += 1

    risk_score = (ioc_count * 2) + (malware_count * 3) + suspicious_count

    if risk_score >= 10:
        threat_level = "HIGH"
    elif risk_score >= 5:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    st.subheader("Threat Summary")
    st.metric("IOC Count", ioc_count)
    st.metric("Malware Count", malware_count)
    st.metric("Suspicious Count", suspicious_count)
    st.metric("Risk Score", risk_score)

    st.subheader("Threat Level")
    st.write(threat_level)

    st.subheader("Detected IOCs")
    st.write("IP Addresses:", ip_addresses)
    st.write("Domains:", domains)
    st.write("Malware Names:", malware_names)

    st.subheader("Raw Threat Feed")
    st.write(feeds)