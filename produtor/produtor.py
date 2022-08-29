from kafka import KafkaProducer

topic = 'test'
bootstrap_servers = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Generate 100 messages
for _ in range(10):
    msg = f'kafka msg: {_}'
    future = producer.send(topic, msg.encode('utf-8'))
    print(f'Sending msg: {msg}')
    result = future.get(timeout=60)

metrics = producer.metrics()
print(metrics)