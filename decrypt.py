import os
import time
import base64
from cryptography.fernet import Fernet

os.system("clear")
input("Welcome to the Decryption Chamber! Press enter to continue... ")
os.system("clear")
encryptedKey = input("Please input your key to decrypt -> ")


choice = int(input("Please select the decryption method. \n\t1. base64\n\t2. a85 \n\t3. base16\n\t4. base32\n\t5. base32hex\n\t6. Fernet\n\n Type in an integer -> "))


decode_methods = {
    1: base64.b64decode,
    2: base64.a85decode,
    3: base64.b16decode,
    4: base64.b32decode,
    5: base64.b32hexdecode
}

# logic method
def decryptIt(decryptMethod, encryptedKey):
    return decryptMethod(encryptedKey).decode('utf-8')

if choice in decode_methods:
    decryptedKey = decryptIt(decode_methods[choice], encryptedKey.encode())
elif choice == 6: #fernet debug
    fernetKey = input("Please input the Fernet key for Fernet decryption -> ")
    f = Fernet(fernetKey.encode('utf-8'))
    decryptedKey = f.decrypt(encryptedKey.encode('utf-8')).decode('utf-8')
else:
    print("Error, retrying in 3 seconds...")
    time.sleep(3)
    os.system("python3 decrypt.py")
    exit()

os.system("clear")
print(f"Thank you for using the encryption machine. Here is your decrypted key:\n\n------------------------------------------\n\n{decryptedKey}\n\n\n")
