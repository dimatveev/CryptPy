import click
# -*- coding: utf-8 -*-


class Caesar:
    def encrypt_eng(self, plaintext, key):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                shift = key % 26
                if char.islower():
                    char_code = ord(char) + shift
                    if char_code > ord('z'):
                        char_code -= 26
                elif char.isupper():
                    char_code = ord(char) + shift
                    if char_code > ord('Z'):
                        char_code -= 26
                ciphertext += chr(char_code)
            else:
                ciphertext += char
        return ciphertext

    def encrypt_rus(self, plaintext, key):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                shift = key % 26
                if char.islower():
                    char_code = ord(char) + shift
                    if char_code > ord('z'):
                        char_code -= 26
                elif char.isupper():
                    char_code = ord(char) + shift
                    if char_code > ord('Z'):
                        char_code -= 26
                ciphertext += chr(char_code)
            else:
                ciphertext += char
        return ciphertext

    def decipher_eng(self, ciphertext, key):
        return self.encrypt_eng(ciphertext, -key)

    def decipher_rus(self, ciphertext, key):
        return self.encrypt_rus(ciphertext, -key)


    def hack(self, ciphertext):
        # hack
        return "Deciphered text"


class Vigenere:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.length = len(self.alphabet)

    def shift(self, char, key_char, direction=1):
        if char.upper() in self.alphabet:
            char_idx = self.alphabet.index(char.upper())
            key_char_idx = self.alphabet.index(key_char.upper())

            new_idx = (char_idx + direction * key_char_idx) % self.length

            if char.isupper():
                return self.alphabet[new_idx]
            else:
                return self.alphabet[new_idx].lower()
        else:
            return char

    def encrypt_eng(self, plaintext, key):
        ciphertext = ''
        key_length = len(key)

        for i, char in enumerate(plaintext):
            key_char = key[i % key_length]
            ciphertext += self.shift(char, key_char, direction=1)

        return ciphertext

    def decipher_eng(self, ciphertext, key):
        plaintext = ''
        key_length = len(key)

        for i, char in enumerate(ciphertext):
            key_char = key[i % key_length]
            plaintext += self.shift(char, key_char, direction=-1)

        return plaintext


class Vernam:
    def encrypt_eng(self, plaintext, key):
        pass
        return "Encrypted text"

    def decipher_eng(self, ciphertext, key):
        pass
        return "Deciphered text"

@click.group()
def cli():
    pass

@cli.command()
@click.argument('mode')
@click.argument('filepath')
@click.argument('key')
def operate(mode, filepath, key):
    """Operate function for encryption and decryption."""
    with open(filepath, 'r') as file:
        text = file.read()
    if mode == 'caesar-encrypt_eng':
        caesar = Caesar()
        result = caesar.encrypt_eng(text, int(key))
    elif mode == 'caesar-decipher_eng':
        caesar = Caesar()
        result = caesar.decipher_eng(text, int(key))
    elif mode == 'caesar-encrypt_rus':
        caesar = Caesar()
        result = caesar.decipher_rus(text, int(key))
    elif mode == 'caesar-decipher_rus':
        caesar = Caesar()
        result = caesar.decipher_rus(text, int(key))
    elif mode == 'caesar-hack':
        caesar = Caesar()
        result = caesar.hack(text)
    elif mode == 'vigenere-encrypt_eng':
        vigenere = Vigenere()
        result = vigenere.encrypt_eng(text, key)
    elif mode == 'vigenere-decipher_eng':
        vigenere = Vigenere()
        result = vigenere.decipher_eng(text, key)
    else:
        result = "Invalid mode"
    print(result)


if __name__ == '__main__':
    cli()
