import os
import base64
os.system("clear")
input("Welcome to the Encryption Chamber! Press enter to continue... ")
os.system("clear")
unEncryptedKey = input("Please input your key to encrypt -> ")

choice = int(input("Please input if you want (1)base64 or (2)a85. Type in an integer -> "))
if (choice == 1):
    encryptedKey = base64.b64encode(bytes(unEncryptedKey, 'utf-8')) 
    encryptedKey = encryptedKey.decode('utf-8') 
elif (choice == 2):
    encryptedKey = base64.a85encode(bytes(unEncryptedKey, 'utf-8'))
    encryptedKey = encryptedKey.decode('utf-8')
os.system("clear")
print(f"Thank you for using the encryption machine. Here is your encrypted key\n\n------------------------------------------\n\n{encryptedKey}\n\n\n")