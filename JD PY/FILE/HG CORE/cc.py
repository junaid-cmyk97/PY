
def ciper(text,shift):

    show = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = "A"
            else:
                base = "a"
            show += chr((ord(char) -ord(base)+ shift) % 26 + ord(base))

        else:
            show += char
    return show 


text = input("enter the word:")

shift = 3

encrypt = ciper(text,shift)
decrypt = ciper(encrypt,-shift)

print("original:",text)
print("encrypted:",encrypt)
print("decrypted:",decrypt)










