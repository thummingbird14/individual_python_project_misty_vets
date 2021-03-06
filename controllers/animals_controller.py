from flask import Blueprint, Flask, render_template, redirect, request
from datetime import datetime

from repositories import animal_repository
from repositories import owner_repository
from repositories import vet_repository

from models.animal import Animal

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals = animals)

@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template("animals/new.html", all_owners = owners, all_vets = vets, today = today)

@animals_blueprint.route("/animals", methods=["POST"])
def create_animal():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    species = request.form['species']
    sex = request.form['sex']
    treatment_notes = request.form['treatment_notes']
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)

    animal = Animal(name, date_of_birth, species, sex, treatment_notes, owner, vet)
    animal_repository.save(animal)

    return redirect('/animals')

@animals_blueprint.route("/animals/<id>/edit", methods=['GET'])
def edit_animal(id):
    animal = animal_repository.select(id)
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template('animals/edit.html', animal=animal, all_owners=owners, all_vets=vets, today=today)

@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update_animal(id):
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    species = request.form['species']
    sex = request.form['sex']
    treatment_notes = request.form['treatment_notes']
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    animal = Animal(name, date_of_birth, species, sex, treatment_notes, owner, vet, id)
    animal_repository.update(animal)
    return redirect('/animals')

@animals_blueprint.route("/animals/<id>/delete")
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')



