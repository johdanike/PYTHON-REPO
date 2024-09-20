import unittest
from september_2024.numbs_to_list_and_tuples import numbs_list_tuples_2

class test_numbs_to_list_and_tuples(unittest.TestCase):

    def test_numbs_to_list_and_tuples(self):
        number = "43,65,87,98,24,376,87"
        expected = f"['43','65','87','98','24','374','87'], ('43','65','87','98','24','376','87')"
        actual = numbs_list_tuples_2(number)
        self.assertEqual(expected, actual)