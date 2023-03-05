import unittest
from services.algorithm_service import Algorithm_Service
from services.message_service import Message_Service
from services.rsa_service import RSA_Service

class TestRSA_Service(unittest.TestCase):
    def setUp(self):
        self.algorithm_service = Algorithm_Service()
        self.message_service = Message_Service()
        self.rsa_service = RSA_Service(self.algorithm_service)

    '''Tests encryption and decryption function correctly for a generated key pair.'''
    def test_rsa_key_pair_generation(self):
        self.rsa_service.set_new_rsa_keypair()
        key = self.rsa_service.get_rsa_key()

        message = "test"

        encrypted_message = self.message_service.encrypt_message(message, key)
        decrypted_message = self.message_service.decrypt_message(encrypted_message, key)

        self.assertEqual(decrypted_message, message)
