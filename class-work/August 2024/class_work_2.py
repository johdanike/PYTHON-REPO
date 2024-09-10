
stop = -1
score = 0

while(score != stop):
	score = int(input("Enter score: "))

	result = 'Passed' if score > 45 else 'Failed'
	print(result)