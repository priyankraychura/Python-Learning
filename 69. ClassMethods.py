class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def chnageCompany(cls, newCompay): #can user self insted of cls
        cls.company = newCompay

e1 = Employee()
e1.name = "Priyank"
e1.show()
e1.chnageCompany("Tesla")
e1.show()
print(Employee.company)
