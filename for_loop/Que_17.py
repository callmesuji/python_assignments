# Write a program to generate the first 'N' natural numbers and print them in descending order.

num = int(input("Enter the number of natural numbers to be generated:"))

for num in range(num,0,-1):
    print(num)
