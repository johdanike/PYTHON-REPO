print("\nTHIS PROGRAM CHECKS IF A NUMBER IS EVEN OR ODD")

number = 0
counter = 0
number = int(input("\nEnter number to check:"))

while number != 0: 

	counter += number
	if number % 2 == 0:
		print("Number:", number, " even")
	else:
		print("Number:", number, " is odd")

	number = int(input("\nEnter number to check:"))
