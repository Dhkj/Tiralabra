class RSA_Service:
    '''Class for generating the rsa key pair.'''
    def __init__(self, algorithm_service):
        self._algorithm_service = algorithm_service
        self._n, self._e, self._d = self.create_new_rsa_keypair()

    def get_rsa_key(self):
        '''Returns the rsa key pair in the form (n, e, d), where public key = (n, e) and private key = d.'''
        return (self._n, self._e, self._d)

    def set_new_rsa_keypair(self):
        self._n, self._e, self._d = self.create_new_rsa_keypair()

    def create_new_rsa_keypair(self):
        '''Creates a new rsa key pair.

        Returns:
            n, e, d for the generated key pair of the form: public key = (n, e), private key = d.
        
        '''
        e = 65537

        while True:
            # Generate two large prime numbers coprime to e:
            while True:
                p = self._algorithm_service.generate_potentially_large_random_prime_number()

                if p % e != 1:
                    break

            while True:
                q = self._algorithm_service.generate_potentially_large_random_prime_number()

                if q % e != 1:
                    break

            N = p*q
            L = (p-1)*(q-1)

            d = self._algorithm_service.extended_euclidean_algorithm(L, e)[2]

            if (e*d) % L == 1:
                break

        return N, e, d
