#parser.py #auto
import io
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import json
import html
import re

data = []

for p in range(2, 4):

    url = f"https://kolesa.kz/cars/?mark-country=14&year[from]=2006&year[to]=2022&page=2{p}"
    r = requests.get(url)
    sleep(5)
    soup = BeautifulSoup(r.text, 'lxml')
    print(p)
    autos = soup.findAll('div', class_='a-card a-card--pay-yellow js__a-card')

    for auto in autos:

        auto_data = auto.find('a', class_='a-card__link').text
        auto_price = auto.find('span', class_='a-card__price').text
        auto_description = auto.find('p', class_='a-card__description').text
        year = re.findall(r'\d{2})', auto_description)
        #auto_title = auto.find('div', class_='a-card__text-preview').text
        #auto_city = auto.find('div', class_='card-stats__item').text


        print(year)
       # auto = []
      #  auto.append({
       #         'Цена': auto_price,
       #         'Модель': auto_data,
      #          'Данные': re.split("\, |\,", auto_description)
      #      })
        #print(auto)
        #with io.open('data.json' , 'w', encoding='utf8') as json_file:
         #   json.dump(auto, json_file, indent=3, ensure_ascii=False)






