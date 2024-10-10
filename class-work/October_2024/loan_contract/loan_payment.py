class Loan:
    def __init__(self, borrower: str, interest_rate: int , loan_amount: float, loan_period: int):
        self.borrower = borrower
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.loan_period = loan_period

    def __str__(self):
        return f"""
        * Borrower name: {self.borrower}
        * Interest rate: {self.interest_rate}%
        * Loan amount: {self.loan_amount}
        * Loan_period: {self.loan_period}
        """

    def get_interest_rate(self):
        return self.interest_rate / 100

    def get_loan_amount(self):
        return round(self.loan_amount, 2)

    def get_loan_period(self):
        return self.loan_period

    def get_monthly_interest_rate(self):
        return round(self.interest_rate / 12, 2)


    def set_monthly_payment(self):
        monthly_interest_rate = self.get_monthly_interest_rate()
        top = self.loan_amount * monthly_interest_rate
        bottom = 1 - (1 / (1 + monthly_interest_rate) ** self.loan_period)

        monthly_payment = top / bottom
        return round(monthly_payment, 2)

    def get_monthly_payment(self):
        return self.set_monthly_payment()

    def set_total_payment(self):
        total_payment = self.get_monthly_payment() * self.get_loan_period()
        return total_payment

    def get_total_payment(self):
        return round(self.set_total_payment(), 2)

loan_pay_plan = Loan("DaniKash", 20, 5_000_000, 10)
print(loan_pay_plan)
print(f"Interest Rate: {loan_pay_plan.get_interest_rate()}")
print(f"Loan Amount: {loan_pay_plan.get_loan_amount()}")
print(f"Loan Period: {loan_pay_plan.get_loan_period()}")
print(f"Monthly Interest Rate: {loan_pay_plan.get_monthly_interest_rate()}")
print(f"Monthly Payment Amount: {loan_pay_plan.get_monthly_payment()}")
print(f"Total Payment Amount: {loan_pay_plan.get_total_payment()}")



