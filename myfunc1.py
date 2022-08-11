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

