# Version 1: Conditional test
age = ""

while age != "quit":
    age = input("How old are you? ")

    if age != "quit":
        age = int(age)

        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")


# Version 2: Active variable
active = True

while active:
    age = input("How old are you? ")

    if age == "quit":
        active = False
    else:
        age = int(age)

        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")


# Version 3: Break statement
while True:
    age = input("How old are you? ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")