"""PROGRAM DISPLAYS A TABLE OF A, B AND 'A**B' """
"""PSEUDOCODE"""
#Output table for a, b and a**b
#Using a for loop 
#Initialize CONSTANT FOR MONTHLY_INTEREST_RATE = 5%

#Using the formula (initial_deposit_amount = FINAL_ACCOUNT_VALUE / ((1 + MONTHLY_INTEREST_RATE) ** NUMBER_OF_MONTHS) )
#Output result for initial deposit amount

"""Execution"""
print('\ta \tb \ta**b')
a = []
b = []
for index in range(1, 6):
	a += [index]
	
for index in a:
	b += [index+1]

for index in range(len(b)):
	a *= [index]
	

print(a)
print(b)
print(raised_to_power)


for number in range (0, 6):
	print(f'{number: 6}	{(number +1):6}	{(number**(number +1)):6}')