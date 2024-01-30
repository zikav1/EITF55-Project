import random

class RabinMiller:

    def __init__(self) -> None:
        pass

    # Checking if the number is prime according to Rabin-Miller's algorithm
    # Tests if it's not prime, if it's composit
    # Say our n = 53
    def rabin_miller_is_prime(self, n):
        
        n = n - 1
        k , m = 1 , 0


        while n % pow(2, k) == 0:
            k += 1

        
        k = k - 1 # We need the prev k val
        m += n // pow(2, k)

        # now lets find the a. condition for a: 1 < a < n - 1
        # a = random.randint(2, n - 1)
        a = 2
        b = pow(a, m) % (n + 1)
        return b


    








        








rabin_miller = RabinMiller()
print(rabin_miller.rabin_miller_is_prime(53))

    





    

