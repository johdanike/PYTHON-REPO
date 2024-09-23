import unittest
from september_24 import password_generator
from september_24.password_generator import convert_strings_to_ascii, encrypt_ascii, \
    convert_encrypted_ascii_back_to_string


class TestPassword(unittest.TestCase):

    def test_that_password_generator_class_exists(self):
        self.assertTrue(password_generator)
    def test_that_convert_to_ascii_method_exists(self):
        given = convert_strings_to_ascii("goodboy")
        expected = [103, 111, 111, 100, 98, 111, 121]
        self.assertEqual(given, expected)
    def test_that_encrypt_ascii_method_exists(self):
        given = encrypt_ascii([103, 111, 111, 100, 98, 111, 121])
        expected = [105, 113, 113, 102, 100, 113, 123]
        self.assertEqual(given, expected)
    def test_that_convert_ascii_back_to_string_method_exists(self):
        given = convert_encrypted_ascii_back_to_string([105, 113, 113, 102, 100, 113, 123])
        expected = "iqqfdq"
        self.assertEqual(given, expected)


