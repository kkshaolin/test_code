from my_tests_code.Staircase import staircase
import unittest

class StaircaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = '#'
        expected_output = " #\n" +"##"
        expected = " #\n" +"##"

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected, f'Should be {expected_output}')

    def test_give_31_with_hash_should_be_out_of_size(self):
        # arrange
        n = 31
        pattern = '#'
        expected_output = "out of size"
        expected = "out of size"

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected, f'Should be {expected_output}')