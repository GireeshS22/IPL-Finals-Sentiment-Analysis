# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:43:38 2018

@author: Gireesh Sundaram
"""

#Importing the packages
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from textblob import TextBlob
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#%%
tweets_df = pd.read_pickle("D:\\CBA\\Practicum\\Practicum_1\\IPLFinals.pk1")

#%%
#Building a word cloud:
words = pd.Series(tweets_df["Translated"].tolist()).astype(str)

stop_words = ["https", "co", "rt"]
stop = set(stopwords.words('english'))

for i in range(0, len(words)):
    words[i] = " ".join([x for x in words[i].lower().split() if x not in stop_words])
    words[i] = " ".join([x for x in words[i].lower().split() if x not in stop])

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
tweet_text = tweets_df["Tweet"]
polarity = []
for i in tweet_text:
    txt = TextBlob(i)
    polarity.append( (txt.sentiment.polarity)*10 )
    
columns = ['Tweet','Polarity', 'DateTime']
data = pd.DataFrame(tweets_df, columns=columns)
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

#%%
sent = SentimentIntensityAnalyzer()

tweets_df["Compounded_polarity"] = tweets_df.Translated.apply(lambda x: sent.polarity_scores(x)['compound']*10)
tweets_df["Neutral"] = tweets_df.Translated.apply(lambda x: sent.polarity_scores(x)['neu']*10)
tweets_df["Negative"] = tweets_df.Translated.apply(lambda x: sent.polarity_scores(x)['neg']*10)
tweets_df["Positive"] = tweets_df.Tweet.apply(lambda x: sent.polarity_scores(x)['pos']*10)
tweets_df["Sentiment"] = ""
tweets_df.loc[tweets_df.Compounded_polarity > 0, "Sentiment"] = "Positive"
tweets_df.loc[tweets_df.Compounded_polarity == 0, "Sentiment"] = "Neutral"
tweets_df.loc[tweets_df.Compounded_polarity < 0, "Sentiment"] = "Negative"

#%%
tweets_df.Sentiment.value_counts().plot(kind = 'bar')

#%%
tweets_df.to_pickle("D:\\CBA\\Practicum\\Practicum_1\\IPLFinals.pk1")


#%%
tweets_df["tweet_lower"] = tweets_df['Translated'].str.lower()

PlayerSentiment = pd.DataFrame(columns= ["Player", "Translated", "Compounded_polarity", "Sentiment"])

def PlayerSentimentDef(PlayerName, SearchString):
    global PlayerSentiment
    print(PlayerName)
    print(SearchString)
    playerDF = tweets_df.loc[tweets_df.tweet_lower.str.contains(SearchString)]
    print(playerDF.head())
    playerDF["Player"] = PlayerName
    playerDF = playerDF[["Player", "Translated", "Compounded_polarity", "Sentiment"]]
    PlayerSentiment = PlayerSentiment.append(playerDF)
    
#%%
PlayerSentimentDef("MS Dhoni", "dhoni")
PlayerSentimentDef("S Watson", "watson")
PlayerSentimentDef("L Ngidi", "ngidi")
PlayerSentimentDef("SK Raina", "raina")
PlayerSentimentDef("R Jadeja", "jadeja")

PlayerSentimentDef("S Dhawan", "dhawan")
PlayerSentimentDef("KS Williamson", "williamson")
PlayerSentimentDef("YK Pathan", "pathan")
PlayerSentimentDef("B Kumar", "bhuvneshwar")
PlayerSentimentDef("Rashid Khan", "rashid")

PlayerSentimentDef("V Kohli", "kohli")
PlayerSentimentDef("SR Tendulkar", "sachin")
PlayerSentimentDef("R Ashwin", "ashwin")
PlayerSentimentDef("Sunil Narine", "narine")
PlayerSentimentDef("Sanju Samson", "sanju")


PlayerSentiment = PlayerSentiment.drop_duplicates()
PlayerSentiment = PlayerSentiment.loc[PlayerSentiment.Compounded_polarity != 0]

#%%
tweets_df["geo_lower"] = tweets_df['Geo'].str.lower()

city_not_null = tweets_df.dropna(subset = ["Geo"])

CitySentiment = pd.DataFrame(columns= ["City", "Translated", "Compounded_polarity", "Sentiment"])

def CitySentimentDef(CityName, SearchString):
    global CitySentiment
    playerDF = city_not_null.loc[city_not_null.geo_lower.str.contains(SearchString)]
    playerDF["City"] = CityName
    playerDF = playerDF[["City", "Translated", "Compounded_polarity", "Sentiment"]]
    CitySentiment = CitySentiment.append(playerDF)
    
CitySentimentDef("Chennai", "chennai")
CitySentimentDef("Kolkata", "kolkata")
CitySentimentDef("Mumbai", "mumbai")
CitySentimentDef("Hyderabad", "hyderabad")
CitySentimentDef("Bangalore", "bangalore")
CitySentimentDef("Bangalore", "Bengaluru")
CitySentimentDef("Delhi", "delhi")
CitySentimentDef("Jaipur", "jaipur")
CitySentimentDef("Pune", "pune")
CitySentimentDef("Coimbatore", "coimbatore")
CitySentimentDef("Dubai", "dubai")
CitySentimentDef("Paris", "paris")
CitySentimentDef("Dhaka", "dhaka")
CitySentimentDef("Kabul", "kabul")

CitySentiment = CitySentiment.drop_duplicates()
CitySentiment = CitySentiment.loc[CitySentiment.Compounded_polarity != 0]

#%%
dhoni = city_not_null.loc[city_not_null.tweet_lower.str.contains('dhoni')]
dhoni = dhoni[["Geo", "Translated", "Compounded_polarity", "Sentiment"]]
dhoni = dhoni.drop_duplicates()
dhoni = dhoni.loc[dhoni.Compounded_polarity != 0]

#%%
dhoni["geo_lower"] = dhoni['Geo'].str.lower()
DhoniSentiment = pd.DataFrame(columns= ["City", "Translated", "Compounded_polarity", "Sentiment"])

def CitySentimentDef(CityName, SearchString):
    global DhoniSentiment
    playerDF = dhoni.loc[dhoni.geo_lower.str.contains(SearchString)]
    playerDF["City"] = CityName
    playerDF = playerDF[["City", "Translated", "Compounded_polarity", "Sentiment"]]
    DhoniSentiment = DhoniSentiment.append(playerDF)
    
CitySentimentDef("Chennai", "chennai")
CitySentimentDef("Kolkata", "kolkata")
CitySentimentDef("Mumbai", "mumbai")
CitySentimentDef("Hyderabad", "hyderabad")
CitySentimentDef("Bangalore", "bangalore")
CitySentimentDef("Bangalore", "Bengaluru")
CitySentimentDef("Delhi", "delhi")
CitySentimentDef("Jaipur", "jaipur")
CitySentimentDef("Pune", "pune")
CitySentimentDef("Coimbatore", "coimbatore")
CitySentimentDef("Dubai", "dubai")
CitySentimentDef("Paris", "paris")
CitySentimentDef("Dhaka", "dhaka")
CitySentimentDef("Kabul", "kabul")

DhoniSentiment = DhoniSentiment.drop_duplicates()
DhoniSentiment = DhoniSentiment.loc[DhoniSentiment.Compounded_polarity != 0]

#%%
PlayerSentiment.to_excel("D:\\CBA\\Practicum\\Practicum_1\\PlayerSentiments.xlsx")
CitySentiment.to_excel("D:\\CBA\\Practicum\\Practicum_1\\CitySentiment.xlsx")
DhoniSentiment.to_excel("D:\\CBA\\Practicum\\Practicum_1\\DhoniSentiment.xlsx")