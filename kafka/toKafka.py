import json
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka.future import log

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers='localhost: 9092')

future = producer.send('my-topic', b"test")

try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    log.exeption()
    pass

print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)

producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer.send('json-topic', {'key': 'value'})

for _ in range(100):
    producer.send('my-topic', b"test")
    producer.send('my-topic', b"\xc2Hola, mundo!")
    time.sleep(1)
