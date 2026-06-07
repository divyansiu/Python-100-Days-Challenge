"""
Question 2: Area and Perimeter of Rectangle

Take the following inputs:
- Length
- Width

Calculate and print:
- Area
- Perimeter

Formula:
Area = Length × Width
Perimeter = 2 × (Length + Width)
"""
#Solution:-

length = float(input("Enter the Length of the rectangle : "))
width = float(input("Enter the width of the rectangle : "))

area = length * width
perimeter = 2 * (length + width)

print("Area of the rectangle = ",area)
print("Perimeter of the rectangle = ",perimeter)