from cryptography.fernet import Fernet
#bottom code used to generate key
key = Fernet.generate_key()

def genKey():
    with open('myKey.key', 'wb') as mykey:
        mykey.write(key)

def showKey():
    with open('myKey.key', 'rb') as mykey:
        key = mykey.read()
        print(key)