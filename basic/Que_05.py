amount = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate of interest :"))
time = int(input("Enter the time (years)"))

interest = (amount * time * rate) / 100

print(f"Simple interest is {interest}")
