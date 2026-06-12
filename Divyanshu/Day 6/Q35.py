"""
Question 35: ATM Withdrawal Validation
"""

#Solution : 

balance = float(input("Enter the Account Balance : "))
wid_amount = float(input("Enter the Amount You  want to withdraw : "))

if wid_amount <= balance :
    print("Withdraw Successfull.")
else :
    print("Ensufficient Balance.")