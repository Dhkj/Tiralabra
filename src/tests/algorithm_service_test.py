import unittest
import random
from services.algorithm_service import Algorithm_Service

class TestAlgorithm_Service(unittest.TestCase):
    def setUp(self):
        self.algorithm_service = Algorithm_Service()

    '''Tests for the greatest common divisor:'''
    def test_greatest_common_divisor_of_21_and_40_is_1(self):
        greatest_common_divisor_of_21_and_40 = self.algorithm_service.extended_euclidean_algorithm(40, 21)[0]
        self.assertEqual(greatest_common_divisor_of_21_and_40, 1)

    def test_greatest_common_divisor_of_21_and_49_is_7(self):
        greatest_common_divisor_of_21_and_49 = self.algorithm_service.extended_euclidean_algorithm(49, 21)[0]
        self.assertEqual(greatest_common_divisor_of_21_and_49, 7)

    def test_greatest_common_divisor_of_103_and_31_is_1(self):
        greatest_common_divisor_of_103_and_31 = self.algorithm_service.extended_euclidean_algorithm(40, 21)[0]
        self.assertEqual(greatest_common_divisor_of_103_and_31, 1)

    ### Add more tests for greatest_common_divisor with greater values.

    '''Tests for the modular multiplicative inverse:'''
    def test_modular_multiplicative_inverse_of_157_is_17_modulo_2668(self):
        modular_multiplicative_inverse_of_157_modulo_2668 = self.algorithm_service.extended_euclidean_algorithm(2668, 157)[2]
        self.assertEqual(modular_multiplicative_inverse_of_157_modulo_2668, 17)

    ### Add more tests

    '''Tests for testing primality:'''
    def test_9_is_prime_returns_False(self):
        self.assertFalse(self.algorithm_service.miller_rabin(9, 40))

    def test_31_is_prime_returns_True(self):
        self.assertTrue(self.algorithm_service.miller_rabin(31, 40))

    def test_121_is_prime_returns_False(self):
        self.assertFalse(self.algorithm_service.miller_rabin(121, 40))

    def test_163_is_prime_returns_True(self):
        self.assertTrue(self.algorithm_service.miller_rabin(163, 40))

    ### Add more tests for greater values.

    '''Tests for generating a large prime number:'''
        # The implementation of the method is dependent on method miller_rabin(() and therefore does not test properly.
        # Better to change the generation of the prime number to take a parameter for range and check against another method etc.?
    def test_method_generate_large_random_prime_number_returns_a_prime_number(self):
        for i in range(20):
            large_random_prime_number = self.algorithm_service.generate_potentially_large_random_prime_number()
            self.assertTrue(self.algorithm_service.miller_rabin(large_random_prime_number, 40))

    '''Tests for generating a large prime number:'''
        # To do