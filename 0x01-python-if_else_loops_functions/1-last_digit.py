#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastNumber = number % 10 if number >= 0 else -(-number % 10)

print(f"Last digit of {number:d} is {lastNumber}", end=" ")

if lastNumber != 0 and lastNumber <= 6:
    print("and is less than 6 and not 0")
elif lastNumber == 0:
    print("and is 0")
elif lastNumber > 5:
    print(f"and is greater than 5")
