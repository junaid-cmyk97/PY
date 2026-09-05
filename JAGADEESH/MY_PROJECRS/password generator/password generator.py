import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','r','v','w','x','y','z']
symbols = ['!','@','#','$','%','&','*']
numbers = [1,2,3,4,5,6,7,8,9,10]

# n_letters = int(input("Enter the number of letters: "))
# n_symbols = int(input("Enter the number of symbols: "))
# n_numbers = int(input("Enter the number of numbers: "))
# password = ''
n_letters = random.choice(letters)
n_symbols = random.choice(symbols)
n_numbers = random.choice(numbers)
password = ''
num = 0
user_num = input("required number of letters in password: ")
for i in range(1,n_letters+1):
    if num == user_num:
        num+=1
        break

    char = random.choice(letters) + random.choice(symbols) + str(random.choice(numbers))
    password += char
print(password)