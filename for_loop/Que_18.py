#  Write a program to accept the lower bound number and the upper bound number from the user
#  and print the prime numbers between them.

lb = int(input("Enter the lower bound value:"))
ub = int(input("Enter the upper  bound value:"))

def isprime(num):
    if num < 2 :
        return False
    if num % 2 == 0 and num != 2 :
        return False
    else :
        for i in range(2,num // 2 + 1):
            if num % i == 0:
                return False
        else:
            return True

print(f"The prime numbers between {lb} and {ub} are :",end=" ")
for i in range(lb,ub+1):
    if isprime(i):
        print(f"{i}",end=" ")


