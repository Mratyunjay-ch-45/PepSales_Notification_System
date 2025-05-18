from confluent_kafka import Consumer
import json
from app.services.notification_handlers import handle_notification
from app.utils.retry import retry

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'notification-consumer-group',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['notifications'])

def consume_messages():
    while True:
        msg = consumer.poll(1.0)
        if msg is None or msg.error():
            continue
        data = json.loads(msg.value())
        retry(lambda: handle_notification(data), retries=3)
