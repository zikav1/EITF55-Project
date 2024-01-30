import random

class RabinMiller:

    def __init__(self) -> None:
        pass
    
    # Checking if the number is prime according to Rabin-Miller's algorithm
    # Tests if it's not prime, if it's composit
    # Say our n = 53
    def rabin_miller_is_prime(self, n):
        if n <= 1 or n % 2 == 0:
            return False
        
        N = n # Saving the original "n" value
        n = n - 1
        k = 1
        found = False

        while n % pow(2, k) == 0:
            k += 1

        
        k = k - 1 # We need the prev k val
        m = n // pow(2, k)

        # now lets find the a. condition for a: 1 < a < n - 1.
        a = 2

        b = pow(a, m, N)
        
        if b == 1:
            return False

        while not found:
            b = pow(b, 2, N)
            b = abs(b)

            if b == N - 1:
                found = True
            
        
        if b == N - 1:
            return True

        
        return False
    

        


    




rabin_miller = RabinMiller()
print(rabin_miller.rabin_miller_is_prime(547381))

    





    

