class Employee:
    def __init__(self):
        self.__name = "Priyank"

a = Employee()
# print(a.__name) Cannot be accessed directly
print(a._Employee__name) #Can be accessed indirectly
print(a.__dir__())

class Student:
    def __init__(self):
        self._name = "Priyank"

    def _funname(self):
        return "PriyankRaychura"
    
class Subject(Student):
    pass

obj = Student()
obj1 = Student()

#Calling by student of object of student class
print(obj._name)
print(obj._funname())

#Calling by subject of object of student class
print(obj1._name)
print(obj1._funname())