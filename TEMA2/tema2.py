import random
import sympy
import sys

x = 3*10**10
y = 4*10**10

#MILLER - RABIT PRIME CHECKER
def isPrime(n, k = 2):
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2
    for i in range(k):
        x = pow(int(random.randint(2, n-1)),int(d), n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True


def findGoodPrime(numBits=512):
    candidate = 1
    while not goodPrime(candidate):
        candidate = random.getrandbits(numBits)
    print(candidate)
    return candidate


def next_usable_prime(x):
    p = sympy.nextprime(x)
    while (p % 4 != 3):
        p = sympy.nextprime(x)
    return p

def getN():
    return next_usable_prime(x) * findGoodPrime(y)


def getSeed(modul):
    return random.randint(2, modul - 1)


def LSB(n):
    return sum(int(x) for x in bin(n)[2:]) % 2

def test(bytes):
    zero = 0
    unu = 0;
    for byte in bytes:
        if byte == '0':
            zero = zero+1
        else:
            unu = unu +1
    print(abs(zero-unu))


def jacobi(a, n):
    if n<=0 or n%2 == 0:
        return 0
    t = 1
    if a<0:
        a = -a
        if n%4 == 3:
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


if __name__ == '__main__':
    sys.setrecursionlimit(300000)
    #GENERATOR 1
    modul = 3004678071438487542754278090603102760455239497070791305959356857237130152659177687616920816410297584481112484604895834294779025657776976947676329563678427340358075645052676950187011222573760731244234632308110108757364277475414855268283244688127811019866481407895554126765887677452071762857308074568584043881
    seed = getSeed(modul)
    outputBits = ''
    out = ''
    for bit in range(16):
        outputBits += str((((seed+bit)**2)%modul)%2)
        seed = ((seed+bit)**2)%modul
        if len(outputBits) == 16:
            break
    print(outputBits)
    test(outputBits)

    #GENERATOR2
    modul = 3004678071438487542754278090603102760455239497070791305959356857237130152659177687616920816410297584481112484604895834294779025657776976947676329563678427340358075645052676950187011222573760731244234632308110108757364277475414855268283244688127811019866481407895554126765887677452071762857308074568584043881
    seed = getSeed(modul)
    outputBits = ''
    out = ''
    for bit in range(16):
        outputBits += str(jacobi(seed+bit, modul)%2)
        seed = jacobi(seed+bit, modul)
    print(outputBits)
    test(outputBits)








