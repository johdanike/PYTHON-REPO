"""PROGRAM READS WEIGHT IN POUNDS FROM USER AND CONVERTS IT TO KILO_GRAMS"""
"""PSEUDOCODE"""
#Prompt & Initialise and read value in pounds from user input
#Store number in 'pounds'
#Initialise and set 'kilo_gram' as a constant to 0.454
#Multiply pounds by kilo_gram 
#Output result

"""Execution"""
pounds = float(input("Enter weight in pounds:"))
KILO_GRAM = 0.454
result = pounds * KILO_GRAM
print(f'Result: {pounds}pounds is {result} in kilograms')