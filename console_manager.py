from rsa_encryptor import RSAEncryptor


class ConsoleManager:
    def __init__(self):
        self.app = RSAEncryptor()

    @staticmethod
    def help():
        print(
            'Command list:\n'
            '-k | --keys                       - создает пару ключей\n'
            '-e | --encrypt -p | --path {path} - шифрует содержимое файла или файла по умолчанию\n'
            '-d | --decrypt -p | --path {path} - расшифровывает содержимое файла или файла по умолчанию\n'
            'Примеры использования:\n'
            'py program.py -e\n'
            'py program.py -e -p "C:/.../.../file.txt"\n'
            'py program.py -d\n'
        )

    def generate_keys(self):
        self.app.generate_keypair()

    def encrypt(self, arg_dict):
        if '-p' in arg_dict:
            self.app.opened_text_path = arg_dict['-p']

        if '--path' in arg_dict:
            self.app.opened_text_path = arg_dict['--path']

        self.app.encrypt()

    def decrypt(self, arg_dict):
        if '-p' in arg_dict:
            self.app.encrypted_text_path = arg_dict['-p']

        if '--path' in arg_dict:
            self.app.encrypted_text_path = arg_dict['--path']

        self.app.decrypt()
