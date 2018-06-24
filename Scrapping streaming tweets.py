# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:25:01 2018

@author: Gireesh Sundaram
"""
#Importing the packages
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import pandas as pd
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from textblob import TextBlob
import numpy as np

#%%
#Auth twitter using the access
auth = tweepy.OAuthHandler("CODE HERE", "CODE HERE")
auth.set_access_token("CODE HERE", "CODE HERE")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#%%
#This code is used to take tweets from a given user and convert into to a dataframe
tweets_df = pd.DataFrame(columns = ["Username", "Tweet", "Liks", "Retweet", "DateTime", "Lang", "Geo", "Source"])

def getTweets(account):
    global tweets_df
    tweets_json = api.user_timeline(id = account, count = 250)
        
    for tweets in tweets_json:
        tweets_data = pd.DataFrame([[tweets.user.name, tweets.text, tweets.favorite_count, tweets.retweet_count, tweets.created_at, tweets.lang, tweets.author.location, tweets.source]], columns = ["Username", "Tweet", "Liks", "Retweet", "DateTime", "Lang", "Geo", "Source"])
        tweets_df = tweets_df.append(tweets_data, ignore_index=True)
        
    return None

team_usernames = ["ChennaiIPL", "SunRisers", "rajasthanroyals", "mipaltan", "KKRiders", "RCBTweets",
                  "IPL", "DelhiDaredevils ", "lionsdenkxip"]

for teams in team_usernames:
    getTweets(teams)

#%%
#Saving the dataframe for future analysis:
tweets_df.to_csv("...\\Files\\tweets.csv")

#%%
#To filter the dataset by Dhoni
tweets_df["tweet_lower"] = tweets_df['Tweet'].str.lower()
Dhoni = tweets_df.loc[tweets_df.tweet_lower.str.contains("dhoni") | tweets_df.tweet_lower.str.contains("msd")]

#%%
#Twitter streaming to get the realtime trend for a topic and saving it into a dataframe
class listener(StreamListener):

    def on_data(self, data):
#        print(data)
        
        with open("...\\Files\\IPL Tweets.json", "a") as streaming:
            streaming.write(data)
            
        return(True)

    def on_error(self, status):
        print(status)
        
twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=["#IPLFinals2018"])
