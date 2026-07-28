
def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only change letters
         
            if char.isupper():
               base = 'A'
            else:
               base = 'a'
            # Shift letter and wrap around alphabet
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char  # Keep spaces and punctuation
    return result
message = input("user ")
shift = 3
#1
encrypted = caesar(message, shift)       # Encrypt
#2
decrypted = caesar(encrypted, -shift)    # Decrypt

print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
