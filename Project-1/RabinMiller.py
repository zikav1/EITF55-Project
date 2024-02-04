import random
import time

class RabinMiller:

    def is_prime(self, n):
        if n % 2 == 0 or n < 3:
            return False
        
        r, s = 0, n - 1

        while s % 2 == 0:
            r += 1
            s //= 2

        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        print(a)

        if x == 1 or x == n - 1:
            return True
        
        for j in range(1,r):
            x = pow(x,2,n)
            #x = pow(a, pow(2, j) * s, n)
            if x == 1:
                return False
            if x == n - 1:
                return True 
        return False


        
        



rabin_miller = RabinMiller()


with open('RabinMillerTest.txt', 'w') as file:
    for _ in range(20):
        file.write(str(rabin_miller.is_prime(131)) + '\n')






    

