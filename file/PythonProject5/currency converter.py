

import currency
with open("currency.txt") as file:
    lines = file.readlines()

currencyDict= {}

for line in lines:
    parsed = line.split("\t")

    currencyDict[parsed[0]] = parsed[1]

print(currencyDict)


amount =  int(input("Enter the amount you want to convert: "))

print("Enter the name of the currency you want to convert!, available options:\n", currencyDict.keys())






