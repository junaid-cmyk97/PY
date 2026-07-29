sunday_works = []

def add_work():
    work = input("add a thing for a sunday: ").strip()
    if work:
        sunday_works.append(work)
        print(f"by pre_lunch complete {work} this sunday!")
    else:

        print("no work is added")

def show_work():
    if not works:
        print("your works are empty.lets add some works")
    else:
        print("\n your Works for sunday")
        for i, work in enumerate(sunday_works,start =1):
            print(f"{i}.{works}")


def completed_work():

    show_work()

    if works:
        try:
            num = int(input("which no.that completed:"))
            if 1 <= num <= len(works):
                print(f"completed {add_work[num-1]}!")
            else:
                print("its not in the works")
        except:
            print("Please enter a valid number")

def delete_work():
    show_work()
    if works():
        try:
            num = input("Enter which work to delete: ")
            if 1 <= num <= len(works):
                removed= works.pop(num-1)
                print(f"{removed}the work")
            else:
                print("its not in the works")
        except:
            print("type the work number")


def works():
    while True:
        print("1. add the work:")   # .append
        print("2. show the work list")
        print("3. ✅completed a thing")
        print("4. 🗑️ remove the work")     #.pop
        print("5. exit the program")

        choice = input("pick a number:")

        if choice == "1":
            add_work()
        elif choice == "2":
            show_work()
        elif choice == "3":
            completed_work ()
        elif choice == "4":
            delete_work ()
        elif choice == "5":
            print("the work list is empty")
            break
        else:
            print("Please enter a valid choice")

works()





