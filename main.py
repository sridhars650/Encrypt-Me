import os, time

os.system("clear")
input("Welcome to the Encrypt/Decrypt Machine! Press enter to continue... ")
os.system("clear")
encryptOrDecrypt = int(input("Do you want to encrypt a password or decrypt a password?\n\t1. Encrypt a password\n\t2. Decrypt a password\n\nPlease choose now (make sure its an integer) --> "))
if (encryptOrDecrypt == 1):
    os.system("python3 encrypt.py")
elif (encryptOrDecrypt == 2):
    os.system("python3 decrypt.py")
else:
    print("Error, trying again!")
    time.sleep(2)
    os.system("python3 main.py")