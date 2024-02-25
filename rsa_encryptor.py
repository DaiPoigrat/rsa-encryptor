import string
import sys

from ss_test import is_simple
from random import getrandbits, randrange
from math import gcd


class RSAEncryptor:
    def __init__(self):
        self.opened_text_path = 'files/text.txt'
        self.encrypted_text_path = 'files/encrypted_text.txt'
        self.decrypted_text_path = 'files/decrypted_text.txt'

        self.public_key_path = 'files/public.txt'
        self.private_key_path = 'files/private.txt'

        self._ru_abc = 'абвгдеёжизийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self._numbers = string.digits
        self._punctuation_marks = string.punctuation

        self._valid_characters = self._ru_abc + self._numbers + self._punctuation_marks + ' \n\t'

    def symbol_to_number(self):
        # все символы алфавита привести к числовому коду, который я сам придумаю
        ...

    def generate_keypair(self, bit_length: int = 64):
        p = 0
        q = 0
        k = 2

        while not is_simple(p, k):
            p = getrandbits(bit_length)

        while not is_simple(q, k) or q == p:
            q = getrandbits(bit_length)

        n = p * q
        phi = (p - 1) * (q - 1)

        e = randrange(1, phi)
        while gcd(e, phi) != 1:
            e = randrange(1, phi)

        d = pow(e, -1, phi)

        with open(self.public_key_path, 'w', encoding='utf-8') as file:
            key_pair = (str(e), '\n', str(n))
            print(f'Public key: {key_pair}')
            file.writelines(key_pair)

        with open(self.private_key_path, 'w', encoding='utf-8') as file:
            key_pair = (str(d), '\n', str(n))
            print(f'Private key: {key_pair}')
            file.writelines(key_pair)

    def encrypt(self):
        with open(self.opened_text_path, 'r', encoding='utf-8') as file:
            text = ''.join(file.readlines())

            if not text:
                # no text.txt message
                print(f'Нет текста для шифрования')
                sys.exit()

            filtered_text = ''
            for letter in text:
                if letter in self._valid_characters:
                    filtered_text += letter

        with open(self.public_key_path, 'r', encoding='utf-8') as file:
            try:
                e, n = file.readlines()
                e = int(e)
                n = int(n)
                encrypted_text = [str(pow(ord(char), e, n)) + '\n' for char in filtered_text]
            except Exception as e:
                print(f'Ошибка чтения public key')
                print(f'{e = }')
                sys.exit()

        with open(self.encrypted_text_path, 'w', encoding='utf-8') as file:
            file.writelines(encrypted_text)

    def decrypt(self):
        with open(self.encrypted_text_path, 'r', encoding='utf-8') as file:
            encrypted_text = file.readlines()

            encrypted_text = [int(char) for char in encrypted_text]

            if not encrypted_text:
                # no encrypted_text.txt message
                print(f'Нет текста для дешифрования')
                sys.exit()

        with open(self.private_key_path, 'r', encoding='utf-8') as file:
            try:
                d, n = file.readlines()
                d = int(d)
                n = int(n)
                decrypted_text = [chr(pow(char, d, n)) for char in encrypted_text]
                decrypted_text = ''.join(decrypted_text)
            except Exception as e:
                print(f'Ошибка чтения pivate key')
                sys.exit()

        with open(self.decrypted_text_path, 'w', encoding='utf-8') as file:
            file.write(decrypted_text)

        lines = decrypted_text.split('\n')
        print(f'{"-" * 30}decrypted text{"-" * 30}')
        for line in lines:
            print(line)
        print(f'{"-" * 74}')


if __name__ == '__main__':
    obj = RSAEncryptor()
    obj.encrypt()
    obj.decrypt()
