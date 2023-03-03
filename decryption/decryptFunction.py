from cryptography.fernet import Fernet

with open('myKey.key', 'rb') as mykey:
    key = mykey.read()

def decFile():
    f = Fernet(key)
    with open('encrypted_topsecret.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open('decrypted_topsecret.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)