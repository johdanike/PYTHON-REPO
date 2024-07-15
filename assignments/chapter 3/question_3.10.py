principal = float(input("Enter principal amount: "))
return_on_investment =  7 / 100

investment_time = int(input("How many years are you willing to stake: ")) 

counter = 1;

for years in range(investment_time):
	amount_on_deposit = principal * (1 + return_on_investment) ** counter

	print("\nThe amount on deposit at the end of ",counter,"years is: ",amount_on_deposit )
	counter += 1
