def cipher(text,shift_no):
    show = ""
    for char in text:
        if char.isalpha():

            if char.isupper():
                base = "A"
            else:
                base = "a"
            show += chr((ord(char)-ord(base)+shift_no) % 26 + ord(base))
        else:
            show += letter

    return show

text = input("Enter your text: ")

shift_no = 2
#task 01
encrypt = cipher(text,shift_no)
#task 02
decrypt = cipher(text,-shift_no)

print("original:",text)
print("encrypted:",encrypt)
print("decrypted:",decrypt)

