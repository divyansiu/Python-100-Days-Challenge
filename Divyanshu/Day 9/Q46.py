"""
Question 46: Fibonacci Series
"""
#Solution :

term = int(input("Enter number of Terms you want : "))
first = 0
second = 1
next = 0
if term == 0 :
    print("Please enter a positive number")
elif term == 1 :
    print("0")
elif term == 2 :
    print("0")
    print("1")
else :
    print("0")
    print("1")
    while term-2 > 0 :
        next = first + second
        print(next)
        first = second
        second = next
        term -= 1

        

    