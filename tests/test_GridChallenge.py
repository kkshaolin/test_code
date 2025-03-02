import unittest
from my_tests_code.GridChallenge import gridChallenge

class TestGridChallenge(unittest.TestCase):

    def test_empty_grid(self):
        self.assertEqual(gridChallenge([]), "YES")  #Empty grid should pass

    def test_single_row(self):
        self.assertEqual(gridChallenge(["abc"]), "YES")
        self.assertEqual(gridChallenge(["cba"]), "YES")


    def test_small_grid(self):
        self.assertEqual(gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES")
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")
        self.assertEqual(gridChallenge(["cba", "dae", "gfe"]), "YES") # Example where rows are sorted but cols are not
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")
        self.assertEqual(gridChallenge(["abc", "adc", "ghi"]), "NO") # Example of a "NO" case


    def test_larger_grid(self):
        grid = ["eabcd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")

        grid = ["mpxz", "abcd", "wlmf"]
        self.assertEqual(gridChallenge(grid),"NO")

        grid = ["abc", "lmn", "xyz"]
        self.assertEqual(gridChallenge(grid),"YES")


    def test_unsorted_grid(self):
        grid = ["abcd", "efgh", "ijkl", "mnop"]
        self.assertEqual(gridChallenge(grid), "YES")

        grid = ["mpxz", "abcd", "wlmf"]
        self.assertEqual(gridChallenge(grid), "NO")