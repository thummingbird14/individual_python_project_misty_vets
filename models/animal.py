class Animal:
    def __init__(self, name, date_of_birth, species, sex, treatment_notes, owner, vet, id=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.species = species
        self.sex = sex
        self.treatment_notes = treatment_notes
        self.owner = owner
        self.vet = vet
        self.id = id