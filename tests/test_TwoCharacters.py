import unittest
from my_tests_code.TwoCharacters import alternate

class TestAlternate(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)

    def test_single_character(self):
        self.assertEqual(alternate("A"), 0)

    def test_two_characters_alternating(self):
        self.assertEqual(alternate("ABABAB"), 6)
        self.assertEqual(alternate("BABABA"), 6)

    def test_two_characters_non_alternating(self):
        self.assertEqual(alternate("AAABBB"), 0)
        self.assertEqual(alternate("AAAA"),0)


    def test_multiple_characters_alternating(self):
        self.assertEqual(alternate("ABABCA"), 6) #A,B
        self.assertEqual(alternate("ABACABA"), 6) #A,B
        self.assertEqual(alternate("BEAAAAAEB"), 4) #A,B
        self.assertEqual(alternate("AAABBBCCCDDDEEE"),0)

    def test_multiple_characters_non_alternating(self):
        self.assertEqual(alternate("AAABBBCCCDDDEEE"), 0)
        self.assertEqual(alternate("ABCDEF"),0)

    def test_complex_string(self):
        self.assertEqual(alternate("ABAACBABAA"), 6) #A,B

    def test_no_alternating_pairs(self):
        self.assertEqual(alternate("AAABBBCCC"), 0)
