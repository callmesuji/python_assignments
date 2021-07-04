name = input("Enter the name:")
mobile_number = input("Enter the mobile number:")
age = int(input("Enter the age:"))
if age > 18:
    print(f"Congratulations {name} for your successful registration.")
else:
    print(f"Sorry! You need to be at least 18 years old to get membership.")
