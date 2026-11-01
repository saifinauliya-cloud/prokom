# Approach 1: Import the entire module
import city_functions

print(city_functions.city_country("Surakarta", "Indonesia"))


# Approach 2: Import a specific function
from city_functions import city_country

print(city_country("Tokyo", "Japan"))