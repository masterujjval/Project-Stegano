import random
import string
import cryptography
from colorama import Fore,Style
from cryptography.fernet import Fernet
import os.path
from os import path
import sys
import os
from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint


os.system('cls' if os.name == 'nt' else 'clear')
cprint(figlet_format('End to End Encryption Tool', font='starwars'), 'yellow', attrs=['bold'])


plain_text=input(Fore.GREEN + "Enter text to encrypt: "+ Fore.YELLOW)
plain_text=plain_text.encode()
key=Fernet.generate_key()

print(Fore.GREEN + "Save this key for decrypting the message: " + Fore.RED)

print(key)

f_obj=Fernet(key)

cipher_text=f_obj.encrypt(plain_text)
print(Fore.GREEN + "\nEncrypted text : "+ Fore.YELLOW)
print(cipher_text)


