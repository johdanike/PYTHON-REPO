import unittest
import equalstrings
from biggestodd import result


class TestEqualStrings(unittest.TestCase):
    def test_equal_strings(self):
        equalstrings.equal_strings("love", "evol")

    def test_for_equal_strings(self):
        result = equalstrings.equal_strings("lonco", "colon")
        self.assertTrue(result)