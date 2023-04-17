from flask import Blueprint, Flask, render_template, request, redirect
from models.destination import Destination
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.destination_repository as destination_repository

destination_blueprint = Blueprint("destinations", __name__)

@destination_blueprint.route("/destinations")
def destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", destinations = destinations)

# NEW

@destination_blueprint.route("/destinations/new", methods = ['GET'])
def new_destination():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("destinations/new.html", all_cities = cities, all_countries = countries)

# CREATE

@destination_blueprint.route("/destinations",  methods = ['POST'])
def create_destination():
    country_id = request.form['country_id']
    city_id = request.form['city_id']
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)
    visited = True if 'visited' in request.form else False
    review = request.form['review']
    destination = Destination(city, country, visited, review)
    destination_repository.save(destination)
    return redirect("/destinations")

# SHOW

@destination_blueprint.route("/destinations/<id>", methods = ['GET'])
def show_destination(id):
    destination = destination_repository.select(id)
    return render_template("destinations/show.html", destination = destination)

# EDIT

@destination_blueprint.route("/destinations/<id>/edit", methods = ['GET'])
def edit_destination(id):
    destination = destination_repository.select(id)
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("destinations/edit.html", destination = destination, all_cities = cities, all_country = countries)

# UPDATE

@destination_blueprint.route("/destinations/<id>", methods = ['POST'])
def update_destination(id):
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    city_id = request.form['city_id']
    city = city_repository.select(city_id)
    visited = True if 'visited' in request.form else False
    review = request.form['review']
    destination = Destination(country, city, visited, review, id)
    destination_repository.update(destination)
    return redirect("/destinations")

# DELETE

@destination_blueprint.route("/destinations/<id>/delete", methods = ['POST'])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect("/destinations")