print("\nTHIS PROGRAM CALCULATES THE SMALLEST AND LARGEST")

sum = 0
average = 0
product = 1
largest_value = 0
smallest_value = 0
number1 = 0
number2 = 0
number3 = 0

#counter = input("\nEnter count value: ")
#count = int(counter)

#for loops in range(1, count + 1):
for loops in range(0, 3):

	number = input("\nEnter number: ")
	number = int(number)

	if loops == 1:
		number1 = number
	elif(loops == 2):
		number2 = number
	else:
		number3 = number

 
	sum += number
	average = sum / 3
	product *= number

	
if(number1 > number2 and number1 > number3):
	largest_value = number1

elif(number2 > number1 and number2 > number3):
	largest_value = number2

elif(number3 > number1 and number3 > number2):
	largest_value = number3

	
if(number1 < number2 and number1 < number3):
	smallest_value = number1

elif(number2 < number1 and number2 < number3):
	smallest_value = number2

elif(number3 < number1 and number3 < number2):
	smallest_value = number3


print("The sum of the three integers is", sum)
print("The average of the three integers is", average)
print("The product of the three integers is", product)
print("the largest number is: ", largest_value)
print("The smallest number is : ", smallest_value)

	
	

