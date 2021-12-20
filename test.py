import jmespath
import statistics
from requests import put, get
import sqlite3 as sq

def get():
    with sq.connect('city_weather.db') as con:
        # con.row_factory = sq.Row
        cur = con.cursor()
        # value_type = ['temp', 'pcp', 'clouds', 'pressure', 'humidity', 'wind_speed']
        value_type = "pcp"
        city = "Чернівці"
        cur.execute('PRAGMA foreign_keys = ON')
        cur.execute(f'''SELECT city, avg({value_type}) as mean FROM forecast
                    JOIN city ON forecast.city_id ==  city.id
                    WHERE city.id = (SELECT city.id FROM city  WHERE city="{city}")''')
        mean_select = cur.fetchone()
        mean_value = round(mean_select[1])
        city_select = mean_select[0]
        json_mean ={'value_type': value_type, 'mean': mean_value, 'city': city_select}
        return json_mean

print(get())

#
# p = get('http://localhost:5000/cities').json()
# print(p)
#
import jmespath
d = {'value_type': 'temp', 'city': 'Київ'}
print(jmespath.search('value_type',d))

import datetime
timestamp = 1339521878.04
value = datetime.datetime.fromtimestamp(timestamp)
print(value.strftime('%Y-%m-%d %H:%M:%S'))
#

from datetime import datetime
import time

# time tuple in local time to timestamp
time_tuple = (2021, 12, 22, 10, 00, 00, 0, 000,0)
t = (2021,12,25,10,00,00,0,000,0)
tx = time.mktime(t)
print(int(tx))
timestamp = time.mktime(time_tuple)
print (repr(timestamp))

with sq.connect('city_weather.db') as con:
    # start_dt_get = '2021-12-22 22:13:40'.split()
    # # st_dt = map()
    # print(start_dt_get)
    #
    #
    # end_dt_get = '2021-12-25'.split('-')
    # city = 'Чернівці'
    # # start_dt_get
    # t = (2021, 12, 25, 10, 00, 00, 0, 000, 0)
    # tx = time.mktime(t)
    # start_dt = ''
    # end_dt = ''
    # print(int(tx))

    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    cur.execute(f'''SELECT city,  date(date,'unixepoch') as date,
                              temp, pcp, clouds, pressure, humidity,
                              wind_speed  FROM forecast
                              JOIN city ON forecast.city_id ==  city.id
                              WHERE city.id = (SELECT city.id FROM city  WHERE city="Чернівці")
                              WHERE date(datetime(date, 'unixepoch'))
                              BETWEEN 2021-12-22 and 2021-12-25
                                                                ''')
#     SELECT
#     date(date, 'unixepoch') as date,
#     temp, pcp, clouds, pressure, humidity,
#     wind_speed, city
#     FROM
#     forecast
# JOIN
# city
# ON
# forecast.city_id == city.id
# WHERE
# city.id == (SELECT city.id FROM city  WHERE city="Чернівці")
# WHEN(date(datetime(date, 'unixepoch'))
# BETWEEN
# "2021-12-22" and "2021-12-24" )

forecast_select = cur.fetchall()
    print(forecast_select)