questions =(("what is the colour of milk?"),
           ("what is the colour of apple"))

options =(("a=white", "b=black", "c=tea"),
          ("a=red","b= yellow","c=greeen"))


user_guess = input("What is your guess?")
answer = ("a","a")
question_num = 0

for question in questions:
    print(questions)
    for option in options[question_num]:
        print(option)

    if user_guess == answer[question_num]:
        print ("Correct")
        question_num += 1
    else:
        print ("Wrong")
        print("try again")