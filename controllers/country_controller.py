from flask import Blueprint, Flask, render_template, request, redirect
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.destination_repository as destination_repository

country_blueprint = Blueprint("countries", __name__)

@country_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@country_blueprint.route('/countries/<id>')
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)

@country_blueprint.route('/countries/new', methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("countries/new.html", all_countries = countries)

@country_blueprint.route("/countries",  methods = ['POST'])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    country = Country(name, continent)
    country_repository.save(country)
    return redirect("/countries")

@country_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template('countries/edit.html', country = country, all_cities = cities)

@country_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['name']
    continent = request.form['continent']
    country = Country(name, continent, id)
    country_repository.update(country)
    return redirect('/countries')