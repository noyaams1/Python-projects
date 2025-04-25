import random

budget = int(input("Enter your budget: "))

store_items = {
    'tomato': 5,
    'milk': 10,
    'water': 13,
    'cheese': 20,
    'apple': 7,
    'bread': 23,
    'cookies': 19,
    'coke': 16
}

cart = []

while budget > 0:
    # Filter items you can afford
    affordable_items = [item for item in store_items.items() if item[1] <= budget]

    # If nothing is affordable, stop shopping
    if not affordable_items:
        print("Nothing else can be bought with the remaining budget.")
        break

    # Pick a random affordable item
    random_item = random.choice(affordable_items)
    cart += random_item  # Adds name and price
    budget -= random_item[1]

    print(f"Added {random_item[0]} for ${random_item[1]}. Remaining budget: ${budget}")

# Summary
num_of_items = len(cart) // 2
items = cart[::2]  # Item names
total_spent = sum(cart[1::2])  # Prices

print(f"\nNumber of items: {num_of_items}")
print(f"Items bought: {items}")
print(f"Total money spent: ${total_spent}")
print(f"Money left: ${budget}")
