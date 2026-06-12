"""
Question 42: Palindrome Number Checker
"""
#Solution : 

num = int(input("Enter the number to check plaindrome : "))

rev_num = 0
temp = num 

while temp > 0 :
    digit = temp % 10
    rev_num = rev_num*10 + digit
    temp = temp//10

if num == rev_num :
    print("Given Number is Plaindrome number")
else :
    print("Given Numbr is not a Palindrome number")