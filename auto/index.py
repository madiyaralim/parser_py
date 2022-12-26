#parser.py #auto
import io
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import json
import html
import re
import  psycopg2

data = []

for p in range(2, 4):
    for country in range(8, 14):                                                                                              #12Japan 11USA 10Russia 9Korea 8China 14Europe 13Other
        url = f"https://kolesa.kz/cars/?mark-country={country}&year[from]=2006&year[to]=2022&page=2"   #p обявить для range!!!
        r = requests.get(url)
        sleep(5)
        soup = BeautifulSoup(r.text, 'lxml')
        print(p)
        autos = soup.findAll('div', class_='a-card a-card--pay-yellow js__a-card')

    for auto in autos:

        auto_data = auto.find('h5', class_='a-card__title').find('a', class_='a-card__link').text
        auto_price = auto.find('span', class_='a-card__price').text
        auto_description = auto.find('p', class_='a-card__description').text
        auto_link = auto.find('h5', class_='a-card__title').find('a', class_='a-card__link').get('href')
        link_kolesa = 'https://kolesa.kz'
        year = re.findall(r'\d{4}', auto_description)
        link_for_db = link_kolesa + auto_link
        #print(year)



        #auto_title = auto.find('div', class_='a-card__text-preview').text
        #auto_city = auto.find('div', class_='card-stats__item').text
        auto = []
        auto.append({
            'Цена': auto_price,
            'Модель': auto_data,
            'Год': year,
            'Ссылка': link_kolesa + auto_link

        })

        print(auto.append)

        #with io.open('data.json' , 'w', encoding='utf8') as json_file:
         #   json.dump(auto, json_file, indent=3, ensure_ascii=False)

        #DB Connect
        # connection = psycopg2.connect(
        #     user="postgres",
        #     password="db2022!!!",
        #     host="127.0.0.1",
        #     port="5432",
        #     database="parser_db")
        # print("Database opened successfully")
        #
        # # cur = connection.cursor()            #Create table
        # # cur.execute('''CREATE TABLE PRICE_AUTO
        # #      (MODEL TEXT NOT NULL,
        # #      YEAR TEXT NOT NULL,
        # #      PRICE TEXT NOT NULL,
        # #      LINK CHAR(100));''')
        # #
        # # print("Table created successfully")
        # cur = connection.cursor()
        # cur.execute("INSERT INTO PRICE_AUTO(MODEL,YEAR,PRICE,LINK  ) VALUES (%s, %s, %s, %s)", [auto_data, year, auto_price, link_for_db ])
        # connection.commit()
        # connection.close()







