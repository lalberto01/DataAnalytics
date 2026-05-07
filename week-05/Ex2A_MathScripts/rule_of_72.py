# Current savings amount
savings = 500

# interest rate as deciaml 6%
interest_rate = 0.06 

# convert to percent
rate_percent = interest_rate * 100

# rule of 72 formula
years = 72 / rate_percent

# Double savings
doubled_balance = savings * 2

# Results
print("Your current savings is", savings)
print("At a", format(interest_rate, ".0%"),"interest rate, your savings account will be")
print("worth", format(doubled_balance, ".2f"), "in", format(years, ".1f"), "years")

# Lab 4
# Tip Amount = Bill Total x (Tip Percentage / 100)

# Ask user for values
bill_total = float(input("How much was your restaurant bill? "))
tip_percentage = float(input("What percentage do you want to tip? "))

# Calculate tip
tip_amount = bill_total * (tip_percentage / 100)

# Output using f-string
print(f"The tip on a ${bill_total:.2f} restaurant bill is ${tip_amount:.2f}")