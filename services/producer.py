from confluent_kafka import Producer
import json

p = Producer({'bootstrap.servers': 'localhost:9092'})

def send_to_kafka(topic, message):
    p.produce(topic, key=str(message.get("user_id")), value=json.dumps(message))
    p.flush()
