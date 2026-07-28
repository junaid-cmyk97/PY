
def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only change letters
            base = 'A' if char.isupper() else 'a'
            # Shift letter and wrap around alphabet
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char  # Keep spaces and punctuation
    return result
message = "HELLO WORLD"
shift = 3
encrypted = caesar(message, shift)       # Encrypt
decrypted = caesar(encrypted, -shift)    # Decrypt
print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

