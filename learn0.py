import requests
from bs4 import BeautifulSoup

catalog = requests.get('https://www.ttn.by/computers_and_networks/laptops_and_accessories/laptops')

soup = BeautifulSoup(catalog.text)

list_of_video_adapter = soup.find_all('h2', attrs={
    'class': 'woocommerce-loop-product__title'
})

names = []

for video_adapter in list_of_video_adapter:
    names.append(video_adapter.text)

for laptop in names:
    print laptop
