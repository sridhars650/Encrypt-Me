import os
import time
import base64
from cryptography.fernet import Fernet

os.system("clear")
input("Welcome to the Encryption Chamber! Press enter to continue... ")
os.system("clear")

key = Fernet.generate_key()
f = Fernet(key)

unEncryptedKey = input("Please input your key to encrypt -> ")

choice = int(input("Please select the encryption method. \n\t1. base64\n\t2. a85 \n\t3. base16\n\t4. base32\n\t5. base32hex\n\t6. Fernet\n\n Type in an integer -> "))

encode_methods = {
    1: base64.b64encode,
    2: base64.a85encode,
    3: base64.b16encode,
    4: base64.b32encode,
    5: base64.b32hexencode
}

def encryptIt(encryptMethod, unEncryptedKey):
    return encryptMethod(bytes(unEncryptedKey, 'utf-8')).decode('utf-8')

if choice in encode_methods:
    encryptedKey = encryptIt(encode_methods[choice], unEncryptedKey)
elif choice == 6:
    encryptedKey = f.encrypt(bytes(unEncryptedKey, "utf-8")).decode('utf-8')
else:
    print("Error, retrying in 3 seconds...")
    time.sleep(3)
    os.system("python3 encrypt.py")
    exit()

os.system("clear")
print(f"Thank you for using the encryption machine. Here is your encrypted key:\n\n------------------------------------------------------------\n\n{encryptedKey}\n\n------------------------------------------------------------")
print(f"\nSave this key for decryption: {key.decode()}\n\n------------------------------------------------------------\n")
