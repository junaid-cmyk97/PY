#this is were all the works of person is stored
works = []

##### (add)ing th routine with function


def add_routine():
    routine = input("Enter your routine: ").strip()
# if routine added it shows in if loop or shows nothing in routine
    if routine:
        works.append(routine)
        print(f"{routine} is now working")
    else:
        print(f"yyyyedeeee!{routine} is not working")


###########    viewing routine

def view_routine():
    if not works:
        print("No work available")
    else:
        print("\n your routine:")
        for i ,routine in enumerate(works):
            print(f"{i}. {routine}")


######   marking the routine if completed
def completed_routine():
    view_routine()
    if works:
        try:
            num = int(input("Enter your routine: "))
            if  1 <= num <= len(works):
                print(f"{works[num-1]} is working")
            else:
                print(f"{works[num-1]} is not working")
        except valueError:
            print("please enter a valid number")



############   deleting a routine from the works
def del_routine():
    view_routine()
    if works:
        try:
            num = int(input("Enter your routine to delete: "))
            if 1 <= num <= len(works):
                removed = works.pop(num-1)
                print(f"{removed} is working")
            else:
                print(f"{works[num-1]} is not working")
        except ValueError:
            print("please enter a valid number")

######  the main menu

def habits():
    while True:
        print("\n🎯 What do you want to do?")
        print("1. ➕ Add something fun")
        print("2. 👀 See my fun list")
        print("3. ✅ Mark something as done")
        print("4. 🗑 Remove something")
        print("5. 🚪 Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_routine()
        elif choice == 2:
            view_routine()
        elif choice == 3:
            completed_routine()
        elif choice == 4:
            del_routine()
        elif choice == 5:
            print("Thank you for using this program")
            break
        else:
            print("please enter a valid choice")

habits()

