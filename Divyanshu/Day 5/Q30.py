"""
Question 30: Divisibility Checker
"""
#Solution :

divident = int(input("Enter the number you want to divide : "))
divisor = int(input("Enter the number you want to divide with : "))

if divident%divisor==0 : 
    print("Given Number is divisible by the given Divisor.")
else :
    print("Given Number is not divisible by the given Divisor.")