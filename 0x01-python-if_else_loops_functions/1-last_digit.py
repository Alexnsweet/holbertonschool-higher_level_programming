#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    ldig = number % 10
else:
    ldig = (number % -10) * -1

if ldig == 0:
    suffix = "and is 0"
elif ldig > 5:
    suffix = "and is greater than 5"
else:
    suffix = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, ldig, suffix))
