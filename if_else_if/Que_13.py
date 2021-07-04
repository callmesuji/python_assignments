# Write a program to accept 3 numbers from the user and find the biggest of them.

num1 = int(input("Enter the 1st number num1:"))
num2 = int(input("Enter the 2nd number num2:"))
num3 = int(input("Enter the 3rd number num3:"))

if num1 > num2 and num1 > num3:
    print(f"The biggest of the 3 numbers entered is: {num1}")
elif num2 > num3:
    print(f"The biggest of the 3 numbers entered is: {num2}")
else:
    print(f"The biggest of the 3 numbers entered is: {num3}")
