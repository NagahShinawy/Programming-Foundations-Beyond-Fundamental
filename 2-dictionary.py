"""
created by Nagaj at 14/06/2021
"""
from pprint import pprint


california_symbols = {
    "bird": "California quail",
    "animal": "Grizzly bear",
    "flower": "California poppy",
    "fruit": "Avocado",
}

student = {
    "name": "John",
    "age": 15,
    "id": 343434,
    "class": "a3",
    "subjects": ["arabic", "english", "math"],
}

book = {
    "title": "clean code",
    "author": {
        "fname": "bob",
        "lname": "tst",
        "job_title": "expert",
        "books": ["clean code", "clean agile", "clean arch"],
    },
    "price": 99,
    "published": "23-12-2020",
}
counties = [
    {
        "egypt": {
            "name": "Egypt",
            "code": "+20",
            "capital": "Cairo",
            "lat": 34.45435,
            "lon": 45.23,
            "cities": ["cairo", "alex", "gona"]
        },

        "sa": {
            "name": "Saudi Arabia",
            "code": "+966",
            "capital": "Riyad",
            "lat": 90.43,
            "lon": 23.12,
            "cities": ["riyad", "makka", "gadda"]
        },
    }
]
print(book)

print(california_symbols)

pprint(california_symbols)

print("#" * 100)

print(book["author"]["books"][0])
print(book["author"]["books"][1])
print(book["author"]["books"][2])
