# compile time polymorphism - method overriding

class car:
    def move(self):
        print("Driving a car")

class bike:
    def move(self):
        print("Riding a bike")

obj1 = car()
obj1.move()

obj2 = bike()
obj2.move()




# Runtime polymorphism - method overloading

def calculate(a=0, b=0, c=0, d=0):
    return a+b+c+d

print(calculate(6))
print(calculate(5, 7))
print(calculate(1,2,3))
print(calculate(1,2,3,4))