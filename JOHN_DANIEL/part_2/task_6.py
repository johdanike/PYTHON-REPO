"""PROGRAM THAT RETURNS THE REVERSAL OF AN INTEGER """
"""PSEUDOCODE"""
#Define function and set parameters
#Append numbers into a list
#Using a for loop to walk through the list and compare, return the number from the right
#Output result

"""Execution"""


def get_sortedNumbers(num1, num2, num3):
	number_list1 = []
	number_list2 = []
	number_list3 = []

	number_list1 += [num1]
	number_list2 += [num2]
	number_list3 += [num3]

	numbers = number_list1 + number_list2 + number_list3
	for index in range(len(numbers)):
		if numbers[0] > numbers[1] and numbers[2]:
			return f'{numbers == [number_list1,number_list2, number_list3]}'
		elif numbers[1] > numbers[0] and numbers[2]:
			return f'{numbers == [number_list2,number_list1, number_list3]}'
		elif numbers[2] > numbers[0] and numbers[1]:
			return f'{numbers == [number_list3,number_list1, number_list2]}'
		else: 
			return numbers
result = get_sortedNumbers(4, 2, 5)
print(result)



 
