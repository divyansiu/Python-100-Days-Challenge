"""
Question 45: Prime Numbers in Range
"""
#Solution :

r_1, r_2 = map(int, input("Enter the Range to Check Prime Numbers in format(num_1, num_2) : ").split(","))

remainder = 0

for i in range(r_1,r_2+1) :
    for j in range(1,i+1) :
        if i % j == 0 :
            remainder += 1
    if remainder == 2 :
        print(i)
    remainder = 0