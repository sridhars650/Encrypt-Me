# Encryption and Decryption Web Application

This is a simple web application built with Flask for encrypting and decrypting text using various methods, including Base64, a85, Base16, Base32, Base32hex, and Fernet encryption.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

## Features

- Encrypt text using various methods: Base64, a85, Base16, Base32, Base32hex, and Fernet.
- Decrypt text using the same methods.
- Fernet encryption generates a secure key for encryption/decryption.
- Simple and intuitive user interface.
- Modal pop-ups to display encrypted/decrypted keys.

## Live Demo

You can find a live demo at -> 

## Requirements

- Python 3.x
- Flask
- Cryptography

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sridhars650/Encrypt-Me.git
    cd Encrypt-Me
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000/
    ```

3. **Encrypt a key/secret:**

    - Enter the text you want to encrypt.
    - Select the encryption method.
    - Click "Encrypt" to get the encrypted key.

4. **Decrypt a key/secret:**

    - Enter the encrypted key/secret.
    - If using Fernet encryption, enter the Fernet key.
    - Select the encryption method.
    - Click "Decrypt" to get the decrypted key.

## Screenshots

### Encryption Page

![Encryption Page](images/encryptPage.png)

### Decryption Page

![Decryption Page](images/decryptPage.png)

