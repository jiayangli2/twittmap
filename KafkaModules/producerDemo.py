import kafka_producer, kafka_consumer
producer=kafka_producer.kafka_producer()
producer.send(msg="hello")