import requests
from bs4 import BeautifulSoup 
import os

url = 'https://ifunny.co/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

image_tags = soup.find_all('img', class_='media__image',limit = 10)

if not os.path.exists('target_folder'):
    os.makedirs('target_folder')

os.chdir('target_folder')

x = 0

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
