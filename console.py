import pdb 
from models.vet import Vet
from models.owner import Owner
from models.animal import Animal
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository  

vet_repository.delete_all()

vet_1 = Vet("Jim Roxburghe")

vet_2 = Vet("Harriet Smith")

vet_3 = Vet("Fraser Callaghan")

print(vet_1.__dict__)

vet_repository.save(vet_1)
vet_repository.save(vet_2)
vet_repository.save(vet_3)

results = vet_repository.select_all()

for vet in results:
    print(vet.__dict__)

owner_repository.delete_all()

owner_1 = Owner("Louise O'Rourke", "40 East Kilngate Place", "0131 6661234")
owner_2 = Owner("Fred Anderson", "62 Hyvot View", "0131 2221234")
owner_3 = Owner("Sarah James", "316 Lasswade Road", "0131 3331234")

owner_repository.save(owner_1)
owner_repository.save(owner_2)
owner_repository.save(owner_3)

results = owner_repository.select_all()

for owner in results:
    print(owner.__dict__)

animal_repository.delete_all()

animal_1 = Animal("Jess", "2019-04-05", "Dog", "F", "Ear infection, given antibiotics", owner_1, vet_1)
animal_2 = Animal("Sophie", "2015-04-01", "Cat", "F", "Sophie's treatment notes", owner_1, vet_1)
animal_3 = Animal("Jodie", "2012-08-12", "Dog", "F", "Jodie's treatment notes", owner_2, vet_3)

animal_repository.save(animal_1)
animal_repository.save(animal_2)
animal_repository.save(animal_3)

pdb.set_trace()