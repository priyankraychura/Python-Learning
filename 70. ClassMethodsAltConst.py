# Class methods as alternative constructors
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1 = Employee("Priyank", 100000)
print(e1.name)
print(e1.salary)

string = "Priyank-2000000"
# e2 = Employee(string.split("-")[0], string.split("-")[1])
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
person = Person.from_string("Priyank", 21)
print(person.name, person.age)
    