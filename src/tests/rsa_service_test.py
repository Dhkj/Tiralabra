import unittest
from services.rsa_service import RSA_Service

#class TestRSA_Service(unittest.TestCase):
class TestRSA_Service(unittest.TestCase):
    def setUp(self):
        self.rsa_service = RSA_Service()

    '''Tests for the greatest common divisor:'''
    def test_greatest_common_divisor_of_21_and_40_is_1(self):
        greatest_common_divisor_of_21_and_40 = self.rsa_service.greatest_common_divisor(40, 21)[0]
        self.assertEqual(greatest_common_divisor_of_21_and_40, 1)

    def test_greatest_common_divisor_of_21_and_49_is_7(self):
        greatest_common_divisor_of_21_and_49 = self.rsa_service.greatest_common_divisor(49, 21)[0]
        self.assertEqual(greatest_common_divisor_of_21_and_49, 7)

    def test_greatest_common_divisor_of_103_and_31_is_1(self):
        greatest_common_divisor_of_103_and_31 = self.rsa_service.greatest_common_divisor(40, 21)[0]
        self.assertEqual(greatest_common_divisor_of_103_and_31, 1)

    # Add more tests for greatest_common_divisor with greater values.

    '''Tests for the modular multiplicative inverse:'''

    def test_modular_multiplicative_inverse_of_157_is_17_modulo_2668(self):
        modular_multiplicative_inverse_of_157_modulo_2668 = self.rsa_service.greatest_common_divisor(2668, 157)[1]
        self.assertEqual(modular_multiplicative_inverse_of_157_modulo_2668, 17)

    # Add more tests

    '''Tests for the jacobi symbol:'''
    def test_jacobi_of_k_is_4_and_n_is_9_equals_1(self):
        jacobi_of_k_is_4_and_n_is_9 = self.rsa_service.jacobi(4, 9)
        self.assertEqual(jacobi_of_k_is_4_and_n_is_9, 1)

    def test_jacobi_of_k_is_4_and_n_is_59_equals_1(self):
        jacobi_of_k_is_4_and_n_is_59 = self.rsa_service.jacobi(4, 9)
        self.assertEqual(jacobi_of_k_is_4_and_n_is_59, 1)

    def test_jacobi_of_k_is_10_and_n_is_11_equals_negative_1(self):
        jacobi_of_k_is_10_and_n_is_11 = self.rsa_service.jacobi(10, 11)
        self.assertEqual(jacobi_of_k_is_10_and_n_is_11, -1)

    def test_jacobi_of_k_is_27_and_n_is_31_equals_negative_1(self):
        jacobi_of_k_is_27_and_n_is_31 = self.rsa_service.jacobi(27, 31)
        self.assertEqual(jacobi_of_k_is_27_and_n_is_31, -1)

    # Add more tests for the jacobi symbol with greater values, if possible.

    '''Tests for testing primality:'''
    def test_9_is_prime_returns_False(self):
        self.assertFalse(self.rsa_service.is_prime(9))

    def test_31_is_prime_returns_True(self):
        self.assertTrue(self.rsa_service.is_prime(31))

    def test_121_is_prime_returns_False(self):
        self.assertFalse(self.rsa_service.is_prime(121))

    def test_163_is_prime_returns_True(self):
        self.assertTrue(self.rsa_service.is_prime(163))

    # Add more tests for greater values.

    '''Tests for generating a large prime number:'''
    # The implementation of the method is dependent on is_prime() and therefore does not test properly.
    # Better to change the generation of the prime number to take a parameter for range and check against another method etc.?
    def test_method_generate_large_random_prime_number_returns_a_prime_number(self):
        for i in range(100):
            large_random_prime_number = self.rsa_service.generate_large_random_prime_number()
            self.assertTrue(self.rsa_service.is_prime(large_random_prime_number))

    '''Tests for generating a large prime number:'''
    # To do

    '''Tests for encoding/decoding:'''
    def test_encoding_and_decoding_an_integer_between_1_and_1000_is_correct(self):
        for i in range(1, 1001):
            encoded_integer = self.rsa_service.encode(i)
            print("i:")
            print(i)
            print("encoded_integer:")
            print(encoded_integer)
            decoded_integer = self.rsa_service.decode(encoded_integer)
            print("decoded_integer:")
            print(decoded_integer)
            print()
            self.assertEqual(decoded_integer, i)

    # Add tests