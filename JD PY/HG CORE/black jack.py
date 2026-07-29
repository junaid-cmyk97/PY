import random

player = [random.randint(1,11),random.randint(1,11)]
player_1 = [random.randint(1,11),random.randint(1,11)]

print(f"player have{player}  where is total:{sum(player)}")
print(f"player_1 first number :{player_1[0]}")

while sum(player) < 21:
    choice = input("enter your choice to add the card:yes or no \n")
    if choice == "yes":
        player.append(random.randint(1,11))
    else:
        break

while sum(player_1) < 17:
    player_1.append(random.randint(1,11))

#then printing both
print(f"player have {sum(player)}")
print(f"player_1 first number :{player_1[0]}")

#in game

if sum(player) > 21:
    print(f"player_1 won the game")
elif sum(player_1) >21 :
    print(f"player won the game")
elif player > player_1:
    print(f"player_1 won the game")
else:
    print(f"its a TIE")







