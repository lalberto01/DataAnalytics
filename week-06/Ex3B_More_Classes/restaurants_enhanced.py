class Restaurant:
    '''
    This class represents a restaurant, its food type.
    '''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(self.rest_name, "serves", self.food_type + ".")

    def rest_open(self):
        print(self.rest_name, "is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served = self.number_served + customers

    def print_num_served(self):
        print(self.rest_name, "has served", self.number_served, "customers")

    def customer_rating(self):
        rating = input("How would you rate your experience today on a scale of 1-5? ")

        if rating.isdigit():
            rating = int(rating)

            if rating >= 1 and rating <= 5:
                self.customer_ratings.append(rating)
                average = sum(self.customer_ratings) / len(self.customer_ratings)

                print("Your rating was", rating)
                print("The average rating for this restaurant is", format(average, ".2f"))
            else:
                print("Invalid rating. Please enter a whole number from 1 to 5.")
        else:
            print("Invalid rating. Please enter a whole number from 1 to 5.")


# Create restaurant instances
restaurant1 = Restaurant("Taco Baco", "Mexican food")
restaurant2 = Restaurant("Dunkin Donuts", "breakfast and coffee")
restaurant3 = Restaurant("Burger King", "fast food")


# Test restaurant descriptions
restaurant1.describe_rest()
restaurant1.rest_open()

print()

restaurant2.describe_rest()
restaurant2.rest_open()

print()

restaurant3.describe_rest()
restaurant3.rest_open()

print()


# Test number served
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

print()

restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

print()

restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()

print()


# Test customer ratings
restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()

print()

restaurant2.customer_rating()
restaurant2.customer_rating()
restaurant2.customer_rating()

print()

restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()