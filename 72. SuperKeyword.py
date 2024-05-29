class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Priyank")
        super().parent_method()
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
        
pvr = Programmer("Priyank", 22, "Python")
print(pvr.name)
print(pvr.id)
print(pvr.lang)