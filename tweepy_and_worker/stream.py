from __future__ import absolute_import, print_function
import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import boto.sqs
from boto.sqs.message import Message


consumer_key='GdeEd2wSLwPE3dFBBX7ZxIvzN'
consumer_secret='x2fpqVxPtEOjyO4ct3WqqXIfMhLMswkrdNdYUIqKgpQ6BqyW8n'
access_token='178733793-9cQ3d0dqc9Uf6CHIxdwjYpFmdrkfNAtjCQOkSGpf'  
access_token_secret='1k1ZVULtD6msZgTqPjAeD0fudeMYiCuWD9XpWolKS6z2y'


class StdOutListener(StreamListener):
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.tweet=[]
        self.count=0
        self.conn=boto.sqs.connect_to_region("us-east-2")
        self.my_queue = self.conn.get_queue('twittmap')
    def on_data(self, data):
        if data != None:
            temp = json.loads(data)
            #print(temp['place'])
            if temp['place']!=None and temp['place']['bounding_box']['coordinates'][0][0] != None and temp['lang']=='en':
                self.count+=1
                m=Message()
                m.set_body(data)
                self.my_queue.write(m)
            if self.count <= 50:
                return True
            else:
                return False

    def on_error(self, status):
        print(status)

l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(track=['spring'])



