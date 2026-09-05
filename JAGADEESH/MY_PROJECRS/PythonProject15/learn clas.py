#import os
#things  = os.listdir(".")
#print(things)



#import os
#docs_orestent_in_folder = os.listdir(".")
#print(docs_orestent_in_folder)

#import os

#try:
#    os.mkdir("my_toy_box")
#    print("I made a toy box!")
#except FileExistsError:
#    print("Toy box already exists!")
    
#import os
#folder = os.mkdir("new_folder")
#print(folder)

#import os
#new_folder = os.listdir("new_folder")
#print(new_folder)

#import os
#print("before:",os.getcwd())
#os.chdir("...")
#print("after:",os.getcwd())


# import os
# path_value = os.environ.get("desktop")
# print(path_value)

#f2 = open("file_2.txt","w")
#to_write = f2.write("welcome to the planet")
#print(to_write)


f = open("my_file.txt","r")
while True:
    line = f.readline()
    print(line)
    if not line:
        break







