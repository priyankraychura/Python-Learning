class Employee:
    companyName = "Apple"
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1
    def showDetails(self):
            print(f"The name of the employee is {self.name} and the raise amount in the {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Priyank")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Chaman")
emp2.companyName = "Nestle"
emp2.showDetails()