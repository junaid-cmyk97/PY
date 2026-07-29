import random
#message for user
print("CHOSE RANDOM NUMBER FROM 1 to 20.")

# computer chosen number
result = random.randint(1, 20)
print(result)

#user choosing level
print("CHOSE EASY OR HARD")
level_to_choose = ""
user_chosen_level = input("level_to_choose").lower()


#function for giving user lives and taking return value
def difficult_level(level_to_choose):
    global trails
    if level_to_choose == "easy":
        trails = 5


    elif level_to_choose == "hard":
        trails = 10
    else:
        print("WRONG OUTPUT")
    return trails

#function return value is stored in trails
trails = difficult_level(user_chosen_level)

#message for user
print("you chosen ", user_chosen_level, "you got", trails)


#user guess number taken and converted from string to int
user_guess = int(input("guess the number 1 to 20."))
# print("you chosen", user_guess)
# print("random number is ",result)

#loop to check and evaluate user answer and run accordingly with user lives
while trails >= 0:
    # works only when user chose hard mode or else gets skipped
    if user_chosen_level == "hard":
        result = random.randint(1, 20)
    #user guess
    user_guess = int(input("guess again"))
    #checks user answer it true breaks and win message  is printed
    if user_guess == result:
        print("win")
        break
    #checks for lives if user have lifes user can try again if no life break is applied
    elif trails <= 0:
        print("you looooossssst")
        break
    # if false live becomes -1
    else:
        print("try agin")
        trails -= 1

    print("you chosen", user_guess)
    print("random number is ", result)
    print("trails left", trails)




# import random
# level_to_choose = ""
# user_chosen_level = int(input("choose_a_num"))
# result = random.randint(1, 20)
# print(result)
# print("CHOSE RANDOM NUMBER FROM 1 to 20.")
#
# while user_chosen_level != result:
#     result = random.randint(1, 20)
#     user_chosen_level = int(input("choose_a_num"))
#     if user_chosen_level == result:
#         print("win")
#         break
#     elif user_chosen_level != result:
#         print("lose")
#     print("computer number",result)

