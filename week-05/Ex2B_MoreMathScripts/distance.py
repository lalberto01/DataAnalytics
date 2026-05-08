# distance.py
# Calculate distance between two coordinates

import math

# Example coordinates
x1 = 2
y1 = 3
x2 = 7
y2 = 9

# Distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Result
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")