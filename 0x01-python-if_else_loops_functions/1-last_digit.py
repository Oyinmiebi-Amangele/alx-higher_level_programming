#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# converting the number to positive
if number < 0:
    last = (-number) % 10
    last = -last
else:
    last = (number) % 10
# using the positive number for the main code
if (last > 5):
    print(f"Last digit of {number} is {last} and is greater than 5")
elif (last == 0):
    print(f"Last digit of {number} is {last} and is 0")
elif (last < 6 and not 0):
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
