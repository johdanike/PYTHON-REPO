import unittest

from september_2024.task2 import single_string_from_two_strings


class TestTask2(unittest.TestCase):
    def test_that_task2_class_exists(self):
        single_string_from_two_strings("abc", "xyz")

    def test_that_parameter_takes_2_parameters(self):
        given = single_string_from_two_strings("abc", "xyz")
        expected = "xycabz"
        self.assertEqual(given, expected)

    def test_for_different_caps(self):
        given = single_string_from_two_strings("Abc", "xYz")
        expected = "xYcAbz"