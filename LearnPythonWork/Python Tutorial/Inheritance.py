# Inhertance

# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then exucute the printmane method:
class Student(Person):
    pass

x = Person("John", "Doe")
x.printname()
x.firstname = "Grade"
x.printname()

# Note: Use the pass keyword when you do not want to add any other properties of methods to the class.

x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
x.printname()
print(x.graduationyear)
print(x)


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)

x.welcome()






