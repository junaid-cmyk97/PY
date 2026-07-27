import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ''
for letter in chosen_word:
    placeholder += "_"
print(placeholder)
list_item = []
lives = 5
print("your lives : ", lives)
while lives >=0:
    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
           display +=letter
           list_item.append(guess)
        elif letter in list_item:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        lives -=1
    print("your lives : ", lives)
    if lives == 0:
        print("you lost")
        break
    if display == chosen_word:
        print("you win")
        break
    print(display)
