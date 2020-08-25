#Exercise 1
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x**2+self.y**2+self.z**2)


p1 = Point(1,3,5)
# print(p1.sqSum())

#Exercise 2
class Student:
    totalMarks = 300

    def __init__(self, name=None, phy=None, chem=None, bio=None):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def aggregatePercent(self):
        return self.totalObtained()/self.totalMarks


s1 = Student("Roy", 80, 90, 41)
print("Total: {0}, Percent: {1:.1%}".format(s1.totalObtained(),s1.aggregatePercent()))

#Exercise 3
class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def substract(self):
        return self.num2-self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2/self.num1


c1 = Calculator(10,94)

print(c1.add())
print(c1.substract())
print(c1.multiply())
print(c1.divide())