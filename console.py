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
country6 = Country("Brasil", "South America")
country_repository.save(country6)

england_city1 = City("London", country1, "Europe")
city_repository.save(england_city1)
england_city2 = City("Manchester", country1, "Europe")
city_repository.save(england_city2)
england_city3 = City("Liverpool", country1, "Europe")
city_repository.save(england_city3)

france_city1 = City("Paris", country2, "Europe")
city_repository.save(france_city1)
france_city2 = City("Marseille", country2, "Europe")
city_repository.save(france_city2)
france_city3 = City("Bordeaux", country2, "Europe")
city_repository.save(france_city3)

us_city1 = City("New York", country3, "North America")
city_repository.save(us_city1)
us_city2 = City("Los Angeles", country3, "North America")
city_repository.save(us_city2)
us_city3 = City("Boston", country3, "North America")
city_repository.save(us_city3)

skorea_city1 = City("Seoul", country4, "Asia")
city_repository.save(skorea_city1)
skorea_city2 = City("Busan", country4, "Asia")
city_repository.save(skorea_city2)
skorea_city3 = City("Incheon", country4, "Asia")

canada_city1 = City("Toronto", country5, "North America")
city_repository.save(canada_city1)
canada_city1 = City("Vancouver", country5, "North America")
city_repository.save(canada_city1)
canada_city1 = City("Montreal", country5, "North America")
city_repository.save(canada_city1)

brasil_city1 = City("Rio de Janeiro", country6, "South America")
city_repository.save(brasil_city1)
brasil_city1 = City("Sao Paulo", country6, "South America")
city_repository.save(brasil_city1)
brasil_city1 = City("Salvador", country6, "South America")
city_repository.save(brasil_city1)

pdb.set_trace()