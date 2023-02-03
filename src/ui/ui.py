class UI:
    def __init__(self, console_io, rsa_service):
        self._console_io = console_io
        self._rsa_service = rsa_service

    def run(self):
        self.print_keys()

        while True:
            print()
            print("Commands:")
            print("0: Create new RSA keypair.")
            print("1: Encrypt a message.")
            print("2: Decrypt a message.")
            print("3: End program.")

            input_command = self._console_io.read("Input command: ")

            if input_command == "0":
                self._rsa_service.create_new_rsa_keypair()
                self.print_keys()
            elif input_command == "1":
                input_message = self._console_io.read("Input message:")
                self.print_encrypted_message(input_message)
            elif input_command == "2":                
                encrypted_input_message = self._console_io.read("Input an encrypted message:")
                self.print_decrypted_message(encrypted_input_message)
            elif input_command == "3":
                break
            else:
                self._console_io.print("Invalid input command. Please retype a valid input command!")

    def print_keys(self):
        self._console_io.print("\nPublic key:")
        self._console_io.print((self._rsa_service._n, self._rsa_service._e))
        self._console_io.print("\nPrivate key:")
        self._console_io.print(self._rsa_service._d)

    def print_encrypted_message(self, input_message):
        self._console_io.print("\nEncrypted message:")
        self._console_io.print(self._rsa_service.encrypt_message(input_message))

    def print_decrypted_message(self, encrypted_input_message):
        self._console_io.print("\nDecrypted message:")
        self._console_io.print(self._rsa_service.decrypt_message(encrypted_input_message))