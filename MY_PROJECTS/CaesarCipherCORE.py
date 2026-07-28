def encrypt_value(text, shift, result= ""):
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else :
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt_value(text, shift, result1= ""):
    for char in text:
        if char.isalpha():
            if char.isupper():
                result1 += chr((ord(char) - shift - 65) % 26 + 65)
            else :
                result1 += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result1 += char
    return result1
user_input = input("Type your message for encryption:\n")
shift = int(input("Type the shift number:\n"))
encrypt = encrypt_value(user_input , shift )
print("encrypted value:",encrypt)
decrypt_code = decrypt_value(encrypt, shift )
print("decrypted value:" ,decrypt_code)
# user_input = input("encode or decode:\n")
# if user_input == "encode":
#     encrypt = encrypt_value(user_input, shift)
#     print("encrypted value:",encrypt)
# elif user_input == "decode":
#     decrypt = decrypt_value(user_input, shift)
#     print("decrypted value:",decrypt)
# else:
#     print("invalid input")

