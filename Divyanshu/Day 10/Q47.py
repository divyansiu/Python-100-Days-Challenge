"""
Question 47: Sum of Digits
"""
#Solution :

num = int(input("Enter the number : "))

sum = 0

while num != 0 :
    sum += num % 10
    num = num // 10

print("Sum of the Digits of given nume=ber is",sum)