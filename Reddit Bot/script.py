#!/usr/bin/python
import praw

r = praw.Reddit("bot1")
submissions = r.subreddit("gifrecipes").hot(limit=5)

with open("reddit.txt", "w") as f:
    for i in submissions:
        # print(dir(i))
        if not i.stickied:
            url = i.url.replace("https://", "")
            f.write(i.title + " " + url + "\n")
