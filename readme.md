### Misty Vets App - Brief

The misty_vets app is an app created to meet the following brief:

  ### Vet Management App

  A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet.

  #### MVP

  - The practice wants to be able to register / track animals. Important information for the vets to know is -
    - Name
    - Date Of Birth (use a VARCHAR initially)
    - Type of animal
    - Contact details for the owner
    - Treatment notes
  - Be able to assign animals to vets
  - CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?

  ### Extension

  - If an owner has multiple animals we don't want to keep updating contact details separately for each pet. Extend your application to reflect that an owner can have many pets and to more sensibly keep track of owners' details (avoiding repetition / inconsistencies)

### Misty Vets App - Technologies Used

The misty_vets app was built using HTML & CSS, Python, Flask, PostgreSQL and the psycopg package


### Misty Vets App - Operating Instructions

The misty_vets app runs on the misty_vets database. To create the tables, run db/misty_vets.sql. To seed the database with start data, run console.py. The app runs on Flask and the initial screen is localhost/misty_vets
