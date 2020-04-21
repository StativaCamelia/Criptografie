import time
import random

def random_bistring():
    bitList = []
    for i in range(0, 32):
        x = str(random.randint(0, 1))
        bitList.append(x)
    bitString = ''.join(bitList)
    return bitString

def get_bit_mask():
    primitive_equation = ''
    for i in range(32):
        if i==32 or i==28 or i==27 or i==1:
            primitive_equation += '1'
        else:
            primitive_equation += '0'
    return primitive_equation


def lsfr(seed, mask_binary):
    random_num = ""
    for _ in range(16):
        sum = 0
        for bits_mask, bits_seed in zip(mask_binary, seed):
            if bits_mask == '1':
                sum += int(bits_seed)
        feedback = sum % 2
        seed_int=int(seed,2)
        seed = (seed_int>>1)
        seed = bin(seed)[2:].zfill(32)
        seed_list = list(seed)
        seed_list[0] = str(feedback)
        seed = "".join(seed_list)
        random_num += str(feedback)
    return random_num


def test(bytes):
    zero = 0
    unu = 0;
    for byte in bytes:
        if byte == '0':
            zero = zero+1
        else:
            unu = unu +1
    print(abs(zero-unu))


if __name__ == '__main__':
    print("LSFR")
    mask_binary = ''
    for _ in range(20):
        start_time = time.time()
        seed = random_bistring()
        mask_binary = get_bit_mask()
        print(lsfr(seed, mask_binary))
        print("Diferenta BITI:")
        test(lsfr(seed, mask_binary))
        print("Durata executie:")
        print(time.time()- start_time)
        print("------------------")
