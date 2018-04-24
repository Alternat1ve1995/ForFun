import requests
from bs4 import BeautifulSoup
from time import sleep

token = '531721148:AAExa6LAvTEqWjp_046pov4nFnOd_w680uA'
url = "https://api.telegram.org/bot" + token + "/"
ids = [347415690, ]

while True:
    html_text = requests.get('https://prostocoin.com/c/iota').content
    soup = BeautifulSoup(html_text)
    price = soup.find('span', {'class': 'coinprice'}).text[1:] + ' $'
    for id in ids: requests.post(url + 'sendMessage', data={'chat_id': id, 'text': price})
    sleep(3600)
