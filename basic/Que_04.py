#  Write a program to accept two numbers from the user, swap their values and display the result.

num1 = int(input("Enter the first number num1:"))
num2 = int(input("Enter the second number num2:"))

print(f"Before swap, the values of num1={num1} and num2={num2}")

num1,num2 = num2,num1

print(f"After swap, the values of num1={num1} and num2={num2}")
