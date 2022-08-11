# Arrays:

# Note: pytion does not have built in support for Arrays, but Python lists can be used instead
# this page shows how to use lists as arrays, however, to work with arrays in python you will have to import a library, like the NumPy library.

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

cars[0] = "Toyota"

x = len(cars)

# Note: the length of an array is always one more than the highest array index

for x in cars: 
    print(x)

cars.append("Honda")

cars.pop(1)

cars.remove("Volvo")
