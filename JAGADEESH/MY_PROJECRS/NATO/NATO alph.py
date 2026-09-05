# import pandas
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())
#
# #todo : create a dictory in NATO format
#
# phonetic = {row.letter: row.code for (index,row) in data.iterrows()}
# print(phonetic)


import random

nato_dict = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
}

# Pick a random letter
letter = random.choice(list(nato_dict.keys()))
print(f"What is the NATO code for the letter '{letter}'?")

# Get answer
answer = input("Your answer: ").strip().capitalize()

# Check answer
if answer == nato_dict[letter]:
    print("✅ Correct!")
else:
    print(f"❌ Oops! The correct answer is {nato_dict[letter]}.")















