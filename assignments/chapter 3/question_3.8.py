print("Arithmetic, Smallest and Largest")

sum = 0
product = 0
average = 0
largest_num = 0
smallest_num = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0


for integers in range (1, 5):
	number = int(input('Enter number: '))
	if(integers == 1):
		num_1 = number
	if(integers == 2):
		num_2 = number
	if(integers == 3):
		num_3 = number
	if(integers == 4):
		num_4 = number

	if num_1 > num_2 and num_1 > num_3 and num_1 > num_4:
		largest_num = num_1
	elif num_1 < num_2 and num_1 < num_3 and num_1 < num_4:
		smallest_num = num_1

	if num_2 > num_1 and num_2 > num_3 and num_2 > num_4:
		largest_num = num_2
	elif num_2 < num_1 and num_2 < num_3 and num_2 < num_4:
		smallest_num = num_2

	if num_3 > num_1 and num_3 > num_2 and num_3 > num_4:
		largest_num = num_3
	elif num_3 < num_1 and num_3 < num_2 and num_3 < num_4:
		smallest_num = num_3

	if num_4 > num_1 and num_4 > num_2 and num_4 > num_3:
		largest_num = num_4
	elif num_4 < num_1 and num_4 < num_2 and num_4 < num_3:
		smallest_num = num_4


	
	sum += number
	average = sum / 4
	product = num_1 * num_2 * num_3 * num_4

print("\n ~ The sum of the four integers is: ",sum)
print(" ~ The product of the four integers is: ",product)
print(" ~ The average of the four integers is: ",average)
print(" ~ The largest of the four integers is: ",largest_num)
print(" ~ The smallest of the four integers is: ",smallest_num)




