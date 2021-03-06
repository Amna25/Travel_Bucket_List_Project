from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.destination import Destination

import repositories.country_repository as country_repository

def save(city):
    sql= "INSERT INTO cities (name, visited, country_id) VALUES (%s, %s, %s) RETURNING * "
    values=[city.name, city.visited, city.country.id]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], row['visited'] , country , row['id'])
        cities.append(city)
    return cities

def select(id):
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    country = country_repository.select(result['country_id'])
    city = City(result['name'], result['visited'] ,country, result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, visited, country_id) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.visited, city.country.id, city.id]
    run_sql(sql, values)

def countries(city):
    countries = []

    sql= "SELECT * FROM countries WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)
    for row in results:
        country= Country(row['name'],row['visited'],row['id'])
        countries.append(country)
    return countries

def destinations(city):
    destinations = []

    sql= "SELECT * FROM destinations WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)
    for row in results:
        destination= Destination(row['name'],row['city.id'],row['visited'],row['id'])
        destinations.append(destination)
    return destinations