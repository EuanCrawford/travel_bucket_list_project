import pdb

from models.city import City
from models.country import Country
from models.destination import Destination

import repositories.destination_repository as destination_repository
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

destination_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()

country1 = Country("England", "Europe")
country_repository.save(country1)
country2 = Country("France", "Europe")
country_repository.save(country2)
country3 = Country("USA", "North America")
country_repository.save(country3)
country4 = Country("South Korea", "Asia")
country_repository.save(country4)
country5 = Country("Canada", "North America")
country_repository.save(country5)
country6 = Country("Argentina", "South America")
country_repository.save(country6)

england_city1 = City("London", country1, "Europe")
city_repository.save(england_city1)
england_city2 = City("Manchester", country1, "Europe")
city_repository.save(england_city2)
england_city3 = City("Liverpool", country1, "Europe")
city_repository.save(england_city3)

city2 = City("Paris", country2, "Europe")
city_repository.save(city2)

city3 = City("New York", country3, "North America")
city_repository.save(city3)

city4 = City("Seoul", country4, "Asia")
city_repository.save(city4)

city5 = City("Toronto", country5, "North America")
city_repository.save(city5)

city6 = City("Buenos Aires", country6, "South America")
city_repository.save(city6)

destination1 = Destination(england_city1, country1, True, "Fun!")
destination_repository.save(destination1)

destination2 = Destination(city5, country5, False, "Looks cool!")
destination_repository.save(destination2)

pdb.set_trace()