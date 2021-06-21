class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_info(self):
        return "Vehicle Name: {}, Speed: {} km/h, Mileage: {} mile".format(self.name, self.max_speed, self.mileage)

class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

if __name__=="__main__":
    name = input("Enter name: ").capitalize()
    max_speed = int(input("Enter speed: "))
    mileage = float(input("Enter mileage: "))
    b = Bus(name, max_speed, mileage)
    print(b.print_info())

