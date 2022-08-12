# Modules

def greeting(name):
    print("Hello, " + name)

import Modules

Modules.greeting("Johnathan")

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import Modules

a = Modules.person1["age"]
print(a)

import Modules as Modules1

a = Modules1.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from Modules import person1

print (person1["age"])







