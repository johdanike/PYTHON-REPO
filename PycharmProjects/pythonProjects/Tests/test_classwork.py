import unittest
from pythonProjects import classwork


class TestClassWorks(unittest.TestCase):


    def test_that_checks_that_index_are_raised_and_converted_to_dict(self):
        actual = classwork.raise_to_power_3([1,2,3,4,5])
        expected = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        self.assertEqual(actual, expected)

    def test_that_converted_to_dict(self):
        actual = classwork.get_key_cubes_in_the_dict([1,2,3,4,5])
        expected = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        self.assertEqual(actual, expected)
