import requests
from bs4 import BeautifulSoup

base_url = "https://www.tasteatlas.com/most-popular-food-in-jamaica"
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')
tags = soup.find('h1')
print(tags)