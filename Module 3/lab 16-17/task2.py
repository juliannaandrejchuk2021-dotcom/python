from abc import ABC, abstractmethod, ABCMeta

class Diagnosable(metaclass=ABCMeta):
    @abstractmethod
    def diagnose(self):
        pass

class Car:
    def __init__(self,resource=100000):
        self._resource=resource
        self._current_mileage=0
    def driving(self,mileage):
        self._current_mileage+=15000

class Human:
    def __init__(self):
        self._health=100
    def eat(self,food):
        if food == "junk food":
            self._health -= 20
        elif food == "healthy food":
            self._health += 20
        self._health = self._health if self._health > 0 else 0
        self._health = self._health if self._health < 100 else 100

class Animal:
    def __init__(self):
        self._health=100
    def feed(self,food):
        if food == "junk food":
            self._health -= 20
        elif food == "healthy food":
            self._health += 20
        self._health = self._health if self._health > 0 else 0
        self._health = self._health if self._health < 100 else 100

class DiagnosableCar(Car,Diagnosable):
    def diagnose(self):
        if self._current_mileage>=self._resource:
            return "Car needs maintenance"
        rest= self._resource - self._current_mileage
        rest /= self._resource
        rest *=100
        return "Rest {}% of car resource".format(rest)

class DiagnosableeHuman(Human,Diagnosable):
    def diagnose(self):
        if self._health<=0:
            return "Human needs medical attention"
        elif self._health == 100:
            return "Human is healthy"
        else:
            return "Human health is at {}%".format(self._health)

class DiagnosableAnimal(Animal,Diagnosable):
    def diagnose(self):
        if self._health<=0:
            return "Animal needs medical attention"
        elif self._health == 100:
            return "Animal is healthy"
        else:
            return "Animal health is at {}%".format(self._health)


car=DiagnosableCar()
car.driving(15000)
print(car.diagnose())
human=DiagnosableeHuman()
human.eat("junk food")
print(human.diagnose())
animal=DiagnosableAnimal()
animal.feed("healthy food")
print(animal.diagnose())
