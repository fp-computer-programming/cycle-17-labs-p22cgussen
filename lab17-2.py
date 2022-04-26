# Author CCG 4/29/22

import math

class Circle: # def class
    def __init__(self): # default circle
        self.radius = 1
    def get_area(self): # area function and equation
        return (math.pi * (self.radius**2))
    def get_diameter(self): # find diameter
        return self.radius * 2
    def get_perimeter(self): # find circumference
        return (self.get_diameter() * math.pi)


my_circle = Circle() # calling functions and print statments
my_circle.radius = 3
print(my_circle.get_area())
print(my_circle.get_perimeter())
