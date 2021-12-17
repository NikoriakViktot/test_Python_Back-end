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

url = 'https://time-in.ru/coordinates/ukraine'
def requests_city(url):
    # url = 'https://time-in.ru/coordinates/ukraine'
    get_city = requests.get(url=url)
    content = get_city.content
    soup_city = BeautifulSoup(content, "lxml")
    ul_city = soup_city.find(class_="coordinates-items")
    city = [i for i in zip([''.join(i) for i in
            [re.findall('[А-Яа-я]', str(i) ) for i
            in ul_city.find_all(class_="coordinates-items-left")]],
            [i for i in [re.findall('\d{2,}.\d{1,}..\d{2,}.\d{1,}|\d{2,}', str(i))
            for i in ul_city.find_all(class_ = "coordinates-items-right")]])]
    return city

requests_city(url)

with sq.connect('city.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS city
                   (id_city INTEGER PRIMARY KEY,
                   city TEXT NOT NULL,
                   lat REAL NOT NULL,
                   lon REAL NOT NULL)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS forecast
                       (id INTEGER PRIMARY KEY,
                       date INTEGER NOT NULL,
                       temp REAL NOT NULL,
                       pcp REAL NOT NULL,
                       clouds INTEGER ,
                       pressure INTEGER,
                       humidity INTEGER,
                       wind_speed REAL NOT NULL)''')
    con.commit()




DATA = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=&appid={API_KEY}&units=metric&lang=ua")

t = DATA.json().get('weather')
# p = DATA.json().get('minutely')
c = DATA.json().get('clouds')
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

