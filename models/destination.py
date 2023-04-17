class Destination():
    def __init__(self, city, country, visited, review, id = None):
        self.city = city
        self.country = country
        self.visited = visited
        self.review = review
        self.id = id

    def return_review(self):
        return f"{self.review}"