import jmespath
import statistics
from requests import put, get
import sqlite3 as sq
# def cities():
#     with sq.connect('city_weather.db') as con:
#         cur = con.cursor()
#         cur.execute("SELECT * FROM city")
#         city_list = [x for x in cur.fetchall()]
#         print(city_list)
#         serialized = []
#         for city in city_list:
#             serialized.append({
#                 'id':city[0],
#                 'city': city[1],
#                 'lat': city[2],
#                 'lon': city[3]
#                              })
#
#
#         print(serialized)
def mean():
    value_type = input("")
    with sq.connect('city_weather.db') as con:
        cur = con.cursor()
        cur.execute(f"SELECT {value_type} FROM weather")
cities()

p = get('http://localhost:5000/cities').json()
print(p)


