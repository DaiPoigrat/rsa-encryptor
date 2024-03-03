import string
import sys

from ss_test import is_simple
from abc_encoding import CustomEncoding

from random import randrange
from math import gcd


class RSAEncryptor(CustomEncoding):
    def __init__(self):
        super().__init__()
        self.opened_text_path = 'files/text.txt'
        self.encrypted_text_path = 'files/encrypted_text.txt'
        self.decrypted_text_path = 'files/decrypted_text.txt'

        self.public_key_path = 'files/public.txt'
        self.private_key_path = 'files/private.txt'

    def generate_keypair(self, bit_length: int = 12):
        k = 100

        p = int(input('Введите простое число p: '))
        q = int(input('Введите простое число q: '))

        while not is_simple(p, k):
            p = int(input('Введите простое число p: '))

        while not is_simple(q, k) or q == p:
            q = int(input('Введите простое число q: '))

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

    @staticmethod
    def _create_chunks(input_string, n: int) -> list:
        chunks = []
        current_chunk = ''

        chunk_length = len(str(n))

        for index, char in enumerate(input_string):
            current_chunk += char
            current_chunk_value = int(current_chunk)

            if current_chunk_value >= n or len(current_chunk) > chunk_length:
                chunks.append(current_chunk[:len(current_chunk) - 1])
                current_chunk = char

            if index == len(input_string) - 1 and current_chunk != chunks[-1]:
                chunks.append(current_chunk)

        return chunks

    def encrypt(self):
        with open(self.opened_text_path, 'r', encoding='utf-8') as file:
            text = ''.join(file.readlines())

            if not text:
                # no text.txt message
                print(f'Нет текста для шифрования')
                sys.exit()

            print('открытый текст:')
            print(text)

            filtered_text = ''
            for letter in text:
                if letter.lower() in self._valid_characters:
                    filtered_text += letter.lower()

            print('отфильтрованный текст:')
            print(filtered_text)

        with open(self.public_key_path, 'r', encoding='utf-8') as file:
            try:
                e, n = file.readlines()
                e = int(e)
                chunk_length = len(n)
                n = int(n)
                # записываем символы численным представлением
                encrypted_text = ''.join([self.encode_char(char) for char in filtered_text])
                print('кастомная кодировка:')
                print(encrypted_text)
                # выбираем чанки, чтобы были меньше n
                chunks = self._create_chunks(input_string=encrypted_text, n=n)
                print('деление на чанки:')
                print(chunks)
                encrypted_chunks = [str(pow(int(char), e, n)).zfill(chunk_length) for char in chunks]
                print('зашифрованные чанки:')
                print(encrypted_chunks)

            except Exception as e:
                print(f'Ошибка чтения public key')
                sys.exit()

        with open(self.encrypted_text_path, 'w', encoding='utf-8') as file:
            file.write(''.join(encrypted_chunks))
            print(f'Зашифрованный текст')
            print(''.join(encrypted_chunks))

    def decrypt(self):
        with open(self.encrypted_text_path, 'r', encoding='utf-8') as file:
            encrypted_text = file.read()

            if not encrypted_text:
                # no encrypted_text.txt message
                print(f'Нет текста для дешифрования')
                sys.exit()

            print('текст для расшифрования:')
            print(encrypted_text)

        with open(self.private_key_path, 'r', encoding='utf-8') as file:
            try:
                d, n = file.readlines()
                d = int(d)
                n = int(n)

                chunks = self._create_chunks(input_string=encrypted_text, n=n)
                print('текст для расшифрования разбили на чанки:')
                print(chunks)
                decrypted_chunks = [str(pow(int(char), d, n)) for char in chunks]
                print('расшифровали чанки:')
                print(decrypted_chunks)
                prepared_text = ''.join(decrypted_chunks)
                decrypted_text = self.decode_string(input_text=prepared_text)

            except Exception as e:
                print(f'Ошибка чтения pivate key')
                print(e)
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
