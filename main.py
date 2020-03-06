#Twitter Bot

#requires Twitter API

# use tweepy.org 

import tweepy
import time

# consumer_key,consumer_secret, access_toker, access_token_secret are default values from the Twitter API website (don't share them)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text) #prints tweets from the home timeline 

user = api.me() # prints information about user

print(user.name)
print(user.followers_count) # shows the number of followers 


def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(1000)


# BOT THAT FOLLOWS BACK

for follower in limit_handler(tweepy.Cursor(api.followers).items):
  if follower.name == 'follower-name':
    follow.follow()
    break

  print(follower.name)


#NARCISSIST BOT

search_string = 'bentley'

numberOfTweets = 2 

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
  try:
    tweet.favorite()
    print('That tweet was likeable')
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break

#RETWEET

search_string = 'bentley'

numberOfTweets = 2 

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
  try:
    tweet.retweet()
    print('That tweet was likeable')
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break


