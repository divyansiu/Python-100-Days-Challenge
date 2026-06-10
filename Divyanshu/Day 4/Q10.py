"""
Question 10: Average Marks Calculator
Take marks of 3 subjects.
Calculate total and average.
"""
#Solution : 
sub1 = float(input("Enetr Marks of 1st Subject : "))
sub2 = float(input("Enetr Marks of 2nd Subject : "))
sub3 = float(input("Enetr Marks of 3rd Subject : "))
total = sub1 + sub2 + sub3
avg = (sub1 + sub2 + sub3)/3
print("Total Marks is ",total)
print("Average Marks is ",avg)
