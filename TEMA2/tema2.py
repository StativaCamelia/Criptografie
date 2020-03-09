import random


#MILLER - RABIT PRIME CHECKER
def isPrime(n, k=5):
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2
    for i in range(k):
        x = pow(random.randint(2, n-1), d, n)
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
    return candidate


def goodPrime(p):
    return p % 4 == 3 and isPrime(p)


def getN():
    return findGoodPrime() * findGoodPrime()


def getSeed(modul):
    return random.randint(2, modul - 1)


def LSB(n):
    return sum(int(x) for x in bin(n)[2:]) % 2


if __name__ == '__main__':
    modul = getN()
    seed = getSeed(modul)
    outputBits = ''
    for bit in range(20):
        outputBits += str((seed**2)%modul)
        seed = (seed**2)%modul
        if len(outputBits) == 20:
            break
    print(outputBits)






