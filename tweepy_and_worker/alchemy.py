import boto.sqs
from boto.sqs.message import Message
from watson_developer_cloud import AlchemyLanguageV1
import json

conn = boto.sqs.connect_to_region("us-east-2")
my_queue = conn.get_queue('twittmap')

rs = my_queue.get_messages()
m=rs[0]
body=m.get_body()
toa = json.loads(body)

alchemy_language = AlchemyLanguageV1(api_key='e84c6beb272209974c54c2b61af62699963ecc9a')
result = alchemy_language.sentiment(text=toa['text'])
print(result[''])
print(result['docSentiment'])
sentiment = result['docSentiment']['type']
