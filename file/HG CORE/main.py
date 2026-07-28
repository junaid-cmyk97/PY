
import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
list_of_words = ["ap"]

system_chosen = random.choice(list_of_words)
print(system_chosen)
placeholder = "_"
for letter in system_chosen:
    placeholder += "_"
print(placeholder)

lives = 6

print("your lives:",lives)
    
store_letter = []

while lives < 0:
    display = ""
    
    guess_letter = input("enter the letter:")
    
    for letter in system_chosen:
        
        if letter == guess_letter:
            display += letter
            store_letter.append(guess_letter)
        elif letter in store_letter:
            display += letter
        else:
            display +="_"
            
        if guess_letter not in system_chosen:
            lives -= 1
        print("your lives:",lives)
        
        if lives < 0:
            print("you lose")
            break
        if display == system_chosen:
            print("won")
            break
                
        if lives==0:
            print(stages[lives])
        if lives == 1:
            print(stages[lives])
        if lives == 2:
            print(stages[lives])
        if lives == 3:
            print(stages[lives])
        if lives == 4:
            print(stages[lives])
        if lives == 5:
            print(stages[lives])
        if lives == 6:
            print(stages[lives])
            
    print(display)






