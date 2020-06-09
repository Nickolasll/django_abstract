from frontend.domain.weather.weather import Weather
from frontend.domain.weather.weather_forecast import WeatherForecast


class City:
    def __init__(self, id):
        self.id = id
        self.current_weather = Weather(id)
        meta = self.current_weather.get_meta()
        self.name = meta['city_name']
        self.country = meta['country']
        self.weather_forecast = WeatherForecast(id)

    def update(self):
        self.current_weather.update()
        self.weather_forecast.update()

    def __eq__(self, other):
        if isinstance(other, City):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
        else:
            return False
