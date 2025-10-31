#program using statistics module

import statistics as stats

data = [12, 15, 20, 21, 18, 30, 25]

print("Mean:", stats.mean(data))
print("Median:", stats.median(data))
print("Standard Deviation:", stats.stdev(data))


#program using random  module for generating random passwords

import random
import string

characters = string.ascii_letters + string.digits + "!@#$%&*"
password = "".join(random.choice(characters) for _ in range(12))

print("Generated Password:", password)


#program on using math functions

from math import sqrt, pi

print(sqrt(64))   # Use directly
print(pi)

