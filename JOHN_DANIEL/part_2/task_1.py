"""PROGRAM THAT READS NUMBERS >= 1000 AND <= 3000, THAT ARE EVEN NUMBERS"""
"""PSEUDOCODE"""
#Initialise = 0
#Initialise list
#Using a for loop, walk through the numbers starting from 1000 to 3000
#If number % 2 == 0, add number to list
#Output result

"""Execution"""
number = 0
even_number = []
for number in range(1000,3000):
	if number % 2 == 0:
		even_number += [number]
	
print(f'The even numbers between 1000 - 3000 include {even_number}')