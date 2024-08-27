"""PROGRAM THAT RETURNS THE REVERSAL OF AN INTEGER """
"""PSEUDOCODE"""
#Define function and set parameters
#Using a for loop to walk through the number, return the number from the right
#Output result

"""Execution"""
def reverse(number):
	reverse = " "
	number_formatted = str(number)
	length = len(number_formatted)
	remainder = 0
	for index in range(length):
		remainder = number % 10
		number //= 10
		reverse += str(remainder)
	return reverse



result = reverse(987654321)
print(result)

def is_palindrome(number):
	number2 = str(number)
	length = len(number2)
	divisor = 1
	remainder = 0
	for index in range(length):
		first_num = number // 10
		last_num = number % 10
		if first_num == last_num:
			return "Number is a palindrome"
		elif first_num != last_num:
			return "Number is not a palindrome" 

result = is_palindrome(232)
print(result)

		


