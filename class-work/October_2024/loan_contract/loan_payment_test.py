import unittest

from loan_contract.loan_payment import Loan


class LoanPaymentTest(unittest.TestCase):
    def setUp(self):
        self.loan = Loan("John-Daniel", 15, 2_000_000, 3)

    def test_that_loan_contract_class_exists(self):
        self.assertTrue(self.loan)

    def test_that_we_can_get_borrowers_details(self):
        borrower = self.loan.borrower
        self.assertTrue(borrower)

    def test_that_we_can_get_loan_interest_rate_can_be_gotten(self):
        interest_rate = self.loan.get_interest_rate()
        self.assertEqual(interest_rate, 0.15)

    def test_that_we_can_get_loan_amount_can_be_gotten(self):
        loan_amount = self.loan.get_loan_amount()
        self.assertEqual(loan_amount, 2_000_000)


