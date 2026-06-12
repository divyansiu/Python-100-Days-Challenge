"""
Question 41: Reverse a Number
"""
#Solution : 

num = int(input("Enter the number : "))

temp = num
digit = 0

# 1209 // 10 -> 120 // 10 -> 12 // 10 -> 1 // 10 -> 0

while temp > 0:
    digit += 1
    temp = temp//10

rev_num = 0

while num > 0 :
    rev_num += (num%10)*(10**(digit-1))
    num = num//10
    digit -= 1

print("The Reversed Number is",rev_num)
