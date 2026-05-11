# Description: This script calculates gross pay with overtime
# Example values
pay_rate = 17.30
hours_worked = 45

# Calculate gross pay
if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

# Results
print(f"Pay rate: ${pay_rate:.2f}")
print(f"Hours worked: {hours_worked}")
print(f"Gross pay: ${gross_pay:.2f}")