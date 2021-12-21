from requests import get

# 3.	Створити файл request_samples.py із запитами до
# побудованого rest api з попереднього завдання.
# Для кожного  ресурсу повинно бути 2 приклади запитів.
# Форматувати вивід результатів запитів.

p = get('http://localhost:5000/cities').json()
print(p)
value_type = ['temp', 'pcp', 'clouds', 'pressure', 'humidity', 'wind_speed']
m = get('http://localhost:5000/mean?value_type=temp&city=Київ').json()
print(m)
g = get('http://localhost:5000/mean?value_type=pressure&city=Чернівці').json()
print(g)
f_1 = get('http://localhost:5000/forecast?city=Київ&start_dt=2021-12-22&end_dt=2021-12-23').json()
print(f_1)
f_2 = get('http://localhost:5000/forecast')
print(f_2)