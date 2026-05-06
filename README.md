Here is a professional, ready-to-use `README.md` file based on your project report data. You can copy and paste this directly into your GitHub repository.

# Real-Time IoT Data Injection Agent

## 🚀 Introduction
The **Real-Time IoT Data Injection Agent** is an end-to-end real-time monitoring and analytics system. It is designed to collect live weather or IoT sensor data, stream the data using Apache Kafka, store it securely in a Snowflake cloud database, and visualize live analytics on an interactive Streamlit dashboard. 

This project demonstrates a complete real-time data engineering pipeline used in modern cloud applications, showcasing scalable, fault-tolerant, and event-driven architecture.

---

## ✨ Features
* **Real-Time Data Streaming:** High-throughput event streaming using Apache Kafka.
* **Live Dashboard Analytics:** Interactive data visualization using Streamlit.
* **Cloud Database Storage:** Scalable data warehousing with Snowflake.
* **AWS Cloud Deployment:** Fully hosted and running continuously on an AWS EC2 instance.
* **Event-Driven Architecture:** Decoupled producer-consumer microservices for reliability.
* **Real-Time Monitoring:** Auto-updating metrics for continuous observation.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core Programming Language |
| **Flask** | Backend REST API |
| **Apache Kafka** | Real-Time Data Streaming |
| **Kafka Producer** | Sends incoming API data to Kafka |
| **Kafka Consumer** | Processes streaming messages |
| **Snowflake** | Cloud Data Warehouse |
| **Streamlit** | Real-Time Interactive Dashboard |
| **AWS EC2** | Cloud Hosting & Deployment |
| **Weather API** | Real-Time Data Source / IoT Simulator |

---

## 🏗️ System Architecture

This project utilizes a **Producer-Consumer Kafka Architecture**, ensuring asynchronous communication, scalability, and fault tolerance.

### Data Flow Pipeline

[ Weather API / IoT Device ]
            ↓
[ Flask Backend API ]
            ↓
[ Kafka Producer ]
            ↓
[ Kafka Topic (Message Broker) ]
            ↓
[ Kafka Consumer ]
            ↓
[ Snowflake Database ]
            ↓
[ Streamlit Dashboard ]
            ↓
[ User Browser ]

### Working Procedure
1. **Data Generation:** Weather API or an IoT simulator generates real-time temperature and humidity data.
2. **Backend API:** The Flask backend receives the incoming data via REST API requests.
3. **Kafka Streaming:** The Kafka Producer sends the received data into a Kafka topic.
4. **Data Processing:** The Kafka Consumer continuously polls messages from the Kafka topic and processes them.
5. **Data Storage:** Processed data is safely ingested into the Snowflake cloud database.
6. **Visualization:** The Streamlit dashboard fetches live data from Snowflake to display real-time charts, tables, and analytics.
7. **Cloud Deployment:** The entire ecosystem runs on a public-facing AWS EC2 instance.

---

## ☁️ AWS Deployment & Kafka Integration

The complete project is deployed on an **AWS EC2 Linux instance**. 

### Services Hosted on EC2
* Flask Backend API
* Apache Kafka Server (with Zookeeper)
* Kafka Consumer Script
* Streamlit Dashboard

### Network & Port Configuration
AWS Security Groups are configured to allow public access to the necessary services. Ensure the following ports are open in your EC2 inbound rules:

| Port | Service | Description |
| :--- | :--- | :--- |
| **22** | SSH | For remote terminal access |
| **5000** | Flask Backend | REST API endpoint for incoming IoT data |
| **9092** | Kafka Broker | Bootstrap server for streaming messages |
| **8501** | Streamlit | Web interface for the real-time dashboard |

---

## 🎯 Conclusion
This project provides a practical implementation of modern data engineering workflows. By combining Flask, Kafka, Snowflake, Streamlit, and AWS EC2, the system successfully handles continuous real-time IoT data processing in a scalable and reliable cloud-native environment.
```
