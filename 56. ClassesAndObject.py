class Person:
    name = "Priyank"
    occupation =  "Programemr"
    networth = 11000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()

a.name = "Pruthvi"
a.occupation = "Full Stack Developer"

b.name = "Urvi"
b.occupation = "Programmer"

a.info()
b.info()
