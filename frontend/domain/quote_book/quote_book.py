import os
import random
from pathlib import Path

import requests

from backend.settings import BASE_DIR
from frontend.domain.quote_book.qoute import Quote


class QuoteBook:
    url = "http://rzhunemogu.ru/RandJSON.aspx?CType=4"
    error_quotes = [
        'Да пошло оно все'
    ]
    names = [
        'Джейсон Стетхем'
    ]
    countries = [
        'Испанский'
    ]
    professions = [
        'плотник'
    ]

    @classmethod
    def get_quote(cls):
        static_path = Path(BASE_DIR, 'frontend', 'static', 'quote_book')
        picture = str(Path('quote_book', random.choice(os.listdir(static_path))))
        name = random.choice(cls.names)
        year = f"{random.randint(1000, 2020)} год"
        country = random.choice(cls.countries)
        profession = random.choice(cls.professions)
        quote = random.choice(cls.error_quotes)

        response = requests.get(cls.url)
        if response.status_code != 200:
            return Quote(picture=picture, quote=quote, name=name, year=year, country=country, profession=profession)
        # stupid encoding and bad quoting, so we use trim
        quote = response.content.decode(response.encoding)
        quote = quote.replace('{"content":"', '').split('.')[0]
        return Quote(picture=picture, quote=quote, name=name, year=year, country=country, profession=profession)
