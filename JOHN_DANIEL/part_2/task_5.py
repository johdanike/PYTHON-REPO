"""PROGRAM THAT RETURNS THE REVERSAL OF AN INTEGER """
"""PSEUDOCODE"""
#Define function and set parameters
#Using a for loop to walk through the number, return the number from the right
#Output result

"""Execution"""
def reverse(number):
	num = []
	num += [number]
	for index in num:
		reversed_number = index
		return reversed_number

result = reverse(456)
print(f'The reverse of the number is {result}')

#def is_palindrome(number):
	