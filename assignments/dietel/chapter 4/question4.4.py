def mystery(x):
	y = 0

	for value in x:
		y += value ** 2
	return y

print(mystery([1,2,3,4,5]))

answer = ("THE FUNCTION RAISES EACH ELEMENT OF THE LIST TO THE POWER OF TWO")
print(f'Answer: {answer}')