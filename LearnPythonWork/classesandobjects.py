# classes and objects

class myclass:
    x = 5

p1 = myclass
print(p1.x)

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()  

p1.age = 40

# del p1.age

# del p1

class Person:
    pass