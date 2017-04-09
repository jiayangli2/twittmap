from __future__ import absolute_import, print_function
import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import boto3



consumer_key='GdeEd2wSLwPE3dFBBX7ZxIvzN'
consumer_secret='x2fpqVxPtEOjyO4ct3WqqXIfMhLMswkrdNdYUIqKgpQ6BqyW8n'
access_token='178733793-9cQ3d0dqc9Uf6CHIxdwjYpFmdrkfNAtjCQOkSGpf'  
access_token_secret='1k1ZVULtD6msZgTqPjAeD0fudeMYiCuWD9XpWolKS6z2y'


class StdOutListener(StreamListener):
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.tweet=[]
        self.count=0
        self.sqs=boto3.resource('sqs', region_name="us-east-2")
        self.my_queue = self.sqs.get_queue_by_name(QueueName='twittmap')
    def on_data(self, data):
        if data != None:
            temp = json.loads(data)
            #print(temp['place'])
            if 'place' in temp and temp['place']!=None and temp['place']['bounding_box']['coordinates'][0][0] != None and temp['lang']=='en':
                self.count+=1
                print (1)
                response=self.my_queue.send_message(MessageBody=data)
            if self.count <= 100:
                return True
            else:
                return False

    def on_error(self, status):
        print(status)

l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(track=['music'])



