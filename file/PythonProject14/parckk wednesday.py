wed_day= []


def add_task():
    task = input("you have to do:").strip()
    if task:
        wed_day.append(task)
        print(f"its sunny complete {task} in an hour")
    else:
        print(f"i cautioned that to complete {task} in an hour")

def show_task():
    
    if not wed_day:
        print("no tasks for the day.lets add some!")
    else:
        print("\n show the tasks for the day")
        for i, tasks in enumerate(wed_day,start=1):
            print(f"{i}-{tasks}")

def mark_completed():
    show_task()
    if tasks():
        try:
            num = int(input("please enter your choice no:"))
            if 1<=num<=len(tasks):
                print(f"your {add_task[num-1]} is marked")
            else:
                print("please enter a valid no:")
        except:
            print("please enter a valid no:")

def delete_task():
    show_task()
    if tasks:
        try:
            num = int(input("please enter your choice to delete:"))


            if 1<=num<=len(tasks):
                removed = tasks.pop(num-1)
                print(f"your {removed} is deleted")
            else:
                print("please enter a valid no:")
        except:
            print("please enter a valid no:")


def tasks():
    while True:
        print("1.add task for the day")
        print("2.show tasks for the day")
        print("3.mark task completed")
        print("4.delete task for the day")
        print("5.exit")

        choice = input("Enter your choice no:").strip()


        if choice == "1":
            add_task()
        elif choice == "2":
            show_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("the work list is empty")
            break
        else:
            print("please enter a valid choice")
           
tasks()


