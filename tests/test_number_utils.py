from coe_number.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(is_prime_list([]))  # Empty list should be considered all primes

    def test_single_prime(self):
        self.assertTrue(is_prime_list([2]))
        self.assertTrue(is_prime_list([3]))
        self.assertTrue(is_prime_list([5]))
        self.assertFalse(is_prime_list([1])) #1 is not prime


    def test_multiple_primes(self):
        self.assertTrue(is_prime_list([2, 3, 5, 7, 11]))

    def test_mixed_list(self):
        self.assertFalse(is_prime_list([2, 4, 6])) #Contains even numbers >2
        self.assertFalse(is_prime_list([3, 5, 9])) #9 is not prime
        self.assertFalse(is_prime_list([1,2,3,4,5])) # Contains 1 and 4


    def test_large_primes(self): #Test with some larger prime numbers
        self.assertTrue(is_prime_list([97, 101, 103]))
        self.assertFalse(is_prime_list([100,101, 102]))


    def test_list_with_one_non_prime(self):
        self.assertFalse(is_prime_list([2, 3, 4, 5]))
        self.assertFalse(is_prime_list([7, 11, 15]))
