from requests import get

# 3.	Створити файл request_samples.py із запитами до
# побудованого rest api з попереднього завдання.
# Для кожного  ресурсу повинно бути 2 приклади запитів.
# Форматувати вивід результатів запитів.

p = get('http://localhost:5000/cities').json()
print(p)