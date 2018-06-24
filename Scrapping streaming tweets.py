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
auth = tweepy.OAuthHandler("LpyWeEsv0cabU0tUJEZHhvxwi", "MIowj3BMHSqzRR5ENzCMoBYSCkvTmZRwfvgk9UeOmZ1yKjksyY")
auth.set_access_token("800064916258291712-7wKaBKKo5QswPrl5YT4c5nGXplLpYfN", "jBpVALhJpq9JUS2Qme0klS3X3iH0v8IIMFIkylV4himk9")

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
tweets_df.to_csv("D:\\CBA\\Practicum\\Practicum_1\\tweets.csv")

#%%
#To filter the dataset by Dhoni
tweets_df["tweet_lower"] = tweets_df['Tweet'].str.lower()
Dhoni = tweets_df.loc[tweets_df.tweet_lower.str.contains("dhoni") | tweets_df.tweet_lower.str.contains("msd")]

#%%
#Twitter streaming to get the realtime trend for a topic and saving it into a dataframe
class listener(StreamListener):

    def on_data(self, data):
#        print(data)
        
        with open("D:\\CBA\\Practicum\\Practicum_1\\KaalaTheRageOfRajinikanth.json", "a") as streaming:
            streaming.write(data)
            
        return(True)

    def on_error(self, status):
        print(status)
        
twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=["KaalaTheRageOfRajinikanth"])

#%%
#Loading the JSON file saved as dictionary values
tweets = []
for line in open('D:\\CBA\\Practicum\\Practicum_1\\Trends.txt', 'r'):
    tweets.append(json.loads(line))
    
sample = []
for line in open('D:\\CBA\\Practicum\\Practicum_1\\sample.txt', 'r'):
    sample.append(json.loads(line))    
    
#%%
#Converting the loaded dictionary into a dataframe with useful information
tweets_df = pd.DataFrame(columns = ["Username", "Tweet", "Liks", "Retweet", "DateTime", "Lang", "Geo", "Source"])

for tweet in tweets:
    tweets_data = pd.DataFrame([[tweet['user']['name'], tweet['text'], tweet['favorite_count'], tweet['retweet_count'], tweet['created_at'], tweet['lang'], tweet['user']['location'], tweet['source']]], columns = ["Username", "Tweet", "Liks", "Retweet", "DateTime", "Lang", "Geo", "Source"])
    tweets_df = tweets_df.append(tweets_data, ignore_index=True)
    
#%%
#Filtering the data which is in english:
tweets_in_en = tweets_df[tweets_df.Lang == "en"]

#%%
#Building a word cloud:
words = pd.Series(tweets_in_en["Tweet"].tolist()).astype(str)

stop = set(stopwords.words('english'))    
cloud = WordCloud(width=900, height=900,
                  stopwords=(stop), 
                  colormap='hsv').generate(''.join(words.astype(str)))
plt.figure(figsize=(15, 15))
plt.imshow(cloud)
plt.axis('off')
plt.show()

#%%
#using textblob
tweet_text = tweets_in_en["Tweet"]
polarity = []
for i in tweet_text:
    txt = TextBlob(i)
    polarity.append( (txt.sentiment.polarity)*10 )
    
columns = ['Tweet','Polarity', 'DateTime']
data = pd.DataFrame(tweets_in_en, columns=columns)
data.head()
data['Polarity'] = pd.DataFrame(polarity)

data_by_polarity = data.sort_values(by='Polarity',ascending=False)
data_by_polarity = data_by_polarity.dropna()

dt = data_by_polarity['Polarity']
fig, ax = plt.subplots(figsize=(10,7))
ax.set_title("Frequency of tweet sentiment!")
ax.set_xlabel("Sentiment amount")
ax.set_ylabel("Amount of tweets")
mean = np.mean(dt)
ax.hist(dt)
fig.tight_layout()
plt.show()