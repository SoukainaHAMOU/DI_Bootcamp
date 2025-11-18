class Circle:
    def __init__(self, radius=None, diameter=None):
        if diameter is not None:
            self.radius = diameter / 2
        elif radius is not None:
            self.radius =  radius
        else:
            raise ValueError("Either radius or diameter must be provided.")
    @property
    def diameter(self):
        diamet = self.radius * 2
        return diamet
    
    @property
    def area(self):
        areaa = 3.14 * (self.radius ** 2)
        return areaa

    @property
    def circumference(self):
        circum = 2 * 3.14 * self.radius
        return circum
    
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    def __add__(self, other):   # Add two circles → new circle with combined radius, 
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented
    
    def __gt__(self, other):    # greater than
        return self.radius > other.radius
    
    def __eq__(self, other):    # equal to
        return self.radius == other.radius
    
    def __lt__(self, other): # less than
        return self.radius < other.radius
    


# circle = Circle(4)
# print("Area of the circle:", circle.area)
# print("-"*20)
# print("Diameter of the circle:", circle.diameter)
# print("-"*20)
# print("Circumference of the circle:", circle.circumference)
# print("-"*20)
# circle_diameter = Circle(diameter=10)
# print("-"*20)
# print("Radius of the circle with diameter 10:", circle_diameter.radius)
# print("-"*20)

c1 = Circle(radius=4)
c2 = Circle(diameter=10)

print(c1)  # Circle(radius=4, diameter=8)
print("Area:", c1.area)
print("Circumference:", c1.circumference)

# Adding circles
c3 = c1 + c2
print("New Circle after addition:", c3)

# Comparisons
print("Is c1 bigger than c2?", c1 > c2)
print("Are c1 and c2 equal?", c1 == c2)

# Sorting
circles = [c1, c2, c3, Circle(radius=2)]
sorted_circles = sorted(circles)
print("Sorted circles by radius:", sorted_circles)

import turtle

def draw_circle(circle):
    t = turtle.Turtle()
    t.circle(circle.radius * 10)  # scale up for visibility
    turtle.done()

# Example: draw the largest circle
draw_circle(max(circles))
