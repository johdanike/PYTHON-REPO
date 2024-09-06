from unittest import TestCase
from bankfunc import Account
from decimal import Decimal

class TestAccount(TestCase):

    def test_that_account_can_deposit(self):
        a1 = Account('John', 0000)
        a1.deposit(10000)
        a1.deposit(5000)
        self.assertEqual(a1.balance, 15000)

    def test_that_account_can_be_withdrawn_from(self):
        a1 = Account('John', 0000)
        a1.deposit(10000)
        a1.withdraw(1000)
        self.assertEqual(a1.balance, 9000)