DROP TABLE animals;
DROP TABLE owners;
DROP TABLE vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone_no VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth DATE,
    species VARCHAR(255),
    sex VARCHAR(255),
    treatment_notes TEXT,
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);