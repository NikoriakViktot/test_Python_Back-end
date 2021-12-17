import collections
import sys
import traceback

from config import API_KEY
import requests
from bs4 import BeautifulSoup
import re
import json
import lxml
import sqlite3 as sq

# 1.	Використовуючи API сайту openweathermap.org, “витягнути” щоденний прогноз на 7 днів для п’яти
# українських міст на Ваш вибір. Отримані дані помістити в sqlite базу даних.
# Таблиці в базі даних повинні мати такі стовбці:
# date, temp(середня температура за добу в градусах цельсія),
# pcp (опади за день), clouds, pressure, humidity, wind_speed.
with sq.connect('city_weather.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS city
                   (id_city INTEGER PRIMARY KEY,
                   city TEXT NOT NULL,
                   lat REAL NOT NULL,
                   lon REAL NOT NULL)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS forecast
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       date INTEGER NOT NULL,
                       temp REAL NOT NULL,
                       pcp REAL NOT NULL,
                       clouds INTEGER ,
                       pressure INTEGER,
                       humidity INTEGER,
                       wind_speed REAL NOT NULL)''')
    con.commit()

    url = 'https://time-in.ru/coordinates/ukraine'
    def requests_city(url):
        get_city = requests.get(url=url)
        content = get_city.content
        soup_city = BeautifulSoup(content, "lxml")
        patern_city = re.compile('[А-Яа-я\b]|[А-Яа-я\b\sА-яа-я\b]')
        patern_coord = re.compile('(\d{2,}.\d{1,})..(\d{2,}.\d{1,}|\d{2,})')
        list_city = [''.join(i) for i in[re.findall(patern_city, str(i))
                      for i in soup_city.find_all(class_="coordinates-items-left")]]
        list_coord =  [i for i in [re.findall(patern_coord, str(i))
                        for i in soup_city.find_all(class_ = "coordinates-items-right")]]
        city_list = zip(enumerate(list_city,1),list_coord)
        city = collections.namedtuple('city', ['id', 'name', 'lat', 'lon'])
        for i in city_list:
            id = i[0][0]
            city_name = i[0][1].strip()
            if not city_name == "":
                lat = i[1][0][0]
                lon = i[1][0][1]
                yield city(int(id),str(city_name),float(lat),float(lon))

    # city = [i for i in zip([''.join(i) for i in
    #         [re.findall(patern_city, str(i)) for i
    #         in soup_city.find_all(class_="coordinates-items-left")]],
    #         [i for i in [re.findall(patern_coord, str(i))
    #         for i in soup_city.find_all(class_ = "coordinates-items-right")]])]

    def save_city_db(city):
        for i in city:
            data = i[:]
            print(data)
            cur.execute( ''' INSERT INTO city
                         (id_city, city, lat, lon) 
                         VALUES(?,?,?,?)''', data)
            con.commit()



            # except sq.Error as error:
            #     print("Не удалось вставить данные в таблицу sqlite")
            #     print("Класс исключения: ", error.__class__)
            # finally:
            #     if (cur):
            #         cur.close()
            #         print("Соединение с SQLite закрыто")




            # cur.executemany("insert into characters(c) values (?)", char_generator())
            #
            # cur.execute("select c from characters")
            # print(cur.fetchall())






    # requests_city(url)
    save_city_db(requests_city(url))


DATA = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=&appid={API_KEY}&units=metric&lang=ua")

t = DATA.json().get('weather')
# p = DATA.json().get('minutely')
c = DATA.json().get('daily')
pr = DATA.json().get('daily')
h = DATA.json().get('humidity')
w = DATA.json().get('wind_speed')
# r = DATA.json().get('current')

print(pr)
# get('main')['temp']}°C",
#                          f"Вологість: {DATA.json().get('main')['humidity']}%",
#                          f"Швидкість  вітру: {DATA.json().get('wind')['speed']} km/h",)





    # def pog(self):
    #
    #                      f"Температура: {DATA.json().get('main')['temp']}°C",
    #                      f"Вологість: {DATA.json().get('main')['humidity']}%",
    #                      f"Швидкість  вітру: {DATA.json().get('wind')['speed']} km/h",
    #                      reply_markup=self.keyboard)

