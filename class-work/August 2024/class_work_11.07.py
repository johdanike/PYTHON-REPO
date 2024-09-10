name = 'temitope'

print(id(name))


name = name + 'ayo'
print(id(name))


number = 1
print(id(number))

number = number + 4
print(id(number))


basket = [1,2,3,4]
print(id(basket))

basket.append(5)
print(id(basket))
print(basket)



for char in "techblazers":
	print(char, 'timothy')

for number in range (30):
	print(number, end=', ')


total = 0
for number in range (0, 10):
	if number % 2 == 1:
		total += number
print(total)


#even numbers between 1 - 10

for number in range (1, 10, 2):
	total+=number

#print(total)
print(number)

#0dd numbers between 1 - 10

for number in range (1, 10):
	total+=number

#print(total)
print(number)

for number in range (1,11):
	if number%3==0:
		#print(f"{number}\n")
		print(number)
	#elif number <7:
	#	print(number)
	


