"""
Question 14: Simple Interest Calculator
Calculate simple interest.
"""
#Solution : 

P = float(input("Enter the Principle Value : "))
ROI = float(input("Enter Rate of Intrest : "))
T = int(input("Enter Time : "))

S_I = (P*ROI*T)/100

print("Simple Intrest =",S_I)