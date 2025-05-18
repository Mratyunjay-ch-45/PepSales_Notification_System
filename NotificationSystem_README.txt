Notification System - README
A scalable notification service built with FastAPI and Kafka, supporting Email, SMS, and In-App notifications. Designed for event-driven communication with retry mechanisms.
Features
- Publish and consume notifications via Kafka
- Modular design supporting:
  - Email
  - SMS
  - In-App notifications
- Retry mechanism for failed notifications
- Dockerized for ease of development and deployment
Project Structure

NOTIFICATION_SYSTEM/
│
├── backend/
│   ├── app/                    # FastAPI application
│   │   ├── main.py             # Entry point
│   │   ├── kafka_producer.py   # Kafka producer logic
│   │   ├── kafka_consumer.py   # Kafka consumer logic
│   │   ├── handlers/           # Notification handlers
│   ├── Dockerfile              # Backend Docker setup
│   └── requirements.txt
│
├── docker-compose.yml          # Docker orchestration
├── README.md                   # You're here!

Assumptions

- Kafka and Zookeeper run inside Docker containers.
- Notification consumers (email, SMS, in-app) are handled in code under `handlers/`.
- Email/SMS gateways are mocked or assumed to be configured via env vars.
- Retry policy is managed at the consumer level with backoff or requeue.
- Kafka topics like `email-topic`, `sms-topic`, `inapp-topic` are predefined or auto-created.
- Developer is using VS Code and running commands via integrated terminal.

Requirements
- Docker (ensure it's installed and running)
- Git
- VS Code (recommended)
Setup Instructions
1. Clone the Repository:
   git clone https://github.com/your-username/NOTIFICATION_SYSTEM.git
   cd NOTIFICATION_SYSTEM

2. Start the Services:
   docker compose up -d

3. Build Backend (if not already containerized):
   cd backend/app
   pip install -r requirements.txt
   uvicorn main:app --reload
Sending a Notification (Example)
POST http://localhost:8000/send-notification

Body (JSON):
{
  "type": "email",
  "recipient": "user@example.com",
  "subject": "Test Email",
  "message": "This is a test notification"
}
Kafka Topics

| Notification Type | Kafka Topic     |
|-------------------|-----------------|
| Email             | email-topic     |
| SMS               | sms-topic       |
| In-App            | inapp-topic     |

Retry Mechanism
Notifications are retried using Kafka consumer-level retry logic. Failed messages can be requeued or logged for manual retry.
Docker Compose Services

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest

  kafka:
    image: confluentinc/cp-kafka:latest

  backend:
    build: ./backend/app
    ports:
      - "8000:8000"

To Do
- Add UI for managing notifications
- Integrate actual email/SMS services (e.g., SendGrid, Twilio)
- Add monitoring (e.g., Prometheus + Grafana)
License
MIT License. See LICENSE file for details.