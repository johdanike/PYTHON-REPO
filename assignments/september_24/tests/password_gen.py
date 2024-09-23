import unittest
from os.path import split

from password_generator import password_gen
from password_generator.password_gen import random_password_gen


class TestPassword(unittest.TestCase):

    def test_that_password_gen_exists(self):
        self.assertTrue(password_gen)

    def test_that_random_password_gen_method_exists(self):
        self.assertTrue(password_gen.random_password_gen)

    def test_that_random_password_gen_method_has_length(self):
        expected = 16
        actual = (password_gen.random_password_gen)
