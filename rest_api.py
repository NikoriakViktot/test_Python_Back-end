# 2.	За допомогою flask-restfull побудувати rest-api з такими ресурсами та параметрами:
from flask import Flask
import sqlite3 as sq
from flask_restful import Resource, Api
from flask_restful import reqparse
import jmespath


app = Flask(__name__)
api = Api(app)
client = app.test_client()

# parser.add_argument('value_type', type=str)
# parser.add_argument('city', type=str)

# value_types = args['value_type']
# print(value_types)
#
#
# citis = args['city']
# print(citis)
# value_type = " "
# city = " "


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



class Mean(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("value_type")
        parser.add_argument("city")
        params = parser.parse_args()
        request_get={
                'value_type': params["value_type"],
                'city': params["city"]
                     }
        with sq.connect('city_weather.db') as con:
            value_type= jmespath.search('value_type',request_get)
            city = jmespath.search('city',request_get)
            # con.row_factory = sq.Row
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(f'''SELECT city, avg({value_type}) as mean FROM forecast
                        JOIN city ON forecast.city_id ==  city.id
                        WHERE city.id = (SELECT city.id FROM city  WHERE city="{city}")''')
            mean_select = cur.fetchone()
            mean_value = round(mean_select[1])
            city_select = mean_select[0]
            json_mean = {'value_type': value_type, 'mean': mean_value, 'city': city_select}
            return json_mean


       # /records GET
# 		city – назва міста
# 		start_dt – початкова дата
# 		end_dt – кінцева дата
#return – значення всіх параметрів для вибраного міста впродовж вибраного терміну в форматі json

class Forecast(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("start_dt")
        parser.add_argument("end_dt")
        parser.add_argument("city")
        params = parser.parse_args()
        request_get={
                'start_dt': params["start_dt"],
                'end_dt': params["end_dt"],
                'city': params["city"]
                     }
        with sq.connect('city_weather.db') as con:
            start_dt= jmespath.search('start_dt',request_get)
            end_dt = jmespath.search('end_dt', request_get)
            city = jmespath.search('city',request_get)

            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(f'''SELECT city,  as mean FROM forecast
                        JOIN city ON forecast.city_id ==  city.id
                        WHERE city.id = (SELECT city.id FROM city  WHERE city="{city}")''')
            mean_select = cur.fetchone()
            mean_value = round(mean_select[1])
            city_select = mean_select[0]
            json_mean = {'value_type': value_type, 'mean': mean_value, 'city': city_select}
            return json_mean




# 	/moving_mean
# 		value_type – одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
# 		city – назва міста
# 	return – значення вибраного параметру перераховане за алгоритмом ковзного
# середнього (moving average) для вибраного міста для всіх дат в форматі json
#
api.add_resource(Cities, '/cities')
api.add_resource(Mean, '/mean' )
api.add_resource(Forecast, '/forecast' )

if __name__ == '__main__':
    app.run(debug=True)
    s = Mean.get()
    print(s)