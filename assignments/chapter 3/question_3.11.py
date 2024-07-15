miles = 0
gallons = 0
miles_driven = 0
gallons_used = 0
miles_per_gallon = 0
total_miles_per_gallon = 0
counter = 1
stop = -1
average_miles_per_gallon = 0 

while(miles_driven != -1):
	miles_driven = float(input("Enter miles driven or -1 to exit: "))
	
	if miles_driven <= 0:
		break
	counter += counter

	gallons_used = float(input("Enter amount of gallons used: "))

	miles_per_gallon = miles_driven / gallons_used

	miles_driven += miles
	gallons_used += gallons
	print("Miles driven is: ", miles_driven)
	print("Gallons used is: ", gallons_used)
	print("The miles per trip is: ", miles_per_gallon)


	total_miles_per_gallon += miles_per_gallon
	average_miles_per_gallon = total_miles_per_gallon / counter

print("\nThe average miles per trip for these trips is: ", average_miles_per_gallon)
print("\nThe Cummulative miles per trip is: ", total_miles_per_gallon)