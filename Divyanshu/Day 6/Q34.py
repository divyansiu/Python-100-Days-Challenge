"""
Question 34: Triangle Type Checker
"""
#Solution : 

a = float(input("Enter length on 1st side of triangle : "))
b = float(input("Enter length on 2nd side of triangle : "))
c = float(input("Enter length on 3rd side of triangle : "))

if a == b and b == c :
    print("Equilateral Triangle")
elif a != b and b != c and c != a :
    print("Scalene Triangle")
elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a) :
    print("Isoceles Triangle")
