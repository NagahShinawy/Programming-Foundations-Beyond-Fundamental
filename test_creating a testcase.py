"""
created by Nagaj at 18/06/2021
"""

WEAR = "Wear a Jacket"
PACK = "Pack a Jacket"
LEAVE = "Leave a jacket at home"

LEVELS = {
    "low": "aloe",
    "medium": "pothos",
    "hard": "orchild"
}


def check_temp(temp):
    if 0 <= temp <= 15:
        return WEAR
    elif 16 <= temp <= 25:
        return PACK
    elif 25 < temp <= 35:
        return LEAVE


def planet_recommendation(care):

    if care == "low":
        return LEVELS['low']

    if care == "medium":
        return LEVELS['medium']

    if care == "hard":
        return LEVELS['hard']


def test_wear():
    for tmp in range(0, 16):
        assert check_temp(tmp) == WEAR


def test_pack():
    for tmp in range(16, 26):
        assert check_temp(tmp) == PACK


def test_leave():
    for tmp in range(26, 36):
        assert check_temp(tmp) == LEAVE


def test_low():
    assert planet_recommendation("low") == LEVELS['low']


def test_medium():
    assert planet_recommendation("medium") == LEVELS['medium']


def test_hard():
    assert planet_recommendation("hard") == LEVELS['hard']

