# -----------------------------------
# Function 1: Mailing Label
# -----------------------------------

def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(city, state, zip)


# -----------------------------------
# Function 2: Add Numbers
# -----------------------------------

def add_numbers(*numbers):
    total = 0
    output = ""

    # Add all numbers together
    for num in numbers:
        total = total + num

    # Build output string
    for i in range(len(numbers)):
        output = output + str(numbers[i])

        if i < len(numbers) - 1:
            output = output + " + "

    print(output, "=", total)


# -----------------------------------
# Function 3: Display Receipt
# -----------------------------------

def display_receipt(total_due, amount_paid):
    print("Total Due: $", format(total_due, ".2f"))
    print("Amount Paid: $", format(amount_paid, ".2f"))

    # Check payment amount
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print("Change Due: $", format(change, ".2f"))
    else:
        balance = total_due - amount_paid
        print("Remaining Balance: $", format(balance, ".2f"))


# -----------------------------------
# Mailing Label Tests
# -----------------------------------

display_mailing_label(
    "Lesley Alberto",
    "123 Main St",
    "Concord",
    "NC",
    "28025"
)

print()

display_mailing_label(
    "Rebecca Lopez",
    "456 Oak Drive",
    "Atlanta",
    "GA",
    "30303"
)

print()


# -----------------------------------
# Add Numbers Tests
# -----------------------------------

# One number
add_numbers(5)

print()

# Two numbers
add_numbers(10, 20)

print()

# More than two numbers
add_numbers(2, 4, 6, 8, 10)

print()


# -----------------------------------
# Display Receipt Tests
# -----------------------------------

# Overpaying
display_receipt(25.50, 40.00)

print()

# Exact payment
display_receipt(30.00, 30.00)

print()

# Underpaying
display_receipt(50.00, 35.00)