"""
Question 33: BMI Category Checker
"""
#Solution : 

# BMI RangeCategory< 18.5Underweight18.5 - 24.9Healthy Weight (Normal)25.0 - 29.9Overweight≥ 30.0Obese

height = float(input("Enter your Height in meter : "))
weight = float(input("Enter your Weight in meter : "))

BMI = weight/(height*height)

if BMI < 18.5 :
    print("Your BMI is",BMI,"and your BMI Category is Underweight")
elif BMI < 24.9 :
    print("Your BMI is",BMI,"and your BMI Category is Healthy weight")
elif BMI < 29.9 :
    print("Your BMI is",BMI,"and your BMI Category is Overweight")
else :
    print("Your BMI is",BMI,"and your BMI Category is Obese")