import collections
import json
import time
import asyncio
from config import API_KEY
import requests
import sqlite3 as sq




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
        print(data)
        api_weather = data.json().get('daily')
        for x in api_weather:
            dict_api = dict(x)
            td = dict(id=id,dt=dict_api.get('dt'))
            temp = dict(id=id, temp=dict_api.get('temp'))
            clouds = dict(id=id, clouds=dict_api.get('clouds'))
            pressure = dict(id=id, pressure=dict_api.get('pressure'))
            humidity = dict(id=id, humidity=dict_api.get('humidity'))
            if dict_api.get("raine")!=None:
                raine = dict(id=id, raine=dict_api.get('raine'))
            else:
                raine = None
            if dict_api.get('snow') !=None:
                snow = dict(id=id, snow=dict_api.get('snow'))
            else:
                snow = None

            return [td.items(), temp, clouds.items(),
                    pressure.items(), humidity.items(),
                    raine.items(), snow.items()]





    # with sq.connect('city_weather.db') as con:
    #      cur = con.cursor()
    #      cur.execute(''' INSERT INTO forecast
    #                   (id_city, city, lat, lon)
    #                   VALUES(?,?,?,?)''' )
    #      con.commit()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         for post in post_request_station():
#                async with session.post(url, data=post) as resp:
#                    print(await resp.text())
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())



if __name__ == '__main__':
    reguests_api_openweather()
    save_db_weather()




