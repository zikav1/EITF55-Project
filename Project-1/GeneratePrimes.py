from RabinMiller import RabinMiller
import random

def generate_bits(num, rm):
    s = set()

    while len(s) < 100:
        big_int = random.getrandbits(num)
        if rm.is_prime(big_int) == 'ProbablyPrime':
            s.add(big_int)

    return s

def write_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

rm = RabinMiller()
generated_numbers = generate_bits(512, rm)
print(generate_bits(512, rm))

write_to_file(generated_numbers, '512bits.txt')






