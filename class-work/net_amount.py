print("PROGRAM THAT COMPUTES THE NET AMOUNT OF A BANK ACCOUNT BASED ON TRANSACTION LOG\n") 

name = input("Enter name to proceed: ")


options = ("""SELECT TO PROCEED: 
1: Deposit
2: Withdraw
3: Get Balance
 """)
print(options)

deposit = 0
debit = 0
balance = 0
condition = 1
entry = 0

while(condition == 1):

	entry = int(input("select option: "))

	match entry:
		case 1:
			amount = int(input("Amount to be deposited: "))
			balance += amount
			print(f"Deposit amount = {balance}")
		case 2: 
	
			debit = int(input("Amount to withdraw: "))
			balance = balance - debit

			if balance == 0:
				print("Insufficient balance")
			if debit > balance or balance == 0:
				print("Insufficient balance")
				break
			if debit < 0:
				break
			else: 
				print(f"{debit}"+" has been debited from your account")
				print(f"Your current balance = {balance}")

		case 3:
			current_balance = balance
			print(f"Current balance = {current_balance}")
		case _:
	
        		print("INVALID SELECTION")

	condition = int(input("Do you wish to continue? Press 1 or -1 to terminate: "))
	
				


 
        
			





