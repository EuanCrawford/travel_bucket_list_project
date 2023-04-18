from flask import Blueprint, Flask, render_template, request, redirect
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.destination_repository as destination_repository

city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

@city_blueprint.route("/cities",  methods = ['POST'])
def create_city():
    name = request.form['name']
    country = country_repository.select(request.form['country_id'])
    city = City(name, country)
    city_repository.save(city)
    return redirect("/cities")

@city_blueprint.route('/cities/<id>', methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/show.html", city = city, all_countries = countries)

@city_blueprint.route('/cities/new', methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("cities/new.html", all_cities = cities, all_countries = countries)

@city_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city = city, all_countries = countries)

@city_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    country = country_repository.select(request.form['country_id'])
    city = City(name, country, id)
    city_repository.update(city)
    return redirect("/cities")

@city_blueprint.route('/cities/<id>/delete', methods=['POST'])
def delete_city(id):
    cities = city_repository.delete(id)
    return redirect("/cities")
