import tweepy, time, sys

CONSUMER_KEY = 'kssLzswVxosOd81IY6GemQfwf'
CONSUMER_SECRET = '2Z4aLjNYgGSvw6yl8KWr2ybbOQ14FhsOJKdKkA2ltaLwSF7RYA'
ACCESS_KEY = '888545055719518208-ILV02jz6QvptnirNgLbsuJnd0yD4uTE'
ACCESS_SECRET = 'HER9Phmg1KK9vVlQQMErbp946EPxlpNE2NLJIjDq4m03e'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open('funny.txt', 'r')
f = filename.readlines()
filename.close()




for line in f:
    api.update_status(line)
    time.sleep(60)  # Tweet every 2 minutes
