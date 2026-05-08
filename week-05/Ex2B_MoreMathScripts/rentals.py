# rentals.py
# Calculate charter van rentals for a tour group

import math

# Number of tourists
people = 38

# Van details
seats_per_van = 15
cost_per_van = 250

# Calculate vans needed
vans_needed = math.ceil(people / seats_per_van)

# Total rental cost
total_cost = vans_needed * cost_per_van

# Cost per person
cost_per_person = total_cost / people

# Results
print(f"People going on tour: {people}")
print(f"Vans needed: {vans_needed}")
print(f"Total van cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# Check work
collected_money = people * cost_per_person

print("\nCheck Work:")
print(f"a) Charge per person: ${cost_per_person:.2f}")
print(f"b) Total collected: ${collected_money:.2f}")
print(f"c) Cost of vans: ${total_cost:.2f}")
print("d) Leftover money happens because cost per person was rounded to the nearest cent.")