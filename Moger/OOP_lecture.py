
# 1 Imported packages

import sys
import math

# 2 Rectangles

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height

    def GetX(self):
        return self.x

    def SetX(self, x):
        self.x = x

    def CalcPerimeter(self):
        return 2*self.width + 2*self.height

    def CalcSurface(self):
        return self.width*self.height

# 3 Circles

class Circle:
    def __init__(self, x, y, diameter):
        self.x = x 
        self.y = y
        self.diameter = diameter

    def GetX(self):
        return self.x

    def SetX(self, x):
        self.x = x

    def CalcPerimeter(self):
        return self.diameter*math.pi

    def CalcSurface(self):
        return math.pi*(self.diameter/2)**2


R1 = Rectangle(10, 20, 100, 40)
R2 = Rectangle(40, 80, 100, 80)

C1 = Circle(10, 20, 50)
C2 = Circle(10, 20, 100)

# 4 Test

print("rectangle {0:g} {1:g} {2:g} {3:g} {4:g} {5:g}".format(R1.x, R1.y, R1.width, R1.height, R1.CalcPerimeter(), R1.CalcSurface()))
print("rectangle {0:g} {1:g} {2:g} {3:g} {4:g} {5:g}".format(R2.x, R2.y, R2.width, R2.height, R2.CalcPerimeter(), R2.CalcSurface()))

print("Circle {0:g} {1:g} {2:g} {3:g} {4:g}".format(C1.x, C1.y, C1.diameter, C1.CalcPerimeter(), C1.CalcSurface()))
print("Circle {0:g} {1:g} {2:g} {3:g} {4:g}".format(C2.x, C2.y, C2.diameter, C2.CalcPerimeter(), C2.CalcSurface()))




