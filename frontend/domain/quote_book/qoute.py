class Quote:
    def __init__(self, picture: str, quote: str, name: str, country: str, profession: str, year: str):
        self.picture = picture
        self.quote = quote
        self.name = name
        self.profession = f"{country} {profession}"
        self.year = year
