def vigenere_encrypt(text, key):
    """
    Encrypts a given text using the Vigenère cipher.
    :param text: The plaintext to encrypt
    :param key: The encryption key
    :return: The encrypted ciphertext
    """
    encrypted_text = []
    key = key.upper()  # Convert the key to uppercase for consistency
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift = ord(key[key_index]) - ord('A')  # Calculate the shift based on the key
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
            key_index = (key_index + 1) % key_length  # Move to the next letter in the key
        else:
            encrypted_text.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(encrypted_text)


# Example usage
plain_text = input("Enter the text to encrypt: ")
key = input("Enter the encryption key: ")
encrypted = vigenere_encrypt(plain_text, key)
print("Encrypted text:", encrypted)