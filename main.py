from cryptography.fernet import Fernet
######### Above imported library remains at all times

# Early beta of terminal commands

# imports welcomeMsg contents
from startup.onStart import welcomeMsg

# imports commands to encrypt
from encryption.encryptFunction import encFile
from encryption.makeKey import showKey, genKey

# imports commands to decrypt
from decryption.decryptFunction import decFile


# Progress report: Encryption and decryption commands work. Working on
def main():
    # prompt the welcome message on the start of the program
    print(welcomeMsg)

    while True:
        task = input("What task do you want to accomplish? ")

        match task:
            case "end":
                print("Ending session....")
                exit()
            case "e":
                print("Encrypting...")
                encFile()  # calls encryption function
            case "d":
                print("Decrypting...")
                decFile()  # calls decryption function
            case "show":
                print("Retrieving keys...")
                showKey()
            case "k":
                print("Generating key...")
                genKey()
            case _:
                print("Unrecognized command, try again.")


main()
