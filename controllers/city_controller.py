from flask import Blueprint, Flask, render_template, request, redirect
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.destination_repository as destination_repository

city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

@city_blueprint.route('/cities/<id>')
def show(id):
    city = city_repository.select(id)
    return render_template("cities/show.html", city = city)

@city_blueprint.route('/cities/new', methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("cities/new.html", cities = cities, all_countries = countries)

@city_blueprint.route("/cities",  methods = ['POST'])
def create_city():
    name = request.form['name']
    country = country_repository.select(request.form['country_id'])
    continent = request.form['continent']
    city = City(name, country, continent)
    city_repository.save(city)
    return redirect("/cities")