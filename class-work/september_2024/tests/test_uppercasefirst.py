import unittest
from september_2024.uppercasefirst import uppercasefirst
class Testuppercasefirst(unittest.TestCase):
    def test_upper_case_first_exists(self):
        given = uppercasefirst("sEmIColOn")
        self.assertTrue(given)

    def test_upper_case_first_not_exists(self):
        given = uppercasefirst("sEmIColOn")
        returned = uppercasefirst("EICOsmoln")
        self.assertEqual(given, returned)

    def test_another_test_case(self ):
        given = uppercasefirst("HeLLo")
        returned = uppercasefirst("HLLeo")
        self.assertEqual(given, returned)