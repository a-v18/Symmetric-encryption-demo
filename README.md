# Symmetric File Encryption & Decryption Demo

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight **Proof of Concept (PoC)** demonstrating symmetric file encryption and decryption using the `cryptography` library in Python. Designed purely for educational purposes to illustrate basic cryptographic concepts and key handling.

---

## ⚠️ Disclaimer
> **Educational Purpose Only:** This project is created strictly for academic and learning purposes to demonstrate symmetric encryption techniques. It is not intended for malicious use or deployment in production environments.

---

## 🚀 Features

* **Key Generation:** Generates and exports a secure 256-bit URL-safe Fernet key to a local file (`key.key`).
* **Symmetric Encryption:** Encrypts a specified file using AES in CBC mode with PKCS7 padding and SHA256 HMAC authentication.
* **Decryption & Recovery:** Decrypts `.encrypted` files back to their original state using the generated key.
* **Automatic Cleanup:** Safely handles file removal during encryption/decryption cycles to demonstrate file state transformation.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Core Library:** [`cryptography`](https://cryptography.io/) (Fernet module)

---

## 💻 Installation & Usage

1. **Clone the repository:**
   git clone [https://github.com/a-v18/Symmetric-encryption-demo.git](https://github.com/a-v18/Symmetric-encryption-demo.git)
   cd Symmetric-encryption-demo
2. **Install dependencies:** `pip install cryptography`
3. **Run the demo script:** `python crypto.py`


🔒 How It Works
`generate_key()` creates a new Fernet key and writes it to key.key.
A sample text file `(example.txt)` is generated.<br>
`encrypt_file()` encrypts the content, outputs example.txt.encrypted, and removes the plain file.
`decrypt_file()` reads the encrypted payload, reverses the process using key.key, and restores the original file

📜License
Distributed under the MIT License. See `LICENSE` for more information.
