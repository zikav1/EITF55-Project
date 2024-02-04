import random


class Euclidean:

    def __init__(self) -> None:
        pass

    def inverse_mod(self, a, m):
        d1 = m
        v1 = 0
        v2 = 1
        d2 = a

        while d2 != 0:
            q = d1 // d2
            t2 = v1 - (q * v2)
            t3 = d1 - (q * d2)
            
            v1 = v2
            d1 = d2
            v2 = t2
            d2 = t3

        v = v1
        d = d1

        if d != 1:
            return -1
        
        if v < 0:
            v += m
        
        return v
            

# Test for inverse_mod
# The result is in the textfile Euclidean.txt
    
with open('EuclideanResult.txt', 'w') as file:
    euclidean = Euclidean()
    for _ in range(5):
        a = random.randrange(2**511, 2**512)
        m = random.randrange(2**511, 2**512)
        
        result = euclidean.inverse_mod(a, m)
        
        # Write the formatted output to the file
        file.write(f'For a: {a}\nand m: {m}\nThe inverse mod is: {result}\n{"-" * 20}\n')





        