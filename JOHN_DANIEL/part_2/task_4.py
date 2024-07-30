"""PROGRAM THAT ACCEPTS AN INTEGER NUMBER AS INPUT AND DISPLAY IT'S EVEN OR ODD """
"""PSEUDOCODE"""
#Define function and set parameters
#If number % 2 = 0, it is even, else it is odd
#Output result

"""Execution"""
def even_or_odd(number):
	if number % 2 == 0:
		return "it is an even number"
	else:
		return "it is an odd number"
result = even_or_odd(9)
print(result)