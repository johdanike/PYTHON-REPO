3scores = []

for _ in range(10):
	score = int(input("Enter score: "))
	scores.append(score)
	print(scores)
print(scores)

for _ in range(10):
	score = eval(input("Enter score: "))
	scores.append(score)
	print(scores)
print(scores)