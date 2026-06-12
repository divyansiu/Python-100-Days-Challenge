"""
Question 31: Profit or Loss Calculator
"""
#Solution : 

init_amount = int(input("Enter the Initial Amount of the product : "))
sell_amount = int(input("Enter the selling amount of the product : "))

if init_amount > sell_amount :
    print("Loss =",init_amount - sell_amount)
else :
    print("Profit =",sell_amount - init_amount)
    