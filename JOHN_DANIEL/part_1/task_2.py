"""PROGRAM READS NUMBER IN FEET FROM USER AND CONVERTS IT TO METERS"""
"""PSEUDOCODE"""
#Prompt & Initialise and read number in feet from user input
#Store number in 'number'
#Initialise and set 'meters' as a constant to 0.305
#Multiply number by meters at every instance and store in result
#Output result

"""Execution"""
number = int(input("Enter number in feet: "))
METER = 0.305
result = number * METER

print(f'{number}f:   {result}m')