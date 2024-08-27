"""PROGRAM READS LENGTH AND RADIUS OF CYLINDER AND CALCULATES AREA AND VOLUME"""
"""PSEUDOCODE"""
#Initialise and read radius to be equal to user input
#Initialise and read length to be equal to user input
#Set PI constant to be equal to 22/7
#Initialise Area to br equal to PI * radius ** 2
#Initialise Volume to be equal to Area * Length
#Output result

"""Execution"""
radius = float(input("Enter radius of cylinder: "))
length = float(input("Enter length of cylinder: "))
PI_VALUE = 22 / 7
area = PI_VALUE * radius ** 2
volume = area * length

print(f"The area of the cylinder is {area}")
print(f"The volume of the cylinder is {volume}")