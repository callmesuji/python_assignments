amount = float(input("Enter the bill amount:"))
value = str(input("Do you have a membership card?"))

if value == "YES" or value == "yes":
    total_amount = amount - amount * 0.1
    discount = amount * 0.1
    print(
        f"Thank you! Your total bill amount is Rs {amount}, discount is Rs {discount} and net amount payable is Rs {total_amount}."
    )
elif value == "NO" or value == "no":
    total_amount = amount - amount * 0.03
    discount = amount * 0.03
    print(
        f"Thank you! Your total bill amount is Rs {amount}, discount is Rs {discount} and net amount payable is Rs {total_amount}."
    )
