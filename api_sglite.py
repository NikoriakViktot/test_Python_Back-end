from config import API_KEY
import requests
import sqlite3

# 1.	Використовуючи API сайту openweathermap.org, “витягнути” щоденний прогноз на 7 днів для п’яти
# українських міст на Ваш вибір. Отримані дані помістити в sqlite базу даних.
# Таблиці в базі даних повинні мати такі стовбці:
# date, temp(середня температура за добу в градусах цельсія),
# pcp (опади за день), clouds, pressure, humidity, wind_speed.


CITY= "Чернівці"
DATA = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_KEY}")

con = sqlite3.connect('forecast.db')
cur = con.cursor()
cur.execute('''CREATE TABLE stocks
               (date text, temp text, symbol text, qty real, price real)''')

    #
    # text = ""
    #
    # def __init__(self, chat_id=None):
    #     super().__init__(chat_id)
    #     self.user = self.get_user()
    #
    # def pog(self):
    #
    #                      f"Температура: {DATA.json().get('main')['temp']}°C",
    #                      f"Вологість: {DATA.json().get('main')['humidity']}%",
    #                      f"Швидкість  вітру: {DATA.json().get('wind')['speed']} km/h",
    #                      reply_markup=self.keyboard)
    #
    #
    #
    # def proccess(self, message: types.Message):
    #     if hasattr(message, 'data'):
    #         if message.data == 'nextstate:HelloState':
    #             return GidroPost(self.chat_id)
    #     return self
