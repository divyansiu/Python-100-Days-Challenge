"""
Question 32: Income Tax Slab Checker
"""

#Solution : 

"""
Tax Slab : 
upto 4 lakh == nill
4 - 8 lakh == 5%
8 - 12 lakh == 10%
12 - 16 == 15%
16 - 20 == 20%
20 - 24 == 25%
above 24 == 30% 
"""

income = float(input("Enter the Income of the person : "))

if income <= 400000 : 
    print("Tax is",income*0/100)
elif income <= 800000 :
    print("Tax is",income*5/100)
elif income <= 1200000 :
    print("Tax is",income*10/100)
elif income <= 1600000 :
    print("Tax is",income*15/100)
elif income <= 2000000 :
    print("Tax is",income*20/100)
elif income <= 2400000 :
    print("Tax is",income*25/100)
else :
    print("Tax is",income*30/100)