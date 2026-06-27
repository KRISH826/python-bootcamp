# method overriding allows a child class to provide a specification implementation of a method thats already provided by its parent class

# base class

class Animal:
    def speak(aself):
        return "sound of the animal"

# derived class 1

class Dog(Animal):
    def speak(aself):
        return 'woof!'
    
class Cat(Animal):
    def speak(aself):
        return 'meow!'    

class Cow(Animal):
    def speak(aself):
        return 'moo!'
    
dog = Dog()
cat = Cat()
cow = Cow()

print(dog.speak())
print(cat.speak())
print(cow.speak())


# polymorphism with fiunction and methhos
class Shape:
    def area(self):
        return "the area of the figure"
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius            

def print_area(shape):
    print(f"the area is {shape.area()}")


rectangle = Rectangle(10, 20)
circle = Circle(5)

print_area(rectangle)
print_area(circle)


# polymorphism with abstract base classes
from abc import ABC, abstractmethod

# define a abstract class

class Vehicle(ABC):
    @abstractmethod # decorator
    def driver(self):
        pass


class Car(Vehicle):
    def driver(self):
        print("the person will drive the car")

class Bike(Vehicle):
    def driver(self):
        print("the person will drive the bike")


def start_car(car):
    print(f"the car will start {car.driver()}")        


car = Car()
bike = Bike()

# car.driver()
# bike.driver()

start_car(car)
start_car(bike)

