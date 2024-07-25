def  learn_multiplication():
	from random import randint

	question_1 = randint(1, 9)	
	question_2 = randint(1, 9)

	result = 0
	answer = 1
	
	print("You have 10 attempts to each question")
	
	while result != answer:
		answer = int(input(f"What is the result of {question_1} times {question_2}: "))
		result = question_1 * question_2

		if answer == result:
			feed_back = ("Very good")
		else:
			print("Wrong answer, please try again!!!")

	
	return feed_back

feed_back = learn_multiplication()
print(feed_back)