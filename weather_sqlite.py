import collections
import json
from config import API_KEY
import requests
import sqlite3 as sq
import time
import jmespath
import statistics



# Отримані дані помістити в sqlite базу даних.
# Таблиці в базі даних повинні мати такі стовбці:
# date, temp(середня температура за добу в градусах цельсія),
# pcp (опади за день), clouds, pressure, humidity, wind_speed.


def conect_city():
    with sq.connect('city_weather.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM city")
        city_list = [x for x in cur.fetchall()]
        return city_list


def reguests_api_openweather():
    # coord = collections.namedtuple('cord', ['lat', 'lon'])
    coord = [(x[0],x[2],x[3]) for x in conect_city()]
    for x in coord:
        id = x[0]
        lat = x[1]
        lon = x[2]
        data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?"
                    f"lat={lat}&lon={lon}&"
                    f"exclude=&appid={API_KEY}&units=metric&lang=ua")
        print(data)# response 409 забагато запросів до сервера
        api_weather = data.json().get('daily')
        print(api_weather)
        time.sleep(5)
        yield id, api_weather


def pars_weather():
    for x in reguests_api_openweather():
        id_city = x[0]
        list_weather = x[1]
        for dict_api in list_weather:
            print(dict_api)
            date = dict_api.get('dt')
            temp_mean = round(statistics.fmean([jmespath.search('temp.eve', dict_api),
                                                jmespath.search('temp.night', dict_api),
                                                jmespath.search('temp.morn', dict_api),
                                                jmespath.search('temp.day', dict_api)]), 1)
            clouds =dict_api.get('clouds')
            pressure = dict_api.get('pressure')
            humidity = dict_api.get('humidity')
            wind_speed = dict_api.get('wind_speed')
            if dict_api.get("rain") != None:
                rain = dict_api.get('rain')
            else:
                rain = 0
            if dict_api.get('snow') != None:
                snow = dict_api.get('snow')
            else:
                snow = 0
            pcp = round(rain + snow, 2)
            yield (date, temp_mean, pcp,
               clouds, pressure,
               humidity, wind_speed, id_city)



def save_db_weather(weather):
    with sq.connect('city_weather.db') as con:
        cur = con.cursor()
        id = 0
        for i in weather:
            data = list(i[:])
            id+=1
            data.insert(0,id)
            print(data)
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(''' INSERT INTO forecast
                    (id, date, temp,
                    pcp, clouds, pressure,
                    humidity,wind_speed,
                    city_id)
                    VALUES(?,?,?,?,?,?,?,?,?)''', data)
            con.commit()

if __name__ == '__main__':
    reguests_api_openweather()
    save_db_weather(pars_weather())




