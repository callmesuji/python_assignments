# Write a program to generate the first 'N' natural numbers. Accept the value of 'N' from the user.
num = int(input("Enter the number of natural numbers to be generated:"))

print(f"first {num} natural numbers are :",end=" ")

for i in range(1,num+1):
    print(f" {i}",end=" ")