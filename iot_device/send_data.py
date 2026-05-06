import os
import time
import requests
from dotenv import load_dotenv

# ---------------- LOAD ENV VARIABLES ----------------
load_dotenv()

# ---------------- WEATHER API CONFIG ----------------
API_KEY = os.getenv("WEATHER_API_KEY")

# 🌍 City Name
CITY = "Jaipur"

# 📡 Weatherstack API URL
WEATHER_URL = (
    f"http://api.weatherstack.com/current"
    f"?access_key={API_KEY}&query={CITY}"
)

# ---------------- FLASK API ENDPOINT ----------------
FLASK_URL = "http://127.0.0.1:5000/iot"

# ---------------- REAL-TIME DATA LOOP ----------------
while True:

    try:
        # 🔥 Step 1: Fetch weather data
        weather_response = requests.get(
            WEATHER_URL,
            timeout=10
        )

        weather_data = weather_response.json()

        # 🔥 Validate API response
        if "current" not in weather_data:
            print("❌ Invalid API Response")
            print(weather_data)

            time.sleep(5)
            continue

        # 🔥 Extract required values
        temperature = weather_data["current"]["temperature"]
        humidity = weather_data["current"]["humidity"]

        # 🔥 Prepare payload
        data = {
            "device_id": "weather_api_device",
            "temperature": temperature,
            "humidity": humidity
        }

        # 🔥 Step 2: Send data to Flask backend
        response = requests.post(
            FLASK_URL,
            json=data,
            timeout=5
        )

        # 🔥 Logs
        print("📤 Sent Data:", data)
        print("📥 Backend Response:", response.json())

    except Exception as e:
        print("❌ Error:", e)

    # 🔥 Repeat every 5 seconds
    time.sleep(5)