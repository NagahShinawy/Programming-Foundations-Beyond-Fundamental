"""
created by Nagaj at 18/06/2021
"""
import time

START = 1
END = 10
TIMES = 100
SYMBOL = "#"
SECOND = 1

for number in range(START, END + 1):
    print(number, end=" ")
    if number == END:
        print()
# #################### #################### ###################
print(SYMBOL * TIMES)

names = ["James", "John", "Smith", "Sara", "Leon"]

print(*names, end=" ")  # unpacking to print items using '*'
print()

# #################### #################### ###################
temp = 16

if temp < 25:
    print("Bring the jacket")

# #################### #################### ###################
while END >= 1:
    print(END, end=" ")
    END -= 1

print()

# #################### #################### ###################


def downcount(seconds):
    while seconds >= 1:
        yield seconds
        time.sleep(SECOND)
        seconds -= 1


waiting = downcount(5)
for sec in waiting:
    print(sec)
