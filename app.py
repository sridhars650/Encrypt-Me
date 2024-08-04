from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt')
def encryptPage():
    return render_template('encrypt.html')

@app.route('/decrypt')
def decryptPage():
    return render_template('decrypt.html')

if __name__ == "__main__":
    app.run(debug=True)