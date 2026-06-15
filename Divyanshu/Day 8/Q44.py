"""
Question 44: Prime Number Checker
"""
#Solution :

num = int(input("Enter the Number : "))

temp_1 = num
remainder = 0

for i in range(1,temp_1+1):
    if temp_1 % i == 0 :
        remainder += 1
        
if remainder == 2 :
    print("Given Number is a Prime Numbber.")
else :
    print("given Number is not a Prime Numeber.")