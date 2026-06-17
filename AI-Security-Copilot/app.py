import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Security Copilot", layout="wide")

st.title("🛡️ AI Security Copilot")
st.write("AI-powered cybersecurity assistant for log analysis, threat detection, risk scoring, and incident response.")

def analyze_log(log):
    log_lower = log.lower()

    if "failed login" in log_lower or "ssh" in log_lower:
        return "Brute Force Attack", "High", 80, "Block IP and enable MFA"

    elif "sql injection" in log_lower or "' or '1'='1" in log_lower:
        return "SQL Injection Attack", "Critical", 95, "Sanitize inputs and use prepared statements"

    elif "malware" in log_lower or "trojan" in log_lower:
        return "Malware Detected", "Critical", 98, "Isolate the system and run malware scan"

    elif "port scanning" in log_lower or "scan" in log_lower:
        return "Port Scanning", "Medium", 60, "Monitor network and restrict open ports"

    else:
        return "Unknown Activity", "Low", 20, "Review manually"

uploaded_file = st.file_uploader("Upload Security Log File", type=["txt"])

if uploaded_file:
    logs = uploaded_file.read().decode("utf-8").splitlines()

    results = []

    st.subheader("🔍 Log Analysis Results")

    for log in logs:
        threat, risk, score, action = analyze_log(log)

        results.append({
            "Log": log,
            "Threat": threat,
            "Risk": risk,
            "Score": score,
            "Action": action
        })

        st.code(log)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Threat", threat)
        col2.metric("Risk", risk)
        col3.metric("Risk Score", f"{score}/100")
        col4.metric("Action", action)

        st.divider()

    df = pd.DataFrame(results)

    st.subheader("📊 Attack Summary")
    summary = df["Threat"].value_counts()
    st.write(summary)

    st.bar_chart(summary)

    st.subheader("📋 Full Report")
    st.dataframe(df)

else:
    st.info("Upload sample_logs.txt file to start analysis.")