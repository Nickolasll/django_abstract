import json
from uuid import uuid4

import requests

from frontend.domain.joke.joke import Joke


class JokeFactory:
    url = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"

    @classmethod
    def get_online_joke(cls):
        response = requests.get(cls.url)
        if response.status_code != 200:
            return None
        # stupid encoding and bad quoting, so we use trim
        decoded_text = response.content.decode(response.encoding)
        decoded_text = decoded_text.replace('{"content":"', '').replace('"}', '')
        return Joke(id_=str(uuid4()), text=decoded_text)

    @classmethod
    def create_from_repo(cls):
        pass
