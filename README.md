# IPL-Finals-Sentiment-Analysis
This repository contains the codes and the output materials to the project that I did for ISB CBA term 1 practicum on sentiment analysis for IPL Finals

# Executive Summary:
Indian Premier League (IPL) is one of the most viewed and followed sports events in India. In this project, the tweets that were recorded during the final match of IPL 2018 between Chennai Super Kings (CSK) and Sun Risers Hyderabad (SRH) are analyzed for sentiment level for various players and in different major cities in India. The objective of this study is to see how the fans reacted on twitter to the finals of this year’s IPL.

# Introduction:
During the peak cricket season in India from April till end of May, IPL is consistently proving to be a major factor of entrainment for many people in India. This year’s IPL marked Chennai Super King’s come back season after two years of ban from the league and the team lifted the trophy for the third time in 10 years under the captaincy of MS Dhoni. The purpose behind this study is to analyze the sentiments for different players from tweets that were tweeted under the hashtag #IPLFinals2018.

# Motivation for this study:
As it is always for popularity of players and teams, there as much haters for CSK as fans. There are endless discussions and threads on social media arguing that IPL is scripted. The motivation for this study is to hence capture the fan sentiment of how tweets were posted during the IPL finals match and to compare the sentiment level for different players and tweets from different cities.

# Questions & Hypothesis:
The questions/hypothesis that I would like to test using the data collected are:
1.	What is the sentiment level for players from both the team? Which player had the highest sentiment score and which player had the lowest sentiment score? 
2.	What is the sentiment level across major cities in India? Was the average sentiment score same across all the cities in India?
H0: Mean sentiment score is same across all the cities: µChennai = µMumbai = µDelhi = µBangalore = µHyderabad = µOther Cities
Ha: Mean sentiment score is not same across all the cities: µChennai ≠ µMumbai ≠ µDelhi ≠ µBangalore ≠ µHyderabad ≠ µOther Cities
3.	What is the sentiment score for MS Dhoni across major cities in India? Were there more positive tweets or negative tweets mentioning MS Dhoni?

# Data collection:
1.	Trend data from https://trends.google.co.in using search terms “IPL” and “CSK” from 01-Jan-2018 to 20-Jun-2018.
2.	66,000 tweets collected from twitter using the trend hashtag #IPLFinals2018 through out the match on 27-May-2018.
Tools used:
1.	Python:
a.	Tweepy for gathering tweets
b.	TextBlob for translating tweets other than in English
c.	NLTK for sentiment scores calculation
2.	Tableau for visualization
3.	R-Studio for statistical analysis

# Data cleaning and preparation:
1.	Tweepy twitter API was used to gather the twitter streaming trends for the live tweets. The tweets were dumped in a JSON file.
2.	The JSON file is loaded back into the python environment and the fields such as: Username, Tweet, Likes, Retweets, DateTime, Language, Geography and Source are converted into a dataframe.
3.	The language in which the tweets that are other than in English language are analyzed. The following graph shows the tweets that are in language other than in English:
 
As the chart above shows, there are totally 3,615 tweets in Hindi and 1,064 tweets in Tamil and 2,474 in unidentified language.
4.	The tweets in Hindi and Tamil are converted into English using TextBlob language conversion. The new translated tweets are stored in a separate column in the dataframe.
5.	Using NLKT’s SentimentIntensityAnalyzer module, a compounded sentiment polarity score and sentiment (either positive, negative or neutral) is assigned to all the tweets. The sentiment scores which are obtained in the range of -1 to +1 are then multiplied by 10 to get the scores in the range of -10 to +10 for ease of analysis.
6.	The tweets are then searched to see if player names such as “Dhoni” or “Watson” is present in the tweet text. If the names are found, then the tweet & sentiment score are placed in a separate dataset for analysis.

