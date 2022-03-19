import pdb 
from models.vet import Vet
from models.owner import Owner
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository  

# vet_repository.delete_all()

# vet_1 = Vet("Jim Roxburghe")

# vet_2 = Vet("Harriet Smith")

# print(vet_1.__dict__)

# vet_repository.save(vet_1)
# vet_repository.save(vet_2)

results = vet_repository.select_all()

for vet in results:
    print(vet.__dict__)

owner_repository.delete_all()

owner_1 = Owner("Anita Muldoon", "40 East Kilngate Place", "0131 6661234")
owner_2 = Owner("Fred Anderson", "62 Hyvot View", "0131 2221234")
owner_3 = Owner("Sarah James", "316 Lasswade Road", "0131 3331234")

owner_repository.save(owner_1)
owner_repository.save(owner_2)
owner_repository.save(owner_3)

results = owner_repository.select_all()

for owner in results:
    print(owner.__dict__)

pdb.set_trace()