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
even = []
for number in range(1000,3000):
	even_number += [number]
	for num in range(len(even_number)):
		if num % 2 == 0:
			even += [num]
	
print(f'The even number with even digits between 1000 - 3000 include {num}', end="")