num = []

for index in range(21):
	if index % 2 == 0:
		num.append(index)
print(num)



def func(numbers):
	function_list = []
	for index in range(numbers):
		if index % 2 == 0:
			function_list.append(index)
	return 	function_list

result = func(21)
print(result)


numbers = list(range(1, 21))
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


name = "fabulous"

result = ""

for index in range(len(name)-1):
	if index % 2 == 0:
		result += name[index]

print(result)


#list in list
result = [[0 for _ in range(4)] for _ in range(5)]
print(result)

#breakdown
inner = [0,0,0,0]
outer = []

for _ in range(5):
	outer.append(inner)

print(outer)


#when the length is not known
inner = [0] * 4
outer = []


#outer[1][0] = 10
print(outer)

for _ in range(5):
	outer.append(inner)

print(outer)

##### Multiply strings
print("Abimbola " * 4)




