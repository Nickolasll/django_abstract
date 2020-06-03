from uuid import uuid4
import random

import requests

from frontend.domain.joke.joke import Joke


class JokeFactory:
    url = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"
    error_jokes = [
        "Шутки закончились! :'(",
        "Никаких больше вечеринок!",
        "Что-то пошло не так... Идеи закончились",
    ]

    @classmethod
    def get_online_joke(cls):
        response = requests.get(cls.url)
        if response.status_code != 200:
            return Joke(id_=str(uuid4()), text=random.choice(cls.error_jokes))

        # stupid encoding and bad quoting, so we use trim
        decoded_text = response.content.decode(response.encoding)
        decoded_text = decoded_text.replace('{"content":"', '').replace('"}', '')
        return Joke(id_=str(uuid4()), text=decoded_text)
