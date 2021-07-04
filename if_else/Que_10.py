# Write a program to accept two numbers from the user and determine bigger of the two.

num1 = int(input("Enter the first number num1:"))
num2 = int(input("Enter the second number num2:"))

if num1 > num2:
    print(f"The bigger of the two numbers entered ({num1} and {num2}) is: {num1}")
else:
    print(f"The bigger of the two numbers entered ({num1} and {num2}) is: {num2}")
