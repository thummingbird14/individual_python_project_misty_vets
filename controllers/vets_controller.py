from flask import Blueprint, Flask, render_template, redirect, request
from repositories import vet_repository
from models.vet import Vet

vets_blueprint = Blueprint("tasks", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", all_vets = vets)

# @tasks_blueprint.route("/tasks/new", methods=['GET'])
# def new_task():
#     users = user_repository.select_all()
#     return render_template("tasks/new.html", all_users = users)

# @tasks_blueprint.route("/tasks", methods=["POST"])
# def create_task():
#     description = request.form['description']
#     user_id = request.form['user_id']
#     duration = request.form['duration']
#     completed = request.form['completed']
#     user = user_repository.select(user_id)

#     task = Task(description, user, duration, completed)
#     task_repository.save(task)

#     return redirect('/tasks')

@vets_blueprint.route("/vets/<id>/delete")
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')


# @tasks_blueprint.route("/tasks/<id>", methods=['GET'])
# def show_task(id):
#     task = task_repository.select(id)
#     return render_template('tasks/show.html', task = task)

# @tasks_blueprint.route("/tasks/<id>/edit", methods=['GET'])
# def edit_task(id):
#     task = task_repository.select(id)
#     users = user_repository.select_all()
#     return render_template('tasks/edit.html', task=task, all_users=users)

# @tasks_blueprint.route("/tasks/<id>", methods=['POST'])
# def update_task(id):
#     description = request.form['description']
#     user_id = request.form['user_id']
#     duration = request.form['duration']
#     completed = request.form['completed']
#     user = user_repository.select(user_id)

#     task = Task(description, user, duration, completed, id)
#     task_repository.update(task)
#     return redirect('/tasks')
    

