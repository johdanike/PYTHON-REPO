import unittest

from september_2024.charpolice import new_output


class TestCharPolice(unittest.TestCase):
    def test_that_charpolice_works(self):
        self.assertTrue(new_output("he,llo@"))

    def test_that_output_works(self):
        self.assertTrue(new_output(""))

    def test_that_input_works(self):
        self.assertTrue(new_output(""))

