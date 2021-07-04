# Write a program to accept a number from the user and determine whether it is even or odd.

num = int(input("Enter a number:"))

if num % 2 == 0:
    print(f"The entered number {num} is even")
elif num % 2 != 0:
    print(f"The entered number {num} is odd")
