"""
Question 39: Factorial Calculator
"""
#Solution : 

num = int(input("Which number Factorial do you want : "))
factorial = 1
for i in range(1,num+1) :
    factorial *= i
print("The factorial if the number",num,"is",factorial)
