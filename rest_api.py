
# 2.	За допомогою flask-restfull побудувати rest-api з такими ресурсами та параметрами:
# 	/cities GET
# 	Return – список міст в базі даних в форматі json
# 	/mean GET
# 	Params:
# 		value_type – одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
# 		city – назва міста
# 	return – середнє значення вибраного параметру для вибраного міста в форматі json
# 	/records GET
# 		city – назва міста
# 		start_dt – початкова дата
# 		end_dt – кінцева дата
# 	return – значення всіх параметрів для вибраного міста впродовж вибраного терміну в форматі json
# 	/moving_mean
# 		value_type – одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
# 		city – назва міста
# 	return – значення вибраного параметру перераховане за алгоритмом ковзного
# середнього (moving average) для вибраного міста для всіх дат в форматі json
#
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)