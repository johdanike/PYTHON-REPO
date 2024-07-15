print("Enter two integers, and I will tell you the relationships they satisfy")

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

if number1 <= number2:
	print(number1, 'is less than or equal to', number2)

elif number1 >= number2:
	print(number1, 'is greater than or equal to', number2)

else:
	print(number1, 'is not equal to', number2) 