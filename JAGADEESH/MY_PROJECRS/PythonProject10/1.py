# f2 = open("file_2.txt","r")
# data = f2.read()
# print(data)

# f2 = open("file_2.txt","w")
# mydata= f2.write("Hello World")
# f2.close()
#
# f2 = open("file_2.txt","w")
# written = f2.write("welcome to the planet")
#
#
# f2 = open("file_2.txt","r")
# written1 = f2.read()
# print(written1)
#
# f1 = open("file_3.txt","x")
#
#
#
# f2 = open("file_2.txt","r")
# my_file  = f2.read()
# print(my_file)


# f2 = open("file_2.txt","r+")
# print(f2.tell())
# f2.write("welcome to the planet")
# print(f2.tell())
# print(f2.read())
# print(f2.tell())


# f2 = open("file_4.txt","w+")
# f2.write("brinjal")
# f2.write("carrot")
# folder_contain = f2.read()
# print(folder_contain)
# f2.close()

# f1 = open("fC:/Users/SIC/Pictures/Saved Pictures","a+")
# print(f1.tell())
# f1.seek(0)
# f1.write("welcome planet")
# print(f1.read())
# f1.write("be carful")





# some function
# with open("file_1.txt", "r") as f:
#     print(type(f))
#
# f.seek(10)
#
# data = f.read(5)
# print(data)


# def  appl(fx,value):
#     return 1 + fx(value)
# double = lambda x: x*2
# print (appl(lambda(x : x*x*858))

## map filter and reduce
#MAP
# def square(a):
#     return a * a
#
# numbers = [ 2,4,6,8]
# squares = list(map(square, numbers))
# print(squares)
#

# new_folder = open("important_docs.txt","w")
# new_folder.write("enter pass key")
# # print(new_folder)

# new_folder = open("important_docs.txt","r")
# text = new_folder.read()
# print(text)

# new_folder = open("important_docs.txt","w")
# new_folder.write("blua blur blue")
# new_folder.write(" out of parasite")
# print(new_folder)
#
# new_folder = open("important_docs.txt","w+")
# new_folder.write("no vac")
# new_folder.write("take dolo 650")
# print(new_folder.tell())
# print(new_folder.read())
# print(new_folder.tell())
# new_folder.write(" its danger")
# print(new_folder.tell())
# text = new_folder.read()
# print(text)
# new_folder.close()

# new_folder = open("important_docs.txt","a")
# new_folder.write(" popcorn is white")
# new_folder.write("where is AAQ")



# new_folder.write(" popcorn is white")
# new_folder.write("where is AAQ")
# print(new_folder.tell())
# print(new_folder.read())

# new_folder= open("image.jpg","rb")
# new_folder_1=open("image_2.jpg","wb")
# for i in new_folder:
#     new_folder_1.write()
# print(new_folder_1.read())

# class Instructor:
#
#     def __init__(self,name,age,location):
#         self.name = name
#         self.age = age
#         self.location = location
#
#
# instructor_1 = Instructor("kar_goush",8,"ada_man")
# print(instructor_1.name)
# print(instructor_1.age)
# print(instructor_1.location)


#instructor_2 = instructor("aqua_man",9956,"black_hole")

# instructor_2 = Instructor()
# instructor_2.name = "aqua_man"
# instructor_2.age = 9956
# instructor_2.location = "black_hole"

#read lines

# f = open("readlines.txt","r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     N,sub,MK = line.split(",")
#     print(f"name:{N} subject:{sub} marks:{MK}")

# f = open("readlines","w")
# lines = ("one","two","hhhjd","jsksks","klsl")
# for line in lines:
#     f.write(line+"n")
#     print(line)
# f.close()
#



#
# f = open("file.txt","r")
# f.seek(16.8)
#
#
# data = f.seek(16.8)
# print(int(data))
# f.close()


##lambda
#reg::
def double(x):
    return x*2
print(double(2))

triple = lambda x:  x*2
print(triple(5))

avg = lambda x,y,z: (x+y)/3
print(avg(28,55,11))

def add(x,y):
    return x+y
print(add(2,3))




