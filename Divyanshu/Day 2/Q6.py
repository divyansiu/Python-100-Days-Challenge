"""
Question 6: Swap Two Variables

Take two numbers as input.

Swap their values and print the result.

Part A:
Use a third variable.

Part B:
Swap without using a third variable.
"""
#Solution :-

num1 = float(input("Enter the 1st Number : "))
num2 = float(input("Enter the 2nd Number : "))

temp=num2
num2=num1
num1=temp

print("After Swaping using 3rd variable : ")
print("1st Number",num1)
print("2nd number",num2)

num1=num2
num2=temp

num1=num1+num2
num2=num1-num2
num1=num1-num2
print("without using the 3rd variable : ")
print("1st Number",num1)
print("2nd number",num2)

