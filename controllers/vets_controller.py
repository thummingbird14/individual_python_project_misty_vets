from flask import Blueprint, Flask, render_template, redirect, request
from repositories import vet_repository
from models.vet import Vet

vets_blueprint = Blueprint("tasks", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", all_vets = vets)

@vets_blueprint.route("/vets/new", methods=['GET'])
def new_vet():
    return render_template("vets/new.html")

@vets_blueprint.route("/vets", methods=["POST"])
def create_vet():
    name = request.form['name']
    vet = Vet(name)
    vet_repository.save(vet)
    return redirect('/vets')

@vets_blueprint.route("/vets/<id>/delete")
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')

@vets_blueprint.route("/vets/<id>", methods=['GET'])
def show_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/show.html', vet = vet)

@vets_blueprint.route("/vets/<id>/edit", methods=['GET'])
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet=vet)

@vets_blueprint.route("/vets/<id>", methods=['POST'])
def update_vet(id):
    name = request.form['name']
    vet = Vet(name, id)
    vet_repository.update(vet)
    return redirect('/vets')
    

