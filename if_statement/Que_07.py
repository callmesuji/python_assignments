# Write a program to accept the billing amount, if it is > 6000 then give a discount of 10% and display the net amount.

amount = int(input("Enter the billing amount:"))

if amount > 6000:
    amount -= amount * 0.1

print(f"Your net billing amount: {amount}")
