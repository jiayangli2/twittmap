from kafka import KafkaProducer
from kafka.errors import KafkaError

class kafka_producer():
    def __init__(self):

        #producer = KafkaProducer(bootstrap_servers=['broker1:1234'])
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        # Asynchronous by default
        #future = self.producer.send('my-topic', b'raw_bytes')
        # Block for 'synchronous' sends
        # try:
        #     record_metadata = future.get(timeout=10)
        # except KafkaError:
        #     # Decide what to do if produce request failed...
        #     log.exception()
        #     pass

        # Successful result returns assigned partition and offset
        print("Successfully connected!")
        # print (record_metadata.topic)
        # print (record_metadata.partition)
        # print (record_metadata.offset)

    def send(self, msg,key=None):
        # produce keyed messages to enable hashed partitioning
        #self.producer.send('my-topic', key=b'foo', value=b'bar')

        # encode objects via msgpack
        # producer = KafkaProducer(value_serializer=msgpack.dumps)
        # producer.send('msgpack-topic', {'key': 'value'})
        #
        # # produce json messages
        # producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
        # producer.send('json-topic', {'key': 'value'})

        # produce asynchronously

        self.producer.send('my-topic', key=key,value=msg)

        # block until all async messages are sent
        self.producer.flush()

        # configure multiple retries
        self.producer = KafkaProducer(retries=5)
