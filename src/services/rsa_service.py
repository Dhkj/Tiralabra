import random

class RSA_Service:
    def __init__(self):
        #Think of a better implementation:
        self._n = 0
        self._e = 0
        self._d = 0

        rsa_keypair = self.create_new_rsa_keypair()

    # Add getters for self._n, self._e, self._d ?

    def encode(self, message):
        return pow(message, self._e, self._n)

    def decode(self, encoded_message):
        return pow(encoded_message, self._d, self._n)

    def create_new_rsa_keypair(self):
        #Refactor! Make own method for calculating lambda_n and tests
        #Add verifications that the are really primes, e.g. trying to encrypt/decrypt
        large_prime_number_first = self.generate_large_random_prime_number()
        large_prime_number_second = self.generate_large_random_prime_number()
      
        n = large_prime_number_first * large_prime_number_second #Multiplication ok?

        #Carmichael's totient function:
        lambda_n = abs((large_prime_number_first - 1)*(large_prime_number_second - 1)) / self.greatest_common_divisor(large_prime_number_first - 1, large_prime_number_second - 1)[0] #ok?

        #Step 4:
        #for small rand:
        e = 3
        #for large:
        #e = 2**16 + 1

        #e > 2:
        if e >= lambda_n or self.greatest_common_divisor(e, lambda_n)[0] != 1: #Works correctly?
            print("Error in the value of e.")

        #Step 5:
        #d = self.greatest_common_divisor(e, lambda_n)[1] #e and lambda_n in wrong order?
        
        #This works?
        d = self.greatest_common_divisor(lambda_n, e)[1] #Refactor with the prior step 4

        # For testing:
        '''
        print("n:")
        print(n)
        print("e:")
        print(e)
        print("d:")
        print(d)
        '''

        self._n = n
        self._e = e
        self._d = d


    def generate_large_random_prime_number(self):
        large_random_prime_number = 0

        while True: # Generate a better way to generate odd numbers
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

            if self.is_prime(large_random_prime_number): #!= None:
                return large_random_prime_number


    def is_prime(self, potentially_prime_integer):
        #make sure potentially_prime_integer is odd
        #uniformly_random_integer = random.randint(1, integer - 1)
        '''1. uniformly random?'''

        for i in range(100): # Probability for a false prime is less than (1/2)^100
            uniformly_random_integer = random.randint(1, potentially_prime_integer - 1)
            # is uniformly random?

            '''
            #For testing
            print("uniformly_random_integer:")
            print(uniformly_random_integer)
            '''

            #non-tuple
            #x = self.greatest_common_divisor(potentially_prime_integer, uniformly_random_integer)
 
            #tuple
            x = self.greatest_common_divisor(potentially_prime_integer, uniformly_random_integer)[0]

            '''
            #For testing
            print("gcd:")
            print(x)
            '''

            if x != 1:
                return False

            '''
            # Alternative implementation:
            if self.greatest_common_divisor(potentially_prime_integer, uniformly_random_integer) != 1:
                print("gcd:")
                print(self.greatest_common_divisor(potentially_prime_integer, uniformly_random_integer))
                return False
            '''

            y1 = self.jacobi(uniformly_random_integer, potentially_prime_integer)

            #y2 = uniformly_random_integer ** ((potentially_prime_integer - 1)/2) % potentially_prime_integer #potenssiinkorotusalg tmv?
            y2 = pow(int(uniformly_random_integer), int((potentially_prime_integer - 1)/2), int(potentially_prime_integer))

            '''
            #For testing
            print("jacobi vasen:")
            print(y1)
            print("jacobi oikea:")
            print(y2)
            '''

            if (y1 - y2) % potentially_prime_integer != 0: #toimii? jacobi arg toisinpain
                return False
            '''
            if y1 != y2: #toimii? jacobi arg toisinpain
                return False
            '''
            '''
            if self.jacobi(uniformly_random_integer, potentially_prime_integer) != uniformly_random_integer ** ((potentially_prime_integer - 1)/2) % potentially_prime_integer: #toimii? jacobi arg toisinpain
                print("jacobi vasen:")
                print(self.jacobi(uniformly_random_integer, potentially_prime_integer))
                print("jacobi oikea:")
                print(uniformly_random_integer ** ((potentially_prime_integer - 1)/2) % potentially_prime_integer)
                return False
            '''
        return True #toimii?

    def jacobi(self, integer_first, integer_second):
        #Source Rsapaper page 9
        #Write out conditions
        if integer_first == 1:
            return 1
        elif integer_first % 2 == 0:
            return self.jacobi(integer_first/2, integer_second) * (-1)**((integer_second**2-1)/8)
        else:
            return self.jacobi(integer_second % integer_first, integer_first) * (-1)**((integer_first-1)*(integer_second-1)/4) #Correct?

    def greatest_common_divisor(self, integer_first, integer_second, coefficient_a=-1, coefficient_b=0):
        '''Implements the extended Euclid's algorithm and returns a tuple with: [0]'the greatest common divisor' and [1]'the modular multiplicative inverse of ??? '''
        # Refactor/rename for the modular multiplicative inverse

        next_integer = integer_first % integer_second

        #print(next_integer)

        '''
        coefficient_a = 1
        coefficient_b = integer_first / integer_second
        '''


        ''''''
        coefficient_a *= -1
        '''coefficient_b = -1 * coefficient_b + 1'''
        
        '''coefficient_b = -1 * coefficient_b - integer_first / integer_second'''
        '''coefficient_b = -1 * (coefficient_b - integer_first / integer_second)'''
        '''coefficient_b = -1 * coefficient_a * (coefficient_b + integer_first / integer_second)'''
        '''-1'''
        # Change to more elegant
        old_coefficient_b = coefficient_b

        coefficient_b = coefficient_a * coefficient_b - coefficient_a * (int) (integer_first / integer_second)



        if (next_integer == 0):
            #print("Hei!")
            #print(integer_second)
            #return True


            #######return integer_second


            #print("Hei!!")
            '''1. Oikein?? 2. lisaa muutb palautettavat parametrit'''


            #tuple-toteutus:
            #return (integer_second, coefficient_b)
            return (integer_second, old_coefficient_b)



        else:
            '''rekursio!'''

            '''print((str)integer_second + ", " + (str)next_integer + ", " + (str)coefficient_a + ", " + (str)coefficient_b)'''

            #print(f"{integer_second}, {next_integer}, {coefficient_a}, {coefficient_b}")


            #self.greatest_common_divisor(integer_second, next_integer, coefficient_a, coefficient_b)

            return self.greatest_common_divisor(integer_second, next_integer, coefficient_a, coefficient_b)
