import tweepy
import numpy as np
from dicgen import *
import sys
sys.path.insert(1, '../')

'''
Script for downloading tweets from tweepy API
'''
# keys and tokens from the Twitter Dev Console
consumer_key = 'Exmf1lXUqO89Sm1tIk62CH8mc'
consumer_secret = 'Q6GLPLRmkX1XOljSl02Zb2x0YSdXxP28D2L3Wkw1e6RUgxCovu'
access_token = '1111728489164615682-JVqhenKoMkuvsNM60m9vJqHTOc8YbV'
access_token_secret = 'W8W0aKrrZ6i9N619jh4nJtXbFzS4150QmT01bMonpZNXT'

number_of_tweets=20 # number of tweets

# Function to extract tweets
def get_tweets(username): 
          
    # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

    # Access to user's access key and access secret 
    auth.set_access_token(access_token, access_token_secret)

    # Calling api 
    api = tweepy.API(auth) 

    # 20 tweets to be extracted 

    tweets = api.user_timeline(screen_name=username,count=number_of_tweets, tweet_mode='extended')

    # Empty Array 
    tmp=[]

    # create array of tweet information: username,  
    # tweet id, date/time, text 
    tweets_for_csv = [tweet.full_text for tweet in tweets] # CSV file created
    for j in tweets_for_csv: 

        # Appending tweets to the empty array tmp 
        tmp.append(j)  

    # Returning the tweets 
    return(tmp) 

# Function to extract tweets for usernames in a file
def get_user_tweets(hand_label):
    usertweets=[]
    tag=[]
    with open(hand_label) as f:
        for username in f:
            tag.append(username.split()[2])
            user = username.split()[1]
            print(user)
            usertweets.append( (user, get_tweets(user) ) )
    return usertweets, tag


usertweets , tag = get_user_tweets("../data/Hand_label")

# def gen_feature (user_arr):
#     feature = []
#     y=[]
#     for user,tweets in usertweets:
#         feat = []
#         for tweet in tweets:
#             feat.append(round(sentimentdeg(tweet),4))
#         feature.append(list(feat))
#
#     return feature

def gen_feature (user_arr):
    feature = np.zeros((len(user_arr) ,number_of_tweets ))
    y=[]
    usr =[]
    Tweets=[]
    for user,tweets in usertweets:
        usr.append(user)
        Tweets.append(tweets)

    for i in range(len(Tweets)):
        for j in range(len(Tweets[i])):
            feature[i][j] = round(sentimentdeg(Tweets[i][j]),4)
    return feature

sh = gen_feature(usertweets)
tag = [float(t) for t in tag]
tag=np.array(tag)

np.save("tag", tag)
np.save("array", sh)



print("done")

