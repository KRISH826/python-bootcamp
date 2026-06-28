from abc import ABC, abstractmethod

#abstaract class
class Vehicle(ABC):
    def driver(self):
        print("the person will drive the vehicle")

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("the car will start")


def vehicle_start(vehicle):
    vehicle.start()
    vehicle.driver()

car = Car()
vehicle_start(car)
