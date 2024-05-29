class Employee:
    def __init(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")
    
class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

o = DancerEmployee("Shivani", "Kathak")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())