from db.run_sql import run_sql

from models.destination import Destination
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

def save(destination):
    sql = "INSERT INTO destinations (city_id, country_id, visited, review) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [destination.city.id, destination.country.id, destination.visited, destination.review]
    results = run_sql(sql, values)
    id = results[0]['id']
    destination.id = id
    return destination

def select_all():
    destinations = []

    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        country = country_repository.select(row['country_id'])
        destination = Destination(city, country, row['visited'], row['review'], row['id'] )
        destinations.append(destination)
    return destinations

def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        city = city_repository.select(result['city_id'])
        destination = Destination(city, country, result['visited'], result['review'], result['id'] )
    return destination

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(destination):
    sql = "UPDATE destinations SET (city_id, country_id, visited, review) = (%s, %s, %s, %s) WHERE id = %s"
    values = [destination.city.id, destination.country.id, destination.visited, destination.review, destination.id]
    run_sql(sql, values)
