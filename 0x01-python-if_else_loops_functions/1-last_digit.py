#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
str = f"Last digit of {number:d} is {ld} and is"
if(ld > 5):
    print(f"{str} greater than 5")
elif(ld == 0):
    print(f"{str} 0")
else:
    print(f"{str} less than 6 and not 0")
