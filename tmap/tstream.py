import tweepy  
import sys  
import json  
from textwrap import TextWrapper  
from datetime import datetime  
from elasticsearch import Elasticsearch


consumer_key="GdeEd2wSLwPE3dFBBX7ZxIvzN"  
consumer_secret="x2fpqVxPtEOjyO4ct3WqqXIfMhLMswkrdNdYUIqKgpQ6BqyW8n"

accesstoken="178733793-9cQ3d0dqc9Uf6CHIxdwjYpFmdrkfNAtjCQOkSGpf"  
accesstokensecret="1k1ZVULtD6msZgTqPjAeD0fudeMYiCuWD9XpWolKS6z2y"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accesstoken, accesstokensecret)

es = Elasticsearch(['search-es-twitter-demo-snhzuc3whnp44zlt2nx7iaqeaq.us-west-2.es.amazonaws.com'])


class MyStreamListener(tweepy.StreamListener):  
    def on_status(self, status):
        try:
            json_data = status._json
            es.create(index="idx_twp",
                      doc_type="twitter_twp",
                      body=json_data
                     )

        except Exception, e:
            print e
            pass

myStreamListener = MyStreamListener()
streamer = tweepy.Stream(auth=auth, listener=myStreamListener, timeout=3000000000)

streamer.filter(track=['music'], async=True)  

#streamer.userstream(None)
