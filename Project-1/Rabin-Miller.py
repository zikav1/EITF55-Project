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
    
    


rabin_miller = RabinMiller()
print(rabin_miller.is_prime(14))

    





    

