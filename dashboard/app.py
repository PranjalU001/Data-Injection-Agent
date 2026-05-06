import os
import time
import streamlit as st
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv

# ---------------- LOAD ENV VARIABLES ----------------
load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="IoT Real-Time Dashboard",
    layout="wide",
    page_icon="📊"
)

# ---------------- SNOWFLAKE CONNECTION ----------------
@st.cache_resource
def get_connection():
    return snowflake.connector.connect(
        user=os.getenv("SNOW_USER"),
        password=os.getenv("SNOW_PASSWORD"),
        account=os.getenv("SNOW_ACCOUNT"),
        warehouse=os.getenv("SNOW_WAREHOUSE"),
        database=os.getenv("SNOW_DATABASE"),
        schema=os.getenv("SNOW_SCHEMA")
    )

conn = get_connection()

# ---------------- CUSTOM UI ----------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: white;
}

[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🚀 IoT Real-Time Monitoring Dashboard")

# ---------------- AUTO REFRESH ----------------
REFRESH_INTERVAL = 2

# ---------------- FETCH DATA ----------------
query = """
SELECT * FROM SENSOR_DATA
ORDER BY TIMESTAMP DESC
"""

df = pd.read_sql(query, conn)

# ---------------- MAIN DASHBOARD ----------------
if not df.empty:

    # Convert columns to uppercase
    df.columns = df.columns.str.upper()

    # Latest row
    latest = df.iloc[0]

    # ---------------- KPI SECTION ----------------
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🌡 Temperature",
        f"{latest['TEMPERATURE']} °C"
    )

    col2.metric(
        "💧 Humidity",
        f"{latest['HUMIDITY']} %"
    )

    col3.metric(
        "📟 Device",
        latest['DEVICE_ID']
    )

    st.divider()

    # ---------------- REAL-TIME CHART ----------------
    st.subheader("📈 Temperature & Humidity Trend")

    # Smooth chart using latest 100 rows
    chart_df = df.sort_values("TIMESTAMP").tail(100)

    st.line_chart(
        chart_df.set_index("TIMESTAMP")[["TEMPERATURE", "HUMIDITY"]]
    )

    st.divider()

    # ---------------- LIVE TABLE ----------------
    st.subheader("📊 Complete Sensor Data")

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )

else:
    st.warning("⚠ No data available in Snowflake")

# ---------------- AUTO REFRESH ----------------
time.sleep(REFRESH_INTERVAL)
st.rerun()