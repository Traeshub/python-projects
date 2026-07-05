# Personal encryption script.
"""supported file types | (text files).txt, .csv, .json & (images) .jpg, .png, .gif 
(others) .pdf, .docx, .xlsx & (binary media) .mp3, .mp4, .zip & (source code files) .py, .js etc"""

# Plain text file encrpty smoothly
# images work fine, but cannot be opened/viewed while encrypted
# PDF's and MS office documents work but will be corrupted if editing is attempted while encrypted
# Source code file work as well but should not be run while encrypted

from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

#write_key()        | #uncomment to generate a new key

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open (filename, "rb") as file:
        original_data = file.read()
    encrypt_data = fernet.encrypt(original_data)
    with open (filename, "wb") as file:
        file.write(encrypt_data)

encrypt_file("example_text.txt")