from ss_test import is_simple
from random import getrandbits, randrange
from math import gcd


def generate_keypair(bit_length: int = 64):
    p = 0
    q = 0
    k = 2

    while not is_simple(p, k):
        # print(f'{p = }')
        p = getrandbits(bit_length)

    while not is_simple(q, k) or q == p:
        # print(f'{q = }')
        q = getrandbits(bit_length)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = randrange(1, phi)
    while gcd(e, phi) != 1:
        e = randrange(1, phi)

    d = pow(e, -1, phi)

    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted


def decrypt(encrypted, private_key):
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted]
    return ''.join(decrypted)


if __name__ == '__main__':
    public_key, private_key = generate_keypair()
    message = "Hello, RSA!"
    print(f'{public_key = }')
    print(f'{private_key = }')

    encrypted = encrypt(message, public_key)
    print("Зашифрованное сообщение:", encrypted)

    decrypted = decrypt(encrypted, private_key)
    print("Расшифрованное сообщение:", decrypted)
