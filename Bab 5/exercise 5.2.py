# Tests for equality and inequality with strings
fruit = "apple"

print("Is fruit == 'apple'? I predict True.")
print(fruit == "apple")

print("\nIs fruit == 'orange'? I predict False.")
print(fruit == "orange")

# Tests using the lower() method
car = "SUBARU"

print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == "subaru")

print("\nIs car.lower() == 'audi'? I predict False.")
print(car.lower() == "audi")

# Numerical tests
number = 10

print("\nIs number == 10? I predict True.")
print(number == 10)

print("\nIs number != 10? I predict False.")
print(number != 10)

print("\nIs number > 5? I predict True.")
print(number > 5)

print("\nIs number < 5? I predict False.")
print(number < 5)

print("\nIs number >= 10? I predict True.")
print(number >= 10)

print("\nIs number <= 5? I predict False.")
print(number <= 5)

# Tests using and
print("\nIs number > 5 and number < 20? I predict True.")
print(number > 5 and number < 20)

print("\nIs number > 5 and number < 5? I predict False.")
print(number > 5 and number < 5)

# Tests using or
print("\nIs number > 20 or number == 10? I predict True.")
print(number > 20 or number == 10)

print("\nIs number > 20 or number < 5? I predict False.")
print(number > 20 or number < 5)

# Test whether an item is in a list
fruits = ["apple", "banana", "orange"]

print("\nIs 'apple' in fruits? I predict True.")
print("apple" in fruits)

print("\nIs 'grape' in fruits? I predict False.")
print("grape" in fruits)

# Test whether an item is not in a list
print("\nIs 'grape' not in fruits? I predict True.")
print("grape" not in fruits)

print("\nIs 'banana' not in fruits? I predict False.")
print("banana" not in fruits)
