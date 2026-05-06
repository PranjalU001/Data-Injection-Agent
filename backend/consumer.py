from kafka import KafkaConsumer
import json
from datetime import datetime
from db import get_connection

# ✅ Kafka Consumer
consumer = KafkaConsumer(
    'iot_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

conn = get_connection()

for message in consumer:
    try:
        data = message.value

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO SENSOR_DATA (device_id, temperature, humidity, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (
            data['device_id'],
            data['temperature'],
            data['humidity'],
            datetime.now()
        ))

        conn.commit()
        cursor.close()

        print("✅ Inserted into Snowflake")

    except Exception as e:
        print("Error:", e)