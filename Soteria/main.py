from cryptography.fernet import Fernet
######### Above imported library remains at all times

#Early beta of terminal commands

#imports welcomeMsg contents
from startup.onStart import welcomeMsg 

#imports commands to encrypt
from encryption.encryptFunction import encFile
from encryption.makeKey import showKey, genKey
#imports commands to decrypt
from decryption.decryptFunction import decFile

#Progress report: Encryption and decryption commands work. Working on 
def main():
    #prompt the welcome message on the start of the program
    print(welcomeMsg)

    while True:
        task = input("What task do you want to accomplish? ")

        if task=="end":
            print("Ending session....")
            break

        #Calls encryptions function
        elif task=="e":
            print("Encrypting...")
            encFile() #calls encryption function

        #Calls decrypting function
        elif task=="d":
            print("Decrypting...")
            decFile() #calls decryption function

        #shows functions to show keys
        elif task=="show":
            print("Retrieving keys...")
            showKey()

        #calls function to generate keys
        elif task=="k":
            print("Generating key...")
            genKey()
        
        #Prompts user if they mistyped
        else:
            print("Unrecongized command, try again.")




main()



#show this in class
##############

#bottom code used to generate key
# key = Fernet.generate_key()

# with open('myKey.key', 'wb') as mykey:
#     mykey.write(key)
# # 
#Hope to imlement obfusication to hide the key or at least make it unreadable to humands.
#############

#Defines the key
# with open('myKey.key', 'rb') as mykey:
#     key = mykey.read()

# # ############

# #Commands to encrypt file
# # f = Fernet(key)

# # with open('topsecret.txt', 'rb') as original_file:
# #     original = original_file.read()


# # encrypted = f.encrypt(original)

# # with open('encrypted_topsecret.txt', 'wb') as encrypted_file:
# #     encrypted_file.write(encrypted)

# # ###########

# f = Fernet(key)

# with open('encrypted_topsecret.txt', 'rb') as encrypted_file:
#     encrypted = encrypted_file.read()

# decrypted = f.decrypt(encrypted)

# with open('decrypted_topsecret.txt', 'wb') as decrypted_file:
#     decrypted_file.write(decrypted)