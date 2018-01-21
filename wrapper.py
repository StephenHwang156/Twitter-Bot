import config
from bs4 import BeautifulSoup 
import tweepy, time, os, requests

url = 'https://ifunny.co/'

# creates a response to scrape off of
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# finds first 10 memes found under this class
image_tags = soup.find_all('img', class_='media__image',limit = 10)

# checks if the target folder exists and if not, creates one
if not os.path.exists('target_folder'):
    os.makedirs('target_folder')

# changes the directory to download pictures to right location
os.chdir('target_folder')

# will be used to name images
x = 0

# downloads each meme if
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('meme-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

for image in os.listdir('.'):
    api.update_with_media(image)
    time.sleep(5) # posts every time.sleep(x), x seconds
