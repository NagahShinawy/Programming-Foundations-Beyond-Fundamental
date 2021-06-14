"""
created by Nagaj at 14/06/2021
"""


def words_length(word, *args) -> list:
    words = [word, *args]
    return [(word, len(word)) for word in words]


def welcome(name: str, upper=False) -> str:
    if upper is True:
        return name.upper()
    return name


def adder(x, y, *args):
    return sum([x, y, *args])