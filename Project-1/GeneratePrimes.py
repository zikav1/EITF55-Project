from RabinMiller import RabinMiller
import random
import time


def generate_bits(num, rm):
    s = set()
    start_time = time.time()

    while len(s) < 100:
        big_int = random.randrange(2**(num-1), 2**num)
        if rm.is_prime(big_int):
            s.add(big_int)

    end_time = time.time()
    print(end_time - start_time)
    return s

def write_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')




rm = RabinMiller()
generated_numbers = generate_bits(512, rm)
write_to_file(generated_numbers, '512.txt')






