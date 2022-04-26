# Author CCG 4/29/22

import math # importing math

class Circle: # def class
    def __init__(self): # default values for the circle
        self.radius = 1
    def get_area(self): # function to plug in variables and find area
        return (math.pi * (self.radius**2))

my_circle = Circle() # call funtions and print statement
my_circle.radius = 3
print(my_circle.get_area())
