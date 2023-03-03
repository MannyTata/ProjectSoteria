from cryptography.fernet import Fernet
welcomeMsg = "Hello User, welcome to Soteria. What task do you want to accomplish?\n 'e' for encryption\n 'd' for encryption\n 'k' to generate key\n 'show' to show key\n or type 'end' to close out of the program."

def findKey():
    with open('myKey.key', 'rb') as mykey:
        key = mykey.read()
