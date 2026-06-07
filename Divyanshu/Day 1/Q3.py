"""
Question 3: Simple Interest Calculator

Take the following inputs:
- Principal Amount
- Rate of Interest
- Time

Calculate Simple Interest using:

SI = (P × R × T) / 100

Print the result.
"""
#Solution:-

PA = float(input("Enter principle Amount : "))
ROI = float(input("Enter the Rate of Intrest : "))
Time = float(input("Enter Time : "))

print("Simple Intrest = ",(PA*ROI*Time)/100)