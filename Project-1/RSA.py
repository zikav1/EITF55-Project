from RabinMiller import RabinMiller



file_path = '512.txt'

def generate_primes(file_path):
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            print(int(line.strip()).bit_length())
            line = file.readline()
        

        














    
        