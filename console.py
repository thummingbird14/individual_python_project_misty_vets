import pdb 
from models.vet import Vet
import repositories.vet_repository as vet_repository  

vet_repository.delete_all()

vet_1 = Vet("Jim Roxburghe")

vet_2 = Vet("Harriet Smith")

print(vet_1.__dict__)

vet_repository.save(vet_1)
vet_repository.save(vet_2)

results = vet_repository.select_all()

for vet in results:
    print(vet.__dict__)

pdb.set_trace()