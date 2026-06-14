"""
Question 43: Armstrong Number Checker
"""
#Solution : 

#Armstrong number = An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digit

num = int(input("Enter Number to Check if it is armstrong or not : "))

new_num = 0

temp_1 = num

digit = 0

while temp_1 != 0 :
    digit += 1
    temp_1 //= 10

temp_2 = num

while temp_2 != 0 :
    new_num += (temp_2 % 10) ** digit
    temp_2 //= 10

if new_num == num :
    print("Given number is an Armstrong number")
else :
    print("Given number is not an Armstrong number")
