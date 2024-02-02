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
num = 10030675549058353995577208533577693916287926200584875181994125673837052015084928831492062318871846994547511415083961253112583312762813635810053795131173219
print(rabin_miller.is_prime(num))




    

