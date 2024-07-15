number = int(input("Enter the 5 digit integer: "))

num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0



for counter in range(0, 6):
	if counter == 1:
		num_5 = number // 1 % 10  

	if counter == 2:
		num_4 = number // 10 % 10  


	if counter == 3:
		num_3 = number // 100 % 10  


	if counter == 4:
		num_2 = number // 1000 % 10  


	if counter == 5:
		num_1 = number // 10000 % 10  


print(num_1," " , num_2," ", num_3," ",num_4," ",num_5)



