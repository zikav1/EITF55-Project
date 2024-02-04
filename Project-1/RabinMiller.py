import random
import time

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
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            return True
        
        for j in range(1,r):
            x = pow(x,2,n)
            #x = pow(a, pow(2, j) * s, n)
            if x == 1:
                return False
            if x == n - 1:
                return True 
        

        return True
    
    
    def testRM(self, n):
        s = set()
        while len(s) < 20:
            a = random.randint(2, n - 2)
            s.add(a)
        
        for x in s:
            print("for a:", x,"->", self.is_prime(n, x))

        
        



rabin_miller = RabinMiller()





    

