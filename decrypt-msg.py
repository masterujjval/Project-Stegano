import random
import string
import cryptography
from colorama import Fore,Style

from cryptography.fernet import Fernet

enc_msg=input(Fore.GREEN + "Enter the Encrypted message: "+ Fore.YELLOW)
f_obj=input(Fore.RED + "\nEnter the key: "+ Fore.GREEN)

#encoding to string to bytes
print(Fore.RED)
test_msg=enc_msg.encode('utf-32')

test_key=f_obj.encode('utf-32')
test_key=Fernet(f_obj)



de_msg=test_key.decrypt(test_msg)

print(de_msg)



