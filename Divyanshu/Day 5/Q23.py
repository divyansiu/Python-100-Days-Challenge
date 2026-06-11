"""
Question 23: Largest of Two Numbers
"""
#Solutions :

num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number : "))

if num1==num2 :
    print("Can't select same numbers")
elif num1>num2 :
    print(num1,"is greatest")
else :
    print(num2,"is greatest")