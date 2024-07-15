print("Program that checks and abstracts the factorials of an integer")

number = int(input("Enter integer to check the factorials: "))

factorial = 1
counter = 1
for decrement in range (0, number):
	number -= 1
	print(number+1," ", end="")

	factorial *= (number+1)
print("\n\nThe Factorials of the number equals = ",factorial) 
	
