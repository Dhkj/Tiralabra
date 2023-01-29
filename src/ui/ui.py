#import random
#from services.rsa_service import RSA_Service
#from ui.console_io import Console_IO

class UI:
    def __init__(self, console_io, rsa_service):
        self._console_io = console_io
        self._rsa_service = rsa_service

    def run(self):
        while True:
            print()
            print("Commands:")
            print("0: Create new RSA keypair.")
            print("1: Encrypt a small integer.")
            print("2: Decrypt a small integer.")
            #Change texts for the 1, 2
            #print("1: Encrypt a string consisting of small English alphabet letters.")
            #print("2: Decrypt a string consisting of small English alphabet letters.")
            print("3: End program.")

            input_command = self._console_io.read("Input command: ")

            if input_command == "0":
                self._rsa_service.create_new_rsa_keypair()
            elif input_command == "1":
                #self._rsa_service.encrypt_string()
                input_integer = int(self._console_io.read("Input an integer:"))

                #This is for testing:
                print("Encoded:")
                print(pow(input_integer, self._rsa_service._e, self._rsa_service._n))
 
            elif input_command == "2":
                #self._rsa_service.decrypt_string()
                encyphered_input_integer = int(self._console_io.read("Input an encyphered integer:"))

                #This is for testing:
                print("Decoded:")
                print(pow(encyphered_input_integer, self._rsa_service._d, self._rsa_service._n))

            elif input_command == "3":
                break
            else:
                self._console_io.print("Invalid input command. Please retype a valid input command!")
