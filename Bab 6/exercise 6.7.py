
person_1 = {
    "first_name": "Dzulfikar",
    "last_name": "Kamal",
    "age": 21,
    "city": "Yogyakarta"
}

person_2 = {
    "first_name": "Kacandra",
    "last_name": "Kevan",
    "age": 18,
    "city": "Bali"
}

person_3 = {
    "first_name": "Muhammad",
    "last_name": "Fachry",
    "age": 19,
    "city": "Semarang"
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\nFirst name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
