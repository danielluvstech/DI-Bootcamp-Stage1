# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them

import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please provide either a radius or a diameter.")
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, and area: {self.area:.2f}"
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError("Can only add another Circle instance.")
    
    def __lt__(self, other):
        return self.radius < other.radius if isinstance(other, Circle) else NotImplemented
    
    def __le__(self, other):
        return self.radius <= other.radius if isinstance(other, Circle) else NotImplemented
    
    def __eq__(self, other):
        return self.radius == other.radius if isinstance(other, Circle) else NotImplemented
    
    def __ne__(self, other):
        return not self == other
    
    def __gt__(self, other):
        return self.radius > other.radius if isinstance(other, Circle) else NotImplemented
    
    def __ge__(self, other):
        return self.radius >= other.radius if isinstance(other, Circle) else NotImplemented

c1 = Circle(radius=5)
c2 = Circle(diameter=8)
c3 = c1 + c2
circle_list = [c1, c2, c3]
circle_list.sort()

print(c1)
print(c2)
print(c3)
print(c1 > c2)
print(circle_list)
