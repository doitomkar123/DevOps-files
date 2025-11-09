class abcd:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display(self):
        print("public ->", self.name, "private ->", self.__age)

    def get_age(self):
        return self.__age
    
    def set_age(self, newVal):
        self.__age = newVal

obj = abcd("XYZ", 20)
print(obj.name)
obj.display()
print(obj.get_age())
obj.set_age(25)
print(obj.get_age())
obj.display()
# print(obj.__age)