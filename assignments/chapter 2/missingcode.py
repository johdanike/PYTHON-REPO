print("\nTHIS PROGRAM GRADES AND ALOTS RANGES TO GRADES INPUTED")

grade = 0
counter = 0
grade = int(input("Enter grade: "))

while grade != 0: 

	counter += grade
	if grade >= 90:

		print("\nCONGRATULATIONS!", end="")
		print(" Your grade =",grade, end="")
		print(" earns you an 'A'")

	else:
		print("You most likely scored lower or failed")

	grade = int(input("\nEnter grade to check or '0' to exit program:"))
