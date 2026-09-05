import random

list = ["aeroplane","helicopter","ant"]

trails = 10

chosen_word = random.choice(list)
print(chosen_word)

#list that to be filled
display =[]

#for each letter in chosen_word add [_] in the display[]
for i in range(len(chosen_word)):
##for letter in chosen_word:
    #
    display += "_"
print(display)

#to get user _guess input
trails = False
while not trails:
    guessed_letter = input("guess a letter:")
    
    for position in range(len(chosen_word)):
        
        letter = chosen_word[position]
        
        if letter == guessed_letter:
            
            display[position] = guessed_letter
            
        else:
            
            trails -= 1
            
        
            
        





    
