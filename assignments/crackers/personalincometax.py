options = ['Single filer', 'Married filing jointly' ,'Married filing separately', 'Head of household']
for index, value in enumerate(options):
	print(f"{index}: {value}")


choice = int(input("\nEnter filing status: "))
taxable_income = int(input("Enter taxable income: "))

tax = 0


match choice:
	case 0:	
		tax_1 = 0.10 * 8350
		second_tax = taxable_income - 8350
		if taxable_income >= 8351 and taxable_income <= 33950:
			second_tax = tax_1 + (0.15 * second_tax)
		elif taxable_income >= 33951 and taxable_income <= 82250:
			second_tax = tax_1 + (0.25 * second_tax)
		elif taxable_income >= 82251 and taxable_income <= 171550:
			second_tax = tax_1 + (0.28 * second_tax)
		elif taxable_income >= 171551 and taxable_income <= 372950:
			second_tax = tax_1 + (0.33 * second_tax)
		elif taxable_income >= 372951:
			second_tax = tax_1 + (0.35 * second_tax)
	case 1:
		tax_1 = 0.10 * 16700
		second_tax = taxable_income - 8350
		if taxable_income >= 16700 and taxable_income <= 67900:
			second_tax = tax_1 + (0.15 * second_tax)
		elif taxable_income >= 67901 and taxable_income <= 137050:
			second_tax = tax_1 + (0.25 * second_tax)
		elif taxable_income >= 137051 and taxable_income <= 208850:
			second_tax = tax_1 + (0.28 * second_tax)
		elif taxable_income >= 208851 and taxable_income <= 372950:
			second_tax = tax_1 + (0.33 * second_tax)
		elif taxable_income >= 372951:
			second_tax = tax_1 + (0.35 * second_tax)
	case 2:
		tax_1 = 0.10 * 8350
		second_tax = taxable_income - 8350
		if taxable_income >= 8351 and taxable_income <= 33950:
			second_tax = tax_1 + (0.15 * second_tax)
		elif taxable_income >= 33951 and taxable_income <= 68525:
			second_tax = tax_1 + (0.25 * second_tax)
		elif taxable_income >= 68526 and taxable_income <= 104425:
			second_tax = tax_1 + (0.28 * second_tax)
		elif taxable_income >= 104426 and taxable_income <= 186475:
			second_tax = tax_1 + (0.33 * second_tax)
		elif taxable_income >= 186476:
			second_tax = tax_1 + (0.35 * second_tax)
	case 3:
		tax_1 = 0.10 * 11950
		second_tax = taxable_income - 8350
		if taxable_income >= 11951 and taxable_income <= 45500:
			second_tax = tax_1 + (0.15 * second_tax)
		elif taxable_income >= 45501 and taxable_income <= 117450:
			second_tax = tax_1 + (0.25 * second_tax)
		elif taxable_income >= 117451 and taxable_income <= 190200:
			second_tax = tax_1 + (0.28 * second_tax)
		elif taxable_income >= 190201 and taxable_income <= 372950:
			second_tax = tax_1 + (0.33 * second_tax)
		elif taxable_income >= 372951:
			second_tax = tax_1 + (0.35 * second_tax)
	


	
print(f"Your cummulative tax is {second_tax}")












	
