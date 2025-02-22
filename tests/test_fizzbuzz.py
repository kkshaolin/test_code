from my_tests_code.FizzBuzz import fizzbuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_9_666_return_Fizz(self):
        fizz_list = [3,9,666]
        result = fizzbuzz(fizz_list)
        self.assertEqual(result, 'Fizz')

    def test_give_5_10_125_return_Buzz(self):
        buzz_list = [5,10,125]
        result = fizzbuzz(buzz_list)
        self.assertEqual(result, 'Buzz')

    def test_give_15_30_return_FizzBuzz(self):
        fizzbuzz_list = [15,30]
        result = fizzbuzz(fizzbuzz_list)
        self.assertEqual(result, 'FizzBuzz')

    def test_give_1_2_7_return_number(self):
        numers_list = [1,2,7]
        result = fizzbuzz(numers_list)
        self.assertEqual(result, numers_list)