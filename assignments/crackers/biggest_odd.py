def biggest_odd(numbers):
	number_list = list(numbers)
	big_num_odd = int(number_list[0] )
	



	for elements in number_list:
		
		if elements % 2 == 1 and elements > big_num_odd:
			big_num_odd = elements
			

	return big_num_odd


biggest_odd("23569")	