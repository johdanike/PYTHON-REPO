

print("\nYOUR IDEAL GRADE CALCULATOR\n")
	
name = input("Enter your name to compute grade: ")
score = 0
counter = 0
flag = -1
#score = int(input("Enter your score: "))

while score != flag:
	score = int(input("Enter your score: "))

	if score > 75 and score <= 100:
		print(name+", Your grade is: A")
	if score > 65 and score < 75:
		print(name+", Your grade is: B")
	if score > 50 and score < 64:
		print(name+", Your grade is: C")
	if score > 40 and score < 49:
		print(name+", Your grade is: D")
	if score > 0 and score < 39:
		print(name+", Your grade is: F")
	
	counter += 1



