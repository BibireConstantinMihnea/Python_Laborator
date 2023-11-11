class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self. year = year

    def print_info(self):
        print(f"{self.make} {self.model} {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_ef):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_ef

    def mileage(self, miles):
        return miles / self.fuel_efficiency
    
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_ef):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_ef

    def mileage(self, miles):
        return miles / self.fuel_efficiency
    
class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_ef, tow_cap):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_ef
        self.tow_capacity = tow_cap

    def mileage(self, miles):
        return miles / self.fuel_efficiency
    
    def can_tow(self, load):
        if load <= self.tow_capacity:
            print(f"Load of {load} can be towed.")
        else : print(f"Load of {load} too heavy.")

car = Car("Toyota", "Camry", 2022, 30)
car.print_info()
print("Estimated mileage for 100 miles:", car.mileage(100))

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2022, 10)
motorcycle.print_info()
print("Estimated mileage for 100 miles:", motorcycle.mileage(100))

truck = Truck("Ford", "F-150", 2022, 50, 8000)
truck.print_info()
truck.can_tow(6000)
truck.can_tow(10000)