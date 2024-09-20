import unittest

from chapter_2 import two_point_one_five


class TestTwoPointOneFive(unittest.TestCase):
    def test_that_two_point_one_five_class_exists(self):
        self.assertTrue(two_point_one_five)
    def test_that_sort_in_ascending_order_method_exists(self):
