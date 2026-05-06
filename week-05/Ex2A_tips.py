# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
print("The total due is " + str(total_due))

# a) THe str is used to turn total due into text insead of a number. It helps combine
#    text and numbers without error.

# Known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# The unkown 
total_due = food_cost + tax + tip

# Display the results
print("The total due is " + str(total_due))
print("Food cost is" + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))         # Comment out
print ("Tip is " + format(tip, ".2f"))  # updated line
print("Total due is "+ str(total_due))