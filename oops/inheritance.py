# object oriented programming

# .inheritance class

# parent class
class Car:
    def __init__(self, windows, doors, engineType):
        self.windows = windows
        self.doors = doors
        self.engineType = engineType

    def drive(self):
        print(f"the person will drive the {self.engineType} car")

car1 = Car(4, 4, "petrol")

print(car1.windows)
print(car1.doors)
print(car1.engineType)
car1.drive()


# inheritance the car (sinle inheritance)

class Tesla(Car):
    def __init__(self, windows, doors, engineType, isSelfDriving):
        super().__init__(windows, doors, engineType)
        self.isSelfDriving = isSelfDriving
    def selfDriving(self):
        if self.isSelfDriving == True:
            print("the car is self driving")
        else:
            print("the car is not self driving")


tesla1= Tesla(4, 4, "petrol", False)
print(tesla1.windows)
print(tesla1.doors)
print(tesla1.engineType)
tesla1.drive()
tesla1.selfDriving()    


# multiple inheritance (when a class inheritance more that 1 class)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

class Pet:
    def __init__(self, owner):
        self.owner = owner

    def play(self):
        print(f"{self.owner} is playing with the pet")

class Dog(Animal, Pet):
    def __init__(self, name, age, owner):
        Animal.__init__(self, name, age)
        Pet.__init__(self, owner)

    def bark(self):
        print(f"{self.name} is barking")

# create an object
dog108 = Dog("Buddy", 5, "Alice")
print(dog108.age)
print(dog108.name)
print(dog108.owner)
print(dog108.eat())



