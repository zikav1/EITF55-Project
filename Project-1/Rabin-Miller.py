import random

class RabinMiller:

    def __init__(self) -> None:
        pass
    
    def is_prime(self, n):
        if n % 2 == 0 or n < 3:
            return False
    
        r, s = 0, n - 1

        while s % 2 == 0:
            r += 1
            s //= 2

        a = random.randint(2, n - 2)

        x = pow(a,s,n)

        if x == 1 or x == n - 1:
            return True
        
        for _ in range(r-1):
            x = pow(x,2,n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
        
        return True
    
    
    
    
    
    
    
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

            if (N - 1) == 1 or (N - 1) == -1:
                found = True
            
        
        if (N - 1) == -1:
            return True

        return False
    
            




        


    

rabin_miller = RabinMiller()
print(rabin_miller.is_prime(547381))

    





    

