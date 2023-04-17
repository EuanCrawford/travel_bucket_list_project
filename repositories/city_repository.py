from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.destination import Destination
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (city_name, country_id) VALUES (%s, %s) RETURNING id"
    values = [city.name, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        city = City(result['city_name'], country, result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (city_name, country_id) = (%s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.id]
    print(values)
    run_sql(sql, values)

# def new_city(city):
#     destinations = []

#     sql = "SELECT * FROM cities WHERE city_id = %s"
#     values = [city.id]
#     results = run_sql(sql, values)

#     for row in results:
#         destination = Destination(row['city_id'], row['country_id'], row['visited'], row['id'] )
#         destinations.append(destination)
#     return destinations

# def countries(city):
#     countries = []

#     sql = "SELECT countries.* FROM countries INNER JOIN destination ON destination.country_id = countries.id WHERE city_id = %s"
#     values = [city.id]
#     results = run_sql(sql, values)

#     for row in results:
#         country = Country(row['name'], row['continent'], row['id'])
#         countries.append(country)

#     return countries
