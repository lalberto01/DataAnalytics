# Starting bank balance
balance = 50

# Savings goal
goal = 500

# Weekly savings amount
weekly_savings = 75

# While loop to reach savings goal
while balance < goal:
    balance += weekly_savings

    # 75% or more of goal (treat yourself logic)
    if balance >= goal * 0.75 and balance < goal:
        balance -= 10  # treat cost
        print(f"So close! After treating myself, my balance is up to ${balance:.2f}")

    # More than halfway to goal
    elif balance >= goal / 2:
        print(f"Almost there! This week my balance is up to ${balance:.2f}")

    # Regular weekly update
    else:
        print(f"This week my balance increased to ${balance:.2f}")

# Final message when goal is met
print(f"Goal met! My current balance is ${balance:.2f}")