import click
# -*- coding: utf-8 -*-
"""Импортируем библиотеку click для работы с командной строкой"""

class Caesar:
    def encrypt(self, plaintext, key):
        """
        Шифрование текста алгоритмом Цезаря (английский алфавит).

        :param plaintext: Открытый текст.
        :param key: Ключ (сдвиг).
        :return: Зашифрованный текст.
        """
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

    def decipher(self, ciphertext, key):
        """
        Дешифрует английский текст, зашифрованный методом Цезаря, используя заданный ключ.

        :param ciphertext: str
            Зашифрованный текст, который необходимо дешифровать.
        :param key: int
            Ключ, который использовался при шифровании, и который теперь будет использован для дешифрования.

        :return: str
            Дешифрованный текст.
        """
        return self.encrypt(ciphertext, -key)

    def crack(self, ciphertext):
        """
        Пытается взломать и дешифровать английский текст, зашифрованный методом Цезаря, без знания ключа.

        :param ciphertext: str
            Зашифрованный текст, который необходимо взломать и дешифровать.

        :return: str
            Дешифрованный текст или сообщение, что текст был расшифрован.
        """

        # Частоты букв в английском языке
        english_freqs = {
            'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253,
            'E': 0.12702, 'F': 0.02228, 'G': 0.02015, 'H': 0.06094,
            'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025,
            'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929,
            'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
            'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150,
            'Y': 0.01974, 'Z': 0.00074
        }

        cipher_freqs = {}
        for letter in ciphertext:
            if letter.upper() in english_freqs:
                if letter.upper() in cipher_freqs:
                    cipher_freqs[letter.upper()] += 1
                else:
                    cipher_freqs[letter.upper()] = 1

        most_freq_cipherletter = max(cipher_freqs, key=cipher_freqs.get)
        likely_key = ord(most_freq_cipherletter) - ord('E')
        deciphered_text = self.decipher(ciphertext, likely_key)

        return deciphered_text


class Vigenere:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.length = len(self.alphabet)

    def shift(self, char, key_char, direction=1):
        """
        Сдвигает заданный символ на позицию, определенную ключевым символом, в зависимости от заданного направления.

        :param char: str
            Символ из входного текста, который необходимо сдвинуть.
        :param key_char: str
            Ключевой символ, который определяет, на сколько позиций следует сдвинуть входной символ.
        :param direction: int, optional (default=1)
            Направление сдвига. Значение 1 означает шифрование, а значение -1 - дешифрование.

        :return: str
            Сдвинутый символ. Если входной символ не в алфавите, возвращает исходный символ без изменений.
        """
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

    def encrypt(self, plaintext, key):
        """
        Шифрование текста алгоритмом Виженера (английский алфавит).

        :param plaintext: Открытый текст.
        :param key: Ключевое слово.
        :return: Зашифрованный текст.
        """
        ciphertext = ''
        key_length = len(key)

        for i, char in enumerate(plaintext):
            key_char = key[i % key_length]
            ciphertext += self.shift(char, key_char, direction=1)

        return ciphertext

    def decipher(self, ciphertext, key):
        """
        Расшифровывает текст, используя алгоритм Виженера.

        :param ciphertext: str
            Зашифрованный текст, который необходимо расшифровать.
        :param key: str
            Ключ шифрования, используемый для расшифровки текста.

        :return: str
            Расшифрованный текст.
        """
        plaintext = ''
        key_length = len(key)

        for i, char in enumerate(ciphertext):
            key_char = key[i % key_length]
            plaintext += self.shift(char, key_char, direction=-1)

        return plaintext


class Vernam:
    """
    Инициализация алгоритма Виженера.
    """
    def encrypt(self, plaintext, key):
        """
        Шифрование текста алгоритмом Вернама (английский алфавит).

        :param plaintext: Открытый текст.
        :param key: Ключ (должен быть такой же длины, что и текст).
        :return: Зашифрованный текст.
        """
        if len(plaintext) != len(key):
            raise ValueError("Key and plaintext must be of the same length")
        ciphertext = ''
        for i in range(len(plaintext)):
            if plaintext[i].isupper():
                offset = ord('A')
            else:
                offset = ord('a')

            xor_result = (ord(plaintext[i]) - offset) ^ (ord(key[i]) - offset)
            xor_result = (xor_result % 26) + offset
            ciphertext += chr(xor_result)
        return ciphertext

    def decipher(self, ciphertext, key):
        """
        Расшифровывает текст, используя алгоритм Вернама.

        :param ciphertext: str
            Зашифрованный текст, который необходимо расшифровать.
        :param key: str
            Ключ шифрования одинаковой длины с текстом, используемый для расшифровки.

        :return: str
            Расшифрованный текст.

        :raises ValueError:
            Если длина ключа и длина текста не совпадают.
        """
        if len(ciphertext) != len(key):
            raise ValueError("Key and ciphertext must be of the same length")

        plaintext = ''
        for i in range(len(ciphertext)):
            if ciphertext[i].isupper():
                offset = ord('A')
            else:
                offset = ord('a')

            xor_result = (ord(ciphertext[i]) - offset) ^ (ord(key[i]) - offset)
            xor_result = (xor_result % 26) + offset
            plaintext += chr(xor_result)

        return plaintext



import click

@click.group()
def cli():
    """
    Основная группа команд для работы с шифровальщиками.
    """
    pass

@cli.command()
@click.argument('mode')
@click.argument('filepath')
@click.argument('key', required=False, default=None)
def operate(mode, filepath, key):
    """
    Операция шифрования и дешифрования в зависимости от выбранного режима.

    :param mode: Режим операции (например, "caesar-encrypt").
    :param filepath: Путь к файлу с текстом.
    :param key: Ключ или ключевое слово. Необязательный для некоторых режимов.
    """
    with open(filepath, 'r') as file:
        text = file.read()
    if mode == 'caesar-encrypt':
        caesar = Caesar()
        result = caesar.encrypt(text, int(key))
    elif mode == 'caesar-decipher':
        caesar = Caesar()
        result = caesar.decipher(text, int(key))
    elif mode == 'caesar-crack':
        caesar = Caesar()
        result = caesar.crack(text)
    elif mode == 'vigenere-encrypt':
        vigenere = Vigenere()
        result = vigenere.encrypt(text, key)
    elif mode == 'vigenere-decipher':
        vigenere = Vigenere()
        result = vigenere.decipher(text, key)
    elif mode == 'vernam-encrypt':
        vernam = Vernam()
        result = vernam.encrypt(text, key)
    elif mode == 'vernam-decipher':
        vernam = Vernam()
        result = vernam.decipher(text, key)
    else:
        result = "Invalid mode"
    print(result)
    

if __name__ == '__main__':
    cli()
