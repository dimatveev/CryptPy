import unittest
from main import Caesar, Vigenere, Vernam, Atbash, RSA


class TestCaesarEncryptionDecryption(unittest.TestCase):

    def setUp(self):
        self.caesar = Caesar()

    def test_caesar_encrypt(self):
        plaintext = "HELLO"
        key = 3
        encrypted_text = self.caesar.encrypt(plaintext, key)
        self.assertEqual(encrypted_text, "KHOOR")

    def test_caesar_decrypt(self):
        ciphertext = "KHOOR"
        key = 3
        decrypted_text = self.caesar.decipher(ciphertext, key)
        self.assertEqual(decrypted_text, "HELLO")


class TestVigenereEncryptionDecryption(unittest.TestCase):

    def setUp(self):
        self.vigenere = Vigenere()

    def test_vigenere_encrypt(self):
        plaintext = "HELLO"
        key = "KEY"
        encrypted_text = self.vigenere.encrypt(plaintext, key)
        self.assertEqual(encrypted_text, "RIJVS")

    def test_vigenere_decrypt(self):
        ciphertext = "RIJVS"
        key = "KEY"
        decrypted_text = self.vigenere.decipher(ciphertext, key)
        self.assertEqual(decrypted_text, "HELLO")


class TestVernamEncryptionDecryption(unittest.TestCase):

    def setUp(self):
        self.vernam = Vernam()

    def test_vernam_encrypt_decrypt(self):
        plaintext = "HELLO"
        key = "KEYKE"
        encrypted_text = self.vernam.encrypt(plaintext, key)
        decrypted_text = self.vernam.decipher(encrypted_text, key)
        self.assertEqual(decrypted_text, "HELLO")


class TestAtbashEncryptionDecryption(unittest.TestCase):

    def setUp(self):
        self.atbash = Atbash()

    def test_atbash_encrypt_decrypt(self):
        plaintext = "hello"
        encrypted_text = self.atbash.encrypt(plaintext)
        decrypted_text = self.atbash.decipher(encrypted_text)
        self.assertEqual(decrypted_text, "hello")


class TestRSAEncryptionDecryption(unittest.TestCase):

    def setUp(self):
        self.rsa = RSA()

    def test_rsa_encrypt_decrypt(self):
        plaintext = "HELLO"
        encrypted_text = self.rsa.encrypt(plaintext)
        decrypted_text = self.rsa.decipher(encrypted_text)
        self.assertEqual(decrypted_text, "HELLO")


if __name__ == '__main__':
    unittest.main()
