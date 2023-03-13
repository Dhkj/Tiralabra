import random

class Algorithm_Service:
    '''Class for the applied algorithms.'''
    def generate_potentially_large_random_prime_number(self):
        '''Generates and returns a large random potentially prime number.'''
        large_random_integer = random.randint(2**511, 2**512 - 1)

        if large_random_integer % 2 == 0:
            large_random_integer += 1

        while True:
            if self.miller_rabin(large_random_integer, 40):
                large_random_potential_prime_number = large_random_integer
                return large_random_potential_prime_number

            large_random_integer += 2

    def miller_rabin(self, n, k):
        '''Miller-Rabin Primality Test. First parameter n is an integer to be tested, second parameter is the number of iterations.
        
        Returns:
            True if the integer n is potentially prime, False otherwise.
        '''
        if n in (2, 3):
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

            if x in (1, n - 1):
                continue

            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False

        return True

    def extended_euclidean_algorithm(self, a, b, s0=1, s1=0, t0=0, t1=1):
        '''The extended Euclidean algorithm.

        Args:
            a: First integer, greater than b.
            b: Second integer.
        
        Returns:
            Tuple containing: [0]'the greatest common divisor' and [2]'the modular multiplicative inverse of the second parameter b.
        '''
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
