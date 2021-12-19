# 2.	За допомогою flask-restfull побудувати rest-api з такими ресурсами та параметрами:
from flask import Flask
import sqlite3 as sq
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
client = app.test_client()

# 	/cities GET
# 	Return – список міст в базі даних в форматі json
class Cities(Resource):
    def get(self):
        with sq.connect('city_weather.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM city")
            city_list = [x for x in cur.fetchall()]
            city_json = []
            for city in city_list:
                city_decod = city[1]
                city_json.append( {
                    'id':city[0],
                    'city': city[1],
                    'lat': city[2],
                    'lon': city[3] })
            return city_json



    # 	/mean GET
    # 	Params:
    # 		value_type – одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
    # 		city – назва міста
    # 	return – середнє значення вибраного параметру для вибраного міста в форматі json




# 	/records GET
# 		city – назва міста
# 		start_dt – початкова дата
# 		end_dt – кінцева дата
#return – значення всіх параметрів для вибраного міста впродовж вибраного терміну в форматі json




# 	/moving_mean
# 		value_type – одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
# 		city – назва міста
# 	return – значення вибраного параметру перераховане за алгоритмом ковзного
# середнього (moving average) для вибраного міста для всіх дат в форматі json
#
api.add_resource(Cities, '/cities')

if __name__ == '__main__':
    app.run(debug=True)