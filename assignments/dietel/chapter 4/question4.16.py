def  learn_multiplication_2():
	from random import randint

	question_1 = randint(1, 9)	
	question_2 = randint(1, 9)
	question_3 = randint(1, 19)
	question_4 = randint(1, 19)

	result = 0
	answer = 1

	print("""
	Enter difficulty level:
	1: Level 1
	2: level 2

		""")
	
	option = int(input("Enter option: "))

	match option:
		case 1: 
	
			while result != answer:v
				answer = int(input(f"What is the result of {question_1} times {question_2}: "))
				result = question_1 * question_2
	
				if answer == result:
					feed_back = ("Very good")
				elif answer <= result:
					feed_back = ("Nice Work")
				elif answer < result:
					feed_back = ("Keep up the good work")
				else:
					print("No. Please try again!!!")

			return feed_back

		case 2:
			while result != answer:v
				answer = int(input(f"What is the result of {question_1} times {question_2}: "))
				result = question_3 * question_4
	
				if answer == result:
					feed_back = ("Very good")
				elif answer <= result:
					feed_back = ("Nice Work")
				elif answer < result:
					feed_back = ("Keep up the good work")
				else:
					print("No. Please try again!!!")

			return feed_back

			

feed_back = learn_multiplication()
print(feed_back)