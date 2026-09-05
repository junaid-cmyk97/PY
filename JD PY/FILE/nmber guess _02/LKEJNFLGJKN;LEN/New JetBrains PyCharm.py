import random
#making list
list = ["aeroplane","helicopter"]

#ppicking random word from list
secrete_word = random.choice(list)
print(secrete_word)

#crete blanks for guess word to its length, where * is multiples length of letters in secret_word
guess_letter = ['_']*len(secrete_word)

#then add no. of attepts to guess
attempts = 10

#all set now enter the game
print("welcome to hangman")








