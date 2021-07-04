# Write a program to accept the following details of an employee: empno, name and monthly salary;
#  calculate the yearly salary and display the result.

emp_id = int(input("Enter employee id :"))
emp_name = input("Enter the employee name:")
emp_salary = float(input("Enter the monthly salary:"))

yearly_salary = emp_salary * 12

print(
    f"Hi {emp_name}! Your employee id is {emp_id}, monthly salary is Rs {emp_salary} and yearly salary is Rs {yearly_salary}."
)
