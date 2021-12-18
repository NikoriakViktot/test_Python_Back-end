import collections
import json
from config import API_KEY
import requests
import sqlite3 as sq
import time



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
    coord = [(x[0],x[2],x[3])[0:5] for x in conect_city()]

    for x in coord:
        id = x[0]
        lat = x[1]
        lon = x[2]
        data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?"
                    f"lat={lat}&lon={lon}&"
                    f"exclude=&appid={API_KEY}&units=metric&lang=ua")
        print(data)# response 409 забагато запросів до сервера
        api_weather = data.json().get('daily')
        time.sleep(5)
        yield id, api_weather








def save_db_weather():
    for x in reguests_api_openweather():
        id_city = x[0]
        print(id_city)
        dict_api = x[1][1]
        print(dict_api)
        td = dict_api.get('dt')
        temp = dict_api.get('temp')
        clouds =dict_api.get('clouds')
        pressure = dict_api.get('pressure')
        humidity = dict_api.get('humidity')
        if dict_api.get("rain") != None:
            rain = dict_api.get('rain')
        else:
            rain = None
        if dict_api.get('snow') != None:
            snow = dict_api.get('snow')
        else:
            snow = None
    #
    # td = reguests_api_openweather()[0]
    # print(td)
    # temp = reguests_api_openweather()[1]
    # print(temp)
    # clouds = reguests_api_openweather()[2]
    # print(clouds)
    # pressure = reguests_api_openweather()[3]
    # print(pressure)
    # humidity = reguests_api_openweather()[4]
    # print(humidity)
    # raine = reguests_api_openweather()[5]
    # print(raine)
    # snow = reguests_api_openweather()[6]
    # print(snow)

    # with sq.connect('city_weather.db') as con:
    #      cur = con.cursor()
    #      cur.execute(''' INSERT INTO forecast
    #                   (id_city, city, lat, lon)
    #                   VALUES(?,?,?,?)''' )
    #      con.commit()







reguests_api_openweather()
save_db_weather()




