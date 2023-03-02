from cryptography.fernet import Fernet
from startup.onStart import findKey
#from encryption.getKey import 

#Commands to encrypt file
with open('myKey.key', 'rb') as mykey:
    key = mykey.read()

def encFile():
    f = Fernet(key)

    with open('topsecret.txt', 'rb') as original_file:
        original = original_file.read()


    encrypted = f.encrypt(original)

    with open('encrypted_topsecret.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    
