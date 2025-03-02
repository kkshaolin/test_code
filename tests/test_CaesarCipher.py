import unittest
from my_tests_code.CaesarCipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 1), "")

    def test_no_shift(self):
        self.assertEqual(caesarCipher("abcxyzABCXYZ123", 0), "abcxyzABCXYZ123")

    def test_lowercase_shift(self):
        self.assertEqual(caesarCipher("abcxyz", 1), "bcdyz")
        self.assertEqual(caesarCipher("abcxyz", 2), "cdeza")
        self.assertEqual(caesarCipher("xyz", 1), "yza")
        self.assertEqual(caesarCipher("xyz", 26), "xyz") # Wrap around
        self.assertEqual(caesarCipher("xyz", 27), "yza") #Wrap around

    def test_uppercase_shift(self):
        self.assertEqual(caesarCipher("ABCXYZ", 1), "BCDYZ")
        self.assertEqual(caesarCipher("ABCXYZ", 2), "CDEZA")
        self.assertEqual(caesarCipher("XYZ", 1), "YZA")
        self.assertEqual(caesarCipher("XYZ", 26), "XYZ") # Wrap around
        self.assertEqual(caesarCipher("XYZ", 27), "YZA") # Wrap around

    def test_mixed_case_shift(self):
        self.assertEqual(caesarCipher("AbCdEfGhIjKlMnOpQrStUvWxYz", 1), "BcDeFgHiJkLmNoPqRsTuVwXyZa")

    def test_with_numbers_and_symbols(self):
        self.assertEqual(caesarCipher("Hello, World! 123", 1), "Ifmmp, Xpsme! 123")


    def test_large_shift(self):
        self.assertEqual(caesarCipher("abcxyz", 53), "fghijk") # Multiple of 26 +1