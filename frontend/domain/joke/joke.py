class Joke:
    def __init__(self, id_: str, text: str):
        self.id_ = id_
        self.text = text

    def __eq__(self, other):
        if isinstance(other, Joke):
            return self.id_ == other.id_
        else:
            return False

    def serialize(self):
        return {'id_': self.id_, 'text': self.text}
