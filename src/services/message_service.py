class Message_Service:
    '''Class for encrypting and decrypting a message.'''
    def encrypt_message(self, message, key):
        '''Encrypts a message. Message is ...'''
        n = key[0]
        e = key[1]
        #
        d= key[2]

        message_length = len(message)
        number_of_partial_messages = int(message_length / 40) + 1 #40 ok?

        #print(number_of_partial_messages)

        list_of_characters_in_the_message = [character for character in message]
        #print(list_of_characters_in_the_message)
        list_of_integer_unicode_characters_in_the_message = [ord(character) for character in list_of_characters_in_the_message]
        #print(list_of_integer_unicode_characters_in_the_message)
        list_of_binary_unicode_characters_in_the_message = [bin(integer_unicode_character) for integer_unicode_character in list_of_integer_unicode_characters_in_the_message]
        #print(list_of_binary_unicode_characters_in_the_message)
        # Unicode encoded using 24 bits --> Filling of every character bit presentation to 24 bits:
        list_of_filled_binary_unicode_characters_in_the_message = [binary_unicode_character.split("b")[1].zfill(24) for binary_unicode_character in list_of_binary_unicode_characters_in_the_message]
        #print(list_of_filled_binary_unicode_characters_in_the_message)

        # Encryption and decpryption functions for less than 1023 bits = approx. 40 binary unicode characters. (encryption/decryption modulo is 1023 - 1024 bits):
        list_of_partial_messages = []

        for i in range(number_of_partial_messages): #range ok?
            #print("i:")
            #print(i)

            partial_message = ""

            upper_limit = 40*i + 40

            if upper_limit > len(list_of_filled_binary_unicode_characters_in_the_message): # >=?
                upper_limit = len(list_of_filled_binary_unicode_characters_in_the_message) # - 1 # ok?
            # Add tests for the limit values
            for j in range(40*i, upper_limit): #40*i + 40): # uppoer limit ok for that last?
                partial_message += list_of_filled_binary_unicode_characters_in_the_message[j] #[i] # ok??

            list_of_partial_messages.append(partial_message)
            #list_of_partial_messages.append(message[40*i:40*i + 40]) #toimii, jos yli??
        
        #print(list_of_partial_messages)
        #Muuta nimi encrypt_character
        list_of_encrypted_partial_messages = [self.encrypt_character(partial_message, n, e) for partial_message in list_of_partial_messages]



        ###


        encrypted_message = "".join(list_of_encrypted_partial_messages)

        #print(encrypted_message)




        ######decrypted_message = self.decrypt_character(encrypted_message, n, d)


        #print(decrypted_message)





        return encrypted_message



    # rename decrypt_character
    def decrypt_message(self, message, key):
        '''Decrypts a message.'''
        n = key[0]
        e = key[1]
        d = key[2]

        decrypted_binary_message = str(self.decrypt_character(message, n, d)) #Refaktoroi/muuta palarvo decrypt_character
        #print(decrypted_binary_message)

        decrypted_binary_message_length = len(decrypted_binary_message)
        #print(decrypted_binary_message_length)
        number_of_partial_messages = int (decrypted_binary_message_length / 24) + 1 #24 ok?
        
        #print("number_of_partial_messages")
        #print(number_of_partial_messages)

        number_of_characters_in_the_first_partial_message = decrypted_binary_message_length % 24
        #print("number_of_characters_in_the_first_partial_message")
        #print(number_of_characters_in_the_first_partial_message)

        list_of_partial_messages = []

        for i in range(number_of_partial_messages): #range ok?
            #print("i:")
            #print(i)

            partial_message = ""

            lower_limit = 0
            ##upper_limit = 40*i + number_of_characters_in_the_first_partial_message
            upper_limit = 24*i + number_of_characters_in_the_first_partial_message


            if i > 0:
                #lower_limit = 40*(i-1) + number_of_characters_in_the_first_partial_message
                #lower_limit = 24*(i-1) + number_of_characters_in_the_first_partial_message
                lower_limit = 24*(i-1) + number_of_characters_in_the_first_partial_message


            #if i == 0: # >=?
            #    upper_limit = len(list_of_filled_binary_unicode_characters_in_the_message) # - 1 # ok?
            # Add tests for the limit values
            for j in range(lower_limit, upper_limit): #40*i + 40): # uppoer limit ok for that last?
                partial_message += decrypted_binary_message[j] #[i] # ok??

            list_of_partial_messages.append(partial_message)

            #print(list_of_partial_messages)

            #NEEDED???
            #list_of_partial_messages[0] = list_of_partial_messages[0].zfill(24) ???
        

        list_of_decrypted_unicode_integers_in_the_message = [int(partial_message, base=2) for partial_message in list_of_partial_messages]
        
        #print(list_of_decrypted_unicode_integers_in_the_message)

        list_of_decrypted_characters_in_the_message = [chr(decrypted_unicode_integer) for decrypted_unicode_integer in list_of_decrypted_unicode_integers_in_the_message]

        #print(list_of_decrypted_characters_in_the_message)

        decrypted_message = "".join(list_of_decrypted_characters_in_the_message)

        #print(decrypted_message)

        return decrypted_message

    def encrypt_character(self, char, n, e):
        '''Encrypts a character. Returns a string containing the encrypted character.'''
        return str(pow(int(char), e, n))

    def decrypt_character(self, char, n, d):
        '''Decrypts a character. Returns an integer of the unicode integer value of the decrypted character.'''
        return pow(int(char), d, n)
