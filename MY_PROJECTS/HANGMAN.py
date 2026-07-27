import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ''
for letter in chosen_word:
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()
list_item = []
while True:
    display = " "
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
           display +=letter
           list_item.append(guess)
        elif letter in list_item:
            display += letter
        else:
            display += "_"
    print(display)