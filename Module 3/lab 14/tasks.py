import random
import time
import os
Base_dir=os.path.dirname(__file__)
class Cat:
    def __init__(self, name):
        self._name = name
        self._mood = 50
        self._hunger=40
        self._energy=40
        self._favourite_toys=[]
        self._not_favourite_toys=[]
        self._toy_stats={}  

    def say_hello(self):
        print("Meow!")
    def introduce_yourself(self):
        print(f"My name is" + self._name)
    def favourite_toys(self, toy):
        if toy in self._not_favourite_toys:
            self._not_favourite_toys.remove(toy)

        if toy not in self._favourite_toys:
            self._favourite_toys.append(toy)
            print(f"{self._name} loves playing with {toy}.")
        else:
            print(f"{self._name} already loves {toy}.")
    def dislike_toy(self, toy):
        if toy not in self._not_favourite_toys:
            self._not_favourite_toys.append(toy)
            print(f"{self._name} dislikes playing with {toy}.")
        else:
            print(f"{self._name} already dislikes {toy}.")
        if toy in self._favourite_toys:
            self._favourite_toys.remove(toy)

    def toy_box(self,toy):
        self._toy_stats[toy] = self._toy_stats.get(toy, 0) + 1

        action = random.choice(["ignore", "like", "dislike"])

        if action == "ignore":
            print(f"{self._name} ignores {toy}")

        elif action == "like":
            if toy in self._not_favourite_toys:
                self._not_favourite_toys.remove(toy)

            if toy not in self._favourite_toys:
                self._favourite_toys.append(toy)
                print(f"{self._name} likes {toy}")
            else:
                print(f"{self._name} already likes {toy}")

        elif action == "dislike":
            if toy in self._favourite_toys:
                self._favourite_toys.remove(toy)

            if toy not in self._not_favourite_toys:
                self._not_favourite_toys.append(toy)
                print(f"{self._name} dislikes {toy}")
    def describe_toys(self):
        print(f"Favourite toys: ",self._favourite_toys)
        print(f"Not favourite toys: ",self._not_favourite_toys)
    def take_offense(self):
        print(f"{self._name} is offended!")
    def playing(self, toy):
        if toy in self._favourite_toys:
            print(f"{self._name} is happily playing with {toy}!")
            self._mood+=10
            self._energy-=15
        elif toy in self._not_favourite_toys:
            print(f"{self._name} refuses to play with {toy}.")
            print(self.take_offense())
            self._mood-=20
        else:
            print(f"{self._name} is curious about {toy}.")

    def sleep(self, hours):
        print(f"{self._name} is sleeping for {hours} hours.")
        self._mood+=2*hours
        self._energy+=3*hours

    def eating(self):
        print(f"{self._name} is eating.")
        self._hunger-=20
        self._mood+=5

    def drinking(self):
        print(f"{self._name} is drinking water.")
        self._hunger-=5
        self._mood+=2

    def end_of_day(self):
        print(f"End of the day for {self._name}.")
        self._hunger += 10
        self._energy -= 5
        self._mood -= 5
        print(f"Hunger: {self._hunger}, Energy: {self._energy}, Mood: {self._mood}")
    def living_day(self):
        day_info=f"Day {day} in the life of {self._name}"
        print(f"{day_info:=^50}")
        live_cube=random.randint(1,4)
        if self._hunger > 70:
            print(f"{self._name} is very hungry -> time to eat.")
            self.eating()
        elif self._mood < 30:
            print(f"{self._name} is feeling down -> time to play.")
            self.playing(random.choice(self._favourite_toys + self._not_favourite_toys))
        if live_cube == 1:
            self.playing(random.choice(self._favourite_toys + self._not_favourite_toys))
        elif live_cube == 2:
            self.sleep(random.randint(1,5))
        elif live_cube == 3:
            self.eating()
        else:
            self.drinking()
        self.end_of_day()
        print()
    

class Box:
    def __init__(self,toy):
        self.toy=toy

toys_path=os.path.join(Base_dir, 'Toys.txt')
with open(toys_path, 'r', encoding='utf-8') as file:
    toys = [line.strip() for line in file]

boxes = [Box(toy) for toy in toys]

cat = Cat("Whiskers")
cat.say_hello()
cat.introduce_yourself()

STEPS = 100

for step in range(STEPS):
    print(f"\nStep {step + 1}")
    box = random.choice(boxes)
    cat.toy_box(box.toy)