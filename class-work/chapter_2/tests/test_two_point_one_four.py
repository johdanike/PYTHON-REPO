import unittest

from chapter_2 import two_point_one_four
from chapter_2 import two_point_one_four


class TestTwoPointOneFour(unittest.TestCase):

    def test_two_point_one_four_method_exists(self):
        given = two_point_one_four.target_heart_rate_calculator(35)
        self.assertIsNotNone(given, 35)
