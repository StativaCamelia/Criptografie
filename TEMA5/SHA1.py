
def prepocesare(message):
    # transform mesajul in binar

    bytes_text = ''.join(['{0:08b}'.format(ord(i)) for i in message])
    pad_bits = bytes_text + "1"
    lenght = len(pad_bits)
    while len(pad_bits)%512 != 448:
        pad_bits += "0"
    #adauga dimensiunea mesajului ca 64 de bits(big-endian)
    pad_bits += '{0:064b}'.format(lenght - 1 )
    return pad_bits

def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def left_rotate(bytes, rotation):
    return ((bytes << rotation) | (bytes >> (32 - rotation))) & 0xffffffff


def sha_1(message):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    message = prepocesare(message)
    print(message)
    for chunk in chunks(message, 512):
        #vom avea 16 cuvinte
        sub_chunks = chunks(chunk, 32)
        #o sa formam 80 de cuvinte astfel primele 16 sunt cele deja formate:
        w = [0] * 80
        for i in range(0,80):
            if i < 16:
                w[i] = int(sub_chunks[i],2)
            else:
                w[i] = left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(0,80):
            if 0 <= i  and  i<=19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i and i<=39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i and i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i and i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = left_rotate(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = left_rotate(b,30)
            b = a
            a = temp
            # if(i == 1):
            #     print(a)
            #     print(b)
            #     print(c)
            #     print(d)
            #     print(e)


        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


if __name__ == '__main__':
    print(sha_1("The quick brown fox jumps over the lazy dog"))
