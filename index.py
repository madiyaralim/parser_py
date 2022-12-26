#parser.py
import io
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import json
import html


data = []

for p in range(2, 100000):

    url = f"https://krisha.kz/prodazha/doma/?page={p}"
    r = requests.get(url)
    sleep(30)
    soup = BeautifulSoup(r.text, 'lxml')

    houses = soup.findAll('div', class_='a-card__inc')

    for house in houses:

        house_data = house.find('a', class_='a-card__title').text
        house_price = house.find('div', class_='a-card__price').text
        house_street = house.find('div', class_='a-card__subtitle').text
        #house_title = house.find('div', class_='a-card__text-preview').text
        house_city = house.find('div', class_='card-stats__item').text

        #In [house_price]: str("house_price")
        # print(house_price)
        #data.append([house_data, house_price, house_city])

       # header = ['house_data', 'house_price','house_city']
       # df = pd.DataFrame(data, columns=header)
       # df.to_csv('E:/agronesie_parser/result/result.csv', sep=';', encoding='utf8')
        house = []
        house.append({
                'Цена': house_price,
                'Данные': house_data,
                'Город': house_city
            })
        print(house)
        with io.open('data.json' , 'w', encoding='utf8') as json_file:
            json.dump(house, json_file, indent=3, ensure_ascii=False)

        #json_str = json.dumps(houses_str, ensure_ascii=False).encode('utf8')
        #with open("data.json", "w") as file:
         #    file.write(json_str)

        #print(type(houses_str))

        #print(houses_json)

        #print(house_data)
        #print(house_price)
        #print(house_city)
        #print(house_street)
        #print(house_title)





