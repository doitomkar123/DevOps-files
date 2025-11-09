# better code org
# readability
# reusability
# Security

#Class and Object

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("init function")

    def display(self):
        print("Print from MyClass", self.name, self.age)

# obj1 = MyClass("abcd", 12)
# print("----------")
# obj2 = MyClass("xyz", 15)
# print(obj2.display())

# print("----------")
# obj3 = MyClass("def", 20)
# print(obj3.display())


# Inheritance

class Parent:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

    def display(self):
        print("Car brand - ",self.brand, "car name - ", self.name)
    
    def parentPrint(self):
        print("from parent")


class Child(Parent):
    def __init__(self, brand, name, colour):
        super().__init__(brand, name)
        self.colour = colour
    
    def display(self):
        print("Child class ->", self.brand, self.name, self.colour)


class Child2(Parent):
    def __init__(self, brand, name, age):
        super().__init__(brand, name)
        self.age = age

    def display(self):
        print("child2 -> ", self.name, self.brand, self.age)

# obj1 = Parent("Tata", "Nexon")
# obj1.display()

obj1 = Child("ABC", "NAME", "black")
obj1.display()
obj1.parentPrint()


objChild = Child2("Tata", "Nexon", 5)
objChild.display()
objChild.parentPrint()

############       Parent
                # |     |
            # child1   child2
            #  obj1      obj2