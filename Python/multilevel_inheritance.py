class Parent:
    def __init__(self, name):
        self.name = name
    
    def parentPrint(self):
        print("Printing from parent class", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def childPrint(self):
        print("printing from child class", self.name, self.age)
    
class GrandChild(Child):
    def __init__(self, name, age, pet):
        super().__init__(name, age)
        self.pet = pet

    def grandChildPrint(self):
        print("printing from grandchild class", self.name, self.age, self.pet)

obj = GrandChild("ABC", 15, "dog")
obj.grandChildPrint()
obj.childPrint()
obj.parentPrint()