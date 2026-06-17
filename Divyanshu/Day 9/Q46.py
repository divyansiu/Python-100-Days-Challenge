"""
Question 46: Fibonacci Series
"""
#Solution :

term = int(input("Enter number of Terms you want : "))
temp_1 = 0
temp_2 = 1
if term == 0 :
    print(1)
else :
    print(temp_2)
    while term > 0 :
        temp_2 += temp_1
        print(temp_2)
        temp_1 = temp_2
        term -= 1

    
