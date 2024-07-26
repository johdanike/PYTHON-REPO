"""PROGRAM CALCULATES AMOUNT TO BE DEPOSITED TO HAVE $5000 AFTRE 3 YEARS"""
"""PSEUDOCODE"""
#Initialize CONSTANT FOR FINAL_ACCOUNT_VALUE = 5_000
#Initialize CONSTANT FOR NUMBER_OF_MONTHS = 3
#Initialize CONSTANT FOR MONTHLY_INTEREST_RATE = 5%

#Using the formula (initial_deposit_amount = FINAL_ACCOUNT_VALUE / ((1 + MONTHLY_INTEREST_RATE) ** NUMBER_OF_MONTHS) )
#Output result for initial deposit amount

"""Execution"""
FINAL_ACCOUNT_VALUE = 5_000
NUMBER_OF_MONTHS = 3
MONTHLY_INTEREST_RATE = (4.25 / 100)   #4.25% 
initial_deposit_amount = int(FINAL_ACCOUNT_VALUE / ((1 + MONTHLY_INTEREST_RATE) ** NUMBER_OF_MONTHS))

print(f'initial deposit amount = {initial_deposit_amount}')
