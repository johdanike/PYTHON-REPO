class LoanContract:
    def __init__(self, borrower: str, interest_rate: float, loan_amount: int, loan_period: int):
        self.annual_period = 12
        self.borrower = borrower
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.loan_period = loan_period

    def set_borrower_details(self):
        borrower_details = input("Enter name: ")
        self.borrower = borrower_details

    def set_interest_rate(self):
        interest_rate = self.interest_rate/100
        self.interest_rate = interest_rate

    def get_monthly_interest_rate(self):
        return round(self.interest_rate / 12, 2)

    def set_loan_amount(self, loan_amount):
        self.loan_amount = loan_amount

    def set_loan_period(self, loan_period):
        loan_period_monthly = loan_period / self.annual_period
        self.loan_period = loan_period_monthly

    def cal_monthly_payment(self):
        monthly_interest_rate = self.get_monthly_interest_rate()
        top = self.loan_amount * monthly_interest_rate
        bottom = 1 - (1 / (1 + monthly_interest_rate) ** self.loan_period)

        monthly_payment = top / bottom
        return round(monthly_payment, 2)

    def total_payment(self):
        total_payment = self.cal_monthly_payment() * self.get_loan_period()
        return total_payment

    def __str__(self):
        return f"""
        * Borrower name: {self.borrower}
        * Interest rate: {self.interest_rate}%
        * Loan amount: {self.loan_amount}
        * Loan_period: {self.loan_period}
        * Monthly payment: {self.cal_monthly_payment()}
        """

    def get_loan_amount(self):
        return self.loan_amount
    def get_loan_period(self):
        return self.loan_period
    def get_annual_period(self):
        return self.annual_period
    def get_interest_rate(self):
        return self.interest_rate
    def get_borrower(self):
        return self.borrower


LoanCon = LoanContract("Lagbaja", 15, 2_000_000, 3)

print(LoanCon)