class Parent1:
    def parent1print(self):
        print("printing from parent 1")

class Parent2:
    def parent2print(self):
        print("printing from parent 2")

class child(Parent1, Parent2):
    def childprint(self):
        print("printing from child class")

obj = child()
obj.childprint()
obj.parent1print()
obj.parent2print()
