"""PROGRAM READS INTEGER BETWEEN 0 - 1000 FROM USER AND SUMS ALL THE DIGITS OF THE INTEGER"""
"""PSEUDOCODE"""
#Prompt & Initialise and read entry as 'number' from user input
#if number > 0 or number < 1000
	#third_num = number % 10
	#second_num = number // 10 % 10
	#first_num = number // 100
#cast numbers into an array and using the sum method, add all individual digits 
#Output result

"""Execution"""
number = int(input("Enter number between 0 - 1000: "))
if number > 0 and number < 1000:
	third_num = number % 10
	second_num = number // 10 % 10
	first_num = number // 100
	addition = 0
	num_array = {first_num, second_num, third_num}
	for index in num_array:
		addition += index
else:
	print("Input a number between 1 - 1000")

print(f'The sum of {number} is {addition}')
	
	