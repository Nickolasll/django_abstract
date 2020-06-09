import json
import re
from pathlib import Path

from frontend.domain.weather.city import City


class Manager:
    def __init__(self):
        path = Path(Path(__file__).parent.absolute(), 'city.list.min.json')
        with open(path, 'r') as f:
            raw_cities = f.read()

        self._cities_info = json.loads(raw_cities)
        self.cities = [City(491687), City(499439)]

    def autocomplete(self, name):
        return [s for s in self._cities_info if re.search(f'^{name}', s.get('name', None), re.IGNORECASE) is not None]

    def add_city(self, city_id):
        self.cities.append(City(city_id))
