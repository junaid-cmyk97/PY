import random

list_of_words = ["ap","tg","kp"]

system_chosen = random.choice(list_of_words)
print(system_chosen)

display = " "

for letter in system_chosen:
    display += "_"
    print(display)
    
list_of_letters=[]

while True:
    
    display = " "
    user_guess = input("enter the letter:")
    for letter in system_chosen:
        
        if letter == user_guess:
            display += letter
            list_of_letters.append(letter)
        elif letter in list_of_letters:
            display += letter
        else:
            display += "_"
            
    print(display)
        
        
        




