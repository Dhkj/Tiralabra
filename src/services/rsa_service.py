import random

class RSA_Service:
    def __init__(self):
        self._encryption_alphabet = {'a': '01',
            'b': '02',
            'c': '03',
            'd': '04',
            'e': '05',
            'f': '06',
            'g': '07',
            'h': '08',
            'i': '09',
            'j': '10',
            'k': '11',
            'l': '12',
            'm': '13',
            'n': '14',
            'o': '15',
            'p': '16',
            'q': '17',
            'r': '18',
            's': '19',
            't': '20',
            'u': '21',
            'v': '22',
            'w': '23',
            'x': '24',
            'y': '25',
            'z': '26',
            ' ': '32'}

        self._decryption_alphabet = {n: c for c, n in self._encryption_alphabet.items()}

        self._n = 0
        self._e = 0
        self._d = 0

        self.create_new_rsa_keypair()

    def encrypt_message(self, message):
        '''Encrypts a message.'''
        list_of_words_in_the_message = message.lower().split()
        encrypted_message_word_list = []

        for word in list_of_words_in_the_message:
            characters_in_the_word = [character for character in word]

            encrypted_characters = [self.encrypt_character(self._encryption_alphabet[character], self._n, self._e) for character in characters_in_the_word]
            
            encrypted_word = " ".join(encrypted_characters)
            
            encrypted_message_word_list.append(encrypted_word)

        encrypted_message = f" {self.encrypt_character(self._encryption_alphabet[' '], self._n, self._e)} ".join(encrypted_message_word_list)

        return encrypted_message

    def decrypt_message(self, message):
        '''Decrypts a message.'''
        list_of_characters_in_the_encrypted_message = message.split()

        list_of_decrypted_integer_characters = []

        list_of_characters_in_decrypted_message = []

        for character in list_of_characters_in_the_encrypted_message:
            list_of_decrypted_integer_characters.append(self.decrypt_character(character, self._n, self._d))

        for character in list_of_decrypted_integer_characters:
            list_of_characters_in_decrypted_message.append(self._decryption_alphabet[character])

        decrypted_message = "".join(list_of_characters_in_decrypted_message)

        return decrypted_message

    def encrypt_character(self, char, n, e):
        '''Encrypts a character.'''
        return str(pow(int(char), e, n)).zfill(2)

    def decrypt_character(self, char, n, d):
        '''Decrypts a character.'''
        return str(pow(int(char), d, n)).zfill(2)

    def create_new_rsa_keypair(self):
        '''Creates a new RSA key pair'''
        large_prime_number_first = self.generate_potentially_large_random_prime_number()
        large_prime_number_second = self.generate_potentially_large_random_prime_number()
      
        n = large_prime_number_first * large_prime_number_second
        lambda_n = self.lambda_n(large_prime_number_first, large_prime_number_second)

        #for large:
        #e = 2**16 + 1
        e = 3

        #Only works for small e: ?
        for i in range(3, lambda_n):
            if self.extended_euclidean_algorithm(i, lambda_n)[0] == 1:
                e = i
                break
        
        '''For large values of e, not currently in use:
        while True:
            if e >= lambda_n or self.greatest_common_divisor(e, lambda_n)[0] != 1:
                e -= 2
            else:
                break
        '''
        d = self.extended_euclidean_algorithm(lambda_n, e)[2]

        if d < 0:
            d = lambda_n + d

        self._n = n
        self._e = e
        self._d = d
    
    def lambda_n(self, a, b):
        '''Carmichael's totient function.'''
        return self.lcm(a-1,b-1)
        
    def lcm(self, a, b):
        '''Least common multiple.'''
        return int(abs(a*b)/self.extended_euclidean_algorithm(a, b)[0])

    def generate_potentially_large_random_prime_number(self):
        '''Generates a large random prime number.'''
        #large_random_integer = random.randint(2**511, 2**512 - 1)       
        large_random_integer = random.randint(100, 200)

        if large_random_integer % 2 == 0:
            large_random_integer += 1

        while True:
            if self.miller_rabin(large_random_integer, 40):
                large_random_potential_prime_number = large_random_integer
                # Add further tests for primality, e.g. that the encoding/decoding works?
                return large_random_potential_prime_number
            else:
                large_random_integer += 2

    def miller_rabin(self, n, k):
        '''Miller-Rabin Primality Test.'''
        if n == 2 or n == 3:
            return True

        if n % 2 == 0:
            return False

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def extended_euclidean_algorithm(self, a, b, s0=1, s1=0, t0=0, t1=1):
        '''The extended Euclidean algorithm. Returns a tuple with: [0]'the greatest common divisor' and [2]'the modular multiplicative inverse of the second parameter b.'''
        q = int(a / b)
        r = a - q * b

        if r == 0:
            return (b, s1, t1)

        a = b
        b = r

        s2 = s0 - q*s1
        s0 = s1
        s1 = s2

        t2 = t0 - q*t1
        t0 = t1
        t1 = t2

        return self.extended_euclidean_algorithm(a, b, s0, s1, t0, t1)
