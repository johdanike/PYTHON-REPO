options = ['Single filer', 'Married filing jointly' ,'Married filing separately', 'Head of household']
for index, value in enumerate(options):
	print(f"{index}: {value}")


choice = int(input("\nEnter filing status: "))
taxable_income = int(input("Enter taxable income: "))

tax_rate_10 = 10 / 100
tax_rate_15 = 15 / 100
tax_rate_25 = 25 / 100
tax_rate_28 = 28 / 100
tax_rate_33 = 33 / 100
tax_rate_35 = 35 / 100




match choice:
	case 0:
		if taxable_income >= 0 and taxable_income <= 8350:
			tax = taxable_income * tax_rate_10
		elif taxable_income >= 8351 and taxable_income <= 33950:
			tax = taxable_income * tax_rate_15
		elif taxable_income >= 33951 and taxable_income <= 82250:
			tax = taxable_income * tax_rate_25
		elif taxable_income >= 82251 and taxable_income <= 171550:
			tax = taxable_income * tax_rate_28
		elif taxable_income >= 171551 and taxable_income <= 372950:
			tax = taxable_income * tax_rate_33
		elif taxable_income >= 372951:
			tax = taxable_income * tax_rate_35
	
	case 1:
		if taxable_income >= 0 and taxable_income <= 16700:
			tax = taxable_income * tax_rate_10
		elif taxable_income >= 16701 and taxable_income <= 67900:
			tax = taxable_income * tax_rate_15
		elif taxable_income >= 67901 and taxable_income <= 137050:
			tax = taxable_income * tax_rate_25
		elif taxable_income >= 137051 and taxable_income <= 208850:
			tax = taxable_income * tax_rate_28
		elif taxable_income >= 208851 and taxable_income <= 372950:
			tax = taxable_income * tax_rate_33
		elif taxable_income >= 372951:
			tax = taxable_income * tax_rate_35	
	
	case 2:
		if taxable_income >= 0 and taxable_income <= 8350:
			tax = taxable_income * tax_rate_10
		elif taxable_income >= 8351 and taxable_income <= 33950:
			tax = taxable_income * tax_rate_15
		elif taxable_income >= 33951 and taxable_income <= 68525:
			tax = taxable_income * tax_rate_25
		elif taxable_income >= 68526 and taxable_income <= 104425:
			tax = taxable_income * tax_rate_28
		elif taxable_income >= 104426 and taxable_income <= 186475:
			tax = taxable_income * tax_rate_33
		elif taxable_income >= 186476:
			tax = taxable_income * tax_rate_35

	case 3: 
		if taxable_income >= 0 and taxable_income <= 11950:
			tax = taxable_income * tax_rate_10
		elif taxable_income >= 11951 and taxable_income <= 45500:
			tax = taxable_income * tax_rate_15
		elif taxable_income >= 45501 and taxable_income <= 117450:
			tax = taxable_income * tax_rate_25
		elif taxable_income >= 117451 and taxable_income <= 190200:
			tax = taxable_income * tax_rate_28
		elif taxable_income >= 190201 and taxable_income <= 372950:
			tax = taxable_income * tax_rate_33
		elif taxable_income >= 372951:
			tax = taxable_income * tax_rate_35


	
print(f"Your tax is {tax}")












	
