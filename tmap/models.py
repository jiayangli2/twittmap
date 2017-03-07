from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_text=models.CharField(max_length=150)
    tweet_location=models.CharField(max_length=20)
    def __str__(self):
        return self.tweet_text

