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

