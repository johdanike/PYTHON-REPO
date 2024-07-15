numbers = int(input("Enter number: "))

num_1 = numbers // 10000 % 10
num_2 = numbers // 1000 % 10
num_3 = numbers // 100 % 10
num_4 = numbers // 10 % 10
num_5 = numbers // 1 % 10

if num_1 != num_5 and num_2 != num_4:
	print(numbers ," is not a palindrome")
else:
	print(numbers ," is a palindrome")

