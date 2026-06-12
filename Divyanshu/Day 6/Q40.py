"""
Question 40: Count Digits in Number
"""
#Solution :

num = int(input("Enter the Number : "))

count = 0 

while num % 10 != 0 :
    num = num // 10
    count += 1
print("given number has",count,"Digits")