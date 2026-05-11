# Description: This script uses tuples and sets to create candy combinations
# 1. Create two tuples

candy_types = ("Gummy Bears", "Lollipops", "Jelly Beans")
fruit_flavors = ("Strawberry", "Blue Raspberry", "Watermelon")

# 2. Create a set of candy combinations

candy_options = {
    candy_types[0] + " - " + fruit_flavors[0],
    candy_types[1] + " - " + fruit_flavors[1],
    candy_types[2] + " - " + fruit_flavors[2]
}

# 3. Print output

print("Today's candy options include:")
print(candy_options)

# Print multiple times to compare order
print(candy_options)
print(candy_options)

# Notice:
# Sets do not keep items in a specific order,
# so the order may look different each time.