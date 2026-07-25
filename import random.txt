import random

placeholder = ""
lives = 5
list_items = ["lorem", "epsum"]
random_list = random.choice(list_items)
print(random_list)

length = len(random_list)
print(length)

for i in range(length):
    placeholder += '_'
print(placeholder)

list_item = []  # store guessed letters

while lives > 0:
    display = ''
    user_chosen = input("Please enter your choice: ")

    # check each letter in the word
    for letter in random_list:
        if user_chosen == letter:
            display += letter
            if user_chosen not in list_item:
                list_item.append(user_chosen)

        elif letter in list_item:
            display += letter
        else:
            display += "_"

    # lose a life only if guess not in word
    if user_chosen not in random_list:
        lives -= 1

    print(display)
    print(list_item)

    if "_" not in display:
        print("🎉 You win!")
        break

print("Game over! The word was:", random_list)