# Analysis:
1.	Google trend data: The google trend interest data taken from 01-Jan-2018 to 20-Jun-2018 shows the trend level for IPL and CSK for the period. The blue line indicates that of IPL and the red line indicates that of CSK. The initial spike shows the increase in search volume during the IPL auctions. During the match, both IPL and CSK have had similar search trends but CSK has had low volumes of searches. On the day of finals, CSK and IPL has had almost same search score.
 
2.	Basic sentiment analysis: Based on NLTK. SentimentIntensityAnalyzer’s classification into positive, negative or neutral for all the tweets, the following chart is prepared to see the sentiment for overall tweets. It can be noted that out of 66,000 tweets, around 40,000 tweets are positive, 20,000 tweets are neutral and about 6,000 tweets are negative in sentiment. The amount of positive tweets far outweigh the amount of negative tweets.
 
3.	Average sentiment score by players: The players choose for this analysis are mentioned below. 5 players from CSK, 5 players from SRH and 5 players who did not play in the finals were taken for this analysis. As we can see below, S Narine has the highest positive sentiment score. This is because he was awarded the player of the series for his exceptional performance for KKR. Hence there are many tweets heavily positively aligned mentioning him. Out of all the players B Kumar is the only player who has a negative sentiment score. Though S Watson was the top scorer of the game, his sentiment score is not the highest of all. We can see that S Tendulkar has the 5th highest sentiment score, though he retired from the sport many years back.
 
To extend this further, I have built a two-sided bar chart with positive and negative scores on both the side. The below chart further shows that S Narine did not have any tweets against him and his performance well deserved the Player of the Series award. Out of all the players taken for analysis, S Samson is the player with the highest negative score. On further analyzing the negative polarity for S Watson, there are tweets like “Watson is on fire fire fire” which NLTK classifies as highly negative are contributing to the negative polarity score of Watson, though they are not actually negative.
 
4.	Average sentiment score across cities: There is only a small variation in the average sentiment score across the major cities. The score varies between 5.6 to 4.2 as shown below. 
 
But is it enough to ignore the variation in the sentiment score and conclude that the average sentiment score across all the cities were same? For this I set up a hypothesis test as below:
H0: Mean sentiment score is same across all the cities: µChennai = µMumbai = µDelhi = µBangalore = µHyderabad = µOther Cities
Ha: Mean sentiment score is not same across all the cities: µChennai ≠ µMumbai ≠ µDelhi ≠ µBangalore ≠ µHyderabad ≠ µOther Cities
The below shows the boxplot of sentiment scores across different cities:
 
Using ANOVA, the below results are obtained:
 
At α = 0.05, since the P value is 0.01, we reject the null hypothesis.
5.	Sentiment level for Dhoni across cities: In my next analysis, sentiment level for MS Dhoni across the cities are measured. The below chart shows the positive and negative sentiment scores for tweets mentioning Dhoni. As it can be seen, the score is fairly the same across multiple cities.
 
On performing ANOVA on this data, the below mentioned results are obtained:
 
 
At α = 0.05 since the P-Value is at 0.759, I fail to reject the null hypothesis and can conclude that the average sentiment score for the tweets mentioning Dhoni is same across multiple cities.
Conclusion and Business Recommendations:
Based on the analysis above, the conclusion can be made that the sentiment level for players vary vastly. This sentiment score could be an important factor to the advertisement agencies and to the brands who wish to sign-up certain players as ambassadors. The sentiment level for players across cities should also be measured based on the target region for the brands to market their product efficiently in the market. The analysis could be extended for different sports and league games to find out who the fans have a positive sentiment with. 

# Appendix and other notable related works:
1.	A basic word cloud is first developed from all the tweet texts in that are gathered using WordCloud module in python. This shows the most tweeted words during the finals:
 
# References and Credits:
1.	Priya Ananthram’s Sentiment analysis of tweets: https://www.kaggle.com/priyaananthram/sentiment-analysis-of-tweets
2.	Tweepy documentation: http://docs.tweepy.org/en/v3.5.0/
