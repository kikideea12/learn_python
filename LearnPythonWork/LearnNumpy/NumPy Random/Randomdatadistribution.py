from numpy import random

# Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

x = random.choice([3, 4, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

# The sum of all probability numbers should be 1.

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)


