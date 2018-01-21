import requests
from bs4 import BeautifulSoup 
import os

url = 'https://9gag.com/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

image_class_tags = soup.findAll(class_ = 'post-container', limit=25)

if not os.path.exists('target_folder'):
    os.makedirs('target_folder')

os.chdir('target_folder')

x = 0

for image in image_class_tags:
    try:
        img = image.find('img')
        url = img['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('meme-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
