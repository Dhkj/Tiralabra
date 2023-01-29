import random

class RSA_Service:
    def __init__(self):
        self._n = 0
        self._e = 0
        self._d = 0
        self.create_new_rsa_keypair()

    def encode(self, message):
        '''Encodes a message.'''
        return pow(message, self._e, self._n)

    def decode(self, encoded_message):
        '''Decodes a message.'''
        return pow(encoded_message, self._d, self._n)

    def create_new_rsa_keypair(self):
        '''Creates a new RSA key pair'''
        large_prime_number_first = self.generate_large_random_prime_number()
        large_prime_number_second = self.generate_large_random_prime_number()
      
        n = large_prime_number_first * large_prime_number_second #Multiplication ok?

        #Carmichael's totient function:
        lambda_n = abs((large_prime_number_first - 1)*(large_prime_number_second - 1)) / self.greatest_common_divisor(large_prime_number_first - 1, large_prime_number_second - 1)[0] # Implementation ok?

        #Step 4:
        #for small rand:
        e = 3
        #for large:
        #e = 2**16 + 1

        #e > 2:
        if e >= lambda_n or self.greatest_common_divisor(e, lambda_n)[0] != 1:
            print("Error in the value of e.")

        #Step 5:
        d = self.greatest_common_divisor(lambda_n, e)[1] #Refactor with the prior step 4

        self._n = n
        self._e = e
        self._d = d


    def generate_large_random_prime_number(self):
        '''Generates a large random prime number.'''
        large_random_prime_number = 0

        while True:
            #For large primes:
            #large_random_prime_number = random.randint(10**99, 10**100 - 1)

            #Currently using a small prime:
            large_random_prime_number = random.randint(100, 200)
            
            #Larger prime:
            #large_random_prime_number = random.randint(100000000, 200000000)

            if large_random_prime_number % 2 == 0:
                continue
                # Change to generate only odd numbers
                # Change to match the desired key length

            if self.is_prime(large_random_prime_number):
                return large_random_prime_number


    def is_prime(self, potentially_prime_integer):
        '''Checks whether a given integer is a prime number.'''
        #make sure potentially_prime_integer is odd

        for i in range(100): # Probability for a false prime is less than (1/2)^100
            uniformly_random_integer = random.randint(1, potentially_prime_integer - 1)
            # is uniformly random?

            x = self.greatest_common_divisor(potentially_prime_integer, uniformly_random_integer)[0]

            if x != 1:
                return False

            y1 = self.jacobi(uniformly_random_integer, potentially_prime_integer)
            y2 = pow(int(uniformly_random_integer), int((potentially_prime_integer - 1)/2), int(potentially_prime_integer))

            if (y1 - y2) % potentially_prime_integer != 0:
                return False
        
        return True

    def jacobi(self, integer_first, integer_second):
        '''Solves the jacobi symbol for given two primes.'''
        #Source Rsapaper page 9
        #Write out conditions
        if integer_first == 1:
            return 1
        elif integer_first % 2 == 0:
            return self.jacobi(integer_first/2, integer_second) * (-1)**((integer_second**2-1)/8)
        else:
            return self.jacobi(integer_second % integer_first, integer_first) * (-1)**((integer_first-1)*(integer_second-1)/4)

    def greatest_common_divisor(self, integer_first, integer_second, coefficient_a=-1, coefficient_b=0):
        '''Implements the extended Euclid's algorithm and returns a tuple with: [0]'the greatest common divisor' and [1]'the modular multiplicative inverse of ??? '''
        # Refactor/rename for the modular multiplicative inverse

        next_integer = integer_first % integer_second

        coefficient_a *= -1
        old_coefficient_b = coefficient_b
        coefficient_b = coefficient_a * coefficient_b - coefficient_a * (int) (integer_first / integer_second)

        if (next_integer == 0):
            return (integer_second, old_coefficient_b)
        else:
            return self.greatest_common_divisor(integer_second, next_integer, coefficient_a, coefficient_b)
