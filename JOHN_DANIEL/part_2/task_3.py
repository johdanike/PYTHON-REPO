"""FUNCTION THAT RECIEVES TWO INTEGRAL NUMBERS IN STRING FORM, COMPUTES THEIR SUM AND RETURN THE RESULT IN A STRING"""
"""PSEUDOCODE"""
#Define function and set parameters
#Initialize sum = 0
#Using a for loop, walk through the length of user_input, and increment sum counter
#Output result

"""Execution"""
summation = 0
def String( get_sum_of_string_integers('number_1', 'number_2')):
	summation = number_1 + number_2
	return summation

result = get_sum_of_string_integers('56', '23')
print(f'The sum of the two integers is {result}')