from .models import Tweet
try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from elasticsearch import Elasticsearch

ACCESS_TOKEN = '178733793-9cQ3d0dqc9Uf6CHIxdwjYpFmdrkfNAtjCQOkSGpf'
ACCESS_SECRET = '1k1ZVULtD6msZgTqPjAeD0fudeMYiCuWD9XpWolKS6z2y'
CONSUMER_KEY = 'GdeEd2wSLwPE3dFBBX7ZxIvzN'
CONSUMER_SECRET = 'x2fpqVxPtEOjyO4ct3WqqXIfMhLMswkrdNdYUIqKgpQ6BqyW8n'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.sample()
es=Elasticsearch(["https://search-es-twitter-demo-snhzuc3whnp44zlt2nx7iaqeaq.us-west-2.es.amazonaws.com"])
counter = 2000

for twitt in iterator:
    counter = counter-1
    if 'text' in twitt:
        to=json.dumps(twitt['text'])
        tl=len(to)-1
        lo=json.dumps(twitt['user']['location'])
        ll=len(lo)-1
        t=Tweet(tweet_text=to, tweet_location=lo)
        t.save()
    if counter<=0:
        break

