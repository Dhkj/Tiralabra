import unittest
import random
from services.rsa_service import RSA_Service

class TestRSA_Service(unittest.TestCase):
    def setUp(self):
        self.rsa_service = RSA_Service()

    '''Tests for the greatest common divisor:'''
    def test_greatest_common_divisor_of_21_and_40_is_1(self):
        greatest_common_divisor_of_21_and_40 = self.rsa_service.extended_euclidean_algorithm(40, 21)[0]
        self.assertEqual(greatest_common_divisor_of_21_and_40, 1)

    def test_greatest_common_divisor_of_21_and_49_is_7(self):
        greatest_common_divisor_of_21_and_49 = self.rsa_service.extended_euclidean_algorithm(49, 21)[0]
        self.assertEqual(greatest_common_divisor_of_21_and_49, 7)

    def test_greatest_common_divisor_of_103_and_31_is_1(self):
        greatest_common_divisor_of_103_and_31 = self.rsa_service.extended_euclidean_algorithm(40, 21)[0]
        self.assertEqual(greatest_common_divisor_of_103_and_31, 1)

    ### Add more tests for greatest_common_divisor with greater values.

    '''Tests for the modular multiplicative inverse:'''
    def test_modular_multiplicative_inverse_of_157_is_17_modulo_2668(self):
        modular_multiplicative_inverse_of_157_modulo_2668 = self.rsa_service.extended_euclidean_algorithm(2668, 157)[2]
        self.assertEqual(modular_multiplicative_inverse_of_157_modulo_2668, 17)

    ### Add more tests

    '''Tests for testing primality:'''
    def test_9_is_prime_returns_False(self):
        self.assertFalse(self.rsa_service.miller_rabin(9, 40))

    def test_31_is_prime_returns_True(self):
        self.assertTrue(self.rsa_service.miller_rabin(31, 40))

    def test_121_is_prime_returns_False(self):
        self.assertFalse(self.rsa_service.miller_rabin(121, 40))

    def test_163_is_prime_returns_True(self):
        self.assertTrue(self.rsa_service.miller_rabin(163, 40))

    ### Add more tests for greater values.

    '''Tests for generating a large prime number:'''
        # The implementation of the method is dependent on method miller_rabin(() and therefore does not test properly.
        # Better to change the generation of the prime number to take a parameter for range and check against another method etc.?
    def test_method_generate_large_random_prime_number_returns_a_prime_number(self):
        for i in range(100):
            large_random_prime_number = self.rsa_service.generate_potentially_large_random_prime_number()
            self.assertTrue(self.rsa_service.miller_rabin(large_random_prime_number, 40))

    '''Tests for generating a large prime number:'''
        # To do

    '''Tests for the least commond multiple:'''
    def test_lcm_of_12_and_4_is_4(self):
        self.assertEqual(self.rsa_service.lcm(12, 4), 4) ########

    def test_lcm_of_12_and_4_is_4(self):
        self.assertEqual(self.rsa_service.lcm(17, 4), 68)

    '''Tests for Carmichael's totient function:'''
    def test_lambda_n(self):
        pass

    '''Tests for creating new key pair and encrypting/decrypting (for all characters):'''
    def test_encrypting_and_decrypting_function_properly_for_a_generated_rsa_keypair(self):
        #self.rsa_service.create_new_rsa_keypair()
        j = 1

        for i in range(1, 28): #
            '''
            if i == 27:
                i = 32
            '''
            if j == 27:
                j = 32

            #self.rsa_service.create_new_rsa_keypair()
            #encrypted_character = self.rsa_service.encrypt_character(str(i).zfill(2), self.rsa_service._n, self.rsa_service._e)
            encrypted_character = self.rsa_service.encrypt_character(str(j).zfill(2), self.rsa_service._n, self.rsa_service._e)

            decrypted_character = self.rsa_service.decrypt_character(encrypted_character, self.rsa_service._n, self.rsa_service._d)

            #self.assertEqual(self.rsa_service.decrypt_character(self.rsa_service.encrypt_character(str(i))), str(i))           
            #self.assertEqual(decrypted_character, str(i).zfill(2))
            self.assertEqual(decrypted_character, str(j).zfill(2))

            j += 1

    '''Tests for creating new key pair and encrypting/decrypting a message:'''
    def test_encrypting_and_decrypting_a_message_function_properly_for_a_generated_rsa_keypair(self):
        for i in range(100):
            message = ""

            for j in range(50):
                string_number_between_1_and_27 = str(random.randint(1, 27)).zfill(2)

                if string_number_between_1_and_27 == "27":
                    string_number_between_1_and_27 = "32"

                message += self.rsa_service._decryption_alphabet[string_number_between_1_and_27]

            encrypted_message = self.rsa_service.encrypt_message(message)
            decrypted_message = self.rsa_service.decrypt_message(encrypted_message)

            self.assertEqual("".join(decrypted_message.split()), "".join(message.split()))