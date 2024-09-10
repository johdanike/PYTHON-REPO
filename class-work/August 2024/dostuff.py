def get_lenght_of_args(parameter):
	number = 0
	for indexes in parameter:
		number += 1
	return number


lenght = get_lenght_of_args([1,2,3,4,5])
print(f"The lenght of the parameter is {lenght}")




#keyword and default args
def do_stuff(number, list_of_numbers):
	for numba in list_of_numbers:
		number += numba
	return number

result = do_stuff(10, [1,2,3,4,5])
result1 = do_stuff(list_of_numbers=[1,2,3,4,5], number=10)

print(f"The lenght of the number is {result}")
print(f"The lenght of the number is {result1}")




#Arbitrary list of arguements
def get_product(*numbers):
	product = 1
	for number in numbers:
		product *= number
	return product

print(get_product(1, 4, 5))  #20
print(get_product(2, 4, 8, 10))  #640
print(get_product(5, 8)) #40
print(get_product(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)) #1024



#append list
a_regular_list = []
for numbers in range(1, 11):
	a_regular_list += [numbers]


print(a_regular_list)




	