import unittest

from pythonProjects import account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = account.Account("John", "Daniel")

    def test_that_account_exists(self):
        account.Account("John", "Daniel")

    def test_that_account_can_be_created(self):
        account.Account("John", "Daniel")

    def  test_that_account_pin_can_be_changed(self):
        self.account1.change_pin("0000", "1234")
        self.assertEqual(self.account1.pin, "1234")

    def test_that_account_with_wrong_old_pin_cannot_change_pin(self):
        self.account1.change_pin("2222", "3333")
        self.assertEqual(self.account1.pin, "3333")

    def test_that_account_pin_length_is_valid(self):
        self.assertRaises(ValueError, self.account1.change_pin("0000","12345"), "12345")
