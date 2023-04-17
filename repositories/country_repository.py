from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.destination import Destination

def save(country):
    sql = "INSERT INTO countries (country_name, continent) VALUES (%s, %s) RETURNING id"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['country_name'], row['continent'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = Country(result['country_name'], result['continent'], result['id'])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (country_name, continent) = (%s, %s) WHERE id = %s"
    values = [country.name, country.continent]
    print(values)
    run_sql(sql, values)

def destinations(country):
    destinations = []

    sql = "SELECT * FROM countries WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        destination = Destination(row['city'], row['country_id'], row['visited'], row['id'] )
        destinations.append(destination)
    return destinations