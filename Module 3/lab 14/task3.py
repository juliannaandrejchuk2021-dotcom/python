class Restraunt:
    def __init__(self,name,ctype):
        self.restraunt_name=name
        self.cuisine_type=ctype
        self.number_served=0
    def describe_restraunt(self):
        print(f"Restraunt - {self.restraunt_name} - \n Cuisine type: {self.cuisine_type} \n Served customers: {self.number_served}")

    def open_restraunt(self):
        print(f"Restraunt - {self.restraunt_name} - is open now ")

    def set_number_served(self,new_num):
        self.number_served=new_num

    def increment_number_set(self):
        self.number_served += 250

class IceCreamStand(Restraunt):
    def __init__(self,name):
        super().__init__(name, "Ice cream")
        self.flavors=["Raspberry","Blueberry","Chocolate"]

    def show_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print("-", flavor)

restraunt=Restraunt("Black lagoon","Polish")
restraunt.describe_restraunt()
restraunt.open_restraunt()
restraunt.set_number_served(5)
restraunt.describe_restraunt()
restraunt.increment_number_set()
restraunt.describe_restraunt()
icecreamstand=IceCreamStand("Icy place")
icecreamstand.show_flavors()