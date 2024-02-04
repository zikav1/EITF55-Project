from RabinMiller import RabinMiller
import math

def generate_primes(file_path):
    with open(file_path, 'r') as file:
        p = int(file.readline().strip())
        q = int(file.readline().strip())
    
    return (p, q)


p, q = generate_primes('512.txt') # our p and q
N = p * q





        

        














    
        