import random
import string
import cryptography
from colorama import Fore,Style

from cryptography.fernet import Fernet

plain_text=input(Fore.GREEN + "Enter text to encrypt: "+ Fore.YELLOW)
plain_text=plain_text.encode()
key=Fernet.generate_key()

print(Fore.GREEN + "Save this key for decrypting the message: " + Fore.RED)

print(key)

f_obj=Fernet(key)

cipher_text=f_obj.encrypt(plain_text)
print(Fore.GREEN + "\nEncrypted text : "+ Fore.YELLOW)
print(cipher_text)


