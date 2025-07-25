# Caesar Cipher Encoder/Decoder 🔐

## 📌 Problem Description

This repository contains the solution for a Caesar Cipher encoder/decoder.  
The cipher shifts each alphabet character by a variable integer value. Both encoding and decoding are supported.

---

## ⚙️ Features

- Encode a plaintext string using Caesar Cipher.
- Decode a ciphertext back to original.
- Handles uppercase, lowercase, and ignores non-alphabet characters.
- Variable shift support.

---

## 🚀 Usage

```python
from cipher import caesar_cipher_encode, caesar_cipher_decode

# Encoding
encoded = caesar_cipher_encode("Hello, World!", 3)
print(encoded)  # Khoor, Zruog!

# Decoding
decoded = caesar_cipher_decode(encoded, 3)
print(decoded)  # Hello, World!

## 🧠 Logic Summary
- Shifts letters based on ASCII codes with wrap-around logic for both upper and lowercase.

- Ignores punctuation and whitespace.

- Reversible by applying negative shift during decoding.
```