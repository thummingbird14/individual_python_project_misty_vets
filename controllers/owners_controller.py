from flask import Blueprint, Flask, render_template, redirect, request
from repositories import owner_repository
from models.owner import Owner

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", all_owners = owners)

@owners_blueprint.route("/owners/new", methods=['GET'])
def new_owner():
    return render_template("owners/new.html")

@owners_blueprint.route("/owners", methods=["POST"])
def create_owner():
    name = request.form['name']
    address = request.form['address']
    phone_no = request.form['phone_no']
    owner = Owner(name, address, phone_no)
    owner_repository.save(owner)
    return redirect('/owners')

@owners_blueprint.route("/owners/<id>/edit", methods=['GET'])
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/edit.html', owner=owner)

@owners_blueprint.route("/owners/<id>", methods=['POST'])
def update_owner(id):
    name = request.form['name']
    address = request.form['address']
    phone_no = request.form['phone_no']
    owner = Owner(name, address, phone_no, id)
    owner_repository.update(owner)
    return redirect('/owners')

@owners_blueprint.route("/owners/<id>/delete")
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')



    