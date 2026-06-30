import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="AI SOC Dashboard",
    layout="wide"
)


st.title("🛡️ AI SOC Analyst Dashboard")
st.write("Enterprise Network Security Monitoring System")


try:
    logs = pd.read_csv("network_logs.csv")

except:
    st.error("network_logs.csv not found")
    st.stop()


# Counters

total_logs = len(logs)

failed = len(
    logs[logs["event"]=="Failed Login"]
)

malware = len(
    logs[logs["event"]=="Malware Alert"]
)

unknown = len(
    logs[logs["event"]=="Unknown Device Connected"]
)

suspicious = len(
    logs[logs["event"]=="Suspicious External IP"]
)


risk = (
    failed*2 +
    malware*6 +
    unknown*4 +
    suspicious*5
)


if risk >=15:
    level="HIGH 🔴"

elif risk>=8:
    level="MEDIUM 🟠"

else:
    level="LOW 🟢"



# Dashboard

col1,col2,col3,col4 = st.columns(4)


col1.metric(
"Total Logs",
total_logs
)


col2.metric(
"Malware Alerts",
malware
)


col3.metric(
"Failed Login",
failed
)


col4.metric(
"Risk Score",
risk
)



st.subheader("Threat Level")

st.success(level)



st.subheader("Security Events")


st.dataframe(logs)



st.subheader("AI Alert Classification")


for _,row in logs.iterrows():

    event=row["event"]


    if event=="Malware Alert":
        st.error(
        "🚨 Malware Threat Detected"
        )


    elif event=="Failed Login":
        st.warning(
        "⚠️ Authentication Attack"
        )


    elif event=="Unknown Device Connected":
        st.warning(
        "⚠️ Unauthorized Device"
        )


    elif event=="Suspicious External IP":
        st.error(
        "🚨 Network Threat"
        )


st.subheader("Risk Analysis")


st.bar_chart(
{
"Failed Login":failed,
"Malware":malware,
"Unknown Device":unknown,
"Suspicious IP":suspicious
}
)