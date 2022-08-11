print("Hello, World!")
#print("Hello, World!")
print("Cheers, Mate!")
#comment
#comment
#multiple comment lines
print("Hello, World!")
"""
comment
comment
multiple comment lines
"""
print("Hello, World!")

a = 5
b = "John"
print(int(a))
print(str(b))

c = 4   # c is of type int
c = "Sally"  # c is now of type str
print(c)

d = str(3)   # d will be '3'
e = int(3)   # e will be 3
f = float(3) # f will 3.0

g = "John"
# is the same as
g = 'John'

h = 4
H = "Sally"
# H will not overwrite h

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

i, j, k = "Orange", "Banana", "Cherry"
print(i)
print(j)
print(k)

l = m = n = "Orange"
print(l)
print(m)
print(n)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits 
print(x)
print(y)
print(z)

o = "Python is awesome"
print(x)

p = "Python "
q = "is "
r = "awesome "
print(p, q, r)

''' or:
p = "Python "
q = "is "
r = "awesome "
print(p + q + r)
'''
aa = 5
bb = 10
print(aa + bb)

''' wrong:
x = 5
y = "John"
print(x + y)
'''
cc = 5
dd = "John"
print(cc, dd)

ee = "awesome"


def myfunc():
    print("python is " + ee)

myfunc()

print("Python is " + ee)


def myfunc():
    global ee
    print("python is " + ee)

myfunc()

print("Python is " + ee)

x = 5
print(int(x))


'''
x = 1 # int
y = 2.8 # float
z = 1j # complex

print(int(x))
print(float(y))
print(complex(z))


x = 1
y = 35656222554887711
z = -3255522

print(int(x))
print(int(y))
print(int(z))

x = 1.10
y = 1.0
z = -35.59

print(float(x))
print(float(y))
print(float(z))

x = 35e3
y = 12E4
z = -87.7e100

print(float(x))
print(float(y))
print(float(z))

x = 3+5j
y = 5j
z = -5j

print(complex(x))
print(complex(y))
print(complex(z))

x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from in to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(float(a))
print(int(b))
print(complex(c))

#note: You cannot convert complex numbers into another number type.

'''

import random 

print(random.randrange(1, 10))

'''
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

'''
print("Hello")
print('Hello')

ff = "Hello"
print(ff)

gg = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(gg)

hh = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(hh)

# Note: in the result, the line breaks are inserted at the same position as in the code.

ii = "Hello, World!"
print(ii[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)  

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is not present")

b = "Hello, World!"
print(b[2:5])

# Note: The first character has index 0.

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World!"
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello, "
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the\nnorth"
print(txt)

# Note: All string methods returns new values. They do not change the original string.

# Sets:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# * Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry",}

print(len(thisset))

set1 = {"apple", "banana", "cherry",}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry",}
print(type(myset))

thisset = set(("apple", "banana", "cherry",)) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry",}

for x in thisset: 
    print(x)

thisset = {"apple", "banana", "cherry",}

print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry",}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry",}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry",}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset = {"apple", "banana", "cherry",}

thisset.remove("banana")

print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry",}

thisset.discard("banana")

print(thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset 

thisset = {"apple2", "banana2", "cherry2"}

print(thisset)
for x in thisset:
    print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# dictionaries:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 1964
}
print(thisdict)

print(len(thisdict))


thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

x = thisdict.get("model")

x = thisdict.keys()


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

x = thisdict.values()


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

x = thisdict.items()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("yes, 'model' is one of the keys in the thisdict dictionary")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():
    print(x, y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Conditions and if statements

a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

# This technique is known as Ternary Operators, or Conditional Expressions.

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least of")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
    pass

# While loops

i = 1
while i < 6:
    print(i)
    i += 1

# Note: remember to increment i, or else the loop will continue forever.

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while i < 6:
    
    if i == 3:
        i += 1
        continue

    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For loops:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass

# Functions:

def my_function():
    print("Hello from a function")

def my_function():
    print("Hello from a function")

my_function()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

'''
 Arguments are often shortened to args in Python documentations. From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
'''

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

'''
def my_function(fname, lname):
    print(fname + " " + lname)

my_ function("Emil")

 This would result in a error because the function expects 2 arguments but only gets 1
'''
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
    print("I am from" + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
    pass

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

# Lambda

# Syntax: lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b 
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
    return lambda a : a * n


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

def myfunc(n):
    return lambda a : a * n 

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.

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






















