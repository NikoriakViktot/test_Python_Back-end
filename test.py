
def temp(**kwargs):
    for x in d.get('temp').items():
        # tt = []
        # print(x)
        t = list(x)
        # tt.append(t)

        # print(t)
        # a = t[1]
        # print(a)
        # tem = []
        # tem.append(a)
        yield t
d = {'dt': 1639904400, 'sunrise': 1639892182, 'sunset': 1639921973, 'moonrise': 1639921740, 'moonset': 1639893540, 'moon_phase': 0.5, 'temp': {'day': 0.9, 'min': -2.03, 'max': 2.38, 'night': 2.15, 'eve': 2.15, 'morn': -1.47}, 'feels_like': {'day': -5.43, 'night': -2.69, 'eve': -3.49, 'morn': -7.21}, 'pressure': 1006, 'humidity': 92, 'dew_point': -0.48, 'wind_speed': 8.75, 'wind_deg': 235, 'wind_gust': 15.78, 'weather': [{'id': 616, 'main': 'Snow', 'description': 'дощ та сніг', 'icon': '13d'}], 'clouds': 100, 'pop': 1, 'rain': 1.44, 'snow': 0.42, 'uvi': 0.17}

tt = []
for x in d.get('temp').items():
    tt.append(x)
    print(x)

    t = x[1]
print(tt)

    # t_day = x[1]
    # t_night = x[1]
    # t_eve = x [1]
    # t_morn = x [1]
    # # print(t_day)


# print(temp(**d))
    # print(x)
    # for t in list(x):
    #     temp=[x for x in t]
        # temp.append(t)
    # temp = [x for x in t]
    # temp+=[x for x in t]


    # t =
    #     print(temp)

    #
    # print(t_eve,t_night,t_morn,t_day)