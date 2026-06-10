"""
Question 12: Reverse GST Calculator
Given final amount after GST.
Find original amount.
"""
#Solution :
after_tax = float(input("Enter the Amount after GST : "))
p_price = (after_tax*100)/118
print("The Originall Price of the product was",p_price)