class Parent:
    def __init__(self, name):
        self.name = name

    def parentPrint(self):
        print("Printing from Parent", self.name)


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        # self.name = name
        self.age = age
    
    def childPrint(self):
        print("printing from child class",self.name, self.age)

# obj = Parent("XYZ")
# obj.parentPrint()

obj = Child("ABC", 15)
obj.childPrint()
obj.parentPrint()