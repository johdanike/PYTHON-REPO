import unittest
from password_generator import jscript

class TestJscript(unittest.TestCase):

    def test_jscript(self):
        self.assertTrue(jscript)

    def test_that_method_exists(self):
        self.assertTrue(jscript.object_creator)

    def test_that_method_creates_dict(self):
        given = jscript.object_creator([1,1,2,3,2])
        expected = {
            1: 2,
            2: 2,
            3: 1
        }
        self.assertEqual(given, expected)

    def test_that_method_creates_dict_for_second_entry(self):
        given = jscript.object_creator([5,4,5,6,7,6])
        expected = {
            4: 1,
            5: 2,
            6: 2,
            7: 1
        }
        self.assertEqual(given, expected)

    def test_that_method_returns_empty_dict(self):
        given = jscript.object_creator([])
        expected = {}
        self.assertEqual(given, expected)

