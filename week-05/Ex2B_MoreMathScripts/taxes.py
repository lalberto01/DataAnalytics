# Federal taxes are 23% of monthly salary

salary = 1000.00

tax_withheld = salary * 0.23
take_home = salary - tax_withheld

print(f"If you make ${salary:.2f} per month:")
print(f"Federal taxes withheld: ${tax_withheld:.2f}")
print(f"Pay after taxes: ${take_home:.2f}")