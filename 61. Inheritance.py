class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def showDetails(self):
        print(f"The name of employee {self.id} is {self.name}")

class Programmer(Employee):
    def showLnaguage(self):
        print("The default language is Python.")

e1 = Employee("Chaman", 00)
e1.showDetails()
e2 = Programmer("001", "Priyank")
e2.showDetails()
e2.showLnaguage()