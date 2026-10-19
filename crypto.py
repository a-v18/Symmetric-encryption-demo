"""
Symmetric File Encryption & Decryption Demo (Fernet PoC)
Author: Antonino Valese
"""

from cryptography.fernet import Fernet
import os


def generate_key():
    """Generates a secure Fernet key and saves it to a local file."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """Loads the encryption key from the key file."""
    return open("key.key", "rb").read()


def encrypt_file(file_name, key):
    """Encrypts a file and appends '.encrypted' extension to the output."""
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_name + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    os.remove(file_name)


def decrypt_file(encrypted_file_name, key):
    """Decrypts a '.encrypted' file back to its original state."""
    fernet = Fernet(key)
    with open(encrypted_file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(encrypted_file_name.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)
    os.remove(encrypted_file_name)


if __name__ == "__main__":
    # Generate key and initialize payload
    generate_key()
    key = load_key()
    file_to_encrypt = "example.txt"

    # Create a sample text file
    with open(file_to_encrypt, "w", encoding="utf-8") as file:
        file.write("Questo è un esempio di file per il backup.")

    # Encrypt the sample file
    encrypt_file(file_to_encrypt, key)
    print(f"[+] {file_to_encrypt} encrypted successfully.")

    # Decrypt the sample file back to plain text
    decrypt_file(file_to_encrypt + ".encrypted", key)
    print(f"[+] {file_to_encrypt} decrypted successfully.")