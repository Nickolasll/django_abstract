from datetime import datetime

import requests
from dateutil import tz

from frontend.domain.weather.measure import Measure


class Weather:
    @staticmethod
    def _get_weather(url):
        response = requests.get(url)
        return response.json()

    def __init__(self, city_id):
        self.url = f"http://api.openweathermap.org/data/2.5/" \
                   f"weather?id={city_id}&appid=27fe80d9af9f736e8cb148db7248a7e0&lang=ru&units=metric"
        info = self._get_weather(self.url)
        self.id = info['dt']
        self.date = info.get('dt_txt', datetime.now().astimezone(tz.gettz('Europe/Moscow')).strftime("%H:%M"))
        self.wind_speed = Measure(info['wind']['speed'], "м/c")
        self.description = info['weather'][0]['description'].capitalize()
        self.icon = f"http://openweathermap.org/img/wn/{info['weather'][0]['icon']}@4x.png"
        self.temp = Measure(info['main']['temp'], "°C")
        self.feels_like = Measure(info['main']['feels_like'], "°C")
        self.pressure = Measure(info['main']['pressure'], "гПа")
        self.humidity = Measure(info['main']['humidity'], "%")

        self._meta = {
            'city_name': info['name'],
            'country': info['sys']['country'],
        }

    def update(self):
        info = self._get_weather(self.url)
        self.id = info['dt']
        self.date = info.get('dt_txt', datetime.now().astimezone(tz.gettz('Europe/Moscow')).strftime("%H:%M"))
        self.wind_speed = Measure(info['wind']['speed'], "м/c")
        self.description = info['weather'][0]['description'].capitalize()
        self.icon = f"http://openweathermap.org/img/wn/{info['weather'][0]['icon']}@4x.png"
        self.temp = Measure(info['main']['temp'], "°C")
        self.feels_like = Measure(info['main']['feels_like'], "°C")
        self.pressure = Measure(info['main']['pressure'], "гПа")
        self.humidity = Measure(info['main']['humidity'], "%")

    def get_meta(self):
        return self._meta
