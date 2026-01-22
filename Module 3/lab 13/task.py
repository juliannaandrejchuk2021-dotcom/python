import random
import time
print("== Task 1 ==")
class SportResults:
    points=25

diving = SportResults()
print(diving.points)
diving.points = 150
print(diving.points)

print("== Task 2 ==")
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.gladness-=3
        self.progress+=0.12
    def to_sleep(self):
        print("I will sleep")
        self.gladness+=20
    def to_chill(self):
        print("Rest time")
        self.gladness+=5
        self.progress-=0.2
        self.money-=25
    def to_work(self):
        print("Time to work")
        self.money+=50
        self.gladness-=6
    def end_of_day(self):
        print(f"Gladness={self.gladness}")
        print(f"Progress={round(self.progress, 2)}")
        print(f"Money={self.money}")
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
    def live(self, day):
        day_info = f"Day {day} of {self.name}"
        print(f"{day_info:=^50}")
        live_cube  = random.randint(1, 4)
        if self.money < 0:
            print("No money -> going to work")
            self.to_work()
        elif self.progress < 0.5:
            print("Bad grades -> time to study")
            self.to_study()
           
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            if self.money >= 25:
                self.to_chill()
            else:
                self.to_work()
        else: 
            self.to_work()

        self.end_of_day()
        self.is_alive()
        print()
Nick = Student(name = "Nick")
for day in range(365):
    if not Nick.alive:
       break
    Nick.live(day)
    time.sleep(0.1)
print("== Task 3 ==")
class Human:
    def __init__(self, name="Human", age=24,health=100):
        self.name = name
        self.age = age
        self.money=6000
        self.health=100
        self.mood=50
        self.home=None
        self.work=None
        self.auto=None
    def info(self):
        print(f"""
        Name: {self.name}
        Age: {self.age}
        Money: {self.money}
        Mood: {self.mood}
        """)
    def go_to_work(self):
        if self.work and self.auto:
            print(f"{self.name} drives to work")
            self.money+=self.work.salary
            self.mood-=10
            self.health-=5
            self.work.info()
        else:
            print("No job or car")
    def relaxing_at_home(self):
        if self.home:
            print(f"{self.name} is relaxing at home")
            self.mood+=10
            self.health+=5
            self.home.info()
        else:
            print("No home")

    def buy_car(self,auto):
        if self.money>=auto.price:
            self.auto=auto
            self.money-=auto.price
            print(f"{self.name} bought a {auto.brand}")
        else:
            print("Not enough money to buy a car")

    def live(self):
        print(f"--- {self.name}'s day ---")

        if self.money < 200:
            self.go_to_work()
        elif self.mood<50:
            self.relaxing_at_home()
        else:
            self.go_to_work()

        self.info()
class Auto:
    def __init__(self, brand,price=5000):
        self.brand = brand
        self.price = price
        self.passangers=[]

    def info(self):
        print(f"Brand: {self.brand}, Price: {self.price}")

    def add_passanger(self,*humans):
        for passanger in humans:
            self.passangers.append(passanger)

    def print_passangers_name(self):
        if self.passangers!=[]:
            print(f"Names of {self.brand} passangers:")
            for  passanger in self.passangers:
                print(passanger.name)
        else:
            print(f"There is no passangers in {self.brand}")

class Home:
    def __init__(self, address,comfort=50):
        self.address = address
        self.comfort = comfort
    def relax(self):
        print("Relaxing at home")
        self.comfort += 10
    def info(self):
        print(f"Address: {self.address}, Comfort: {self.comfort}")

class Work:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary
    
    def info(self):
        print(f"Position: {self.position}, Salary: {self.salary}")

    def promote(self, new_position, salary_increase):
        self.position = new_position
        self.salary += salary_increase

home= Home(address="123 Main St", comfort=70)
work = Work(position="Engineer", salary=300)
car = Auto(brand="Toyota",price=5000)

john = Human(name="John", age=30,health=100)
john.home = home
john.work = work
john.buy_car(car)
car.add_passanger(john)
car.print_passangers_name()
for day in range(31):
    print(f"Day {day+1:=^40}")
    john.live()
    time.sleep(0.1)