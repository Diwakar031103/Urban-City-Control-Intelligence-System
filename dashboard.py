import streamlit as st
import requests
import time

# configure page settings (wide layout for dashboard feel)
st.set_page_config(page_title="UCCIS Dashboard", layout="wide")

# main title
st.title("🚦 UCCIS Real-Time Dashboard")

API_URL = "http://127.0.0.1:8000"  # backend FastAPI server

refresh_interval = 2  # refresh data every 2 seconds

placeholder = st.empty()  # used to dynamically update UI without reloading page

# continuous loop to simulate real-time dashboard
while True:
    try:
        # fetch latest zone data from backend
        zone_states = requests.get(f"{API_URL}/zone/state").json()

        # fetch alerts data
        alerts = requests.get(f"{API_URL}/alerts").json()

        # update UI inside placeholder container
        with placeholder.container():

            st.subheader(" Zone State")

            # display each zone's current state
            for zone in zone_states:
                st.write({
                    "zone_id": zone["zone_id"],
                    "traffic_density": zone["traffic_density"],
                    "violation_count": zone["violation_count"],
                    "congestion_level": zone["congestion_level"],
                    "timestamp": zone["timestamp"],
                    "trace_id": zone["trace_id"]
                })

            st.subheader(" Live Alerts")

            # show last 10 alerts (latest first)
            for alert in alerts[-10:]:
                st.error(
                    f"{alert['zone_id']} | Alerts: {alert['alerts']} | Actions: {alert['actions']} | Trace: {alert['trace_id']}"
                )

        # wait before next refresh
        time.sleep(refresh_interval)

    except:
        # if API is not running or fails
        st.warning("API not running...")
        time.sleep(2)