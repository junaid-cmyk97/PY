# questions =(("what is the colour of milk?"),
#            ("what is the colour of apple"))
#
# options =(("a=white", "b=black", "c=tea"),
#           ("a=red","b= yellow","c=greeen"))
#
#
# user_guess = input("What is your guess?")
# answer = ("a","a")
# question_num = 0
#
# for question in questions:
#     print(questions)
#     for option in options[question_num]:
#         print(option)
#
#     if user_guess == answer[question_num]:
#         print ("Correct")
#         question_num = question_num + 1
#     else:
#         print ("Wrong")
#         print("try again")


Q = (("how killed kattapa"),
     ("what is a even"))

options = (("A:charan","B:sai_sai_charan"),
           ("A= 1","B= 2"))



answer = ("B","B")
Q_num = 0

for questions in Q:
    print(questions)
    for option in options[Q_num]:
        print(option)


    charan_guess = input("What is your answer?")

    if answer == options[Q_num]:
        print("Correct")
    else:
        print("Wrong \n try again")
    Q_num += 1







