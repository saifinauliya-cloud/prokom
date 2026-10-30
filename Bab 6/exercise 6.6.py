favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

people = ["jen", "sarah", "michael", "anna", "phil", "david"]

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, please take the favorite languages poll!")
