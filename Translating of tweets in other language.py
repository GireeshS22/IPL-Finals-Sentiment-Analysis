# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:43:38 2018

@author: Gireesh Sundaram
"""

#Importing the packages
import pandas as pd
import json
from textblob import TextBlob

#%%
#Loading the JSON file saved as dictionary values
tweets = []
for line in open('D:\\CBA\\Practicum\\Practicum_1\\Trends.txt', 'r'):
    if not ('{"limit":{"track"') in line:
        tweets.append(json.loads(line))
    
samp = []
for line in open('D:\\CBA\\Practicum\\Practicum_1\\sample.txt', 'r'):
    if not ('{"limit":{"track"') in line:
        tweets.append(json.loads(line))    
    
#%%
#Converting the loaded dictionary into a dataframe with useful information
tweets_df = pd.DataFrame(columns = ["Username", "Tweet", "Likes", "Retweets", "DateTime", "Lang", "Geo", "Source"])

i = 0

for tweet in tweets:
    global i
    tweets_data = pd.DataFrame([[tweet['user']['name'], tweet['text'], tweet['favorite_count'], tweet['retweet_count'], tweet['created_at'], tweet['lang'], tweet['user']['location'], tweet['source']]], columns = ["Username", "Tweet", "Likes", "Retweets", "DateTime", "Lang", "Geo", "Source"])
    tweets_df = tweets_df.append(tweets_data, ignore_index=True)
    i = i + 1
    if (i % 500) == 0:
        print(i)

tweets_df.to_pickle("D:\\CBA\\Practicum\\Practicum_1\\IPLFinals.pk1")
tweets_df.to_csv("D:\\CBA\\Practicum\\Practicum_1\\tweets.csv")
#%%
#Converting tweets that are not in english
tweets_df = pd.read_pickle("D:\\CBA\\Practicum\\Practicum_1\\IPLFinals.pk1")

tweets_df["Translated"] = ""

count = 0

for i in range(0, len(tweets_df)):
    global count
    if tweets_df.iloc[i]['Lang'] in ['hi', 'ta']:
        from_language = tweets_df.iloc[i]['Lang']
        tweet = TextBlob(tweets_df.iloc[i]['Tweet'])
        try:
            tweets_df.set_value(i, 'Translated', str(tweet.translate(from_lang = from_language, to='en')))
        except:
            print(count)

    else:
        tweets_df.set_value(i, 'Translated', tweets_df.iloc[i]['Tweet'])
    count = count +1
    if (count % 500) == 0:
        print(count)
        
#%%
tweets_df.to_pickle("D:\\CBA\\Practicum\\Practicum_1\\IPLFinals.pk1")
