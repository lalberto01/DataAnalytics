import random

products = [
    'Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
    'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp',
    'Surge Protector'
]

print("Product of the Day:", random.choice(products))

print("Survey Products:", random.sample(products, 3))

random.shuffle(products)
print("Shuffled Products:", products)

daily_transactions = random.randint(50, 300)
print("Daily Transaction Count:", daily_transactions)