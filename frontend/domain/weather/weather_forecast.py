import requests

from frontend.domain.weather.measure import Measure


class ShortWeather:
    def __init__(self, temp: str, icon: str, date: str):
        self.temp = Measure(temp, "°C")
        self.icon = f"http://openweathermap.org/img/wn/{icon}@4x.png"
        self.date = date


class WeatherForecast:
    @staticmethod
    def _get_weather(url):
        response = requests.get(url)
        return response.json()

    def __init__(self, city_id):
        self.url = f"http://api.openweathermap.org/data/2.5/" \
                   f"forecast?id={city_id}&appid=27fe80d9af9f736e8cb148db7248a7e0&lang=ru&units=metric"
        self.forecast = []
        info = self._get_weather(self.url)
        for i in range(0, 40, 8):
            temp = info['list'][i]['main']['temp']
            icon = info['list'][i]['weather'][0]['icon']
            date = info['list'][i]['dt_txt']
            self.forecast.append(ShortWeather(temp, icon, date))

    def update(self):
        self.forecast.clear()
        info = self._get_weather(self.url)
        for i in range(0, 40, 8):
            temp = info['list'][i]['main']['temp']
            icon = info['list'][i]['weather'][0]['icon']
            date = info['list'][i]['dt_txt']
            self.forecast.append(ShortWeather(temp, icon, date))
