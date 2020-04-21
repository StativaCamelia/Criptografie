import random
import sympy
import sys
import time

x = 3*10**2
y = 4*10**2


def next_usable_prime(x):
    p = sympy.nextprime(x)
    while p % 4 != 3:
        p = sympy.nextprime(x)
    return p


def get_n():
    return next_usable_prime(x) * next_usable_prime(y)


def get_seed(modul):
    return random.randint(2, modul - 1)


def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        return 0
    t = 1
    if a < 0:
        a = -a
        if n % 4 == 3:
            t = -t
    a /= 2
    r = n % 8
    if r == 3 or r == 5:
        t = -t
    while a % 2 == 0:
        a /= 2
        r = n % 8
        if r == 3 or r == 5:
            t = -t
    a, n = n, a
    if a % 4 == n % 4 == 3:
        t = -t
    a %= n
    while a != 0:
        a /= 2
        r = n % 8
        if r == 3 or r == 5:
            t = -t
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0


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
    sys.setrecursionlimit(300000)
    #GENERATOR 1
    print("BBS")
    for _ in range(20):
        modul = 3004678071438487542754278090603102760455239497070791305959356857237130152659177687616920816410297584481112484604895834294779025657776976947676329563678427340358075645052676950187011222573760731244234632308110108757364277475414855268283244688127811019866481407895554126765887677452071762857308074568584043881
        start_time = time.time()
        seed = get_seed(modul)
        outputBits = ''
        out = ''
        for bit in range(16):
            outputBits += str((((seed+bit)**2)%modul)%2)
            seed = ((seed+bit)**2)%modul
        print(outputBits)
        print("Diferentea biti:")
        test(outputBits)
        print("Durata executie:")
        print(time.time() - start_time)
        print("-----------------")
    #GENERATOR2
    modul = 3004678071438487542754278090603102760455239497070791305959356857237130152659177687616920816410297584481112484604895834294779025657776976947676329563678427340358075645052676950187011222573760731244234632308110108757364277475414855268283244688127811019866481407895554126765887677452071762857308074568584043881
    seed = get_seed(modul)
    outputBits = ''
    out = ''
    for bit in range(16):
        outputBits += str((jacobi(seed+bit, modul) + 1) % 2)
        seed = (jacobi(seed+bit, modul) + 1) % 2
    print(outputBits)
    test(outputBits)








