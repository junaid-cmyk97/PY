#if _else short hand
# a = 505
# b= 5000
# print ("a") if a>b else print("!") if a==b else print("b")

##enumerate function
marks = [ 12,44,45,77,78,56]
sheet = 0
for mark in marks:
    print(mark)
    if(sheet == 3):
        print ("highest mark")
    sheet += 1