import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for letter in chosen_word:
    placeholder+="_"
print(placeholder)
list_view = []
while True:
    display = " "
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if guess == letter:
            display += guess
            list_view+=guess
        elif letter in list_view:
            display += letter
        else:
            display+="_"
    print(display)


