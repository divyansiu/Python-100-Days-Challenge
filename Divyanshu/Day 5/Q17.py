"""
Question 17: Digital Clock Converter
Convert total seconds into hours, minutes and seconds.
"""
#Solution : 
seconds = int(input("Enter total seconds : "))
minutes = seconds//60
hours = minutes//60
minutes = minutes%60
seconds = seconds%60
print("Time in right format is",hours,":",minutes,":",seconds)

