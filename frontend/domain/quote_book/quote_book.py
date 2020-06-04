import os
import random
from pathlib import Path

import requests

from backend.settings import BASE_DIR
from frontend.domain.quote_book.qoute import Quote
from faker import Faker
from .meta import countries


class QuoteBook:
    url = "http://rzhunemogu.ru/RandJSON.aspx?CType=4"
    error_quotes = [
        'Да пошло оно все'
    ]
    names = [
        'Джейсон Стетхем',
        'Конфуций',
        'Стив Джобс',
        'Мухаммед Али',
        'Элтон Джон',
        'Том Круз',
        'Брюс Ли',
        'Чак Норрис',
        'Евгений Петросян',
    ]

    def __init__(self):
        self.faker = Faker('ru_RU')
        self.pictures = os.listdir(Path(BASE_DIR, 'frontend', 'static', 'quote_book'))
        self.countries = countries

    def get_quotes(self, count=3):
        quotes = []
        random.shuffle(self.pictures)
        random.shuffle(self.names)
        random.shuffle(self.countries)
        error_quote = self.error_quotes[0]
        for i in range(count):
            picture = str(Path('quote_book', self.pictures[i]))
            name = self.names[i]
            profession = self.faker.job().lower()
            country = self.countries[i]
            year = f"{random.randint(1000, 2020)} год"
            response = requests.get(self.url)
            if response.status_code != 200:
                q = Quote(picture=picture, quote=error_quote, name=name, year=year, country=country,
                          profession=profession)
            else:
                # stupid encoding and bad quoting, so we use trim
                quote = response.content.decode(response.encoding)
                quote = quote.replace('{"content":"', '').split('.')[0]
                q = Quote(picture=picture, quote=quote, name=name, year=year, country=country, profession=profession)
            quotes.append(q)
        return quotes
