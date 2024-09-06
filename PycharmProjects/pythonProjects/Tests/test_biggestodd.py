import unittest
import biggestodd


class TestBiggestOdds(unittest.TestCase):

    def test_that_checks_biggest_odd_function(self):
        biggestodd.biggest_odd("23956")

    def test_biggest_function_returns_biggest_odd(self):
        result = biggestodd.biggest_odd("23956")
        self.assertEqual(result, 9)

    def test_that_checks_odds(self):
        biggestodd.big_odd("23956")

    def test_that_asserts_biggest_odd(self):
        result = biggestodd.big_odd("23956")
        self.assertTrue(result, 9)

    def test_that_also_checks_biggest_odd(self):
        biggestodd.big_odd("23956")

    def test_that_also_asserts_biggest_odd(self):
        result = biggestodd.biggiie("23956")
        self.assertTrue(result, 9)