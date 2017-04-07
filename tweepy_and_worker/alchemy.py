import boto.sqs
from boto.sqs.message import Message
from watson_developer_cloud import AlchemyLanguageV1
import json
from multiprocessing.dummy import Pool as ThreadPool 

conn = boto.sqs.connect_to_region("us-east-2")
my_queue = conn.get_queue('twittmap')

def get_msg():
    rs = my_queue.get_messages()
    m=rs[0]
    body=m.get_body()
    my_queue.delete_message(m)
    toa = json.loads(body)

    alchemy_language = AlchemyLanguageV1(api_key='e84c6beb272209974c54c2b61af62699963ecc9a')
    result = alchemy_language.sentiment(text=toa['text'])
    #print(toa['text'])
    #print(result['docSentiment'])
    sentiment = result['docSentiment']['type']
    #print(sentiment)

    response = client.publish(
        TopicArn='twittmap',
        TargetArn='arn:aws:sns:us-east-2:851980283070:twittmap',
        #PhoneNumber='string',
        Message=toa,
        Subject='string',
        MessageStructure='json',
        MessageAttributes={
            'string': {
                'DataType': 'string',
                'StringValue': 'string',
                'BinaryValue': b'bytes'
            }
        }
    )
