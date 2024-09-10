principal = float(input("Enter principal amount: "))
return_on_investment =  7 / 100

investment_time = int(input("How many years are you willing to stake: ")) 

#counter = 1;

for years in range(0, (investment_time + 1)):
	amount_on_deposit = principal * (1 + return_on_investment) ** years
	
	# = investment_time
	#investment_return = amount_on_deposit

	#print("\nThe amount on deposit at the end of ",counter,"years is: ",amount_on_deposit )
	print(f"The total amount for {years} is {amount_on_deposit:.2f}")

	#counter += 1
	#principal += amount_on_deposit
