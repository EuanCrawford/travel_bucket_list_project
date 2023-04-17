class Country():
    def __init__(self, name, continent, id = None):
        self.name = name
        self.continent = continent
        self.id = id
        self.cities = []