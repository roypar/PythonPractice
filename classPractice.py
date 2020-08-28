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

print(f"{p1.name} has {p1.teamMembers} as teammates")
print(f"{p2.name} has {p2.teamMembers} as teammates")
print(Players.get_class_name())
print(Players.get_bmi(173, 72))
print(p3._Players__salary)
