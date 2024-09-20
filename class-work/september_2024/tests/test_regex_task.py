
import unittest

from september_2024 import regex_task
from september_2024.regex_task import email_validity_checker


class TestRegexTask(unittest.TestCase):

    def test_that_class_exists(self):
        self.assertTrue(regex_task)

    def test_that_email_checker_method_exists(self):
        self.assertTrue(email_validity_checker)


