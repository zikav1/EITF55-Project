from RabinMiller import RabinMiller

def generate_primes(file_path):
    with open(file_path, 'r') as file:
        p = int(file.readline().strip())
        q = int(file.readline().strip())
    
    return (p, q)


p, q = generate_primes('512.txt') # our p and q

N = p * q #N value
phi_n = (p - 1)*(q - 1)
e = (2**16) + 1






        

        














    
        