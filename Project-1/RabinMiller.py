import random
import time

class RabinMiller:

    def __init__(self) -> None:
        pass
    
    def is_prime(self, n):
        if n % 2 == 0 or n < 3:
            return 'Composite'
    
        r, s = 0, n - 1

        while s % 2 == 0:
            r += 1
            s //= 2


        a = random.randint(2, n - 2)
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            return 'ProbablyPrime'
        
        for j in range(1,r):
            x = pow(x,2,n)
            #x = pow(a, pow(2, j) * s, n)
            if x == 1:
                return 'Composite'
            if x == n - 1:
                return 'ProbablyPrime' 
        

        return 'Composite'
    
    
    def testRM(self, n):
        s = set()
        while len(s) < 20:
            a = random.randint(2, n - 2)
            s.add(a)
        
        for x in s:
            print("for a:", x,"->", self.is_prime(n, x))

        
        



rabin_miller = RabinMiller()
print(rabin_miller.is_prime(7952236179063200785583575468150582320890553302017051109508588953564368638721538511554130642405796793727484085964896600961520842822191165644892337039288283))


num = 11790031505001488507573567744675193426550140425188920905730328214787706066493848044087640950340096388798826600818527376014629498302049779886302442083660509
print(num.bit_length())
    




    

