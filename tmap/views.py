from django.http import HttpResponse#Redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.template import loader
from .models import Tweet
try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
'''
ACCESS_TOKEN = '178733793-9cQ3d0dqc9Uf6CHIxdwjYpFmdrkfNAtjCQOkSGpf'
ACCESS_SECRET = '1k1ZVULtD6msZgTqPjAeD0fudeMYiCuWD9XpWolKS6z2y'
CONSUMER_KEY = 'GdeEd2wSLwPE3dFBBX7ZxIvzN'
CONSUMER_SECRET = 'x2fpqVxPtEOjyO4ct3WqqXIfMhLMswkrdNdYUIqKgpQ6BqyW8n'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.sample()
counter = 100

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
'''

def index(request):
    tweet_list = Tweet.objects.all()
    context = {'tweet_list': tweet_list}
    return render(request, 'tmap/index.html', context)
