# Alright! 😊
# Let’s go through the kid-friendly daily routine tracker step-by-step so you understand exactly how it works.

# 1. The works list
works = []


# This is where we store all the routines (fun activities) the kid adds.
# It starts empty, and we add items to it as the program runs.


# 2. Adding a routine
def add_routine():
    routine = input("🌟 What fun thing do you want to do today? ").strip()
    if routine:
        works.append(routine)
        print(f"🎈 Yay! '{routine}' is now on your fun list!")
    else:
        print("😅 Oops! You didn’t type anything.")


# Ask the kid what fun thing they want to do.
# .strip() removes extra spaces.
# If they type something, it’s added to the list.
# If they press Enter without typing, it shows a friendly reminder.


# 3. Viewing routines
def view_routines():
    if not works:
        print("📭 Your fun list is empty. Let's add something!")
    else:
        print("\n🎨 Your Fun List:")
        for i, routine in enumerate(works, start=1):
            print(f"{i}. {routine}")


# If the list is empty, it tells them to add something.
# If not, it shows all routines with numbers so they can choose later.


# 4. Marking a routine as completed
def completed_a_routine():
    view_routines()
    if works:
        try:
            num = int(input("✅ Which number did you finish? "))
            if 1 <= num <= len(works):
                print(f"🎉 Woohoo! You finished '{works[num-1]}'! High five! ✋")
            else:
                print("😅 That number isn’t on the list.")
        except ValueError:
            print("😅 Please type a number.")


# First, it shows the list so the kid can see the numbers.
# Then it asks which number they finished.
# If the number is valid, it celebrates 🎉.
# If they type something wrong, it gives a friendly warning.


# 5. Deleting a routine
def delete_routine():
    view_routines()
    if works:
        try:
            num = int(input("🗑 Which number do you want to remove? "))
            if 1 <= num <= len(works):
                removed = works.pop(num-1)
                print(f"🚀 '{removed}' flew away from your list!")
            else:
                print("😅 That number isn’t on the list.")
        except ValueError:
            print("😅 Please type a number.")


# Shows the list first.
# Asks which number to remove.
# If valid, it removes that routine from the list and says it “flew away” 🚀.


# 6. The main menu
def habits():
    while True:
        print("\n🎯 What do you want to do?")
        print("1. ➕ Add something fun")
        print("2. 👀 See my fun list")
        print("3. ✅ Mark something as done")
        print("4. 🗑 Remove something")
        print("5. 🚪 Exit")

        choice = input("Pick a number: ").strip()

        if choice == "1":
            add_routine()
        elif choice == "2":
            view_routines()
        elif choice == "3":
            completed_a_routine()
        elif choice == "4":
            delete_routine()
        elif choice == "5":
            print("👋 Bye-bye! Have a super fun day!")
            break
        else:
            print("😅 That’s not a choice. Try again!")


# This is the main loop that keeps the program running.
# Shows a menu with 5 choices.
# Depending on what the kid picks, it calls the right function.
# If they choose 5, it says goodbye and stops.


# 7. Starting the program
if __name__ == "__main__":
    habits()


This makes sure the program starts by showing the menu when you run it.


💡 In short:

# Add → Put fun things in the list.
# View → See the list.
# Complete → Celebrate finishing something.
# Delete → Remove something from the list.
# Exit → Leave the program.
#

If you want,
