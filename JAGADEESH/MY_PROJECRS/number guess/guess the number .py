import random
trails = 10
def diffcult_level(level_to_choose):
    if level_to_choose == "easy":
        trails = 10
    elif level_to_choose == "hard":
        trails = 5
    else:
         print("WRONG OUTPUT")
diffcult_level(level_to_choose = input("level_to_choose").lower())


print("RANDOM NUMBER 1 to 20.")
result= random.randint(1,20)


userguess = input("guess the number 1 to 20.")
print("you chosen", userguess)
print("random number is ",result)
for trails >= 0:
    if user guess == result:
        print("win")
    else:
        print("try agin")
        trails-=1
    print(trails)



