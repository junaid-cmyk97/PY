import random

list_of_words = ["apple", "banana", "cherry"]

system_word = random.choice(list_of_words)
print(system_word)

letters_in_word = " "

for letter in system_word:
    letters_in_word += "_"
print(letters_in_word)

#to store the letters creating a var
bin()
list_items = []

#setting loop for guess the system_chosen_word



while True:
    display = " "

    guess = input("Guess the system word: ")

    for letter in system_word:

        if letter == guess:
            display += letter
            list_items.append(letter)
        elif letter in list_items:
            display += letter
        else:
            display += "_"

    print(display)




