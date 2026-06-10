"""
Question 9: Swap Without Third Variable
Swap values using operators.
"""
#Solution :

a = 1
b = 3
print("Before Swapping : 1st no = ",a,"& 2nd No = ",b)
a += b
b = a-b
a = a-b
print("After Swapping : 1st no = ",a,"& 2nd No = ",b)
