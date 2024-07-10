print("\nTHIS PROGRAM CALCULATES THE INVESTMENT RETURN")

principal = int(input("\nEnter initial investment (principal): "))
return_rate = int(input("\nEnter initial investment (return_rate): "))
number_of_years  = int(input("\nEnter initial investment (number_of_years ): "))

return_rate = 7 / 100
amount = principal *  (1 + return_rate) ** number_of_years

print("\nThe amount of deposit at the end of", number_of_years, "with an initial deposit of",principal, "is",amount)