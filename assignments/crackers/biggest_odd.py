def biggest_odd(numbers):
	maximum_number = 0

	for character in numbers:
		number = int(character)

		if number % 2 != 0 and number > maximum_number:
			maximum_number = number

	return maximum_number


print(biggest_odd("15274"))