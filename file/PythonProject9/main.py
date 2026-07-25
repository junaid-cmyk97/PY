works = []
def routine():
    print("routine_1:")
    print("completed a routine")
    print("delete a routine")
    print("exit:")

def routine():
    first_routine = input("enter the first routine: ")
    if first_routine:
        works.append({first_routine})
        print("routine_1 completed a routine")
    else:
        print("routine_1 yet to be completed")

def completed_a_routine():
            view_routine()
            if not works:
                return
            else:
                print("invalid routine")

def delete_routine():
    delete_routine = input("enter the routine you want to delete: ")
    if delete_routine:
        remove_routine = works.pop(delete_routine-1)
        works.remove(delete_routine)


def habits():

    while True:
        routine()
        do  = input("enter the daily morning routine")

        if do == "routine_1":
            routine_1()
        elif choice == "completed a routine":
            completed_a_routine()
        elif choice == "delete a routine":
            delete_routine()
        else:
            print("invalid routine")

if __name__ == "__main__":
    habits()



