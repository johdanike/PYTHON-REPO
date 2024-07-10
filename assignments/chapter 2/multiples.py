print("\nTHIS PROGRAM CHECKS FOR MULTIPLES")

number = 0
counter = 0
number = int(input("\nEnter number: "))

while number != 0: 

	counter += number
	if number % 4 == 0:
		print("Number:", number, " is a multiple of 4")

	elif number % 2 == 0:
		print("Number:", number, " is a multiple of 2")

	else:
		print("Number is not a multiple of either 4 nor 2")
	
	number = int(input("\nEnter number to check or '0' to exit: "))

	
