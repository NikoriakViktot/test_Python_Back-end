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


#
