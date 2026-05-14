# Restaurant class

class Restaurant:
    '''
    This class represents a restaurant and its food type.
    '''

    # Constructor method
    def __init__(self, rest_name, food_type):

        # Instance variables
        self.rest_name = rest_name
        self.food_type = food_type


    # Method to describe restaurant
    def describe_rest(self):

        print(self.rest_name, "serves", self.food_type + ".")


    # Method to show restaurant is open
    def rest_open(self):

        print(self.rest_name, "is open.")


# -----------------------------------
# Create restaurant instances
# -----------------------------------

restaurant1 = Restaurant("Taco Baco", "Mexican food")

restaurant2 = Restaurant("Donkin Donuts", "breakfast and coffee")

restaurant3 = Restaurant("Burber King", "fast food")


# -----------------------------------
# Test methods
# -----------------------------------

restaurant1.describe_rest()
restaurant1.rest_open()

print()

restaurant2.describe_rest()
restaurant2.rest_open()

print()

restaurant3.describe_rest()
restaurant3.rest_open()

# Call methods for restaurant 1
restaurant1.describe_rest()
restaurant1.rest_open()

print()

# Call methods for restaurant 2
restaurant2.describe_rest()
restaurant2.rest_open()

print()

# Call methods for restaurant 3
restaurant3.describe_rest()
restaurant3.rest_open()