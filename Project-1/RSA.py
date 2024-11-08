from Euclidean import Euclidean
import random

def generate_primes(file_path):
    with open(file_path, 'r') as file:
        p = int(file.readline().strip())
        q = int(file.readline().strip())
    
    return (p, q)




eu = Euclidean()
p, q = generate_primes('512.txt') # our p and q
N = p * q
phi_n = (p - 1)*(q - 1)
e = (2**16) + 1
d = eu.inverse_mod(e, phi_n)



#print(f'D-value: {d}')


s = random.randint(2, N - 1) 
print(f'S value: {s}')

c = pow(s, e, N)
print(f'Crypted: {c}')

z = pow(c, d, N) 
print(f'Decrypted: {z}')

print(z == s)







        

        














    
        