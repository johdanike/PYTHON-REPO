import unittest

from september_2024.dictionarytask import new_dict


class TestDictionaryWord(unittest.TestCase):

    def test_that_function_works(self):
        actual = new_dict("banana")
        expected = {'b': 1, 'a': 3, 'n': 2}
        self.assertTrue(actual, expected)

    def test_that_function_checks_capital_letters(self):
        actual = new_dict("BALABLUEBLUE")
        expected = {'B': 3, 'A': 2, 'U': 2, 'E': 2, 'L': 3}
        self.assertTrue(actual, expected)

    def test_for_small_letter_with_capital_letters(self):
        actual = new_dict("BalaBlueV")
        expected = {'B': 2, 'A': 2, 'U': 1, 'E': 1, 'V': 1, 'L': 2}
        self.assertTrue(actual, expected)

    def test_empty_dict(self):
        actual = new_dict(" ")
        expected = {}
        self.assertTrue(actual, expected)
