class Message_Service:
    '''Class for encrypting and decrypting a message.'''
    def encrypt_message(self, message, key):
        '''Encrypts a message that is no greater than 40 unicode characters in length.
        
        Args:
            message: String message to be encrypted.
            key: RSA encryption key

        Returns:
            The encrypted message as a 1024 bit integer.
        
        '''
        n = key[0]
        e = key[1]

        list_of_characters_in_the_message = [character for character in message]
        list_of_integer_unicode_characters_in_the_message = [ord(character) for character in list_of_characters_in_the_message]
        list_of_binary_unicode_characters_in_the_message = [bin(integer_unicode_character) for integer_unicode_character in list_of_integer_unicode_characters_in_the_message]

        # Assuming unicode characters encoded using 24 bits --> Filling of every character bit presentation to 24 bits:
        list_of_filled_binary_unicode_characters_in_the_message = [binary_unicode_character.split("b")[1].zfill(24) for binary_unicode_character in list_of_binary_unicode_characters_in_the_message]

        message_encoded_into_binary_number = "".join(list_of_filled_binary_unicode_characters_in_the_message)
        message_encoded_into_an_integer = int(message_encoded_into_binary_number, base=2)
        encrypted_message = self.encrypt_character(message_encoded_into_an_integer, n, e)

        return encrypted_message

    def decrypt_message(self, message, key):
        '''Decrypts a message.
        
        Args:
            message: String message to be encrypted.
            key: RSA encryption key

        Returns:
            The encrypted message as a 1024 bit integer.
        
        
        '''
        n = key[0]
        d = key[2]

        decrypted_message_as_an_integer_string = self.decrypt_character(message, n, d)
        decrypted_message_as_a_binary_string = bin(decrypted_message_as_an_integer_string).split("b")[1]
        decrypted_binary_message_length = len(decrypted_message_as_a_binary_string)

        #Unicode characters encoded using 24 bits -> Each 24 bits correspond to a character, except
        #for the first character for which the transformation between binary and integer has omitted the leading zeros.
        number_of_characters_in_message = int (decrypted_binary_message_length / 24) + 1
        number_of_characters_in_the_first_partial_message = decrypted_binary_message_length % 24

        list_of_binary_characters = []

        for i in range(number_of_characters_in_message):
            character_in_binary = ""

            lower_limit = 0
            upper_limit = 24*i + number_of_characters_in_the_first_partial_message

            if i > 0:
                lower_limit = 24*(i-1) + number_of_characters_in_the_first_partial_message

            for j in range(lower_limit, upper_limit):
                character_in_binary += decrypted_message_as_a_binary_string[j]

            list_of_binary_characters.append(character_in_binary)

        list_of_decrypted_characters_in_the_message_as_unicode_integers = [int(binary_character, base=2) for binary_character in list_of_binary_characters]
        list_of_decrypted_characters_in_the_message = [chr(decrypted_unicode_integer) for decrypted_unicode_integer in list_of_decrypted_characters_in_the_message_as_unicode_integers]
        decrypted_message = "".join(list_of_decrypted_characters_in_the_message)

        return decrypted_message

    def encrypt_character(self, char, n, e):
        '''Encrypts a character/an integer.

        Args:
            char: Character/integer to encrypt.
            n, e: public RSA key
        
        Returns:
            String containing the encrypted character/integer.
        '''
        return str(pow(int(char), e, n))

    def decrypt_character(self, char, n, d):
        '''Decrypts a character/an integer.

        Args:
            char: Character/integer to decrypt.
            n, d: private RSA key
        
        Returns:
            Integer representing the decrypted set of characters.
        '''
        return pow(int(char), d, n)
