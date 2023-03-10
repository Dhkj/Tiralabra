import unittest
import random
from services.algorithm_service import Algorithm_Service
from services.message_service import Message_Service
from services.rsa_service import RSA_Service

class TestMessage_Service(unittest.TestCase):
    '''Test class for the encryption and decryption of a message.'''
    def setUp(self):
        self.algorithm_service = Algorithm_Service()
        self.message_service = Message_Service()
        self.rsa_service = RSA_Service(self.algorithm_service)

    def test_encryption_and_decryption_of_a_character_function_properly_for_a_generated_rsa_keypair(self):
        '''Creates a new key pair and tests encryption and decryption for 1000 unicode characters.'''        
        key = self.rsa_service.get_rsa_key()
        n, e, d = key[0], key[1], key[2]

        for i in range(1, 1000):
            encrypted_character = self.message_service.encrypt_character(str(i), n, e)
            decrypted_character = self.message_service.decrypt_character(encrypted_character, n, d)

            self.assertEqual(decrypted_character, i)

    def test_encrypting_and_decrypting_a_message_function_properly_for_a_generated_rsa_keypair(self):
        '''Creates a new key pair and tests encryption and decryption for 100 random strings with length of 10 unicode characters.'''
        key = self.rsa_service.get_rsa_key()
        
        for _ in range(100):
            message = chr(random.randint(100, 1000))

            for _ in range(9):
                character = chr(random.randint(100, 1000))
                message += character

            encrypted_message = self.message_service.encrypt_message(message, key)
            decrypted_message = self.message_service.decrypt_message(encrypted_message, key)

            self.assertEqual(decrypted_message, message)

    def test_encrypting_and_decrypting_a_40_character_message_function_properly_for_a_generated_rsa_keypair(self):
        '''Creates a random new key pair and tests encryption and decryption for 100 random strings of length 40 characters (combined unicode binary length less than 1024 bits).'''
        key = self.rsa_service.get_rsa_key()

        n = key[0]
        e = key[1]
        d = key[2]
        
        for _ in range(100):
            message = ""

            for _ in range(38):
                random_unicode_int = random.randint(100, 1000)
                random_unicode_int_as_binary_string = bin(random_unicode_int)
                random_unicode_binary_string = random_unicode_int_as_binary_string.split("b")[1].zfill(24)

                message += random_unicode_binary_string

            message_as_integer_base_10 = int(message, base=2)
            message_as_integer_base_10_string = str(message_as_integer_base_10)

            encrypted_message = self.message_service.encrypt_character(message_as_integer_base_10_string, n, e)
            decrypted_message = self.message_service.decrypt_character(encrypted_message, n, d)

            self.assertEqual(decrypted_message, message_as_integer_base_10)

    def test_encrypting_and_decrypting_a_40_character_message_function_properly_for_a_generated_rsa_keypair_second_test(self):
        '''Creates a random new key pair and tests encryption and decryption for 100 random strings of length 40 characters (combined unicode binary length less than 1024 bits).'''
        key = self.rsa_service.get_rsa_key()

        for _ in range(100):
            message = ""

            for _ in range(40):
                random_unicode_int = random.randint(100, 1000)
                random_unicode_character = chr(random_unicode_int)
                message += random_unicode_character

            encrypted_message = self.message_service.encrypt_message(message, key)
            decrypted_message = self.message_service.decrypt_message(encrypted_message, key)

            self.assertEqual(decrypted_message, message)

    def test_encrypting_and_decrypting_a_40_character_message_function_properly_for_100_randomly_generated_key_pairs(self):
        '''Creates 100 random new key pairs and tests encryption and decryption for 100 random strings of length 40 characters (combined unicode binary length less than 1024 bits).'''
        for _ in range(100):
            self.rsa_service.set_new_rsa_keypair()
            key = self.rsa_service.get_rsa_key()

            for _ in range(100):
                message = ""

                for _ in range(40):
                    random_unicode_int = random.randint(100, 1000)
                    random_unicode_character = chr(random_unicode_int)
                    message += random_unicode_character

                encrypted_message = self.message_service.encrypt_message(message, key)
                decrypted_message = self.message_service.decrypt_message(encrypted_message, key)

                self.assertEqual(decrypted_message, message)
