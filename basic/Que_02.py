# Write a program to accept the weight of 3 persons, calculate the total weight, 
# determine the average weight and display these details.

num1 = float(input("Enter the weight of the first person:"))
num2 = float(input("Enter the weight of the second person:"))
num3 = float(input("Enter the weight of the second person:"))

weight = num1 + num2 + num3

avg_weight = (num1 + num2 + num3) / 3

print(
    f"The sum of weight of the 3 persons is {weight} Kgs and the average weight is {avg_weight} Kgs"
)
