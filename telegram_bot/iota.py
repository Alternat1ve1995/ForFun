import requests
from bs4 import BeautifulSoup
from time import sleep

token = ''
url = "https://api.telegram.org/bot" + token + "/"
ids = []

while True:
    html_text = requests.get('https://prostocoin.com/c/iota').content
    soup = BeautifulSoup(html_text)
    price = soup.find('span', {'class': 'coinprice'}).text[1:] + ' $'
    for id in ids: requests.post(url + 'sendMessage', data={'chat_id': id, 'text': price})
    sleep(3600)
