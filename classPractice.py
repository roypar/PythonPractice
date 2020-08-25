class Person:
    def __init__(self, name="John Doe", age=35, height=173):
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return f"Name is {self.name}, age is {self.age}, height is {self.height}"


myself = Person("Parijat")
myself.weight = 65
print(myself)
print(myself.weight)