# Trying out out of class instance attribute assignment
class Person:
    def __init__(self, name="John Doe", age=35, height=173):
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return f"Name is {self.name}, age is {self.age}, height is {self.height}"


myself = Person("Parijat")
myself.weight = 65
# print(myself)
# print(myself.weight)

# Trying out Class vs Instance attributes
# Trying out instance vs class vs static method


class Players:
    teamMembers = []
    team_name = 'Liverpool'

    @staticmethod
    def get_bmi(height, weight):
        return weight/(height*height)

    @classmethod
    def get_class_name(cls):
        return cls.team_name

    def __init__(self, name, salary=0):
        self.name = name
        self.teamMembers.append(self.name)
        self.__salary = salary


p1 = Players('Mark', 1000)
p2 = Players('Steve', 2000)
p3 = Players('Parijat', 500)

# print(f"{p1.name} has {p1.teamMembers} as teammates")
# print(f"{p2.name} has {p2.teamMembers} as teammates")
# print(Players.get_class_name())
# print(Players.get_bmi(173, 72))
# print(p3._Players__salary)


class Vehicle:
    def __init__(self, registration, type):
        self.registration = registration
        self.type = type

    def show_vehicle(self):
        print(f"Vahicle has plate number {self.registration} and type {self.type}")

# Trying out single inheritance and super() function
class Car(Vehicle):
    def __init__(self, registration, type, model, color):
        super().__init__(registration, type)
        self.model = model
        self.color = color

    def show_car(self):
        self.show_vehicle()
        print(f"Model is {self.model} and color is {self.color}")


# c1 = Car("WB26s", "Car", "Maruti", "Blue")
# c1.show_vehicle()
# c1.show_car()


# Trying out Hybrid inheritance(both Multilevel and Multiple) inheritance

class Engine:
    def __init__(self, max_power, max_torqure):
        self.max_power = max_power
        self.max_torque = max_torqure

    def show_engine_capacity(self):
        print(f"Max-Power is {self.max_power} KW and Max-Torque is {self.max_torque} N-M.")


class PetrolEngine(Engine):
    def __init__(self, max_power, max_torque, fuel_capacity=0):
        super().__init__(max_power, max_torque)
        self.fuel_capacity = fuel_capacity

    def show_engine_capacity(self):
        print(f"Fuel capacity in {self.fuel_capacity} L.")

    def set_fuel_capacity(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity


class ElectricEngine(Engine):
    def __init__(self, max_power, max_torque, cell_capacity):
        super().__init__(max_power, max_torque)
        self.cell_capacity = cell_capacity

    def show_engine_capacity(self):
        print(f"Cell capacity in {self.cell_capacity} A/H.")

    def set_cell_capacity(self, cell_capacity):
        self.cell_capacity = cell_capacity


# Multiple and Multilevel here
class HybridEngine(PetrolEngine, ElectricEngine):
    def __init__(self, max_power, max_torque, fuel_capacity, cell_capacity):
        Engine.__init__(self, max_power, max_torque)
        PetrolEngine.set_fuel_capacity(self, fuel_capacity)
        ElectricEngine.set_cell_capacity(self, cell_capacity)

    def show_engine_specs(self):
        Engine.show_engine_capacity(self)
        PetrolEngine.show_engine_capacity(self)
        ElectricEngine.show_engine_capacity(self)


# engine_1 = HybridEngine(2000, 1300, 50, 115)
# engine_1.show_engine_specs()


# Implementing Abstract Classes and Interfaces
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

    def perimeter(self):
        return 4*self.length


sq = Square(10)
print(sq.area())
print(sq.perimeter())
