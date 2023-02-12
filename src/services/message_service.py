class Message_Service:
    '''Class for encrypting and decrypting a message.'''
    def encrypt_message(self, message, key):
        '''Encrypts a message.'''
        n = key[0]
        e = key[1]

        list_of_characters_in_the_message = [character for character in message]
        list_of_integer_unicode_characters_in_the_message = [ord(character) for character in list_of_characters_in_the_message]
        list_of_encrypted_characters_in_the_message = [self.encrypt_character(integer_unicode_character, n, e) for integer_unicode_character in list_of_integer_unicode_characters_in_the_message]

        #The character used for spacing in the encryption is chosen to be unicode character 6000:
        space_character_in_encryption_as_integer_unicode = str(6000)
        encrypted_space_character_in_encryption = self.encrypt_character(space_character_in_encryption_as_integer_unicode, n, e)

        encrypted_message = encrypted_space_character_in_encryption.join(list_of_encrypted_characters_in_the_message)

        return encrypted_message

    def decrypt_message(self, message, key):
        '''Decrypts a message.'''
        n = key[0]
        e = key[1]
        d = key[2]

        #The character used for spacing in the encryption is chosen to be unicode character 6000:
        space_character_in_encryption_as_integer_unicode = str(6000)
        encrypted_space_character_in_encryption = self.encrypt_character(space_character_in_encryption_as_integer_unicode, n, e)

        list_of_encrypted_characters_in_the_encrypted_message = message.split(encrypted_space_character_in_encryption)
        list_of_decrypted_unicode_integers_in_the_message = [self.decrypt_character(encrypted_character, n, d) for encrypted_character in list_of_encrypted_characters_in_the_encrypted_message]
        list_of_decrypted_characters_in_the_message = [chr(int(decrypted_unicode_integer)) for decrypted_unicode_integer in list_of_decrypted_unicode_integers_in_the_message]

        decrypted_message = "".join(list_of_decrypted_characters_in_the_message)

        return decrypted_message

    def encrypt_character(self, char, n, e):
        '''Encrypts a character.'''
        return str(pow(int(char), e, n))

    def decrypt_character(self, char, n, d):
        '''Decrypts a character.'''
        return str(pow(int(char), d, n))
