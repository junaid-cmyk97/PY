import random

letters = ['a','b','c','d','e','f','g''h','i','j','k','l','m','n','o','p','q','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','&','*']
numbers = [0,1,2,3,4,5,6,7,8,9,10]

n_letters = [random.choice(letters)]
n_symbols = [random.choice(symbols)]
numbers =[random.choice(numbers)]
password = ""
for i in range(6):
    password += random.choice(n_letters)
    password += random.choice(n_symbols)
    password += str(random.choice(numbers))
print(password)
