from encoding_object import encoding_object

import string

from random import randint


class CustomEncoding:
    def __init__(self):
        self._ru_abc = 'абвгдеёжизийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self._numbers = string.digits
        self._punctuation_marks = string.punctuation

        self._valid_characters = self._ru_abc + self._numbers + self._punctuation_marks + ' \n\t'

        self._encoding_object = encoding_object
        if not self._encoding_object:
            self.generate_encoding_object()
            print(f'{self._encoding_object = }')

        self._reversed_encoding_object = {v: k for k, v in self._encoding_object.items()}

    def generate_encoding_object(self):
        used_values = []
        for char in self._valid_characters:

            num_representation = randint(100, 999)

            while num_representation in used_values or '0' in str(num_representation):
                num_representation = randint(100, 999)

            used_values.append(num_representation)
            encoded_char = str(num_representation)

            self._encoding_object[char] = encoded_char

    def encode_string(self, input_text):
        result_text = ''

        for char in input_text:
            result_text += self._encoding_object[char]

        return result_text

    def decode_string(self, input_text):
        result_text = ''
        for i in range(0, len(input_text), 3):
            result_text += self._reversed_encoding_object[input_text[i:i + 3]]

        return result_text

    def encode_char(self, input_char) -> str:
        return self._encoding_object[input_char]

    def decode_char(self, input_char) -> str:
        return self._reversed_encoding_object[input_char]


if __name__ == '__main__':
    entity = CustomEncoding()