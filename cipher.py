def caesar_cipher(text, shift, decode=False):
    if decode:
        shift = -shift
    result = []

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return "".join(result)


# Example usage
encoded = caesar_cipher("Hello World!", 3)  # Khoor Zruog!
decoded = caesar_cipher(encoded, 3, decode=True)  # Hello World!
