"""
created by Nagaj at 14/06/2021
"""
# while : something happens repeatedly until it is done

# count from 1 to 100 by 5 ===>  5, 10, 15, 20, 25, ..... 100
counter = 0

while counter < 100:
    counter += 5
    print(counter, end=" ")

print()

counter = 5

while counter <= 100:
    print(counter, end=" ")
    counter += 5

print()

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango"
]
print("Our Fruits Selection")
for fruits in fruits:
    print(fruits)

print(fruits)  # Mango
print("Done")

