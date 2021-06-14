"""
created by Nagaj at 13/06/2021
"""
from collections import namedtuple

city1 = "Riyad"
city2 = "Cairo"
city3 = "Maka"
city4 = "Madina"

cities = ["Riyad", "Cairo", "Maka", "madina"]
guests = ["John", "James", "Leon", "Smith"]

City = namedtuple("City", ["name", "lat", "lon"])

cairo = City("Cairo", 34.65, 54.23)

print(cairo)
print(cairo.name, cairo[0])
print(cairo.lat, cairo[1])
print(cairo.lon, cairo[2])

print(guests)
print(guests[0])
print(guests[1])
print(guests[2])
print(guests[3])

# ####### ####### ####### ####### ####### ######
print("#" * 100)
john = ["john", 14, 90, True]
james = ["james", 13, 30, False]

# ####### ####### ####### ####### ####### ######
john_profile = {
    "name": "John",
    "age": 14,
    "degree": 90,
    "is_success": True
}

james_profile = {
    "name": "James",
    "age": 13,
    "degree": 30,
    "is_success": False
}

# list is mutable container
# tuple is immutable list
