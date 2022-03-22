from db.run_sql import run_sql

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

def save(animal):
    sql = "INSERT INTO animals (name, date_of_birth, species, sex, treatment_notes, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.species, animal.sex, animal.treatment_notes, animal.owner.id, animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def select_all():
    animals = []

    sql = "SELECT * FROM animals ORDER BY vet_id"
    results = run_sql(sql)

    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        date_of_birth_ccyy_mm_dd = row['date_of_birth']
        date_of_birth_dd_mm_ccyy = date_of_birth_ccyy_mm_dd.strftime("%d/%m/%Y")
        animal = Animal(row['name'], date_of_birth_dd_mm_ccyy, row['species'], row['sex'], row['treatment_notes'], owner, vet, row['id'] )
        animals.append(animal)
    return animals

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['name'], result['date_of_birth'], result['species'], result['sex'], result['treatment_notes'], owner, vet, result['id'] )
    return animal

def update(animal):
    sql = "UPDATE animals SET (name, date_of_birth, species, sex, treatment_notes, owner_id, vet_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.date_of_birth, animal.species, animal.sex, animal.treatment_notes, animal.owner.id, animal.vet.id, animal.id]
    run_sql(sql, values)     

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

