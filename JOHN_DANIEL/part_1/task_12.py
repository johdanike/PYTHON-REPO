from random import randint
computer = randint(1, 1000)

sentinel = ""
print("Let's play a game!")

while(sentinel != "no"):
	print("Guess my number between 1 to 1000 with the fewest guesses\n")

	user_input = 0
	counter = 0
	while(computer != user_input):
		user_input = int(input("Enter any 3 digit number: "))
		counter = counter + 1

		if(user_input > computer ):
			print("Too High! Try Again")
		elif (user_input < computer):
			print("Too low. Try Again!")
		if(user_input == computer and counter <= 10):
			print("Congratulations. You Guessed The Number")
			print(f"You got it at {counter} attempts. You Rock!!!!")
		elif(user_input == computer and counter > 10):		
			print("You got it at ",+counter," attempts. It took too long to get it!")
	


	sentinel = input("Do yo want to comtinue? Yes or no?: \n ")


