class UI:
    def __init__(self, console_io, message_service, rsa_service):
        self._console_io = console_io
        self._message_service = message_service
        self._rsa_service = rsa_service

    def run(self):
        self.create_new_rsa_key_pair()

        while True:
            print()
            print("Commands:")
            print("0: Create a new RSA key pair.")
            print("1: Encrypt a message.")
            print("2: Decrypt a message.")
            print("3: End program.")

            input_command = self._console_io.read("Input command: ")

            if input_command == "0":
                self.create_new_rsa_key_pair()            
            elif input_command == "1":
                self.encrypt_message()
            elif input_command == "2":
                self.decrypt_message()
            elif input_command == "3":
                break
            else:
                self._console_io.print("Invalid input command. Please retype a valid input command!")

    def create_new_rsa_key_pair(self):
        '''Creates and prints a new key pair.'''
        self._rsa_service.set_new_rsa_keypair()        
        key = self._rsa_service.get_rsa_key()
        n, e, d = key[0], key[1], key[2]
        self._console_io.print("\nPublic key:")
        self._console_io.print((n, e))
        self._console_io.print("\nPrivate key:")
        self._console_io.print(d)

    def encrypt_message(self):
        '''Encrypts a given input message and prints the encrypted message.'''
        input_message = self._console_io.read("Input message:")

        if len(input_message) > 40:
            print("\nMaximum length of 40 characters for a message exceeded.\nPlease input a message no greater than 40 characters in length for encryption!")
        else:
            key = self._rsa_service.get_rsa_key()
            encrypted_message = self._message_service.encrypt_message(input_message, key)
            self._console_io.print("\nEncrypted message:")
            self._console_io.print(encrypted_message)

    def decrypt_message(self):
        '''Decrypts a given input message and prints the decrypted message.'''
        encrypted_input_message = self._console_io.read("Input an encrypted message:")
        key = self._rsa_service.get_rsa_key()
        decrypted_message = self._message_service.decrypt_message(encrypted_input_message, key)
        self._console_io.print("\nDecrypted message:")
        self._console_io.print(decrypted_message)
