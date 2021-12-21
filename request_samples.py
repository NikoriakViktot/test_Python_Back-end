from requests import get

# 3.	Створити файл request_samples.py із запитами до
# побудованого rest api з попереднього завдання.
# Для кожного  ресурсу повинно бути 2 приклади запитів.
# Форматувати вивід результатів запитів.
#
p = get('http://localhost:5000/cities').json()
print(p)
value_type = ['temp', 'pcp', 'clouds', 'pressure', 'humidity', 'wind_speed']
m = get('http://localhost:5000/mean?value_type=temp&city=Київ').json()
print(m)
g = get('http://localhost:5000/mean?value_type=pressure&city=Чернівці').json()
print(g)
f_1 = get('http://localhost:5000/forecast?city=Київ&start_dt=2021-12-22&end_dt=2021-12-23').json()
print(f_1)
f_2 = get('http://localhost:5000/forecast?city=Львів&start_dt=2021-12-22&end_dt=2021-12-26').json()
print(f_2)

m_1 = get('http://localhost:5000/moving?value_type=pressure&city=Чернівці').json()
print(m_1)
m_2 = get('http://localhost:5000/moving?value_type=temp&city=Чернівці').json()
print(m_2)
m_3 = get('http://localhost:5000/moving?value_type=pcp&city=Чернівці').json()
print(m_3)
m_4 = get('http://localhost:5000/moving?value_type=clouds&city=Чернівці').json()
print(m_4)
m_5 = get('http://localhost:5000/moving?value_type=wind_speed&city=Чернівці').json()
print(m_5)