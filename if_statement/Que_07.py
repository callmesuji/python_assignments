amount = int(input("Enter the billing amount:"))

if amount > 6000:
    amount -= amount * 0.1


print(f"Your net billing amount: {amount}")
