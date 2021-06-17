"""
created by Nagaj at 17/06/2021
"""
MILE_TO_KILOS = 1.609344

miles = float(input("Enter Distance In Miles: "))

from_miles_to_kilos = miles * MILE_TO_KILOS

print(f"{miles} Mile(s) Is {miles * MILE_TO_KILOS} Kilos")

# print("#" * 1.5)  # TypeError: can't multiply sequence by non-int of type 'float'

msg = input("Leave a message")

while not msg:
    msg = input("Message can not be empty")

print("Your message is '{}'".format(msg))
