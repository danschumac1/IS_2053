'''
2025-07-21
Author: Dan Schumacher
How to run:
    python ./src/lessons/oop/inheritance_examples.py
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def description(self):
        return f"This is a {self.make} {self.model}."

    def start_engine(self):
        return "The engine starts with a roar!"


# Child class
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def description(self):
        # Override to include battery info
        return f"This is a {self.make} {self.model} with a {self.battery_size}kWh battery."

    def start_engine(self):
        # Override with EV specific behavior
        return "The electric motor starts silently."


# Another child class
class GasVehicle(Vehicle):
    def __init__(self, make, model, fuel_capacity):
        super().__init__(make, model)
        self.fuel_capacity = fuel_capacity

    def refuel(self):
        return f"Refueled {self.fuel_capacity} liters of gas."


# Example usage
def main():
    car = Vehicle("Toyota", "Corolla")
    print(car.description())
    print(car.start_engine())

    tesla = ElectricVehicle("Tesla", "Model 3", 75)
    print(tesla.description())
    print(tesla.start_engine())

    mustang = GasVehicle("Ford", "Mustang", 60)
    print(mustang.description())
    print(mustang.start_engine())
    print(mustang.refuel())


if __name__ == "__main__":
    main()
