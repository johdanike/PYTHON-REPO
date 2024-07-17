print("School Score Grade")

name = input("\nEnter your name: ")
passed = 0
fail = 0
counter = 1

for loop in range(1, 16):
	score = int(input(f"Enter your {loop} score: "))
	if(score > 45):
		passed = passed + 1
	elif(score < 45):
		fail = fail + 1
	counter = + 1

print(f"TOTAL STUDENTS THAT PASSED = {passed}")
print(f"TOTAL STUDENTS THAT FAILED = {fail}")

	

