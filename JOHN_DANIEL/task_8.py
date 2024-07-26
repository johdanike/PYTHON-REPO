"""PROGRAM DISPLAYS A TABLE OF A, B AND 'A**B' """
"""PSEUDOCODE"""
#Output table for a, b and a**b
#Using a for loop to iterate through 1 - 5 to get values for "a"
#Add 1 to the values of 'a' still in the loop
#Raise "a" to the power of "b" 
#print result

#Using the formula (initial_deposit_amount = FINAL_ACCOUNT_VALUE / ((1 + MONTHLY_INTEREST_RATE) ** NUMBER_OF_MONTHS) )
#Output result for initial deposit amount

"""Execution"""
print('a \tb \ta**b')

for number in range (0, 6):
	print(f'{number}	{(number +1)}	{(number**(number +1))}')



