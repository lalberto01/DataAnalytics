# Formula 
# Tip Amount = Bill Total x (Tip Percentage/100)

# Known
bill_total = 100.00
tip_percentage = 20

# Calculate tip
tip_amount = bill_total * (tip_percentage / 100)

# Results
print("The tip on a $"+ format(bill_total, ".2f") + "restaurant bill is $" + format(tip_amount, ".2f"))