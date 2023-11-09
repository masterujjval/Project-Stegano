import random
import string
import cryptography

from cryptography.fernet import Fernet

enc_msg=input("Enter the Encrypted message: ")
f_obj=input("Enter the key: ")

#encoding to string to bytes
test_msg=enc_msg.encode('utf-32')

test_key=f_obj.encode('utf-32')
test_key=Fernet(f_obj)



de_msg=test_key.decrypt(test_msg)
print(de_msg)



