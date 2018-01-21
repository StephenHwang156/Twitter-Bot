import config
import tweepy, time, sys


auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

os.chdir('target_folder')
for image in os.listdir('.'):
    api.update_with_media(image)
    time.sleep(5)
