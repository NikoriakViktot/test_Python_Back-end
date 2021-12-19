import jmespath
import statistics


dict_api = {'dt': 1639904400, 'sunrise': 1639892182, 'sunset': 1639921973,
            'moonrise': 1639921740, 'moonset': 1639893540, 'moon_phase': 0.5,
            'temp': {'day': 0.9, 'min': -2.03, 'max': 2.38, 'night': 2.15, 'eve': 2.15,
                     'morn': -1.47},
            'feels_like': {'day': -5.43, 'night': -2.69, 'eve': -3.49, 'morn': -7.21},
            'pressure': 1006, 'humidity': 92, 'dew_point': -0.48, 'wind_speed': 8.75,
            'wind_deg': 235, 'wind_gust': 15.78,
            'weather': [{'id': 616, 'main': 'Snow', 'description': 'дощ та сніг', 'icon': '13d'}],
            'clouds': 100, 'pop': 1, 'rain': 1.44, 'snow': 0.42, 'uvi': 0.17}
# tep = tuple(jmespath.search('temp.*',d))
#
wind_speed = dict_api.get('wind_speed')
print(wind_speed)
if dict_api.get("rain") != None:
    rain = dict_api.get('rain')
else:
    rain = 0
if dict_api.get('snow') != None:
    snow = dict_api.get('snow')
else:
    snow = 0
pcp = round(rain+snow,2)
print(pcp)
#

id = (1639990800, -0.8, 2.77, 91, 1003, 80, 5.83, 3)
for x in id:
    print(enumerate(x,1))
# print(tep)
# tt = [ ]
# for x in d.get('temp').items():
#     tt.append(x)
# print(tt)
#
# t_day = jmespath.search('temp.day',d)
# t_night = jmespath.search('temp.night',d)
# t_eve = jmespath.search('temp.eve',d)
# t_morn = jmespath.search('temp.morn',d)
# temp_doba = [jmespath.search('temp.eve',d),jmespath.search('temp.night',d),
#              jmespath.search('temp.morn',d),jmespath.search('temp.day',d)]
# s = sum(temp_doba)/len(temp_doba)
#
# t_me = statistics.mean(temp_doba)
# temp_mean = round(statistics.fmean([jmespath.search('temp.eve',d),
#                               jmespath.search('temp.night',d),
#                               jmespath.search('temp.morn',d),
#                               jmespath.search('temp.day',d)]),1)

#
# print(t_me)
# print()
# print(round(temp_mean,1))
# print(s)
# print(t_eve,t_night,t_morn,t_day)

dict_api = {'dt': 1639990800, 'sunrise': 1639977041, 'sunset': 1640007105,
     'moonrise': 1640009820, 'moonset': 1639981560, 'moon_phase': 0.54,
     'temp': {'day': 0.93, 'min': -4.24, 'max': 0.93, 'night': -4.24,
              'eve': -0.03, 'morn': 0.72},
       'feels_like': {'day': -3.02, 'night': -8.25, 'eve': -4.11, 'morn': -4.56},
       'pressure': 1001, 'humidity': 88, 'dew_point': -0.67, 'wind_speed': 9.58,
       'wind_deg': 234, 'wind_gust': 16.49,
       'weather': [{'id': 601, 'main': 'Snow',
              'description': 'сніг', 'icon': '13d'}],
       'clouds': 100, 'pop': 1, 'snow': 3.94, 'uvi': 0.41}


if dict_api.get("rain") != None:
    rain = dict_api.get('rain')
else:
    rain = 0
if dict_api.get('snow') != None:
    snow = dict_api.get('snow')
else:
    snow = 0

pcp = round(rain+snow,2)
print(pcp)