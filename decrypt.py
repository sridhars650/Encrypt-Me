import os
import base64
os.system("clear")
input("Welcome to the Decryption Chamber! Press enter to continue... ")
os.system("clear")
encryptedKey = input("Please input your key to decrypt -> ")
choice = int(input("Please input if you want (1)base64 or (2)a85. Type in an integer -> "))
if (choice == 1):
    decryptedKey = base64.b64decode(encryptedKey).decode()
elif (choice == 2):
    decryptedKey = base64.a85decode(encryptedKey).decode()

os.system("clear")
print(f"Thank you for using the encryption machine. Here is your decrypted key:\n\n------------------------------------------\n\n{decryptedKey}\n\n\n")