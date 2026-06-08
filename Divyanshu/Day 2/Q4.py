"""
Question 4: Total Seconds Converter

Take the following inputs:
- Hours
- Minutes
- Seconds

Convert the entire time into total seconds.

Example:

Input:
1 hour
30 minutes
20 seconds

Output:
5420 seconds
"""
#solution :- 
hours = float(input("Enter Hour : "))
minutes = float(input("Enter Minutues : "))
seconds = float(input("Enter Second : "))

show = (hours*60*60)+(minutes*60)+seconds

print("Time in second is",show)