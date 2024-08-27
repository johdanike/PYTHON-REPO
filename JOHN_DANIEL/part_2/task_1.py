"""PROGRAM THAT READS NUMBERS >= 1000 AND <= 3000, THAT ARE EVEN NUMBERS"""
"""PSEUDOCODE"""
#Initialise = 0
#Initialise list
#Using a for loop, walk through the numbers starting from 1000 to 3000
#Append numbers into list 
#Walk through the list using another for loop 
#If number % 2 == 0, add number to list
#Output result

"""Execution"""

1000

for number in range(1000,3001):
	last_num = number % 10	
	third_num = number // 10 % 10
	second_num = number // 100 % 10
	first_num = number // 1000 % 10
	if last_num % 2 == 0 and third_num % 2 == 0 and second_num % 2  == 0 and first_num % 2  == 0:
		print(number, end=", ")