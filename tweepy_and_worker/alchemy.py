import boto3
from watson_developer_cloud import AlchemyLanguageV1
import json
import cPickle
from threading import Thread

def get_msg(i): 
     while(True):
        response=sqs.receive_message(QueueUrl = 'https://sqs.us-east-2.amazonaws.com/851980283070/twittmap')
        if(response==None):
            continue
        print "ko"
        if not ('Messages' in response): 
            continue
        t=response['Messages']
        toa = json.loads(t[0]['Body'])
        receipt_handle = t[0]['ReceiptHandle']
        sqs.delete_message(QueueUrl='https://sqs.us-east-2.amazonaws.com/851980283070/twittmap', ReceiptHandle=receipt_handle)
        alchemy_language = AlchemyLanguageV1(api_key='e84c6beb272209974c54c2b61af62699963ecc9a')
        result = alchemy_language.sentiment(text=toa['text'])
        #print(toa['text'])
        #print(result['docSentiment'])
        sentiment = result['docSentiment']['type']
        #toa['sentiment']=sentiment
        toa['geo_location'] = {"lat":toa['place']['bounding_box']['coordinates'][0][0][1], "lon":toa['place']['bounding_box']['coordinates'][0][0][0]}
        tbs = {"text":toa['text'], "sentiment":sentiment, "geo_location":toa['geo_location'],}
        to_be_sent = json.dumps({"default":json.dumps(tbs)})
        # print len(to_be_sent)
        #to_be_sent = json.dumps(to_be_sent)
        response = client.publish(
            TopicArn='arn:aws:sns:us-east-2:851980283070:twittmap',
            Message = to_be_sent,
            Subject='PNNTwitt',
            MessageStructure='json'
        )
        break

sqs = boto3.client('sqs', region_name='us-east-2')
client = boto3.client('sns', region_name='us-east-2')

for i in range(5):
    t=Thread(target=get_msg, args=(i, ))
    t.setDaemon(True)
    t.start()

