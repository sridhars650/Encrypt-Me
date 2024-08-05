from flask import Flask, render_template, request
import base64
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

encode_methods = {
    1: base64.b64encode,
    2: base64.a85encode,
    3: base64.b16encode,
    4: base64.b32encode,
    5: base64.b32hexencode
}
decode_methods = {
    1: base64.b64decode,
    2: base64.a85decode,
    3: base64.b16decode,
    4: base64.b32decode,
    5: base64.b32hexdecode
}

def encryptIt(encryptMethod, unEncryptedKey):
    return encryptMethod(bytes(unEncryptedKey, 'utf-8')).decode('utf-8')

# logic method
def decryptIt(decryptMethod, encryptedKey):
    return decryptMethod(encryptedKey).decode('utf-8')

@app.route('/encrypt', methods=['GET', 'POST'])
def encryptPage():
    encryptedKey = None # default value
    fernet_key = None # default value
    if request.method == 'POST': # if post was recieved
        key = request.form['key'] # add key form param to var key
        method = int(request.form['method']) # same thing with method but convert to int
        if method in encode_methods: # detects method
            encryptedKey = encryptIt(encode_methods[method], key) # does encryption
        elif method == 6: # special case for fernet encryption
            fernet_key = Fernet.generate_key() # generates a secure fernet key
            if fernet_key: # if there is the key
                f = Fernet(fernet_key) # encodes it
                encryptedKey = f.encrypt(bytes(key, "utf-8")).decode('utf-8') # using key, it encrypts
                fernet_key = fernet_key.decode()
            else:
                encryptedKey = "Fernet key is required for Fernet encryption." # else it gives error

    return render_template("encrypt.html", encryptedKey=encryptedKey, fernet_key=fernet_key) # returns with variables

@app.route('/decrypt', methods=['GET','POST']) 
def decryptPage():
    decryptedKey = None
    fernet_key = None
    if request.method == 'POST':
        key = request.form['key']
        method = int(request.form['method'])
        fernet_key = request.form['fernet_key']
        if method in decode_methods:
            decryptedKey = decryptIt(decode_methods[method], key)
        elif method == 6: # special case for fernet encryption
            if fernet_key: # if there is the key
                f = Fernet(fernet_key.encode('utf-8')) # encodes it
                decryptedKey = f.decrypt(bytes(key, "utf-8")).decode('utf-8') # using key, it encrypts
            else:
                decryptedKey = "Fernet key is required for Fernet encryption." # else it gives error
    return render_template('decrypt.html', decryptedKey=decryptedKey)

if __name__ == "__main__":
    app.run(debug=True)