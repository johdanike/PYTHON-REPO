def big_odd(numbers):
	big_num = numbers
	big_list = list(big_num)
	big = 0

	for elements in big_list:
		number = int(elements)

		if number % 2 != 0 and number > big:
			big = number
			
	return big


print(big_odd("122427465438674"))	




