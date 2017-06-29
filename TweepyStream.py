#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:30:08 2017

@author: ShuoGuo
"""
import MyAuth
import tweepy


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status):
        print("Error!")
        print(status)
        if status == 420:
            return False

auth = tweepy.OAuthHandler(MyAuth.consumer_key, MyAuth.consumer_secret)
auth.set_access_token(MyAuth.access_token, MyAuth.access_token_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['trading'])