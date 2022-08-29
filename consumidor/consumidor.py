from kafka import KafkaConsumer


topic = 'test'
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer(
    topic, bootstrap_servers=bootstrap_servers, group_id='my_consumer')
for msg in consumer:
    print(msg.partition)
    print(msg.offset)
    print(msg.value)