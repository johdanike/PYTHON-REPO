print("Mortgage Calculator")

principal = int(input("Enter principal amount:"))
annual_rate = int(input("Enter annual rate:"))
duration_of_loan = int(input("Enter duration of the loan: "))
monthly_rate = (annual_rate / 100) / 12
duration = duration_of_loan * 12


mortgage = principal * (monthly_rate * (1 + monthly_rate) ** duration) / (((1 + monthly_rate) ** duration ) - 1)

print(f"Your monthly payment is ${mortgage}")


