#  In a shopping mall, privileged customers (if they have a membership card) are being given a 10% discount
#  on the billed amount, and the others are being given a 3% discount. Write a program to accept the billing amount
#  and confirm the membership card from the customer; calculate and display the net amount to be paid by the customer.

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
