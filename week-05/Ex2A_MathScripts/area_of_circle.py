python
import math # gives access to pi and other math tools

# Known
diameter = 21 # day of birthdate

# Calculate Radius
radius = diameter / 2 # Radius is half the diameter

# Area of the circle
area = math.pi * (radius ** 2)  # ** means power to

Answer
print("The area of a circle with radius " + str(radius) + "is" + format(area, ".2f") )
