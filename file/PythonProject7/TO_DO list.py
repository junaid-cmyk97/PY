# Simple To-Do List Application

tasks = []  # Global list to store tasks


def display_menu():
    """Display the main menu options."""
    print("\n--- TO-DO LIST MENU ---")
    print("1: Add task")
    print("2: Mark task as completed")
    print("3: Delete task")
    print("4: View tasks")
    print("5: Exit")


def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty.")


def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("📭 Your to-do list is empty.")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{index}. {task['task']} [{status}]")


def mark_completed():
    """Mark a task as completed."""
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("✅ Task marked as completed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def delete_task():
    """Delete a task from the list."""
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"🗑️ Task '{removed_task['task']}' removed successfully!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def to_do_app():
    """Main loop for the to-do list app."""
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_completed()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("👋 Exiting To-Do App. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


# Run the app
if __name__ == "__main__":
    to_do_app()

