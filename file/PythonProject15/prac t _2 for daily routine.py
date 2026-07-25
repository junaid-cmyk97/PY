wed_day= []


def add_task():
    task = input("choice a no:")
    wed_day.append(task)
    if add_task:
        print(f"its sunny complete {task} in an hour")
    else:
        print(f"i cautioned that to complete {task} in an hour")

def show_task():
    add_task()
    if not tasks:
        print("no tasks for the day")
    else:
        print(f"show the tasks for the day")
        for i in task.enumerate(wed_day,start=1):
            print(f"{i},{tasks}")

def mark_completed():
    add_task()
    if tasks():
        try:
            num = int(input("please enter your choice no:"))
            if 1<=num<=len(tasks):
                print(f"your {task} is marked")
            else:
                print("please enter a valid choice")
        except:
            print("please enter a valid no:")

def delete_task():
    add_task()
    if tasks():
        try:
            num = int(input("please enter your choice to delete:"))
            removed = tasks.pop(wed_day[num-1])
            if 1<=num<=len(tasks):
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

        choice = int(input("Enter your choice no:"))

        if choice == "1":
            add_task()
        elif choice == "2":
            show_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        else:
            print("please enter a valid choice")
            print("exit")
            break
tasks()




