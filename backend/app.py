from flask import Flask, request, jsonify
from kafka import KafkaProducer
from dotenv import load_dotenv
import json
import os

# ---------------- LOAD ENV VARIABLES ----------------
load_dotenv()

app = Flask(__name__)

# ---------------- KAFKA PRODUCER ----------------
producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_SERVER"),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("✅ Kafka Producer Connected")

# ---------------- HOME ROUTE ----------------
@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "service": "IoT Kafka Producer API"
    })

# ---------------- IOT ROUTE ----------------
@app.route('/iot', methods=['POST'])
def receive_data():

    try:
        # 🔥 Receive JSON data
        data = request.get_json()

        # 🔥 Validate fields
        required_fields = [
            "device_id",
            "temperature",
            "humidity"
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": f"Missing field: {field}"
                }), 400

        # 🔥 Send data to Kafka
        producer.send('iot_topic', data)

        producer.flush()

        print("📤 Sent to Kafka:", data)

        return jsonify({
            "status": "success",
            "message": "Data sent to Kafka"
        }), 200

    except Exception as e:

        print("❌ Error:", e)

        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 500

# ---------------- MAIN ----------------
if __name__ == '__main__':

    app.run(
        host="0.0.0.0",
        port=5000,
        threaded=True,
        debug=True
    )