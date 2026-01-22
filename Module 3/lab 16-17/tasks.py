from abc import ABC, abstractmethod, ABCMeta

class Pet(ABC):
    def __init__(self,name):
        self._name = name
        self.isHappy=True
        self.isHungry=False
        self.isHealthy=True

    @abstractmethod
    def accept(self, visitor):
            pass

    def __str__(self):
        return f"Name: {self._name}\nHappy: {self.isHappy}\nHungry: {self.isHungry}\nHealthy: {self.isHealthy}"

    def treat(self):
        self.isHealthy=True

    def hurt(self):
        self.isHealthy=False
        self.isHappy=False

class Cat(Pet):
    def __str__(self):
            return f"Cat\n{super().__str__()}"

    def accept(self, visitor):
        visitor.visit_cat(self)

    def feed(self):
        self.isHungry=False

    def play(self):
        self.isHappy=True
        self.isHungry=True

class Dog(Pet):
    def __init__(self,name) -> None:
        super().__init__(name)
        self.skills=0

    def __str__(self):
            return f"Dog\n{super().__str__()}\nSkills: {self.skills}"
    def accept(self, visitor):
            visitor.visit_dog(self)
    def getBone(self):
            self.isHungry=False

    def walking(self):
            self.isHappy=True
            self.isHungry=True
            
    def trainDog(self):
            self.skills+=10
            self.isHungry=True
            self.isHappy=False
class Parrot(Pet):
    def __str__(self):
            return f"Parrot\n{super().__str__()}"
    def feed(self):
        print("Parrot is eating.")
        self.isHungry=False
    def talk(self):
        print(f"Parrot {self._name} is talking with visitor")
        self.isHappy=True
        self.isHungry=True
    def accept(self, visitor):
        print (f"Parrot {self._name} is accepting visitor")
        visitor.visit_parrot(self)

class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit_cat(self, pet):
        pass
    @abstractmethod
    def visit_dog(self, pet):
        pass
    @abstractmethod
    def visit_parrot(self, pet):
        pass

class Veterinarian(Visitor):
    def visit_cat(self, pet):
        print("Veterinarian is treating the cat.")
        pet.treat()
    def visit_dog(self, pet):
        print("Veterinarian is treating the dog.")
        pet.treat()
    def visit_parrot(self, pet):
        print("Veterinarian is treating the parrot.")
        pet.treat()
    def __str__(self):
        return "Veterinarian"
        
class Scoundrel(Visitor):
    def visit_cat(self, pet):
        print("Scoundrel is hurting the cat.")
        pet.hurt()
    def visit_dog(self, pet):
        print("Scoundrel is hurting the dog.")
        pet.hurt()
    def visit_parrot(self, pet):
        print("Scoundrel is hurting the parrot.")
        pet.hurt()
    def __str__(self):
        return "Scoundrel"

class DogTrainer(Visitor):
    def visit_cat(self, pet):
        return "I can train only dogs!"
    def visit_dog(self, pet):
        print("Dog Trainer is training the dog.")
        pet.trainDog()
    def visit_parrot(self, pet):
        return "I can train only dogs!"
    def __str__(self):
        return "Dog Trainer"
class Master(Visitor):
    def visit_cat(self, pet):
        print("Master is feeding the cat.")
        pet.feed()
    def visit_dog(self, pet):
        print("Master is giving a bone to the dog.")
        pet.getBone()
    def visit_parrot(self, pet):
        print("Master is feeding the parrot.")
        pet.feed()

    def __str__(self):
        return "Master"
class Child(Visitor):
   def visit_cat(self, pet):
        print("Child is playing with the cat.")
        pet.play()
   def visit_dog(self, pet):
        print("Child is walking the dog.")
        pet.walking()
   def visit_parrot(self, pet):
        print("Child is talking to the parrot.")
        pet.talk()

pets=[ Cat("Whiskers"), Dog("Buddy"), Parrot("Polly")]
visitors=[ Veterinarian(), Scoundrel(), DogTrainer(), Master(), Child() ]
for pet in pets:
    print("-----")
    for visitor in visitors:
        pet.accept(visitor)
    print(pet)
    print("-----")
