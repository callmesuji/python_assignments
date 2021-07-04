# Write a program to accept the marks scored in three subjects; 
# determine the sum and average of the entered marks.
#  Grade is awarded based on following criteria.

num1 = int(input("Enter the marks scored in 1st subject:"))
num2 = int(input("Enter the marks scored in 2nd subject:"))
num3 = int(input("Enter the marks scored in 3rd subject:"))

total_marks = num1 + num2 + num3

average = total_marks / 3

if average < 35:
    grade = "C"
    print(f"Total marks: {total_marks}")
    print(f"Average is: {average}")
    print(f"Grade: {grade}")
elif average > 35 and average < 60:
    grade = "B"
    print(f"Total marks: {total_marks}")
    print(f"Average is: {average}")
    print(f"Grade: {grade}")
else:
    grade = "A"
    print(f"Total marks: {total_marks}")
    print(f"Average is: {average}")
    print(f"Grade: {grade}")