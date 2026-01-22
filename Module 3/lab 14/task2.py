class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def readodometer(self):
        print("This car has " + str(self.odometer_reading) + " kilometers on it")

    def update_odometer(self,km):
        if km >= self.odometer_reading:
            self.odometer_reading=km
        else:
            print("You cant roll back odometer!")

    def increase_odometer(self,kkm):
        self.odometer_reading += kkm    

    def fill_petrol_tank(self):
        print("This car is equipped with petrol tank")

class Battery:
    def __init__(self, battery_size=70):
        self.battery_size= battery_size

    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)} -kWh battery")

    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        elif self.battery_size==100:
            range=300
        message= f"This car can go approximately {str(range)} kilometers on full charge"
        print(message)

    def upgrade_battery(self):
        if self.battery_size !=100:
            print(f"Changed battery size from {self.battery_size} to 100")
            self.battery_size=100
        else:
            print("Battery is already upgraded")

class Electric_Car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def fill_petrol_tank(self):
        print("This car doesnt need a petrol tank!")

my_tesla=Electric_Car("tesla","model s",2018)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()