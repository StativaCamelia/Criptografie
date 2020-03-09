from random import randrange
MAX_LENGTH = 20

alphabet = []
english_frequences = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
key = []


def new_letter_shift(letter, key_j):
    return chr((ord(letter) - ord('a') + key_j) % 26 + ord('a'))


def new_letter_deshift(letter, key_j):
    return chr((ord(letter) - ord('a') - key_j) % 26 + ord('a'))


def filtrare_text(plaintext):
    new_text = []
    for character in plaintext:
        if character.isalpha():
            new_text.append(character.lower())
    return ''.join(new_text)


def criptare(plaintext):
    crypto_text = []
    j = 0
    for index, letter in enumerate(plaintext):
        if index % len(key) == 0:
            j = 0
            crypto_text.append(new_letter_shift(letter, key[j]))
        else:
            j = j + 1
            crypto_text.append(new_letter_shift(letter, key[j]))
    print("TEXTUL CRIPTAT:\n")
    print(''.join(crypto_text))
    return crypto_text


def decriptare(cript_text):
    original_text = []
    j = 0
    for index, letter in enumerate(cript_text):
        if index % len(key) == 0:
            j = 0
            original_text.append(new_letter_deshift(letter, key[j]))
        else:
            j = j + 1
            original_text.append(new_letter_deshift(letter, key[j]))
    print("TEXTUL DECRIPTAT:\n")
    print(''.join(original_text))
    return original_text


def frequecy_of_letter(text, letter):
    return text.count(letter)


def calculate_ic(text):
    freq = 0.0
    lenght = float(len(text))
    for letter in alphabet:
        freq += frequecy_of_letter(text, letter) * (frequecy_of_letter(text, letter) - 1)
    ic = freq/(lenght*(lenght-1))
    return ic


def key_lenght(text):
    possible_key_len = 1
    while True:
        ic_sum = 0.0
        avg_ic = 0.0
        for key_len in range(possible_key_len):
            sequence = ""
            #formare subsiruri
            for j in range(0, len(text[key_len:]), possible_key_len):
                sequence += text[key_len + j]
            # suma totala + indicele de incidenta al subsirului
            ic_sum += calculate_ic(sequence)
            #daca dimensinuea key nu este 0 calculam indicele mediu de incidenta ca fiindca indicele total / dimensiune cheie
        if not possible_key_len == 0:
            avg_ic = ic_sum / possible_key_len
            #verificam daca indicele de incidenta este cuprins intre valorile normale(daca toate sunt aproximativ 0.065 atunci suma tuturor impartita
            # la cate subsiruri sunt ar trebui sa fie tot aproximativ 0.06)
        if 0.063 < avg_ic < 0.07:
            key_maxim = possible_key_len
            return key_maxim
            #verificam pana la dimensiunea maxima de 30
        elif possible_key_len < 30:
            possible_key_len += 1
        else:
            break
    #daca nu am gasit o dimensiune e posibil ca textul sa fie prea scurt
    print("Textul nu este sufiect de lung")


def possible_letter(sequence_of_cryptotext):
    freq_compared_all_letters = [0] * 26
    mini = 1000
    for letter_to_shift in range(26):
        freq_in_seq = [0] * 26
        freq_compared_one_letter = 0.0
        #deshiftam primul subsir cu fiecare litera din alfabet
        new_sequence_list = [new_letter_deshift(sequence_of_cryptotext[j], letter_to_shift) for j in range(len(sequence_of_cryptotext))]
        #frecventa in secventa
        for letter in new_sequence_list:
            freq_in_seq[ord(letter) - ord('a')] += 1
        #procentele frecventelor literelor in subsecventa
        for letter1 in range(0,26):
            freq_in_seq[letter1] *= (1.0/float(len(sequence_of_cryptotext)))
        for letter2 in range(0,26):
            #deviatia standard a acestei variante de shiftare
            freq_compared_one_letter += ((freq_in_seq[letter2] - float(english_frequences[letter2])) ** 2) / float(english_frequences[letter2])
        #alegem litera pentru care deviatia standard este cea mai mica
        if freq_compared_one_letter < mini:
            mini = freq_compared_one_letter
            index = letter_to_shift
    #returnez aceea litera care are cea mai mica diferenta intre frecvente si frecventele din limba engleza
    return chr(index + ord('a'))


def get_key(text, key_len):
    key = [] * key_len
    for i in range(key_len):
        sequence=""
        #secventa asupra careia se aplica elementul din cheie pe care incercam sa il aflam la momentul actual
        for j in range(0,len(text[i:]), key_len):
            sequence+=text[i+j]
        key.append(possible_letter(sequence))
    return key


if __name__ == '__main__':
    alpha = 'a'
    key_dimension = 3
    key = []
    #creare alfabet
    for i in range(0, 26):
        alphabet.append(alpha)
        alpha = chr(ord(alpha) + 1)
    #Textul care trebuie criptat  filtrare
    plain_text = input("Enter the word you want to crypt:")
    plain_text = filtrare_text(plain_text)
    #generare random de cheie
    answer = input("Doriti sa generati random o cheie(RANDOM) sau sa introduceti o cheie de la tastatura(INSERT)?:")
    if answer.upper() == "RANDOM":
        for i in range(0, key_dimension):
            key.append(ord(alphabet[randrange(len(alphabet))]) - ord('a'))
    elif answer.upper() == "INSERT":
        print("Introduceti literele din care este formata cheia:")
        key_read = input();
        key_dimension = len(key_read)
        for letter in key_read:
            key.append(ord(letter) - ord('a'))
    else:
        print("Introduceti insert sau random")
    #cheie cu care se face criptarea
    print("CHEIA ESTE:")
    key_letter = [chr(key_j + ord('a')) for key_j in key]
    print(key_letter)
    #criptarea textului
    text_criptat = criptare(plain_text)
    #determinare dimensiune cheie
    key_dimension = key_lenght(text_criptat)
    print("LUNGIMEA CHEII AR PUTEA FI:" + str(key_dimension))
    #determinare componentei cheii
    print("CHEIA DETERMINATA AR PUTEA FI:")
    key = get_key(text_criptat, key_dimension)
    print(key)
    key = [ord(key_j) - ord('a') for key_j in key]
    print(key)
    decriptare(text_criptat)
