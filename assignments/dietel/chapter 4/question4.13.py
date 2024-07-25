def products_calculator(*sargs):
	product = 1
	for numbers in sargs:
		product = product * numbers
	return product

result = products_calculator(100, 50, 43, 4, 2, 67)

print(f"Result of products is = {result}")