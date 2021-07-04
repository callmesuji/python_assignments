# Write a program to accept a number from the user and print its multiplication table (upto “times 10”).

num = int(input("Enter the number to generate its multiplication table:"))

print(f"Multiplication table for {num} is :")

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
