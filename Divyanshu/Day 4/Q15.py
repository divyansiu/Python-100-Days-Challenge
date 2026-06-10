"""
Question 15: Compound Interest Calculator
Calculate compound interest for 2 years.
"""
#Solution : 
P = float(input("Enter the Principle Amount : "))
ROI = float(input("Enter the rate of intrest : "))
time = 2

# first_year_intrest = P*ROI/100
# amount_after_first_year = P + P*ROI/100
# second_year_intrest = amount_after_first_year*ROI/100
# compound_intrest = first_year_intrest + second_year_intrest

amount_after_1st_year = P*(1+ROI/100)
amount_after_2nd_year = amount_after_1st_year*(1+ROI/100)
compound_intrest = amount_after_2nd_year - P


print("Compund Intrest Of the given Data is",compound_intrest)

