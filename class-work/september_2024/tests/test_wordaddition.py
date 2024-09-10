import unittest
from september_2024.wordaddition import word_plus_ce

class TestWordAddition(unittest.TestCase):

    def test_word_plus_ce(self):
       value = word_plus_ce("helloo")
       self.assertTrue(word_plus_ce("helloo"))

    def test_that_func_works_on_even_count_strings(self):
        value = word_plus_ce("helloo")
        expected = "helceloo"
        self.assertEqual(value, expected)

    def test_that_func_works_on_odd_count_strings(self):
        value = word_plus_ce("hello")
        expected = "helloce"
        self.assertEqual(value, expected)

    def test_that_func_throws_exception_when_passed_an_empty_string(self):
        with self.assertRaises(Exception) as context:
            "Enter a valid word"


