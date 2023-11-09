import random
import string
import cryptography

from cryptography.fernet import Fernet

plain_text=input("Enter text to encrypt: ")
plain_text=plain_text.encode()
key=Fernet.generate_key()

print("Save this key for decrypting the message: ")

print(key)

f_obj=Fernet(key)

cipher_text=f_obj.encrypt(plain_text)
print("Encrypted text : ")
print(cipher_text)


