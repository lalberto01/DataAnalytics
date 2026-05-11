# Sales data (name, region, total sales)
sales_data = [
    ("Marcus Webb", "East", 4250.00),
    ("Priya Sharma", "West", 5875.50),
    ("DeShawn Carter", "East", 3100.75),
    ("LaTonya Rivers", "South", 6420.00),
    ("Bob Nguyen", "West", 4980.25),
]

# Loop through and unpack each tuple
for name, region, total in sales_data:
    
    # Print summary line
    print(f"{name} ({region}): ${total:,.2f}")
    
    # Check for top performers
    if total > 5000:
        print(" ^ Top performer!")