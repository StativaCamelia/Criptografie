import random
import time
from decimal import Decimal
from Crypto.Util import number

prime1 = number.getPrime(512)
prime2 = number.getPrime(512)


def generate_key_pair():
    n = prime1 * prime2
    tot = (prime1 - 1) * (prime2 - 1)
    while True:
        e = random.randrange(2, n)
        if number.GCD(e, tot) == 1:
            break
    d = number.inverse(e, tot)
    return (e, n), (d, n)


def generate_vulnerable_key():
    n = prime1 * prime2
    tot = (prime1 - 1) * (prime2 - 1)
    ok_d = False
    while not ok_d:
        d = random.randrange(2, 2 ** 32)
        if number.GCD(d, tot) == 1 and 36 * pow(d, 4) < n:
            ok_d = True
    e = number.inverse(d, tot)
    return (e, n), (d, n)


def encrypt(public_key, plaintext):
    e = public_key[0]
    n = public_key[1]
    return pow(plaintext, e, n)


def decrypt(public_key, cryptext):
    start_time = time.time()
    n = public_key[1]
    d = public_key[0]
    print("Timp de executie decriptare normala:")
    result = pow(cryptext, d, n)
    print(time.time() - start_time)
    return result


def decrypt_with_CRT(d, c, p, q):
    start_time = time.time()
    dP = d % (p - 1)
    dQ = d % (q - 1)
    qINV = number.inverse(q, p)
    m1 = pow(c, dP, p)
    m2 = pow(c, dQ, q)
    h = qINV * (m1 - m2) % p
    print("Timp executie decriptare CRT:")
    print(time.time() - start_time)
    return m2 + h * q % (p * q)


def associated_continue_fraction(e, n):
    rest = e // n
    fraction = [rest]
    while rest * n != e:
        e,n = n, e - rest * n
        rest = e // n
        fraction.append(rest)
    return fraction


def associated_rational_fraction(frac):
    if len(frac) == 0:
        return 0, 1
    x = frac[-1]
    y = 1
    for i in range(-2, -len(frac) - 1, -1):
        x, y = frac[i] * x + y, x
    return x, y


def conv_from_continue_fraction(frac):
    c = [];
    for i in range(len(frac)):
        c.append(associated_rational_fraction(frac[0:i]))
    return c


def square(n):
    if n == 0:
        return 0
    a, b = divmod(number.size(n), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def perfect_square(n):
    h = n & 0xF;
    if h > 9:
        return -1
    if h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8:
        t = square(n)
        if t * t == n:
            return t
        else:
            return -1
    return -1


def wiener_attack(pK):
    e = pK[0]
    n = pK[1]
    continue_fraction = associated_continue_fraction(e, n)
    conv = conv_from_continue_fraction(continue_fraction)
    for (x, d) in conv:
        if x != 0 and (e * d - 1) % x == 0:
            tot = (e*d - 1) // x
            s = n - tot + 1
            delta = s**2 - 4*n
            if delta >= 0:
                t = perfect_square(delta)
                if (s + t) % 2 == 0 and t != -1:
                    return d


if __name__ == '__main__':
    public_key, private_key = generate_key_pair()
    plaintext = 123
    cryptoText = encrypt(public_key, plaintext)
    print(cryptoText)
    decryptText = decrypt(private_key, cryptoText)
    print(decryptText)
    print(decrypt_with_CRT(private_key[0], cryptoText, prime1, prime2))

    vul_public_key, vul_private_key = generate_vulnerable_key()
    print('Vulnerable Key:')
    print(vul_private_key[0])
    print('Key Found by Wiener Attack:')
    print(wiener_attack(vul_public_key))





