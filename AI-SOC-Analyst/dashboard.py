import streamlit as st

st.title("AI SOC Analyst Dashboard")

uploaded_file = st.file_uploader("Upload Log File", type=["txt"])

def classify_alert(alert):
    alert_lower = alert.lower()

    if "sql injection" in alert_lower:
        return "Web Attack"
    elif "malware" in alert_lower:
        return "Malware"
    elif "failed login" in alert_lower or "brute force" in alert_lower:
        return "Authentication Threat"
    elif "suspicious network" in alert_lower:
        return "Network Threat"
    else:
        return "Unknown Threat"

if uploaded_file is not None:
    logs = uploaded_file.read().decode("utf-8").splitlines()

    info_count = 0
    warning_count = 0
    error_count = 0
    alerts = []

    for log in logs:
        if "INFO" in log:
            info_count += 1
        elif "WARNING" in log:
            warning_count += 1
            alerts.append(log)
        elif "ERROR" in log:
            error_count += 1
            alerts.append(log)

    risk_score = warning_count + (error_count * 2)

    if risk_score >= 6:
        threat_level = "HIGH"
    elif risk_score >= 3:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    st.subheader("SOC Analysis Report")

    st.metric("INFO Logs", info_count)
    st.metric("WARNING Logs", warning_count)
    st.metric("ERROR Logs", error_count)

    st.subheader("Risk Assessment")
    st.write("Risk Score:", risk_score)
    st.write("Threat Level:", threat_level)

    st.subheader("AI Alert Classification")

    for alert in alerts:
        st.write(alert, "=>", classify_alert(alert))