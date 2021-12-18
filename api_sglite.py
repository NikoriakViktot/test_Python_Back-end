import collections
import requests
from bs4 import BeautifulSoup
import re
import sqlite3 as sq

# 1.	Використовуючи API сайту openweathermap.org,
# “витягнути” щоденний прогноз на 7 днів для п’яти
# українських міст на Ваш вибір.

def main():
    with sq.connect('city_weather.db') as con:
        cur = con.cursor()
        # cur.execute('PRAGMA foreign_keys = on')
        cur.execute('''CREATE TABLE  forecast
                                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        date INTEGER NOT NULL,
                                        temp REAL NOT NULL,
                                        pcp REAL,
                                        clouds INTEGER ,
                                        pressure INTEGER,
                                        humidity INTEGER,
                                        wind_speed REAL ,
                                        city_id INTEGER NOT NULL,
                                        FOREIGN KEY (city_id) REFERENCES city(id)
                                        ) ''')
        cur.execute('''CREATE TABLE IF NOT EXISTS city
                   (id INTEGER PRIMARY KEY,
                   city TEXT NOT NULL,
                   lat REAL NOT NULL,
                   lon REAL NOT NULL)''')
        con.commit()



def requests_city(url):
    get_city = requests.get(url=url)
    content = get_city.content
    soup_city = BeautifulSoup(content, "lxml")
    patern_city = re.compile('[А-Яа-я\b]|[А-Яа-я\b\sА-яа-я\b]')
    patern_coord = re.compile('(\d{2,}.\d{1,})..(\d{2,}.\d{1,}|\d{2,})')
    list_city = [''.join(i) for i in [re.findall(patern_city, str(i))
                                      for i in soup_city.find_all(class_="coordinates-items-left")]]
    list_coord = [i for i in [re.findall(patern_coord, str(i))
                              for i in soup_city.find_all(class_="coordinates-items-right")]]
    city_list = zip(enumerate(list_city, 1), list_coord)
    city = collections.namedtuple('city', ['id', 'name', 'lat', 'lon'])
    for i in city_list:
        id = i[0][0]
        city_name = i[0][1].strip()
        if not city_name == "":
            lat = i[1][0][0]
            lon = i[1][0][1]
            yield city(int(id), str(city_name), float(lat), float(lon))



def save_city_db(city):
        with sq.connect('city_weather.db') as con:
            cur = con.cursor()
            for i in city:
                data = i[:]
                print(data)
                cur.execute(''' INSERT INTO city
                           (id, city, lat, lon) 
                                 VALUES(?,?,?,?)''', data)
                con.commit()



# city = [i for i in zip([''.join(i) for i in
#         [re.findall(patern_city, str(i)) for i
#         in soup_city.find_all(class_="coordinates-items-left")]],
#         [i for i in [re.findall(patern_coord, str(i))
#         for i in soup_city.find_all(class_ = "coordinates-items-right")]])]

if __name__ == '__main__':
    main()
    url = 'https://time-in.ru/coordinates/ukraine'
    save_city_db(requests_city(url))






