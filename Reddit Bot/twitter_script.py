import tweepy, time
import config

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

with open("reddit.txt", "r") as f:
    for line in f.readlines():
        try:
            api.update_status(line)
            time.sleep(5) # posts every time.sleep(x), x seconds
        except:
            pass
