# Write a program to accept a number and determine whether it is a prime number or not.
num = int(input("Enter any number:"))


def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0 and num != 2:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        else:
            return True


if is_prime(num):
    print(f"The entered number {num} is a prime number")
else:
    print(f"The entered number {num} is not a prime number")

 
