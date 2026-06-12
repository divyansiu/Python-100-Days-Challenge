"""
Question 37: Sum of First N Numbers
"""
#Solution : 

N = int(input("Enter Number till you want sum of natural numnbers : "))
sum = 0
for i in range(1,N+1) :
    sum += i
print(sum)