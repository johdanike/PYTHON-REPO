def only_floats(a , b):
	counter = 0
	if type(a) == float and type(b) == float:
		counter = 2
	
	if type(a) != float and type(b) == float:
		counter += 1

	if type(a) == float and type(b) != float:
		counter += 1

	if type(a) != float and type(b) != float:
		counter = 0
	
	return print(counter)


only_floats(12.1, 23.0)
only_floats(12.1, 23)
only_floats(12, 23)
