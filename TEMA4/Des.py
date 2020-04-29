schedule_of_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
IP = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)
IP_INV = (
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
)
PC1 = (
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
)
PC2 = (
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)

E = (
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)

Sbox = {
    0: (
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ),
    1: (
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ),
    2: (
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ),
    3: (
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ),
    4: (
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ),
    5: (
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
    ),
    6: (
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
    ),
    7: (
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
    )
}

P = (
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
)


def apply_permutation(table, key, lenght):
    #completam pana la 64 de biti
    block = bin(key)[2:].zfill(lenght)
    #permutam conform tabelei
    permutare = [block[table[_]-1] for _ in range(len(table))]
    return int(''.join(permutare), 2)


def left_shift(prev_key, rot_val):
    return (prev_key << rot_val % 28) & (2 ** 28 - 1) | ((prev_key & (2 ** 28 - 1)) >> (28 - (rot_val % 28)))


def get_round_keys(key):
    C0 = key >> 28
    D0 = key & (2 ** 28 - 1)
    round_keys = dict.fromkeys(range(1, 17))
    C1 = left_shift(C0, schedule_of_shifts[0])
    D1 = left_shift(D0, schedule_of_shifts[0])
    round_keys[1] = (C1, D1)
    i = 1
    for current_schedule in schedule_of_shifts[1:]:
        i += 1;
        Ci = left_shift(round_keys[i - 1][0], current_schedule)
        Di = left_shift(round_keys[i - 1][1], current_schedule)
        round_keys[i] = (Ci, Di)

    for i, (Ci, Di) in round_keys.items():
        round_keys[i] = apply_permutation(PC2, (Ci << 28) + Di, 56)
    return round_keys


def round_function(Ri, Ki):
    #Expandam de la 32 de bits la 48 de bits
    Ri = apply_permutation(E, Ri, 32)
    #Kn + E(Rn-1)
    Ri ^= Ki

    Ri_adresses = []
    #grupam biti in grupuri de cate 6 si fiecare grup ne ofera un bloc din Sboxes
    for adress in (42, 36, 30, 24, 18, 12, 6, 0):
        Ri_adresses.append((Ri & (0b111111 << adress)) >> adress)

    for i, block in enumerate(Ri_adresses):
        #primul si ultimul bit al blocului
        row = ((0b100000 & block) >> 4) + (0b1 & block)
        #cei 4 biti din mijloc
        col = (0b011110 & block) >> 1
        #elementul de pe linia si coloana obtinuta
        Ri_adresses[i] = Sbox[i][16 * row + col]
    Ri = 0
    for block, lshift_val in zip(Ri_adresses, (28, 24, 20, 16, 12, 8, 4, 0)):
        Ri += (block << lshift_val)
    Ri = apply_permutation(P, Ri, 32)
    return Ri

def new_keys(cript_block, decrypt = False):
    # il impartim in doua
    L0 = cript_block >> 32
    R0 = cript_block & (2 ** 32 - 1)
    Ln = L0
    Rn = R0
    if(not decrypt):
        for i in range(1, 17):
            Li = Rn
            Ri = Ln ^ round_function(Rn, round_keys[i])
            Ln = Li
            Rn = Ri
    else:
        for i in range(16, 0, -1):
            Li = Rn
            Ri = Ln ^ round_function(Rn, round_keys[i])
            Ln = Li
            Rn = Ri
    return Ri,Li


if __name__ == '__main__':
    #permutan tabela cu PC1
    key = 0b0001001100110100010101110111100110011011101111001101111111110001
    msg= 0b100100011010001010110011110001001101010111100110111101111
    key = apply_permutation(PC1, key, 64)
    print("Mesaj de criptat: "  + bin(msg)[2:].zfill(56))

    #impartit in doua si obtinem 16 blocuri shiftand la stanga blocul anterior

    #generam cheiele de runda shiftand la stanga blocul anterior
    round_keys = get_round_keys(key)

    #repetam procedeul si pentru mesaj
    cript_block = apply_permutation(IP, msg, 64)

    #Ln = Rn-1
    #Rn = Ln-1 + f(Rn-1,Kn)
    Ri,Li = new_keys(cript_block)

    #reverse keys
    cipher_block = (Ri << 32) + Li

    cipher_block = apply_permutation(IP_INV, cipher_block, 64)
    print("MESAJ CRIPTAT:")
    print(bin(cipher_block)[2:].zfill(64))

    #decriptare:
    print("DECRIPTARE")
    # permutan tabela cu PC1
    key = 0b0001001100110100010101110111100110011011101111001101111111110001
    cript = 0b1000010111101000000100110101010000001111000010101011010000000101;

    key = apply_permutation(PC1, key, 64)
    print("\nMesaj criptat: " + bin(cript)[2:].zfill(56))

    # impartit in doua si obtinem 16 blocuri shiftand la stanga blocul anterior
    # generam cheiele de runda shiftand la stanga blocul anterior
    round_keys = get_round_keys(key)

    # repetam procedeul si pentru mesaj
    cript_block = apply_permutation(IP, cript, 64)

    Ri,Li = new_keys(cript_block, True)

    decrypt = (Ri << 32) + Li
    decrypt = apply_permutation(IP_INV, decrypt, 64)

    print("MESAJ DECRIPTAT")
    print(bin(decrypt)[2:].zfill(64))