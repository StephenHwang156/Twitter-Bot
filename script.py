import config
import tweepy, time, sys


auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

filename = open('funny.txt', 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(3)  # Tweet every 3 seconds
