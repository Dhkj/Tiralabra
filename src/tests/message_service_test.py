import unittest
import random
from services.algorithm_service import Algorithm_Service
from services.message_service import Message_Service
from services.rsa_service import RSA_Service

class TestMessage_Service(unittest.TestCase):
    def setUp(self):
        self.algorithm_service = Algorithm_Service()
        self.message_service = Message_Service()
        self.rsa_service = RSA_Service(self.algorithm_service)

    '''Creates a new key pair and tests encryption and decryption for 1000 unicode characters.'''
    def test_encryption_and_decryption_of_a_character_function_properly_for_a_generated_rsa_keypair(self):        
        key = self.rsa_service.get_rsa_key()
        n, e, d = key[0], key[1], key[2]

        for i in range(1, 1000):
            encrypted_character = self.message_service.encrypt_character(str(i), n, e)
            decrypted_character = self.message_service.decrypt_character(encrypted_character, n, d)

            self.assertEqual(decrypted_character, str(i))

    '''Creates a new key pair and tests encryption and decryption for 100 random strings with length of 10 unicode characters.'''
    def test_encrypting_and_decrypting_a_message_function_properly_for_a_generated_rsa_keypair(self):
        key = self.rsa_service.get_rsa_key()
        
        for _ in range(100):
            message = chr(random.randint(1000, 1000))

            for _ in range(9):
                character = chr(random.randint(1000, 1000))
                message += character

            encrypted_message = self.message_service.encrypt_message(message, key)
            decrypted_message = self.message_service.decrypt_message(encrypted_message, key)

            self.assertEqual(decrypted_message, message)
