# List of favorite foods
foods = ["tacos", "ramen", "pizza", "sushi", "burgers"]

# Numbered list using enumerate (starting at 1)
for index, item in enumerate(foods, start=1):
    
    # If first item, add special message
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:
        print(f"{index}. {item}")